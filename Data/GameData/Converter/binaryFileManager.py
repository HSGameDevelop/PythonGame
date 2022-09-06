from pydoc import writedoc
import codecs

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
        return self.DecodeData(readData)

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
        writeData = self.EncodeData(data)
        file.write(writeData)
        file.close()

    # １６進数のバイト文字に変換
    def EncodeData(self, data):
        returnData = codecs.encode(data.encode('utf-8'), 'hex_codec') 
        return returnData

    # 16進数のバイト文字から変換
    def DecodeData(self, data):
        returnData = data.decode() # バイト文字から文字列へ
        returnData = codecs.decode(returnData, 'hex_codec').decode('utf-8')
        return returnData