import tweepy
import os
import time

max_new_friends = os.environ['max_new_friends']
api_key = os.environ['api_key']
api_secret = os.environ['api_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']
timeout = os.environ['timeout']
keyword = os.environ['keyword']

friends = []
followers = []
people = []
added_people = []

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def follow():
  i = 0
  for tweet in tweepy.Cursor(api.search, q=keyword, result_type="recent").items():
    user = tweet.user
    if user.id not in people:
			if user.id not in added_people:
				api.create_friendship(id=user.id)
      	added_people.append([user.id])
      	print("NAME: " + user.name + " DESC: " + user.description)
    
      	i = i + 1
      	if i == int(max_new_friends):
        	break
      	time.sleep(int(timeout))

def my_friends():
  for page in tweepy.Cursor(api.friends_ids).pages():
    friends.extend(page)

def my_followers():
  for page in tweepy.Cursor(api.followers_ids).pages():
    followers.extend(page)

print("max_new_friends=" + max_new_friends)

my_friends()
my_followers()	
people_total = friends + followers
people = list(set(people_total))

follow()
