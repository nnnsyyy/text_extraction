# @Project : block_extraction
# @Filename: word_test
# @Date    : 2017-04-26
# @Author  : Shiyue Nie


import argparse
import base64
import json
import os.path
import copy
import text_block.block as blk
import format.fragment as fm

from googleapiclient import discovery
#from oauth2client.client import GoogleCredentials
from oauth2client.service_account import ServiceAccountCredentials
scopes = ['https://www.googleapis.com/auth/sqlservice.admin']


from PIL import Image
from PIL import ImageDraw


# Check the level to print the polyboxes and provide the output.
# If the output level is Page, just print the text (Page does not have
# polyboxes).
def save_draw_box(draw, ctype, name, output, item, fm_list):
    if name == ctype:
        if name == "page":
            print(output)
        else:
            # save 4 cornered points
            nfm = fm.Fragment()
            box = [(v.get('x', 0.0), v.get('y', 0.0))
                   for v in item['boundingBox']['vertices']]

            draw.line(box + [box[0]], width=3, fill='#f000ff')

            temp = copy.copy(blk.fmtoblock(nfm, output, box))
            fm_list.append(temp)


def text_extraction(input_folder, output_folder, output_level, name, fm_list):
    """Run a request on a single image"""
    credentials = ServiceAccountCredentials.from_json_keyfile_name("E:\DHLAB\ptry-efe4ae49a335.json")
    service = discovery.build('vision', 'v1', credentials=credentials)
    img = os.path.join(input_folder, name)

    with open(img, 'rb') as image:
        # print(os.path.join(input_folder, name))
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'DOCUMENT_TEXT_DETECTION',
                    'maxResults': 20
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
                full_text = response['fullTextAnnotation']
                pages = full_text['pages']
                for page in pages:
                    page_text = ""
                    blocks = page['blocks']
                    for block in blocks:
                        #block_type = block['blockType']
                        paras = block['paragraphs']
                        block_text = ""
                        for para in paras:
                            words = para['words']
                            para_text = ""
                            for word in words:
                                word_text = ""
                                symbols = word['symbols']
                                print('word symbols')
                                for symbol in symbols:
                                    print(symbol['text'])
                                    word_text = word_text + symbol['text']
                                if para_text == "":
                                    para_text = para_text + word_text
                                else:
                                    para_text = word_combine(para_text, pre_word, word_text)
                                pre_word = word_text
                            # save_draw_box(draw, output_level, "para", para_text, para, fm_list)
                            block_text = block_text + para_text
                        save_draw_box(draw, output_level, "block", block_text, block, fm_list)
                        page_text = page_text + block_text

        # Save output with the drawn polyboxes based on the requested level.
        im.save(os.path.join(output_folder, 'try' + "_" + name))


def word_combine(para_text, prew, curw):
    if prew.isalpha():
        if curw.isalpha() or curw == '(':
            para_text = para_text + ' ' + curw
        elif curw.isdigit():
            para_text = para_text + ' ' + curw
        else:
            para_text = para_text + curw
    elif prew.isdigit():
        para_text = para_text + ' ' + curw
    else: #punctuation
        if curw.isalpha():
            if prew == '\'' or prew == '(':
                para_text = para_text + curw
            else:
                para_text = para_text + ' ' + curw
        # elif curw.isdigit() and prew == '/':
        #     para_text = para_text + curw
        else:
            para_text = para_text + ' ' + curw
    return para_text

#def single_block(input_folder, output_folder, name, fm_list):
    # parser = argparse.ArgumentParser()
    # parser.add_argument('input_folder', help='The folder of text_extraction images.')
    # parser.add_argument('output_folder', help='The folder of block_plot images.')
    # parser.add_argument('output_level', help='Level of the output. Can be one of 4 options: page, block, para, word')
    # parser.add_argument('name', help='The name of image.')
    # args = parser.parse_args([os.path.join(folder, 'text_section'), os.path.join(folder, 'block_plot'), 'block', name])
    # text_extraction(args.input_folder, args.output_folder, args.output_level, args.name)
    #output_level = 'para'
    #output_level = 'block'
    # text_extraction(input_folder, output_folder, output_level, name, fm_list)


def piles_block():
    # input_path = 'E:\workplace\pycharm\\block_extraction\images\\text_section'
    # output_path = 'E:\workplace\pycharm\\block_extraction\images\\block_plot'
    input_path = 'E:/workplace/pycharm/block_extraction/images/text_section'
    output_path = 'E:/workplace/pycharm/block_extraction/images'

    # for name in os.listdir(input_path):
    name = '10A_216.jpg'
    print(name)
    fm_list = []
    # detect_document(input_path, output_path, name, fm_list)
    text_extraction(input_path, output_path, 'block', name, fm_list)
    blk.save_img_text(name, fm_list)


piles_block()

