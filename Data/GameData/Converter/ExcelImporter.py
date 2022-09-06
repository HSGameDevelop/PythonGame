import pandas as pd

class excelFileManager:

    # Excelファイルを読み込む
    def ReadExcelFile(self, filePath):
        readData = pd.read_excel(filePath)
        return readData
    
    # シート名を読み込む
    def ReadExcelSheetNames(self, filePath):
        file = pd.ExcelFile(filePath)
        return file.sheet_names

    # CSVファイルを読み込む
    def ReadCsvFile(self, filePath):
        readData = pd.read_csv(filePath, encoding = "shift-jis")
        return readData


