import tweepy
import time
import os

api_key = os.environ['api_key']
api_secret = os.environ['api_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']
timeout = os.environ['timeout']
max_friends_to_destroy = os.environ['max_friends_to_destroy']

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

friends = []
followers = []

def my_friends():
	for page in tweepy.Cursor(api.friends_ids).pages():
		friends.extend(page)

def my_followers():
	for page in tweepy.Cursor(api.followers_ids).pages():
		followers.extend(page)

my_friends()
my_followers()
unfollow_friends = list(set(friends) - set(followers))

def unfollow():
  i = 0
  for userid in unfollow_friends:
    api.destroy_friendship(id=userid)
    print("iUnfollow user: " + str(userid))
    i = i + 1
    if i == int(max_friends_to_destroy):
      break
    time.sleep(int(timeout))

unfollow()
