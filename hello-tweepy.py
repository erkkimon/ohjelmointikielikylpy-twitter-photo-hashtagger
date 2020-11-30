import tweepy
import credentials

# Authenticate to Twitter
auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN_KEY, credentials.ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello once again")
