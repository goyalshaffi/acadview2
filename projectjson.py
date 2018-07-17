'''
import json
#sourceFile=open()
text="hello freinds"
json_data=json.load(text)
parser=tweepy.parsers.JSONParser()
print(json_data)
'''
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
