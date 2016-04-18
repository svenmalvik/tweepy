docker run -it --rm --name unfollow \
  -e api_key=<YOUR_VALUE> \
  -e api_secret=<YOUR_VALUE> \
  -e access_token=<YOUR_VALUE> \
  -e access_token_secret=<YOUR_VALUE> \
  -e timeout=2 \
  -e max_friends_to_destroy=10 \
  svenmalvik/tweepy unfollow.py
