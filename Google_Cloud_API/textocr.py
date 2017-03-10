# @Project : ftry
# @Filename: textocr
# @Date    : 2017-03-03
# @Author  : Shiyue Nie

import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
#from oauth2client.client import GoogleCredentials
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "E:\DHLAB\Google_Vision\ptry-efe4ae49a335.json"
#credentials = vision.Credentials()
#credentials = GoogleCredentials.get_application_default()


def detect_label(path):
    """Detects label in the file."""

    # Loads the image into memory
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)
    # Performs label detection on the image file

    labels = image.detect_labels()
    print('Labels:')
    for label in labels:
        print(label.description)


def detect_text(path):
    """Detects text in the file."""

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    texts = image.detect_text()
    print('Texts:')
    for text in texts:
        print(text.description)

# service account is stored in a JSON keyfile.
# Instantiates a client
vision_client = vision.Client().from_service_account_json('E:\DHLAB\Google_Vision\ptry-efe4ae49a335.json')
# vision_client = vision.Client(credentials=creds)

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'E:/workplace/pycharm/ftry/try/01.png')

detect_label(file_name)
detect_text(file_name)
