
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
from collections import Counter
import nltk
from nltk.corpus import *
nltk.download('stopwords')

def retrive_tweets():
    tweet=input("enter the hashtag")
    print(api.search(tweet))
def count():
    username=input("input user name")
    user=api.get_user(username)
    print(user.followers_count)
def sentiments():
    text = "have a nice day"
    sentiment_value = sentiment(text)
    print(sentiment_value["sentiment"])

def compare():
    narendramodi = input().split()
    realdonaldtrump=input().spilt()
    y=input().spilt()
    z=input().spilt()
   # w = input("enter the tweet 1 which we want to compare")
    #x = input("enter the tweet 2 which we want to compare")
    tweets1 = api.user_timeline(screen_name="narendramodi")
    tweets2 = api.user_timeline(screen_name= "realdonaldtrump")
    s1 = ''
    s2 = ''
    for tweet in tweets1:
        s1 += tweet.text
    print(s1.count(y))
    for tweet in tweets2:
        s2 += tweet.text
    print(s2.count(z))


def loc_lan_tz():
    t=input("enter the hashtag u want to search")
    g=api.search(t)
    for i in g:
        print('location',i.user.location)
        print('language',i.user.lang)
        print('time zone',i.user.time_zone)
def top_usage():
    t = input("enter the hashtag u want to search")
    text = api.search(t)
    #text = "hello to all i am isha from punjabi university patiala patiala is very nice place"
    stop_words = set(stopwords.words('english'))
    print(stop_words)
    list1 = text.split()
    print(list1)
    for i in list1:
        if i not in stop_words:
            print(i)
    count = Counter(list1).most_common(5)
    print(count)
def tweet_message():
    update_status = api.update_status(status="Hello Everyone !")
    print(update_status)

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
dis()
option=int(input("what option you want: "))
if(option==1):
    retrive_tweets()
    dis()
elif(option==2):
    count()
    dis()
elif(option==3):
    sentiments()
    dis()
elif(option==4):
    compare()
    dis()
elif(option==5):
    loc_lan_tz()
    dis()
elif(option==6):
    top_usage()
    dis()
elif(option==7):
    tweet_message()
    dis()
else:
    print("choose a correct option")




from keys2 import consumer_key,consumer_secret,access_token,access_secret
import tweepy
import json


oauth=tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
x=print(api.search("#sanju"))
for tweet in x:
    json_data=json.dumps(tweet._json)

print(json_data)
