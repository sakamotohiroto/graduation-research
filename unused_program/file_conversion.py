#csvファイルをexcelファイルに変換するプログラム respiration.csv → sample.xlsx
import pandas as pd
import openpyxl
csv_file = 'respiration.csv'
df = pd.read_csv(csv_file)
xlsx_file = 'sample.xlsx'
df.to_excel(xlsx_file, engine='openpyxl', index=False)