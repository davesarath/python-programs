import bs4
import requests
def flp(name):
    page_url="https://www.flipkart.com/search?q="+name

    page= requests.get(page_url)
    print(page)
    soup = bs4.BeautifulSoup(page.content,'lxml')       # you need to pip install "xml"
    # print(soup)

    ### method two once
    scor = soup.select("._1HmYoV .bhgxx2 ._31qSD5 ._1-2Iqu div ._3wU53n")
    for match in scor:
        print("strt:",match.text)


def main():
    while(True):
        name=input("Enter product name : ")
        flp(name)


if __name__=="__main__":
    main()