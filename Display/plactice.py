import tkinter as tk
import math

root = tk.Tk()
root.geometry("1280x960")
root.title('windowPlactice')

#これで描画できる
canvas = tk.Canvas(root)
canvas.pack()

# 扇形の座標
# 左上(x1, y1)
x1 = 10
y1 = 10
# 右下(x2, y2)
x2 = 200
y2 = 200
# 作成の方法が四角形の左上と右下の座標から生成する。

extent_type = 100

#  扇形の作成
canvas.create_arc(x1, y1, x2, y2, width=1, extent=extent_type, start=10)

# 基準の点からのずれの分を戻すために初期座標のx1,y1をx1_1,x2_1・y1_1,y2_1にそれぞれ加算する
# 左上(x1_1, y1_1)
x1_1 = (x2 - x1) / 2 - 5 + x1
y1_1 = (y2 - y1) / 2 - 5 + y1
# 右下(x2_1, y2_1)
x2_1 = (x2 - x1) / 2 + 5 + x1
y2_1 = (y2 - y1) / 2 + 5 + y1

#  円の作成
canvas.create_oval(x1_1, y1_1, x2_1, y2_1, width=5, fill="#ff0000")


# Canvasの作成
#canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
#canvas.pack(fill = tk.BOTH, expand = True)
#canvas.create_oval(x0, y0, x1, y1, )
# 線の描画
#canvas.create_line(20, 10, 280, 190, fill = "Blue", width = 5)

root.mainloop()