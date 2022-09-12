from pydoc import writedoc
import codecs
import numpy as np

class binaryFileManager:

    # 読み込み用にファイルを開く
    def OpenFileRead(self, filepath):
        file = open(filepath, 'rb')
        return file

    #ファイルを読み込む
    def ReadFile(self, filepath):
        file = self.OpenFileRead(filepath)
        readData = file.read()
        file.close()
        return readData

    # ファイルを読み込んで文字列に変換する
    def ReadFileToString(self, filepath):
        readData = self.ReadFile(filepath)
        return self.DecodeDataBytes16(readData)

    # 書き込み用にファイルを開く
    def OpenFileWrite(self, filepath):
        file = open(filepath, 'wb')
        return file

    # ファイルに書き込む
    def WriteFile(self, filepath, data):
        file = self.OpenFileWrite(filepath)
        file.write(data)
        file.close()

    # 文字列をファイルに書き込む
    def WriteFileFromString(self, filepath, data):
        file = self.OpenFileWrite(filepath)
        writeData = self.ConvertString(data)
        writeData = self.EncodeDataBytes16(writeData)
        file.write(writeData)
        file.close()

    # 文字列への変換処理
    def ConvertString(self, data):
        str = ''
        columnSize = len(data.columns)

        # データ名を先頭行に文字列としてつけておく
        for i in range(columnSize):
            str += data.columns[i] + ','
        str += '\n'
        
        # 各データの値を文字列に変換
        dataSize = data.size
        for i in range(dataSize):
            row = i // columnSize
            col = i % columnSize
            tmp = data.iat[row, col]
            if type(tmp) is np.int64:
                tmp = tmp.astype(np.unicode_)
            addStr =  tmp + ','
            if (col) == (columnSize - 1):
                addStr += '\n'
            str += addStr

        return str

    # １６進数のバイト文字に変換
    def EncodeDataBytes16(self, data):
        returnData = codecs.encode(data.encode('utf-8'), 'hex_codec') 
        return returnData

    # 16進数のバイト文字から変換
    def DecodeDataBytes16(self, data):
        returnData = data.decode() # バイト文字から文字列へ
        returnData = codecs.decode(returnData, 'hex_codec').decode('utf-8')
        return returnData