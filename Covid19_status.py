from bs4 import BeautifulSoup
import sys
import datetime
import requests

open_api_key = "ayVCtybZx%2B%2FDZiEINx1jlkml4UI%2BIiYjaePes3S2TQwtkzbdaKg94XMQVUgjP%2FDCHsVbETilML4ofr%2FfqK4Lhw%3D%3D"

info_url = "https://openapi.data.go.kr/openapi/service/rest/Covid19"
response = requests.get(info_url)
soup = BeautifulSoup(response.content, 'html.parser')

data = soup.find_all('item')

if __name__ == "__main__":
    print("COVID-19 STATUS")

    cur_time = datetime.datetime.now()
    print("Current time : %s" % cur_time)

    for item in data:
        newcases = item.find('decideCnt')
        print("New Cases : newcases")

    while True:
        userInput = input()
        if userInput == "exit":
            sys.exit()