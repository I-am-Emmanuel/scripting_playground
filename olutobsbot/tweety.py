import tweepy
import time



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)



search = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I like that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# # Generous Bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'Adekunle Babatunde':
#         follower.follow()
#         break
#     # print(follower.name)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

