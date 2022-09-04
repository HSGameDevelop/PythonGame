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
        return readData.decode()

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
        file.write(hex(writeData).encode())
        file.close()

    def EncodeData(self, data):
        returnData = codecs.encode(data)
        returnData = int.from_bytes(returnData, byteorder='big')
        return returnData
