import requests
from flask import Flask, render_template
import json
from datetime import datetime

app = Flask(__name__)

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




@app.route('/' , methods=['GET', 'POST'])
def method_get():  # put application's code here
    return render_template('ex.html')

@app.route('/method_get_act', methods=['GET', 'POST'])
def method_get_act():  # put application's code here
    if requests.method == 'GET':
        now = datetime.now()
        now_date = now.strftime('%y%m%d')
        now_hour = now.hour
        now_time = now.minute


        apiKey = "k2FhBBQxor2i%2B9pBvFADgh%2B6ld8CDQul1g46DdYsfyg40rzqKGlBNpHWPcgV88Nj0FFBbu2iFfC24Q3cNzUCXg%3D%3D"
        numOfRow = '100'

        if( now_time < 45):                           #초단기예보는 매시간 45분을 기준으로 base_time이 갱신,  18시45분에 18시
            if((now_hour / 10) < 1):
                now_hour -= 1
                now_hour = '0' + str(now_hour)
                now_hour = str(now_hour) + '30'
            else:
                now_hour -= 1
                now_hour = str(now_hour) + '30'
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
        for i in range(24, 30):
            result=arr[i]["baseDate"]+"일"+arr[i]["fcstTime"]+"시"+arr[i]["fcstValue"]+"도입니다"

        return render_template('ex.html', result=result)

if __name__ == '__main__':
    app.run()

