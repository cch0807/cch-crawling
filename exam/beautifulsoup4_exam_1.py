from bs4 import BeautifulSoup
import requests

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"

req = requests.get(base_url)

# print(req.text)

soup = BeautifulSoup(req.text, "html.parser")

# print(soup)

# items = soup.select(".api_txt_lines.total_tit")
items = soup.select(".total_wrap.api_ani_send")

# print(items)
# print(items[0])
# print(items[1].text)

for rank_num, item in enumerate(items, 1):
    ad = item.select_one(".link_ad")
    if ad:
        continue
    print(f"<<{rank_num}>>")

    blog_title = item.select_one(".sub_txt.sub_name").text
    print(f"{blog_title}")

    post_title = item.select_one(".api_txt_lines.total_tit._cross_trigger")
    print(f"{post_title.text}")
    # print(f"{post_title['href']}")

    print()
