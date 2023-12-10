#excelファイルの呼吸を測定したデータを波グラフ化するプログラム
#excelでグラフ化する前にちゃんとカメラでデータがとれてるか確認するのに使用
import numpy as np
import openpyxl
import matplotlib.pyplot as plt

#excelファイルの読み込み
wb = openpyxl.load_workbook('./Book1.xlsx')
ws = wb['Sheet1']

#データをグラフ化のために一時配列に入れるための配列の定義
time_arry = []
val_arry = []

#データをexcelから配列に入れる処理
for row in ws.iter_cols():
    for cell in row:
        if cell.col_idx == 1:
            time_arry.append(cell.value)
        if cell.col_idx == 2:
                val_arry.append(cell.value)

#配列の値を使ってグラフ化
fig, ax = plt.subplots()
ax.plot(time_arry,val_arry) 
plt.show()
fig.savefig("figure.jpg")





