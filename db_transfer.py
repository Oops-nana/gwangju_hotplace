from datetime import datetime
import imp
from django.template import engine
import pymysql
from datetime import datetime
from numpy import eye
import requests
import sqlalchemy as db
import pandas as pd

url = "http://apis.data.go.kr/6290000/msmartglrbaseinfo/getmsmartglrbaseinfo?serviceKey=Rlfdq09A0Ugnv74UoCTmxwta5%2Fx1TvZJEappaXfTi67p8u8sz%2Bjj5NZw49ooBRwrR534ex7u9TJkr%2Fj3zHYOtg%3D%3D&numOfRows=100&pageNo=1&type=json"
#관광지 데이터
resonse = requests.get(url)
parseResponse = resonse.json() #json을 딕셔너리로 변경

row = parseResponse["MsmArtGlrBaseInfo"]
datas = []

tour_id = 3000
import sqlalchemy.dialects.mysql
class sqlalchemy(sqlalchemy.types.DATETIME):
    def __init__(self):
        sqlalchemy.dialects.mysql.DATETIME.__init__(self,timezone=True, fsp=None)


# for r in row :
#     dict = {}
#     dict['place_id'] = tour_id + int(r["id"])
#     dict['place_name'] = r["festivalNm"]
#     dict['lnglat'] = r["lat"] +' '+ r["lng"]
#     dict['road_address'] = r["addrRoad"]
#     dict['phone'] = r["tel"]
#     dict['info'] = r["festivalInfo"]
#     dict['rate'] = ''
#     datas.append(dict)
for r in row :
    dict = {}
    dict['place_id'] = tour_id + int(r["id"])
    dict['website'] = r["homePage"]
    dict['week_begin'] = r["weekdayBeginTime"]
    dict['week_end'] = r["weekdayEndTime"]
    dict['holiday_begin'] = r["holidayBeginTime"]
    dict['holiday_end'] = r["holidayEndTime"]
    dict['close_info'] = r["closeInfo"]

    datas.append(dict)

print(datas)

tour_dataFrame = pd.DataFrame(datas)
print(tour_dataFrame)

engine = db.create_engine('mysql+pymysql://root:aivle@127.0.0.1:3306/aaa')

tour_dataFrame.to_sql("museum_detail", engine, index=False, if_exists="append")