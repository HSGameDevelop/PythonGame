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
isCanConver = False # コンバートできるかどうかのフラグ
buttonConvert = None # コンバートボタン

# 各種フラグ群
sheetBln = {} # シート一覧チェックボックスのフラグ群

# ファイル指定の関数
def filedialog_clicked():
    fTyp = [("Excelファイル", "*.xlsx")]
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = filedialog.askopenfilename(filetype = fTyp, initialdir = iFile)
    if entrySelectFile:
        entrySelectFile.set(iFilePath)

# バイナリファイルへのコンバート
def ConverBinaryDataFromExcel(filePath):
    # Excelファイルの読み込み
    excelManager = excelFileManager()
    readData = excelManager.ReadExcelFile(filePath)
    
    binaryManager = binaryFileManager()
    dir = os.path.dirname(filePath)
    path = pathlib.Path(filePath)
    beforeFileName = path.stem
    afterFileName = beforeFileName + ".bin"
    convertFilePath = dir + "/" + afterFileName
    binaryManager.WriteFileFromString(convertFilePath, readData.to_string())

# 実行ボタン押下時の実行関数
def conductMain():
    text = ""
    filePath = entrySelectFile.get()

    if filePath:
        text += "ファイルパス：" + filePath + "\nのコンバートを行いました。"
        ConverBinaryDataFromExcel(filePath)

    if text:
        messagebox.showinfo("info", text)
    else:
        messagebox.showerror("error", "パスの指定がありません。")

def CheckSelectFile():
    excelManager = excelFileManager()
    sheetList = excelManager.ReadExcelSheetNames(entrySelectFile.get())

    frameSheetLabel = ttk.Frame(window, padding=5)
    frameSheetLabel.grid(row=2,column=0,sticky=NW)
    labelSheet = ttk.Label(frameSheetLabel, text="シート一覧：", padding=(5, 2))
    labelSheet.pack(side=LEFT)

    frameSheet = ttk.Frame(window, padding=5)
    frameSheet.grid(row=2,column=1,sticky=NW)
    global sheetBln
    for i in range(len(sheetList)):
        sheetBln[i] = tkinter.BooleanVar()
        chk = tkinter.Checkbutton(frameSheet, variable=sheetBln[i], text=sheetList[i], command=SelectSheeteNamesCheckBox) 
        chk.grid(row=0,column=i)
        

def SelectSheeteNamesCheckBox():
    global buttonConvert
    buttonConvert['state'] = tkinter.DISABLED

    for i in range(len(sheetBln)):
        if sheetBln[i].get():
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