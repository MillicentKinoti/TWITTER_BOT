import tweepy
import time

auth= tweepy.OAuthHandler('consumer_key','consumer_secret')
auth.set_access_token('access_key','access_secret')

api=tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
#print(user)
#this prints all my twitter details

#shows the list of all my twitter followers

#for follower in tweepy.Cursor(api.followers).items():
 #   print(follower.name

 
search='search term'# e.g @freeCodeCamp
number_of_tweets = 500
for tweet in tweepy.Cursor(api.search, search).items(number_of_tweets):
     try:
         print('Tweet Liked')
         tweet.favorite()
         print('Retweeted')
         tweet.retweet()
         time.sleep(10)
     except tweepy.TweepError as e:
         print(e.reason)
     except StopIteration:
         break