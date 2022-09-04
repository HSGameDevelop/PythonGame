from pydoc import writedoc

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
        file.write(writeData)
        file.close()

    # １６進数のバイト文字に変換
    def EncodeData(self, data):
        returnData = data.encode() # 文字列を直接intにできないためバイト文字に変換
        returnData = int.from_bytes(returnData, byteorder='big') # バイト文字をintに変換
        returnData = hex(returnData) # 16進数に変換
        returnData = returnData.encode() # 再びバイト文字に変換
        return returnData

    # 16進数のバイト文字から変換
    def DecodeData(self, data):
        returnData = data.decode() # バイト文字から文字列へ
        returnData = int(data, 16) # 10進数に戻す
        returnData = bytes(returnData) # バイト文字に変換
        return returnData