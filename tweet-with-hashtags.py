import tweepy
import kredentiaalit

def detect_labels(path):
    """Detects labels in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    hashtag_string=""
    for label in labels:
        #print(label.description)
        hashtag=label.description.replace(" ", "")
        hashtag=hashtag.lower()
        hashtag_string=hashtag_string + "#" + hashtag + " "

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
    return(hashtag_string)

status=detect_labels("perhonen.jpg")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(kredentiaalit.consumer_key, kredentiaalit.consumer_secret)
auth.set_access_token(kredentiaalit.access_token, kredentiaalit.access_token_secret)

# Create API object
api = tweepy.API(auth)

# load imag
imagePath = "./perhonen.jpg"

# Send the tweet.
api.update_with_media(imagePath, status)

