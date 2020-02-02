# pip install textblob
from textblob import TextBlob


txt="not bad  choice"
analysis = TextBlob(txt)
print(analysis.sentiment.polarity)
if analysis.sentiment.polarity > 0:
    print('positive')
elif analysis.sentiment.polarity == 0:
    print('neutral')
else:
    print('negative')

