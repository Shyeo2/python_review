'''
  1) 일별시세 정보가 있는 페이지 접속
  2) 페이지에서 날짜 / 체결가가 들어있는 태그 검색 
  3) 태그 중에서 우리가 찾은 조건에 맞는 데이터만 가져옴
  4) 마지막 페이지까지 반복함 

'''
import requests 
import bs4

page_no = 1
page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"

source = requests.get(page_url).text
source = bs4.BeautifulSoup(source)

last_url = source.find_all("td", class_ = "pgRR")[0].find_all("a")[0]["href"]
# 마지막 페이지 번호 찾기 
last_page = int(last_url.split('&page=')[-1])

date_list = []
prices_list = []

for page_no in range(1, last_page+1):
  page_url  = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"

  source = requests.get(page_url).text
  source = bs4.BeautifulSoup(source)
  # 날짜 크롤링 
  dates = source.find_all('td', class_ = 'date')
  for date in dates:
    date_list.append(date.text)

  # 체결가 추출 
  prices = source.find_all('td', class_ = 'number_1')
  for price in prices[::4]:
    prices_list.append(price.text)

print(len(date_list))
print(len(prices_list))

print(date_list)
print(prices_list)

import pandas as pd 

df = pd.DataFrame({"date ": date_list , "price" : prices_list})
print(df)

df.to_excel("KPI200.xlsx", index=False)


# print(len(date_list))
# print(len(prices_list))

 #/html/body/div/table[2]/tbody/tr/td[11]/a
# result = source.find_all("td", class_ = "pgRR")[0]
# print(result)

