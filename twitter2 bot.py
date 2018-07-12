from keys2 import consumer_key,consumer_secret,access_token,access_secret
import tweepy
from paralleldots import set_api_key,get_api_key
from paralleldots import *
from keys3 import api_key
set_api_key(api_key)
get_api_key()



oauth=tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)

user=api.get_user('isha71413661')
# print (user.screen_name)
# print (user.followers_count)
def dis():
    print('''
1.Retrieve Tweets
2.Count the followers
3.Determine the sentiment
4.Compare tweets 
5.Determine location,language and time zone.
6.Analyze top usage 
7.Tweet a message 
8.Exit
'''
)
    option=int(input("what option you want: "))
dis()

option=int(input("what option you want: "))
if(option==1):
    print(api.search("#sanju"))
elif(option==2):
    print(user.followers_count)
elif(option==3):
    text = "have a nice day"
    sentiment_value = sentiment(text)
    print(sentiment_value["sentiment"])
elif(option==4):
    from collections import Counter
    import nltk
    from nltk.corpus import *

    nltk.download('stopwords')
    text = "hello to all i am isha from punjabi university patiala patiala is very nice place"
    stop_words = set(stopwords.words('english'))
    print(stop_words)
    list1 = text.split()
    print(list1)
    for i in list1:
        if i not in stop_words:
            print(i)
    count = Counter(list1).most_common(5)
    print(count)
elif(option==5):
    pass
elif(option==6):
    pass
elif(option==7):
    pass
else:
    print('exit')

from keys2 import consumer_key,consumer_secret,access_token,access_secret
import tweepy
import json


oauth=tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
#status=api.user_timeline(api.search("#sanju")))
#status=status_list[0]
x=print(api.search("#sanju"))
json_data=json.load(x)

print(json_data)

from collections import Counter
    import nltk
    from nltk.corpus import *

    nltk.download('stopwords')
    text = "hello to all i am isha from punjabi university patiala patiala is very nice place"
    stop_words = set(stopwords.words('english'))
    print(stop_words)
    list1 = text.split()
    print(list1)
    for i in list1:
        if i not in stop_words:
            print(i)
    count = Counter(list1).most_common(5)
    print(count)




