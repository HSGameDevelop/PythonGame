import pandas as pd

class excelFileManager:

    def ReadExcelFile(self, filePath):
        readData = pd.read_excel(filePath)
        return readData
