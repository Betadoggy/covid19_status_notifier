from bs4 import BeautifulSoup
import os
import sys
import datetime
import requests
from pyfiglet import Figlet # ASCII 텍스트 아트 모듈

# Figlet 객체
f = Figlet(font='slant')

# 인증키 디코딩
api_key = "ayVCtybZx%2B%2FDZiEINx1jlkml4UI%2BIiYjaePes3S2TQwtkzbdaKg94XMQVUgjP%2FDCHsVbETilML4ofr%2FfqK4Lhw%3D%3D"
api_key_decode = requests.utils.unquote(api_key)

# 현재시간, 시작/종료 일자 포매팅
cur_time = datetime.datetime.now()
eday = str(cur_time.date()).replace('-','')
sday = str(cur_time.date()-datetime.timedelta(days=2)).replace('-','')  # 현재일 - 2일

url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson"
parameters = {
    "serviceKey":api_key_decode,
    "pageNo":1,
    "numOfROws":10,
    "startCreateDt":sday,
    "endCreateDt":eday}

req = requests.get(url, params = parameters)
html = req.text
soup = BeautifulSoup(html, 'html.parser')


def sepLine():
    print("="*10)

def clear():
    os.system('cls')

def invalidInputError():
    print("INVALID INPUT! try again...")

if __name__ == "__main__":
    print(f.renderText("COVID-19 STATUS"))
    sepLine()

    # 현재시간
    cur_time = datetime.datetime.now()
    print("Current Time \t%s" % cur_time)

    # 기준일 
    statedate = soup.find_all('statedt')[0].text
    print("State Date \t%s" % statedate[:4]+'-'+statedate[4:6]+'-'+statedate[6:])

    # 총, 일일 확진자
    totalcases = int(soup.find_all('decidecnt')[0].text)
    dailycases = totalcases - int(soup.find_all('decidecnt')[1].text)

    print("Daily Cases \t%d" % dailycases)
    print("Total Cases \t%d" % totalcases)

    sepLine()
    print("To exit, type 'exit'")

    while True:
        userInput = input()
        if userInput == "exit":
            sys.exit()
        else:
            invalidInputError()
            continue