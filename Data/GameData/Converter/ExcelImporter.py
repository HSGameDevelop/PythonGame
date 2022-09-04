import pandas as pd

class excelFileManager:

    def ReadExcelFile(self, filePath):
        readData = pd.read_excel(filePath)
        return readData

    def ReadCsvFile(self, filePath):
        readData = pd.read_csv(filePath, encoding = "shift-jis")
        return readData
