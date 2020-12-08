from __future__ import print_function
from google.cloud import vision
from pprint import pprint
import re

image_uri = 'https://upload.wikimedia.org/wikipedia/commons/4/4c/Neminath_Ji.jpg'

client = vision.ImageAnnotatorClient()
image = vision.Image()
image.source.image_uri = image_uri

response = client.label_detection(image=image)

for item in response.label_annotations:
    desc = re.sub(r' ', '', item.description)
    desc = desc.lower()
    desc = "#" + desc
    print(desc)

#for label in response.label_annotations:
#    print(label)

#print('Labels (and confidence score):')
#print('=' * 30)
#for label in response.label_annotations:
#    print(label.description, '(%.2f%%)' % (label.score*100.))

# Ajetaan seuraavalla terminaalikomennolla hakemistossa, johon hello-google-machine-vision.py on tallennettu:
# GOOGLE_APPLICATION_CREDENTIALS=~/primordial-hall-key.json python3 label-detection.py
# Lisäksi kotihakemistosta tarttee löytyä primordial-hall-key.json 
