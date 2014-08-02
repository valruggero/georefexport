"""
/***************************************************************************
Name		     : GeorefExport
Description          : GeorefExport export map as georeferenced image
Date                 : 18/07/2014
copyright            : (C) 2012 by Ruggero Valentinotti
email                : valruggero@gmail.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


def classFactory(iface): 
  
  from GeorefExport import GeorefExport 
  return GeorefExport(iface)
