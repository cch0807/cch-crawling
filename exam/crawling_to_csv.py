import csv

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus

url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"

html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

total = soup.select(".api_txt_lines.total_tit")
search_list = []

for i in total:
    temp = []
    temp.append(i.text)
    temp.append(i.attrs["href"])
    search_list.append(temp)

f = open("result.csv", "w", encoding="utf-8", newline="")
csvWriter = csv.writer(f)

for i in search_list:
    csvWriter.writerow(i)

f.close()

print("end")
