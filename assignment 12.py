
# q1

'''
An access token is an object that describes the security context of a process or thread. The information in a token includes the identity and privileges of the user account associated with the process or thread. ... The security identifier (SID) for the user's account. SIDs for the groups of which the user is a member.
consumer_key="6VN4R5D1tiC0KTjZqrf83vP6X"
consumer_secret="FTll6EDOfDsKx3kDmrorxVTvvvKF5zPQwBHeAE8ismOnsMqkkb"
access_token="1011804333061517312-dJhtkCa8LZeE8Noio2MlxFMm7IXIKj"
access_secret="yKfeV5n6NUqdFKOcbRFswBEuuH7v1JglQUgnZe4waqjht"

'''

# q2


'''
Service. Google Public DNS operates recursive name servers for public use at the IP addresses 8.8.8.8 and 8.8.4.4 for IPv4 service, and 2001:4860:4860::8888 and 2001:4860:4860::8844, for IPv6 access. The addresses are mapped to the nearest operational server by anycast routing.




Below are some of the most common active IP addresses for Facebook.com:

    69.63.176.13
    69.63.181.15
    69.63.184.142
    69.63.187.17
    69.63.187.18
    69.63.187.19
    69.63.181.11
    69.63.181.12

'''


# q3

from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy
oauth=tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
print(api.search("#sanju"))



# q4
'''
A library is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of projects. (Various specialized services in our case)

An API is an interface for other programs to interact with your program or library  without having direct access. ( giving specifications for our need to various vendors in our case)

A Library is a chunk of code that you can call from your own code, to help you do things more quickly/easily. For example, a Bitmap Processing library will provide facilities for loading and manipulating bitmap images, saving you having to write all that code for yourself.a library performs specific, well-defined operations.

An API (application programming interface) is a term meaning the functions/methods in a library that you can call to ask it to do things for you - the interface to the library.An API is an interface for other programs to interact with your program without having direct access.

'''


#  q5

from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy


oauth=tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
print(api.search("#sanju"))

user=api.get_user('isha goyal')
print (user.screen_name)
print (user.followers_count)