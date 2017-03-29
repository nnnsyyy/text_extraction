# @Project : ftry
# @Filename: text_nlp
# @Date    : 2017-03-10
# @Author  : Shiyue Nie

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials
import os
import io
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud import language

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "E:\DHLAB\Google_Vision\ptry-efe4ae49a335.json"

DISCOVERY_URL = ('https://{api}.googleapis.com/'
                 '$discovery/rest?version={apiVersion}')


def nlp(text):
    http = httplib2.Http()

    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])

    credentials.authorize(http)

    service = discovery.build('language', 'v1beta1',
                              http=http, discoveryServiceUrl=DISCOVERY_URL)

    service_request = service.documents().analyzeSentiment(
        body={
            "encodingType": "UTF8",
            # "language": "es",
            # not valid for languages if not eng, esp & Japanese
            "document": {
                'type': 'PLAIN_TEXT',
                'content': text
            }
        })

    response = service_request.execute()
    polarity = response['documentSentiment']['polarity']
    magnitude = response['documentSentiment']['magnitude']
    print('Sentiment: polarity of %s with magnitude of %s' % (polarity, magnitude))
    print('Whole result:')
    print(response)
    return response


def nlapi(text):
    # Instantiates a client
    language_client = language.Client()

    # The text to analyze
    document = language_client.document_from_text(text)

    # Detects the sentiment of the text
    sentiment = document.analyze_sentiment().sentiment

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))


def detect_text(path):
    """Detects text in the file."""

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    texts = image.detect_text()
    # Returns:	List of EntityAnnotation.

    return texts[0].description


if __name__ == '__main__':
    # service account is stored in a JSON keyfile.
    # Instantiates a client
    vision_client = vision.Client().from_service_account_json('E:\DHLAB\Google_Vision\ptry-efe4ae49a335.json')
    # vision_client = vision.Client(credentials=creds)

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        'E:/workplace/pycharm/ftry/test/02.png')

    raw_text = detect_text(file_name)
    result = nlapi(raw_text)
    print(result['sentences'])
