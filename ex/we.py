import requests
from flask import Flask, render_template, request
import json
from datetime import datetime

we = Flask(__name__)

# now = datetime.now()
# now_date = now.strftime('%y%m%d')
# now_hour = now.hour
# now_time = now.minute
#
#
# apiKey = "k2FhBBQxor2i%2B9pBvFADgh%2B6ld8CDQul1g46DdYsfyg40rzqKGlBNpHWPcgV88Nj0FFBbu2iFfC24Q3cNzUCXg%3D%3D"
# numOfRow = '100'
#
# if( now_time < 45):                           #초단기예보는 매시간 45분을 기준으로 base_time이 갱신,  18시45분에 18시
#     if((now_hour / 10) < 1):
#         now_hour -= 1
#         now_hour = '0' + str(now_hour)
#         now_hour = str(now_hour) + '30'
#     else:
#         now_hour -= 1
#         now_hour = str(now_hour) + '30'
# else:
#     now_hour = str(now_hour) + '30'
# base_date = '20'+str(now_date)
# # print(base_date)
# base_time = now_hour
# print(base_time)
# # print(base_time)
# nx = str(61)
# ny = str(127)
# api = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst?serviceKey={apiKey}&pageNo=1&numOfRows={numOfRow}&dataType=json&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}"
# print(api)
# result = requests.get(api, verify = False)
# result = json.loads(result.text)
# arr = result["response"]["body"]["items"]["item"]
# for i in range(24, 30):
#     print(arr[i]["baseDate"]+"일"+arr[i]["fcstTime"]+"시 온도는"+arr[i]["fcstValue"]+"도입니다")




@we.route('/' , methods=['GET', 'POST'])
def method_get():  # put application's code here
    return render_template('ex.html')

@we.route('/method_get_act', methods=['GET', 'POST'])
def method_get_act():  # put application's code here
    if request.method == 'GET':
        now = datetime.now()
        now_date = now.strftime('%y%m%d')
        now_hour = now.hour
        now_time = now.minute


        apiKey = "k2FhBBQxor2i%2B9pBvFADgh%2B6ld8CDQul1g46DdYsfyg40rzqKGlBNpHWPcgV88Nj0FFBbu2iFfC24Q3cNzUCXg%3D%3D"
        numOfRow = '100'

        if( now_time < 45):                           #초단기예보는 매시간 45분을 기준으로 base_time이 갱신,  18시45분에 18시
            if((now_hour / 10) <= 1):
                now_hour -= 1
                print(now_hour)
                now_hour = '0' + str(now_hour)
                print(now_hour)
                now_hour = str(now_hour) + '30'
                print(now_hour)
            else:
                now_hour -= 1
                now_hour = str(now_hour) + '30'
        else:
            if ((now_hour / 10) < 1):
                print(now_hour)
                now_hour = '0' + str(now_hour)
                print(now_hour)
                now_hour = str(now_hour) + '30'
                print(now_hour)
            else:
                now_hour = str(now_hour) + '30'
        base_date = '20'+str(now_date)
        # print(base_date)
        base_time = now_hour
        print(base_time)
        # print(base_time)
        nx = str(61)
        ny = str(127)
        api = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst?serviceKey={apiKey}&pageNo=1&numOfRows={numOfRow}&dataType=json&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}"
        print(api)
        result = requests.get(api, verify = False)
        result = json.loads(result.text)
        arr = result["response"]["body"]["items"]["item"]
        res={}
        date=[]
        time=[]
        temp=[]
        for i in range(24, 30):
            #result1.append(arr[i]["baseDate"]+"일"+arr[i]["fcstTime"]+"시"+arr[i]["fcstValue"]+"도입니다")
            # k = arr[i]["baseDate"] + " " + arr[i]["fcstTime"] + " " + arr[i]["fcstValue"]
            # result1.append(k.split())
            # for i in result1:
            #     i = i.strip().split()
            date.append(arr[i]["baseDate"])
            time.append(arr[i]["fcstTime"])
            temp.append(arr[i]["fcstValue"])

        print(date)
        print(time)
        print(temp)
        return render_template('ex.html', res=res, date=date, time=time ,temp=temp)

if __name__ == '__main__':

    we.run()
