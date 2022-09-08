import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pathlib
import shutil
import tkinter
from turtle import left
from ExcelImporter import excelFileManager
from binaryFileManager import binaryFileManager

entrySelectFile = 0 # ファイル選択のエントリー
buttonConvert = None # コンバートボタン

# 各種フラグ群
sheetBln = {} # シート一覧チェックボックスのフラグ群

sheetNameList = {}
selectSheeteNameIndex = 0 # シート一覧チェックボックス用
readData = None

# 列名用変数一覧
frameColumn = None
columnBln = {} # 列一覧チェックボックスのフラグ群
checkBoxComlumns = {}

# ファイル指定の関数
def filedialog_clicked():
    fTyp = [("Excelファイル", "*.xlsx")]
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = filedialog.askopenfilename(filetype = fTyp, initialdir = iFile)
    if entrySelectFile:
        entrySelectFile.set(iFilePath)

# バイナリファイルへのコンバート
def ConverBinaryDataFromExcel(filePath):
    #global readData
    # 読み込んでいるデータにフィルターを掛ける
    writeData = FilterData(readData)
    # 確認用
    print(writeData)
    # バイナリファイルの作成
    binaryManager = binaryFileManager()
    convertFilePath = ExtensionToBin(filePath)
    binaryManager.WriteFileFromString(convertFilePath, writeData.to_string())

# データにフィルターを掛ける
def FilterData(data):
    returnData = data
    
    selectColumns = GetSelectColumns();
    filterCount = len(selectColumns)

    # 強引にフィルターを掛ける
    if filterCount == 1:
        returnData = returnData.filter(items=[selectColumns[0]])
    elif filterCount == 2:
        returnData = returnData.filter(items=[selectColumns[0], selectColumns[1]])
    elif filterCount == 3:
        returnData = returnData.filter(items=[selectColumns[0], selectColumns[1], selectColumns[2]])
    elif filterCount == 4:
        returnData = returnData.filter(items=[selectColumns[0], selectColumns[1], selectColumns[2], selectColumns[3]])
    elif filterCount == 5:
        returnData = returnData.filter(items=[selectColumns[0], selectColumns[1], selectColumns[2], selectColumns[3], selectColumns[4]])
    elif filterCount == 6:
        returnData = returnData.filter(items=[selectColumns[0], selectColumns[1], selectColumns[2], selectColumns[3], selectColumns[4], selectColumns[5]])

    return returnData

# .binに拡張子を変換する
def ExtensionToBin(filePath):
    dir = os.path.dirname(filePath)
    path = pathlib.Path(filePath)
    beforeFileName = path.stem
    afterFileName = beforeFileName + ".bin"
    return dir + "/" + afterFileName

# 選択しているシートの名前を取得
def GetSelectSheetName():
    for i in range(len(sheetBln)):
        if sheetBln[i].get():
            return sheetNameList[i]

    return None

# 実行ボタン押下時の実行関数
def conductMain():
    text = ""
    filePath = entrySelectFile.get()

    if filePath:
        ConverBinaryDataFromExcel(filePath)
        text += "ファイルパス：" + filePath + "\nシート名："+ sheetNameList[selectSheeteNameIndex] +"\n列名："+ GetSelectColumns()[0] +"\nのコンバートを行いました。"

    if text:
        messagebox.showinfo("info", text)
    else:
        messagebox.showerror("error", "パスの指定がありません。")

# 読み込みボタン押下時の処理
def CheckSelectFile():
    global selectSheeteNameIndex
    global buttonConvert
    buttonConvert['state'] = tkinter.DISABLED

    excelManager = excelFileManager()
    global sheetNameList
    filePath = entrySelectFile.get()
    sheetNameList = excelManager.ReadExcelSheetNames(filePath)

    frameSheetLabel = ttk.Frame(window, padding=5)
    frameSheetLabel.grid(row=2,column=0,sticky=NW)
    labelSheet = ttk.Label(frameSheetLabel, text="シート一覧：", padding=(5, 2))
    labelSheet.pack(side=LEFT)

    frameSheet = ttk.Frame(window, padding=5)
    frameSheet.grid(row=2,column=1,sticky=NW)
    global sheetBln
    for i in range(len(sheetNameList)):
        sheetBln[i] = tkinter.BooleanVar()
        if i == 0:
            sheetBln[i].set(True)
            selectSheeteNameIndex = i
        chk = tkinter.Checkbutton(frameSheet, variable=sheetBln[i], text=sheetNameList[i], command=SelectSheetNamesCheckBox) 
        chk.grid(row=0,column=i)
    
    # 列名用テキスト作成
    frameColumnLabel = ttk.Frame(window, padding=5)
    frameColumnLabel.grid(row=3,column=0,sticky=NW)
    labelColumn = ttk.Label(frameColumnLabel, text="列名一覧：", padding=(5, 2))
    labelColumn.pack(side=LEFT)

    # 列名チェックボックスの更新
    DestroyColumnsCheckBox()
    CreateColumnsCheckBox(filePath)

# 列名のチェックボックスを作成する
def CreateColumnsCheckBox(filePath):
    # Excelファイルの読み込み
    global readData
    excelManager = excelFileManager()
    readData = excelManager.ReadExcelFile(filePath, GetSelectSheetName())
    dataColumn = readData.columns
    
    # 各列名用チェックボックス作成
    global frameColumn
    global columnBln
    global checkBoxComlumns
    frameColumn = ttk.Frame(window, padding=5)
    frameColumn.grid(row=3,column=1,sticky=NW)
    for i in range(len(dataColumn)):
        columnBln[i] = tkinter.BooleanVar()        
        checkBoxComlumns[i] = tkinter.Checkbutton(frameColumn, variable=columnBln[i], text=dataColumn[i], command=SelectColumnsCheckBox) 
        checkBoxComlumns[i].grid(row=0,column=i)     

# 列名のチェックボックスを削除する
def DestroyColumnsCheckBox():
    global frameColumn
    global columnBln
    global checkBoxComlumns
    for i in range(len(checkBoxComlumns)):
        checkBoxComlumns[i].destroy()

    columnBln.clear()

# 選択している列を取得する
def GetSelectColumns():
    dataColumn = readData.columns
    selectColumns = {}
    index = 0
    for i in range(len(columnBln)):
        if columnBln[i].get():
            selectColumns[index] = dataColumn[i]
            index += 1
    return selectColumns
    
# シート名チェックボックス押下時の処理
def SelectSheetNamesCheckBox():
    global buttonConvert
    global selectSheeteNameIndex

    for i in range(len(sheetBln)):
        if i == selectSheeteNameIndex:
            sheetBln[i].set(not sheetBln[i].get())

        if sheetBln[i].get():
            #buttonConvert['state'] = tkinter.NORMAL 
            if i != selectSheeteNameIndex:
                buttonConvert['state'] = tkinter.DISABLED
                sheetBln[selectSheeteNameIndex].set(False)
                selectSheeteNameIndex = i
                
                # 列名一覧の更新
                filePath = entrySelectFile.get()
                DestroyColumnsCheckBox()
                CreateColumnsCheckBox(filePath)
            break

# 列名チェックボックス押下時の処理
def SelectColumnsCheckBox():
    global buttonConvert
    buttonConvert['state'] = tkinter.DISABLED

    for i in range(len(columnBln)):
        if columnBln[i].get():
            buttonConvert['state'] = tkinter.NORMAL 
            break
    
# ウィンドウを画面中央に作成
def CreateCenterWindow(title, width, height):
     # rootの作成
    window = Tk()
    # 画面タイトル
    window.title(title)

    window.update_idletasks()
    width = width
    height = height
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    return window

# ファイル選択メニューの作成
def CreateSelectFile(window):
    # ファイル選択Frameの作成
    frameSelectFile = ttk.Frame(window, padding=5)
    frameSelectFile.grid(row=0, column=0,sticky=NW)

    # 「ファイル選択」ラベルの作成
    IFileLabel = ttk.Label(frameSelectFile, text="ファイル選択：")
    IFileLabel.pack(side=LEFT)

    frameSelectFile2 = ttk.Frame(window, padding=5)
    frameSelectFile2.grid(row=0, column=1,sticky=NW)

    # 「ファイル選択」エントリーの作成
    entry = StringVar()
    IFileEntry = ttk.Entry(frameSelectFile2, state="readonly", textvariable=entry, width=60)
    IFileEntry.pack(side=LEFT)

    # 「ファイル選択」ボタンの作成
    IFileButton = ttk.Button(frameSelectFile2, text="参照", command=filedialog_clicked)
    IFileButton.pack(side=LEFT)

    return entry

# 各ボタンの作成
def CreateButtons(window):
    # Frameの作成
    frameButtonCheck = ttk.Frame(window, padding=5)
    frameButtonCheck.grid(row=1,column=0,sticky=NW)

    # 確認ボタンの設置
    buttonCheck = ttk.Button(frameButtonCheck, text="読み込み", command=CheckSelectFile)
    buttonCheck.pack(fill = "x", side = "left")
    
    # Frameの作成
    frameButtonConvert = ttk.Frame(window, padding=5)
    frameButtonConvert.grid(row=1,column=1,sticky=NW)

    # 実行ボタンの設置
    global buttonConvert
    buttonConvert = ttk.Button(frameButtonConvert, state="disable", text="コンバート", command=conductMain)
    buttonConvert.pack(fill = "x", side = "left")

if __name__ == "__main__":

    # 画面位置調整
    window = CreateCenterWindow('ExcelConvertor', 640, 150)
    
    entrySelectFile = CreateSelectFile(window)

    CreateButtons(window)
    
    window.mainloop()