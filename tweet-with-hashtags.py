from __future__ import print_function
from google.cloud import vision
from pprint import pprint
import re
import tweepy
import credentials

image_uri = 'https://upload.wikimedia.org/wikipedia/commons/4/4c/Neminath_Ji.jpg'

client = vision.ImageAnnotatorClient()
image = vision.Image()
image.source.image_uri = image_uri

response = client.label_detection(image=image)

tweet_content = ""

for item in response.label_annotations:
    desc = re.sub(r' ', '', item.description)
    desc = desc.lower()
    desc = "#" + desc
    tweet_content = tweet_content + desc + " "

# Authenticate to Twitter
auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN_KEY, credentials.ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status(tweet_content)

print("Tweet doned with the following content: " + tweet_content)