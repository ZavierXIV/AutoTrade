import os
from openpyxl import load_workbook


def createAddressDir(rootPath):
    projNames = getProjNames()

    for projName in projNames:
        dirPath = os.path.join(rootPath, projName)
        subDirs = [
            os.path.join(dirPath, '標示部'),
            os.path.join(dirPath, '所有權部'),
            os.path.join(dirPath, '他項權利')
        ]

        if not os.path.exists(dirPath):
            os.mkdir(dirPath)

        for idx, dirName in enumerate(subDirs):
            if not os.path.exists(dirName):
                os.mkdir(dirName)


def getProjNames():
    workbook = load_workbook('109.6.21.xlsx')
    worksheet = workbook.get_sheet_by_name('工作表1')
    projNames = [item.value for item in list(worksheet.columns)[2]]
    projNames.remove('案名')
    return projNames

createAddressDir('./')