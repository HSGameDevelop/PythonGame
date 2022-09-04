import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from ExcelImporter import excelFileManager

# ファイル指定の関数
def filedialog_clicked():
    fTyp = [("Excelファイル", "*.xlsx")]
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = filedialog.askopenfilename(filetype = fTyp, initialdir = iFile)
    entry2.set(iFilePath)

# 実行ボタン押下時の実行関数
def conductMain():
    text = ""

    filePath = entry2.get()

    if filePath:
        text += "ファイルパス：" + filePath
        manager = excelFileManager()
        readData = manager.ReadExcelFile(filePath)
        print(readData)

    if text:
        messagebox.showinfo("info", text)
    else:
        messagebox.showerror("error", "パスの指定がありません。")
    
# ウィンドウを中央に移動する    
def CenterWindow(window, width, height):
    window.update_idletasks()
    width = width
    height = height
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

if __name__ == "__main__":

    # rootの作成
    root = Tk()
    # 画面タイトル
    root.title('ExcelConvertor')

    # 画面位置調整
    CenterWindow(root, 400, 150)
    
    # ファイル選択Frameの作成
    frameSelectFile = ttk.Frame(root, padding=10)
    frameSelectFile.grid(row=2, column=1, sticky=E)

    # 「ファイル選択」ラベルの作成
    IFileLabel = ttk.Label(frameSelectFile, text="ファイル選択＞＞", padding=(5, 2))
    IFileLabel.pack(side=LEFT)

    # 「ファイル選択」エントリーの作成
    entry2 = StringVar()
    IFileEntry = ttk.Entry(frameSelectFile, textvariable=entry2, width=30)
    IFileEntry.pack(side=LEFT)

    # 「ファイル選択」ボタンの作成
    IFileButton = ttk.Button(frameSelectFile, text="参照", command=filedialog_clicked)
    IFileButton.pack(side=LEFT)

    # Frameの作成
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=5,column=1,sticky=W)

    # 実行ボタンの設置
    button1 = ttk.Button(frame3, text="実行", command=conductMain)
    button1.pack(fill = "x", padx=30, side = "left")

    root.mainloop()