import tkinter as tk
import math

root = tk.Tk()
root.geometry("1280x960")
root.title('windowPlactice')

#これで描画できる
canvas = tk.Canvas(root)
canvas.pack()
canvas.create_arc(100, 50, 300, 250, width=1, fill="#00ff00")


# Canvasの作成
#canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
#canvas.pack(fill = tk.BOTH, expand = True)
#canvas.create_oval(x0, y0, x1, y1, )
# 線の描画
#canvas.create_line(20, 10, 280, 190, fill = "Blue", width = 5)

root.mainloop()