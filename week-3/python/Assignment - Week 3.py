import urllib.request as sightData
import json
import csv
# 連線網址取得json資料
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with sightData.urlopen(src) as response:
    sightData = json.load(response) #利用 json 模組處理 json 資料格式

#取得所有景點
sightList = sightData["result"]["results"]

#台北行政區列表
TaipeiRegion = ['中正區','萬華區','中山區','大同區',
                '大安區','松山區','信義區','士林區',
                '文山區','北投區','內湖區','南港區']

# 建立寫入CSV物件
getSight = open('data.csv',mode='w',newline='',encoding='utf-8') 
w = csv.writer(getSight)   

#將列表所需要的鍵各自提取並命名
for sight in sightList:
    stitle       =   sight["stitle"]
    address      =   sight["address"]
    longitude    =   sight["longitude"]
    latitude     =   sight["latitude"]
    ImgFileList  =   sight["file"]

    #比對 台北行政區列表  如address包含行政區域 則該景點就為 該行政區
    for region in TaipeiRegion:
       if region in address:
          SpotLocation = region
    
    #分割圖片網址並組合字串
    picLink = ImgFileList.split('https://')
    firstPicLink = 'https://' + picLink[1]
    
    # 寫入一列資料至CSV
    w.writerow([stitle,SpotLocation,longitude,latitude,firstPicLink])

    




