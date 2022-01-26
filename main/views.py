from marshal import loads
from black import jupyter_dependencies_are_installed
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json
import pymysql.cursors
from django.shortcuts import render

from django.template import exceptions
from .models import CommonPlace
# 위도 lat 30 [0]
# 경도 lng 100 [1]
# 클라이언트에서 받아온 경도,위도 정보를 가지고 데이터베이스에 해당하는 모든 경도,위도 중 클라이언트가 설정한 범위 이내에 있는 경도 위도 세트만 반환.
# 반환된 세트 이후


def dictToJson(jsondata):
    returnJson = []
    for i in range(len(jsondata)):
        returnJson.append(json.loads(json.dumps(jsondata[i]).encode()))
    return returnJson


def calculateLocation(places, startLat, startLng, distance):
    data_obj = []
    lnglat_set = places.objects.values_list("lng", "lat")
    count = CommonPlace.place_count_by_count()
    for i in range(count):
        # 좌표셋을 가져옴.
        # lnglat_set = places.objects.values_list("lng", "lat")
        # print(lnglat_set)
        cursor = connection.cursor()

        startLat_ = startLat
        startLng_ = startLng
        dest_lng = lnglat_set[i][0]
        dest_lat = lnglat_set[i][1]

        strSql = f"SELECT distinct *, (6371 * acos (cos(radians({dest_lat}) )* cos( radians({startLat_}) )* cos( radians({startLng_} ) - radians({dest_lng}) )+ sin ( radians({dest_lat}) )* sin( radians({startLat_} ))) )AS distance from place_common having distance <= {distance} order by distance limit 1;"

        # 쿼리 실행
        result = cursor.execute(strSql)
        print(result)
        row = [x[0] for x in cursor.description]

        # 실행한 쿼리결과를 저장
        data = cursor.fetchall()
        connection.close()

        # 쿼리로 받아온 데이터를 딕셔너리형식으로 변환
        jsondata = []
        for result in data:
            jsondata.append(dict(zip(row, result)))

            # 딕셔너리를 인코딩하여 json형식으로 변환
        data_obj.append(dictToJson(jsondata))

    return data_obj

    # data_obj[i] = datas[i]
    # 시작위치와 목표위치의 거리 값들 중 맥스 거리보다 작은 값들에 해당하는 좌ㅇ표와 그 장소 정보
    # for target in datas:
    #     if target <= distance:
    #         places.objects.get(lat = )
    #         data_obj['lat'] = target['lat']
    #         data_obj['lng'] = target['lng']

    # except:
    #     connection.rollback()
    #     print('에러', exceptions)


@ csrf_exempt
def requestLocation(request):
    places = CommonPlace
    startLat = request.GET.get('startLat')
    # print(startLat)
    startLng = request.GET.get('startLng')
    # print(startLng)
    distance = request.GET.get('distance')
    # print(distance)
    result = calculateLocation(places, startLat, startLng, distance)
    # print(data)

    return JsonResponse(result, safe=False)


# Create your views here.
