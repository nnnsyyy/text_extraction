# @Project : ftry
# @Filename: nlapi
# @Date    : 2017-03-14
# @Author  : Shiyue Nie

# Imports the Google Cloud client library
from google.cloud import language

def nlapi(text):
    # Instantiates a client
    language_client = language.Client()

    # The text to analyze
    document = language_client.document_from_text(text)

    # Detects the sentiment of the text
    sentiment = document.analyze_sentiment().sentiment
    entities = document.analyze_entities().entities

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

    return entities


entity = nlapi('Hello world Shiyue!')
print("Entities: \n")
print("Language: {}".format(entity.language))
items = entity[0]
for item in items:
    print(item.metadata)

#print(entity.mentions)

