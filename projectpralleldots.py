from paralleldots import set_api_key,get_api_key
from paralleldots import *
from keys3 import api_key
set_api_key(api_key)
get_api_key()
text="have a nice day"
sentiment_value=sentiment(text)
print(sentiment_value["sentiment"])
location_value=location(text)