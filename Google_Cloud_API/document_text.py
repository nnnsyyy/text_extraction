# @Project : ftry
# @Filename: document_text
# @Date    : 2017-03-10
# @Author  : Shiyue Nie

import argparse
import base64
import json

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

from PIL import Image
from PIL import ImageDraw


# Check the level to print the polyboxes and provide the output.
# If the output level is Page, just print the text (Page does not have
# polyboxes).
def checkAndDrawBox(draw, checkType, itemName, outputText, item):
    if itemName == checkType:
        if itemName == "page":
            print(outputText)
        else:
            box = [(v.get('x', 0.0), v.get('y', 0.0))
                   for v in item['boundingBox']['vertices']]
            draw.line(box + [box[0]], width=5, fill='#00ff00')
            print(outputText)
    return


def main(image_file, output_level, output_file):
    """Run a request on a single image"""
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)

    with open(image_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'DOCUMENT_TEXT_DETECTION',
                    'maxResults': 10
                }]
            }]
        })

        # Get libraries to draw the image.
        im = Image.open(image)
        draw = ImageDraw.Draw(im)

        # Walk through the fullTextAnnotation block in the response.
        # Walk through all the Pages.
        # For each page, walk through the Blocks.
        # For each block, walk through the Paras.
        # For each para, walk through the Words.
        # For each word, consolidate the Symbols into a Word.
        # At each level, draw a box and print output based on the requested
        # output level.
        apiresponse = service_request.execute()
        data = json.dumps(apiresponse)
        urlresponse = json.loads(data)
        for key, value in urlresponse.items():
            responses = urlresponse[key]
            for response in responses:
                if 'fullTextAnnotation' not in response:
                    print
                    "full text not available"
                    return
                fullText = response['fullTextAnnotation']
                pages = fullText['pages']
                for page in pages:
                    pageText = ""
                    blocks = page['blocks']
                    for block in blocks:
                        blockType = block['blockType']
                        paras = block['paragraphs']
                        blockText = ""
                        for para in paras:
                            words = para['words']
                            paraText = ""
                            for word in words:
                                wordText = ""
                                symbols = word['symbols']
                                for symbol in symbols:
                                    wordText = wordText + symbol['text']
                                checkAndDrawBox(draw, output_level, "word", wordText, word)
                                paraText = paraText + wordText
                            blockText = blockText + paraText
                            checkAndDrawBox(draw, output_level, "para", paraText, para)
                        checkAndDrawBox(draw, output_level, "block", blockText, block)
                        pageText = pageText + blockText
                    checkAndDrawBox(draw, output_level, "page", pageText, page)

        # Save output with the drawn polyboxes based on the requested level.
        im.save(output_level + "_" + output_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to label.')
    parser.add_argument('output_level', help='Level of the output. Can be one of 4 options: page, block, para, word')
    parser.add_argument('output_file', help='Output file containing the input images with boxes drawn around the text')
    args = parser.parse_args(['E:/workplace/pycharm/ftry/test/02.png', 'para', 'text.jpg'])
    main(args.image_file, args.output_level, args.output_file)
