from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import qgis.utils 
from Ui_GeorefExport import Ui_GeorefExport

import os, time, subprocess, platform, datetime
from osgeo import gdal, ogr
from osgeo.gdalconst import *



class GeorefExportDialog(QDialog, Ui_GeorefExport):

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface
        self.setupUi(self)
        self.connect(self.btnOutputFile, SIGNAL("clicked()"), self.outFileFun)
        self.connect(self.buttonBox, SIGNAL("accepted()"),self.accept)
        QObject.connect(self.buttonBox, SIGNAL("rejected()"),self, SLOT("reject()"))
	QObject.connect(self.buttonBox, SIGNAL("helpRequested()"),self.call_help)

        mapCanvas = self.iface.mapCanvas()
	self.mapRenderer = iface.mapCanvas().mapRenderer()
	# get projecr epsg
	if QGis.QGIS_VERSION_INT < 10900:
		projectCRS=self.mapRenderer.destinationSrs().epsg()
	else:
		projectCRS=int(self.mapRenderer.destinationCrs().postgisSrid())
	self.lineEditSourceSrs.clear()	
	self.lineEditSourceSrs.insert(str(projectCRS))	
	
	#define available raster formats
	drvCodeSelected=["PDF","GTiff","JPEG","PNG","JPEG2000","ECW","JP2ECW","JP2MrSID","JP2OpenJPEG"]

	#define dictionary for drivers description and extension
	self.drvDescription={}
	self.drvExt={}
	
	#popolate dictionary for file formats supported (in create or createcopy method) by local gdal installation 
	gdal.AllRegister()		
	for i in range(0, len(drvCodeSelected)):
		#print(gdal.__version__)
		drv = gdal.GetDriverByName(drvCodeSelected[i])
		if drv:
			drv_meta = drv.GetMetadata()
			#print(str(drvCodeSelected[i]))
			#print(str(drv_meta))
			if 'DMD_EXTENSION' in drv_meta and \
				((drv_meta.has_key(gdal.DCAP_CREATE) and drv_meta[gdal.DCAP_CREATE] == 'YES') or \
					(drv_meta.has_key(gdal.DCAP_CREATECOPY) and drv_meta[gdal.DCAP_CREATECOPY] == 'YES')): 
				drvLName="["+drvCodeSelected[i]+"] "+drv.LongName				
				self.drvDescription[drvLName]=drv.GetDescription()
				self.drvExt[drvLName]=drv_meta['DMD_EXTENSION']
				self.cmboxImgFormat.addItem(drvLName)	
	
	# get map rectangle
	mapRect = self.mapRenderer.extent()
	self.xStart = mapRect.xMinimum()
	self.xEnd = mapRect.xMaximum()
	self.yStart = mapRect.yMinimum()
	self.yEnd = mapRect.yMaximum()
	self.metersPerPixel=0.0000

    def call_help(self):
	qgis.utils.showPluginHelp()

    def createWorldFile(self,fileName, mainScale, wFileExt):
	#>>Create World File
	mapRect = self.mapRenderer.extent()
	f = open(fileName + "." + wFileExt, 'w')
	f.write(str(mainScale) + '\n')
	f.write(str(0) + '\n')
	f.write(str(0) + '\n')
	f.write('-' + str(mainScale) + '\n')
	f.write(str(mapRect.xMinimum() + mainScale/2) + '\n')
	f.write(str(mapRect.yMaximum() - mainScale/2))
	f.close()

        
    def outFileFun(self):
        "Display file dialog for output file"
        self.lineOutput.clear()
        fileName = QFileDialog.getSaveFileName(self, "Raster graphic output file",".", "")
	if QGis.QGIS_VERSION_INT < 10900:		
		if not fileName.isEmpty():
			self.lineOutput.clear()
			self.lineOutput.insert(fileName)
	else:
		if fileName:
			self.lineOutput.clear()
			self.lineOutput.insert(fileName)	
        return fileName

    
    def doImage(self,myImagePath,myImagepathNoExt):

	dpi = self.spinBoxDpi.value()
	myWidth = self.spinBoxWidth.value() #width in pixels

	self.metersPerPixel = (self.xEnd-self.xStart)/(myWidth)
	myHeight = int((self.yEnd - self.yStart)/self.metersPerPixel) 
	#print myWidth
	#print myHeight
	xPaperSize = myWidth/(dpi/25.4)
	yPaperSize = myHeight/(dpi/25.4)
	#self.textEdit.append("xPaperSize %f" % (xPaperSize))
	#self.textEdit.append("yPaperSize %f" % (yPaperSize))
	
	composition = QgsComposition(self.mapRenderer)
        composition.setPrintResolution(dpi)
        composition.setPaperSize(xPaperSize, yPaperSize)
        composition.setPlotStyle(QgsComposition.Print)
	#dpi = composition.printResolution()
        dpmm = dpi / 25.4 #get dots per mm
        # add a map to the composition
        composerMap = QgsComposerMap(composition,0,0,composition.paperWidth(),composition.paperHeight())
        composition.addItem(composerMap)
        # create output image and initialize it
        image = QImage(QSize(myWidth, myHeight), QImage.Format_ARGB32) #output image size
        image.setDotsPerMeterX(dpmm * 1000) #mm to meters
        image.setDotsPerMeterY(dpmm * 1000) #mm to meters
        image.fill(0)
        # render the composition
        imagePainter = QPainter(image)
        sourceArea = QRectF(0, 0, composition.paperWidth(), composition.paperHeight() )
        targetArea = QRectF(0, 0, myWidth, myHeight)
        composition.render(imagePainter, targetArea, sourceArea)
        imagePainter.end()
#	self.textEdit.append(imagepath)
        image.save(myImagePath , "tif")	
        self.createWorldFile(myImagepathNoExt, self.metersPerPixel, "tfw")

    def loadOutputFile(self,outFile):
        "Load map in TOC"
	self.textEdit.append("")
        fileInfo = QFileInfo(outFile)
        baseName = fileInfo.baseName()
        rlayer = QgsRasterLayer(outFile, baseName)
        if not rlayer.isValid():
            self.textEdit.append("Layer "+outFile+" failed to load.")
	else:
	    self.textEdit.append("Layer "+outFile+" loaded.")
	QgsMapLayerRegistry.instance().addMapLayer(rlayer)
	return rlayer

    def accept(self):
        # Called when "OK" button pressed
        
	self.textEdit.clear()
	inizio = datetime.datetime.now()
        self.textEdit.append("Starting...")
	outFile=self.lineOutput.text()
	if (outFile == ''):
		QMessageBox.critical(None,"Exiting gracefully","Output file not defined %s!" % (outFile))
		return
	if (len(outFile.split(' ')) > 1):
		QMessageBox.critical(None,"Exiting gracefully","File path contains spaces %s!" % (outFile))
		return

	ssrs=self.lineEditSourceSrs.text()
	
	# retrieve dirname and basenamen from outFile
	outDir=os.path.dirname(outFile)
	outImage=os.path.basename(outFile)
	
	#create temp file
	tmpimagepath=outDir+"/.tmp_"+outImage+".tif"
	tmpimagepathNoExt=tmpimagepath[:-4]
	imagepathNoExt=outDir+"/"+outImage
	
	self.doImage(tmpimagepath,tmpimagepathNoExt)
	
	imgFormat=self.cmboxImgFormat.currentText()
	
	outputFormat=self.drvDescription[imgFormat]
	outputExt=self.drvExt[imgFormat]	

	# do translate...
	gdal_translateCMD=str("-of "+ outputFormat+" -a_srs epsg:"+ssrs+" "+tmpimagepath+" "+imagepathNoExt+"."+outputExt )
	self.textEdit.append("gdal_translate "+gdal_translateCMD)

	#call gdal_translate process
    	processTranslate = QProcess( parent=None )
	if QGis.QGIS_VERSION_INT < 10900:
	    	processTranslate.start( "gdal_translate",QStringList() << gdal_translateCMD.split(" "), QIODevice.ReadOnly )
        else:
		processTranslate.start( "gdal_translate",gdal_translateCMD.split(" "), QIODevice.ReadOnly )
	arr = QByteArray()
    	if processTranslate.waitForFinished(-1):
    		arr = processTranslate.readAllStandardOutput()
    		processTranslate.close()
    	self.textEdit.append("gdal_translate:\n - "+ str(arr) )
    	
	# if outFile exist, create the world file (if required)
    	if os.path.isfile(imagepathNoExt+"."+outputExt):
		self.textEdit.append(imagepathNoExt+"."+outputExt+ " created.")
		if self.checkWFile.isChecked():
    			wfext=outputExt[0]+outputExt[-1:]+"w"
    			self.createWorldFile(imagepathNoExt, self.metersPerPixel, wfext.lower())
			if os.path.isfile(imagepathNoExt+"."+wfext):			
				self.textEdit.append(imagepathNoExt+"."+wfext+ " created.")
			else:
				self.textEdit.append("ERROR: "+imagepathNoExt+"."+wfext+ " NOT created!")
	else:
		self.textEdit.append("ERROR: "+imagepathNoExt+"."+outputExt+ " NOT created!")
	
	#load file in canvas if required
	if self.checkAddRes.isChecked():
		self.loadOutputFile(imagepathNoExt+"."+outputExt)
		
    	
    	#remove tmp files
	os.remove(tmpimagepathNoExt+".tfw")
    	os.remove(tmpimagepath)
    	
	#print time in textEdit log
	self.textEdit.append("")
	fine = datetime.datetime.now()
	self.textEdit.append( 'Starting time: '+ str(inizio) )
	self.textEdit.append( 'Ending time: '+ str(fine) )
	diff = fine-inizio
	self.textEdit.append( "Elapsed time: " + str(diff) )
	

