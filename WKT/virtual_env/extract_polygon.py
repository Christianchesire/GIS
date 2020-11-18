import zipfile
import os
                                                                                               
                                                                                               
dir = "/home/techmozart/GIS/GIS/WKT/virtual_env/polygon.zip"
                                                                                               
                                                                                               
def extract_files(file):                                                                       
    """Extract zip files"""                                                                    
    zip = open(file, "rb")                                                                     
    zipShape = zipfile.ZipFile(zip)
    for fileName in zipShape.namelist():
        out = open(fileName, "wb")
        out.write(zipShape.read(fileName))
        out.close()


extract_files(dir)

