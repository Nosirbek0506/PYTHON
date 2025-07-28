import csv  # csv kutubxonasini chaqiramiz

# Fayl yaratamiz va yozamiz
with open('talabalar.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)  # yozuvchi (writer) obyekt
    writer.writerow(['Ism', 'Yosh', 'Kasb'])  # sarlavhalar
    writer.writerow(['Ali', 25, 'Dasturchi'])
    writer.writerow(['Vali', 30, "O'qituvchi"])
    writer.writerow(['Gulnoza', 22, 'Talaba'])

print("CSV fayl yaratildi va yozildi.")

import pandas as pd
df=pd.read_csv('talabalar.csv')
print(df)

print(df.columns)
print(df['Yosh'],["Ism"])