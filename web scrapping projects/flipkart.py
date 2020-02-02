import bs4
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
page_url="https://www.flipkart.com/google-pixel-3a-just-black-64-gb/product-reviews/itmfgk4jfgstaack?pid=MOBFFGFP7UHHJUZU&page="
analyzer=SentimentIntensityAnalyzer()
pros=0
cons=0
for i in range(1,2):
    page= requests.get(page_url+str(i))
    # print(page_url+str(i))
    soup = bs4.BeautifulSoup(page.content,'lxml')
    scor = soup.select(".bhgxx2 ._390CkK .qwjRop div div")
    for review in scor:
        # print(review.getText())
        senti=analyzer.polarity_scores(review.getText())
        if(senti["neg"]>senti["pos"]):
            cons+=1
        elif(senti["neg"]<senti["pos"]):
            pros+=1
print("total positive comments are {} and negative comments are{}".format(pros,cons))

