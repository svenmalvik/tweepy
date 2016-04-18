docker run -it --rm --name follow \
  -e max_new_friends=10 \
  -e api_key=<YOUR_VALUE> \
  -e api_secret=<YOUR_VALUE> \
  -e access_token=<YOUR_VALUE> \
  -e access_token_secret=<YOUR_VALUE> \
  -e timeout=2 \
  -e keyword=#devops \
  svenmalvik/tweepy python follow.py
