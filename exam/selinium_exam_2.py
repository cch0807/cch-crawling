import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

base_url = "https://naver.com"

driver.get(base_url)

time.sleep(1)

# iframe = driver.find_element(By.CLASS_NAME, "input_text").send_keys("블랙핑크")
# time.sleep(5)
# driver.switch_to.frame(iframe)

# driver.find_element(By.ID, "query").send_keys("뉴진스")
# time.sleep(1)

# driver.find_element(By.CSS_SELECTOR, "#query").send_keys("블랙핑크")
# time.sleep(1)

# driver.find_element(By.CSS_SELECTOR, "[title='검색어 입력']").send_keys("에스파")
# time.sleep(1)

# driver.find_element(By.CSS_SELECTOR, "[placeholder='검색어를 입력해 주세요.']").send_keys("에스파")
# time.sleep(1)

# driver.find_element(By.XPATH, '//*[@id="query"]').send_keys("에스파")
# time.sleep(1)

# driver.find_element(By.LINK_TEXT, "쇼핑").click()
# time.sleep(1)

# driver.find_element(By.PARTIAL_LINK_TEXT, "쇼핑").click()
# time.sleep(1)

# driver.find_element(By.TAG_NAME, "")
# time.sleep(1)

navs = driver.find_elements(By.CSS_SELECTOR, ".shortcut_item")

for nav in navs:
    print(nav.get_attribute("outerHTML"))
    print()
