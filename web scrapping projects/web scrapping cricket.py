import bs4
import requests


page_url="https://www.cricbuzz.com/cricket-match/live-scores"

page= requests.get(page_url)
# print(page)
soup = bs4.BeautifulSoup(page.content,'lxml')       # you need to pip install "xml"
# print(soup)


# ###using find all
# contain_class="cb-mtch-lst cb-col cb-col-100 cb-tms-itm"
# scor =  soup.find_all(class_=contain_class)
#
# row_Container="cb-lv-scrs-col"
# for match in scor:
#     data_table=match.find(class_=row_Container)
#     if data_table:
#         print(data_table.get_text())


### using select
## method 1 again and again
contain_class="cb-mtch-lst cb-col cb-col-100 cb-tms-itm"
scor = soup.select(".cb-mtch-lst")
row_Container="cb-lv-scrs-col"
for match in scor:
    data_table=match.select(".cb-lv-scrs-col")
    if data_table:
        print(data_table[0].get_text())



### method two once
# scor = soup.select(".cb-mtch-lst .cb-lv-scrs-col")
# for match in scor:
#     print(match.get_text())
