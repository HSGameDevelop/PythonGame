import sys, os

sys.path.append('../System/IO/')
from ..System.IO.BinaryFileManager import BinaryFileManager

# データ読み込みのベースクラス
class DataLoaderBase:
    LOAD_BIN_FILE_DIRECTORY = os.getcwd() + '/Resource/Bin/'

    # データ読み込み処理(読み出し先の形に添ったで変換関数を指定する)
    def LoadData(self, filePath, convertFunc):
        bfm = BinaryFileManager()
        data = bfm.ReadFileToString(filePath)
        return convertFunc(data)

    # データの変換処理(outputDataの形に変換する)
    def ConvertOutputData(self, inputData, outputData, createDataFunc):
        convertData = inputData.splitlines()
        columns = convertData[0].split(',') # 先頭行はパラメータ名

        for i in range(len(convertData)):
            if i == 0: # 先頭行はパラメータ名の為、弾く
                continue
            outputData.append(createDataFunc(convertData[i], columns))
        return outputData

    # データの作成(outputDataの形で生成する)
    def CreateOutputData(self, inputData, columns, outputData):
        keys = list(outputData.__dict__.keys()) 
        params = inputData.split(',')

        for i in range(len(params)):
            for j in range(len(keys)):
                if keys[j].lower() == columns[i].lower():
                    outputData.__setattr__(keys[j], params[i]) 
                    break

        return outputData
