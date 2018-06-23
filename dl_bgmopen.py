"""
全國營業(稅籍)登記資料集
http://data.gov.tw/node/9400

"""

import os
import requests
from datetime import datetime, date
import sys

todayFileName = ''.join(str(date.today()).split('-')) + '.zip'

files = os.listdir()

if todayFileName in files:
    print("今日資料已下載 : " + todayFileName)

else:
    print("today: " + str(date.today()) + ' , 開始下載今日資料...')


# res 開始抓檔
res = requests.get('http://www.fia.gov.tw/opendata/bgmopen1.zip')

# res 狀態無誤的話, return None
if res.raise_for_status() != None:
    print("網址錯誤? 伺服器錯誤? ......")

else:
    # 建立檔案
    ff = open(todayFileName, 'wb')
    
    # buffer write
    for chunk in res.iter_content(1000000):
        ff.write(chunk)
    ff.close()

res.close()
print(todayFileName + ' 下載完成!')
