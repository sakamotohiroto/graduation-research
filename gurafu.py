import numpy as np
import openpyxl
import matplotlib.pyplot as plt

#カメラのexcelファイルを読み込む
wb = openpyxl.load_workbook('./Book1.xlsx')
ws = wb['Sheet1']

#シャツのexcelファイルを読み込む
# wb2 = openpyxl.load_workbook('./Book1.xlsx')
# ws2 = wb2['Sheet1']

#カメラのデータを格納する配列
time_arry = []
val_arry = []

#シャツのデータを格納する配列
time_arry2 = []
val_arry2 = []

#カメラのデータをexcelから配列に入れる処理
for row in ws.iter_cols():
    for cell in row:
        if cell.col_idx == 1:
            time_arry.append(cell.value)
        if cell.col_idx == 2:
            val_arry.append(cell.value)

#シャツのデータをexcelから配列に入れる処理
# for row in ws2.iter_cols():
#     for cell in row:
#         if cell.col_idx == 1:
#             time_arry.append(cell.value)
#         if cell.col_idx == 2:
#             val_arry.append(cell.value)


fig, ax = plt.subplots()
ax.plot(time_arry,val_arry)
# ax[1].plot(time_arry2,val_arry2) #３９行目をax[0]に変える

plt.show()
fig.savefig("figure.jpg")





