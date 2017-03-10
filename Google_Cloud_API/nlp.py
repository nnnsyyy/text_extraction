# @Project : ftry
# @Filename: nlp
# @Date    : 2017-03-10
# @Author  : Shiyue Nie

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "E:\DHLAB\Google_Vision\ptry-efe4ae49a335.json"

DISCOVERY_URL = ('https://{api}.googleapis.com/'
                 '$discovery/rest?version={apiVersion}')


def main():
    http = httplib2.Http()

    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])

    credentials.authorize(http)

    service = discovery.build('language', 'v1beta1',
                              http=http, discoveryServiceUrl=DISCOVERY_URL)

    service_request = service.documents().analyzeSentiment(
        body={
            'document': {
                'type': 'PLAIN_TEXT',
                'content': "Google Cloud Natural Language API rocks. It works well."
            }
        })

    response = service_request.execute()
    polarity = response['documentSentiment']['polarity']
    magnitude = response['documentSentiment']['magnitude']
    print('Sentiment: polarity of %s with magnitude of %s' % (polarity, magnitude))
    print('Whole result:')
    print(response)
    return 0


if __name__ == '__main__':
    main()
