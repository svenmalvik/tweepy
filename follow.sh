docker run -it --rm --name follow \
  -v ~/projects/tweepy/:/usr/src/app/ \
  -e max_new_friends=10 \
  -e api_key= \
  -e api_secret= \
  -e access_token= \
  -e access_token_secret= \
  -e timeout=2 \
  -e keyword=#devops \
  svenmalvik/tweepy python follow.py
