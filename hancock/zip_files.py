"""
    This file is used to work with zipped files
"""
import zipfile


dir = "/home/techmozart/GIS/GIS/hancock/hancock.zip"


def extract_files(file):
    """Extract zip files"""
    zip = open(file, "rb")
    zipShape = zipfile.ZipFile(zip)
    for fileName in zipShape.namelist():
        out = open(fileName, "wb")
        out.write(zipShape.read(fileName))
        out.close()


def tar_extract(file):
    """Extract tar, i.e tar.gz files"""
    tar = tarfile.open(file, "r:gz")
    tar.extractall()
    tar.close()


extract_files(dir)
