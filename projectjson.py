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
#status=api.user_timeline(api.search("#sanju")))
#status=status_list[0]
x=print(api.search("#sanju"))
json_data=json.load(x)

print(json_data)
