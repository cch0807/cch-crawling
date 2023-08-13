import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(base_url)

time.sleep(2)

for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

items = soup.select(".api_txt_lines.total_tit")

for e, item in enumerate(items, 1):
    print(f"{e} : {item.text}")
