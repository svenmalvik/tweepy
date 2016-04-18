# tweepy
Follows and unfollows users based on defined keywords

## Follow
```
docker run -it --rm --name follow \
  -v ~/projects/tweepy/:/usr/src/app/ \
  -e max_new_friends=10 \
  -e api_key=<YOUR_VALUE> \
  -e api_secret=<YOUR_VALUE> \
  -e access_token=<YOUR_VALUE> \
  -e access_token_secret=<YOUR_VALUE> \
  -e timeout=2 \
  -e keyword=#devops \
  tweepy python follow.py
```
## Unfollow
```
docker run -it --rm --name unfollow \
  -v ~/projects/tweepy/:/usr/src/app/ \
  -e api_key=<YOUR_VALUE> \
  -e api_secret=<YOUR_VALUE> \
  -e access_token=<YOUR_VALUE> \
  -e access_token_secret=<YOUR_VALUE> \
  -e timeout=2 \
  -e max_friends_to_destroy=10 \
  python unfollow.py
```
