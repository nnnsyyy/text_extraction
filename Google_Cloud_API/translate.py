# @Project : ftry
# @Filename: translate
# @Date    : 2017-03-14
# @Author  : Shiyue Nie

import io
import os
# from googleapiclient import discovery
# import httplib2
# from oauth2client.client import GoogleCredentials
from google.cloud import translate
from google.cloud import vision

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "E:\DHLAB\Google_Vision\ptry-efe4ae49a335.json"
#
# DISCOVERY_URL = ('https://{api}.googleapis.com/'
#                  '$discovery/rest?version={apiVersion}')

# http = httplib2.Http()
# credentials = GoogleCredentials.get_application_default().create_scoped(
#     ['https://www.googleapis.com/auth/cloud-platform'])
# credentials.authorize(http)


def detect_language(text):

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.detect_language(text)

    print('Text: {}'.format(text))
    print('Confidence: {}'.format(result['confidence']))
    print('Language: {}'.format(result['language']))


def detect_text(path):
    """Detects text in the file."""

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    texts = image.detect_text()
    print('Texts:')
    #for text in texts:
    #    print(text.description)
    return texts[0].description

if __name__ == '__main__':

    """Detects the text's language."""
    translate_client = translate.Client().from_service_account_json('E:\DHLAB\Google_Vision\ptry-efe4ae49a335.json')

    # Instantiates a client
    vision_client = vision.Client().from_service_account_json('E:\DHLAB\Google_Vision\ptry-efe4ae49a335.json')
    file_name = os.path.join(
        os.path.dirname(__file__),
        'E:/workplace/pycharm/ftry/test/02.png')
    text=detect_text(file_name)
    print("Raw Text:%s " % text)
    print("Translation: \n")
    detect_language(text)
