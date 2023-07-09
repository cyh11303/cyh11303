import requests
from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
        initTime = datetime.now().strftime('%H%m')
        initDate = datetime.now().strftime('%Y%m%d')
        # 현재시간이 API 갱신시간인 02시10분 05시10분 08시10분  11시10분  14시10분  17시10분 20시10분 23시10분이 되지않았을 때 이전 시간의 API를 사용토록함
        # 현재시간이 새벽2시보다 이르면 오늘의 예보가 아직 생성되지 않았을 시기이므로 전날의 예보를 사용
        if int(initTime) < 210:
                initDate = int(initDate) - 1
                initTime = "2300"
        elif int(initTime) < 510:
                initTime = "0200"
        elif int(initTime) < 810:
                initTime = "0500"
        elif int(initTime) < 1110:
                initTime = "0800"
        elif int(initTime) < 1410:
                initTime = "1100"
        elif int(initTime) < 1710:
                initTime = "1400"
        elif int(initTime) < 2010:
                initTime = "1700"
        elif int(initTime) < 2310:
                initTime = "2000"
        else:
                initTime = "2300"
        # print(initDate)
        # print(initTime)
        # api url의 https 형식으로 불러올 시 열리지않는 문제가 생김
        api = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey=k2FhBBQxor2i%2B9pBvFADgh%2B6ld8CDQul1g46DdYsfyg40rzqKGlBNpHWPcgV88Nj0FFBbu2iFfC24Q3cNzUCXg%3D%3D&pageNo=1&numOfRows=1000&dataType=json&base_date={initDate}&base_time={initTime}&nx=55&ny=127"
        # 이를 해결하기위해 api의 https를 http로 바꿔준 후 requests.get()에서 verify=False를 이용하여 HTTPS 요청에 대한 SSL 인증 확인과정을 없앴음 (참고: https://seculog.tistory.com/9)
        result = requests.get(api, verify=False)
        # api에서 json형식의 데이터를 받아옴
        result = json.loads(result.text)
        arr = result["response"]["body"]["items"]["item"]
        temp = []
        date = []
        time = []
        # 리스트의 총 길이를 알기 위해 count를 이용하였음
        count = 0
        for i in range(0, 809):
                print(arr[i])
                count += 1
                print(count)
                # 카테고리의 값이 TMP 즉, 기온을 나타낼 경우에만 date, time, temp에 예상날짜, 예상시간, 예상값을 각각의 리스트에 추가함
                if arr[i]["category"] == 'TMP':
                                temp.append(arr[i]["fcstValue"])
                                date.append(arr[i]["fcstDate"])
                                time.append(arr[i]["fcstTime"])
                # date를 zip()을 이용해서 {1: a, 2: b, 3:c}와 같은 딕셔너리형으로 바꾸어줌
                date_dict = dict(zip(range(1, len(date) + 1), date))
                # 딕셔너리형으로 변환된 date를 json형식으로 바꿈
                json.dumps(date_dict)
                time_dict = dict(zip(range(1, len(time) + 1), time))
                json.dumps(time_dict)
                temp_dict = dict(zip(range(1, len(temp) + 1), temp))
                json.dumps(temp_dict)

        return render_template("weather.html", date=date_dict, time= time_dict, temp=temp_dict)

# 사용자가 특정 날짜를 검색한 경우, 특정날짜의 값들만 출력하도록 함
@app.route('/method_get', methods=['GET', 'POST'])
def method_get():  # put application's code here
        if request.method == 'GET':
                initTime = datetime.now().strftime('%H%m')
                initDate = datetime.now().strftime('%Y%m%d')
                if int(initTime) < 210:
                        initDate = int(initDate) - 1
                        initTime = "2300"
                elif int(initTime) < 510:
                        initTime = "0200"
                elif int(initTime) < 810:
                        initTime = "0500"
                elif int(initTime) < 1110:
                        initTime = "0800"
                elif int(initTime) < 1410:
                        initTime = "1100"
                elif int(initTime) < 1710:
                        initTime = "1400"
                elif int(initTime) < 2010:
                        initTime = "1700"
                elif int(initTime) < 2310:
                        initTime = "2000"
                else:
                        initTime = "2300"

                api = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey=k2FhBBQxor2i%2B9pBvFADgh%2B6ld8CDQul1g46DdYsfyg40rzqKGlBNpHWPcgV88Nj0FFBbu2iFfC24Q3cNzUCXg%3D%3D&pageNo=1&numOfRows=1000&dataType=json&base_date={initDate}&base_time={initTime}&nx=61&ny=127"
                result = requests.get(api, verify=False)
                result = json.loads(result.text)
                arr = result["response"]["body"]["items"]["item"]
                temp=[]
                date=[]
                time=[]
                count=0
                # weather.html에서 get 방식으로 사용자에게 입력받은 날짜를 받아옴
                user_date = request.args.get("date1")
                for i in range(0,809):
                        count+=1
                        if arr[i]["category"] == 'TMP':
                                #category가 TMP(기온)인 경우 중 예상날짜가 사용자가 입력한 날짜의 값만 리스트에 담도록 함
                                if arr[i]["fcstDate"]==user_date:
                                        print(arr[i]["fcstValue"])
                                        temp.append(arr[i]["fcstValue"])
                                        date.append(arr[i]["fcstDate"])
                                        time.append(arr[i]["fcstTime"])
                date_dict=dict(zip(range(1, len(date)+1), date))
                json.dumps(date_dict)
                time_dict=dict(zip(range(1, len(time)+1), time))
                json.dumps(time_dict)
                temp_dict=dict(zip(range(1, len(temp)+1), temp))
                json.dumps(temp_dict)
                print(date_dict)
                print(temp_dict)
                print(time_dict)
                return render_template("weather.html", date1=user_date, date=date_dict, time= time_dict, temp=temp_dict)

if __name__ == '__main__':
    app.run()


