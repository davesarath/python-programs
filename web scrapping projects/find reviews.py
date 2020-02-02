import bs4
import requests

page_url="https://www.cricbuzz.com/live-cricket-scores/26548/zim-vs-sl-1st-test-sri-lanka-tour-of-zimbabwe-2020"

page= requests.get(page_url)
# print(page)
soup = bs4.BeautifulSoup(page.content,'lxml')       # you need to pip install "xml"
# print(soup)

scor = soup.select("#page-wrapper #matchCenter .cb-col-scores .cb-scrs-wrp")

for match in scor:
    print(match.text)

