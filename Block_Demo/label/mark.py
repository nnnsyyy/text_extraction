# @Project : block_extraction
# @Filename: mark
# @Date    : 2017-03-24
# @Author  : Shiyue Nie

import json
import os
import cv2
import copy


def plot_text():
    json_path = 'E:/workplace/pycharm/block_extraction/results'
    input_path = 'E:/workplace/pycharm/block_extraction/images/block_plot'
    output_path = 'E:/workplace/pycharm/block_extraction/images/text_plot'

    for name in os.listdir(json_path):
        basename = os.path.splitext(name)[0]
        with open(os.path.join(json_path, name), 'r') as result:
            # with open(os.path.join(input_path, 'block_3C_64.jpg'), 'rb') as image:
            im = cv2.imread(os.path.join(input_path, 'block_' + basename +'.jpg'), 1)
            nim = copy.copy(im)
            raw = json.load(result)
            #print(len(raw))
            for index in range(len(raw)):
                blocks = raw[str(index)]
                x0 = min(blocks['coordinate'][0][0], blocks['coordinate'][2][0])
                x1 = x0 + 150
                y = min(blocks['coordinate'][0][1], blocks['coordinate'][2][1])-10
                cv2.putText(nim, blocks['tag'], (x0, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (250, 0, 100), 2)
                cv2.putText(nim, blocks['transcription'], (x1, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            cv2.imwrite(os.path.join(output_path, 'mark_' + basename + '.jpg'), nim)


def plot_cen(cen, name):
    # for testing
    input_path = 'E:/workplace/pycharm/block_extraction/images/block_plot'
    output_path = 'E:/workplace/pycharm/block_extraction/images/'
    imname = os.path.splitext(name)[0] + '.jpg'

    im = cv2.imread(os.path.join(input_path, 'block_' + imname), 1)
    nim = copy.copy(im)
    for index in range(len(cen)):
        s = str(index+1) + '(' + str(cen[index][0]) + ', ' + str(cen[index][1]) + ')'
        cv2.putText(nim, s, (cen[index][0], cen[index][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (250, 0, 100), 2)
    cv2.imwrite(os.path.join(output_path, 'cen_' + imname), nim)

# def plot_text():
#     json_path = 'E:/workplace/pycharm/block_extraction'
#     input_path = 'E:/workplace/pycharm/block_extraction/images'
#     output_path = 'E:/workplace/pycharm/block_extraction/images'
#
#     name = '10A_216.json'
#     with open(os.path.join(json_path, name), 'r') as result:
#         # with open(os.path.join(input_path, 'block_3C_64.jpg'), 'rb') as image:
#         im = cv2.imread(os.path.join(input_path, 'try_10A_216.jpg'), 1)
#         nim = copy.copy(im)
#         raw = json.load(result)
#         # print(len(raw))
#         for index in range(len(raw)):
#             blocks = raw[str(index)]
#             x0 = min(blocks['coordinate'][0][0], blocks['coordinate'][2][0])
#             x1 = x0 + 150
#             y = min(blocks['coordinate'][0][1], blocks['coordinate'][2][1]) - 10
#             cv2.putText(nim, blocks['tag'], (x0, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (250, 0, 100), 2)
#             cv2.putText(nim, blocks['transcription'], (x1, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
#         cv2.imwrite(os.path.join(output_path, 'mark_' + '10A_216' + '.jpg'), nim)

plot_text()
