from google.cloud import vision

client = vision.ImageAnnotatorClient()

image_to_open = 'images/public-domain-image.jpg'

with open(image_to_open, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

text_response = client.text_detection(image=image)

texts = [text.description for text in text_response.text_annotations]

print(texts[0])