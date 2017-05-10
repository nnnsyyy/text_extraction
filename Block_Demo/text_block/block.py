# @Project : block_extraction
# @Filename: block
# @Date    : 2017-03-24
# @Author  : Shiyue Nie


import json
import os
import random

import cv2
import numpy as np
from format.line import detect_riddes, get_line_mask, close_lines
import copy


tag_list = ['place', 'author', 'institution', 'description',
            'collection', 'collection_num', 'others']


def listtodict(nfm):
    dicfm = {k: v for k, v in enumerate(nfm)}
    # print('Dict: ')
    # print(dicfm)
    return dicfm


def fmtoblock(nfm, ntranscription, ncoordinate, cnt, ntag=None):
    if ntag is None:
        ntag = random.choice(tag_list)
    return nfm.setfragment(ntag, ntranscription, ncoordinate, cnt)


def save_img_text(name, fm_list, json_path):
    raw = listtodict(fm_list)
    fname = os.path.splitext(name)[0] + '.json'
    #fname = name + '.json'
    file = os.path.join(json_path, fname)
    #file = os.path.join('E:/workplace/pycharm/block_extraction', fname)
    with open(file, 'w') as fp:
        json.dump(raw, fp, indent=4)


# def block_detect(nfm, name, contours, cen, json_path):
#     # open json to assign each fm's cnt
#     if len(cen) > 0:
#         fm_list=[]
#         fname = os.path.splitext(name)[0] + '.json'
#         file = os.path.join(json_path, fname)
#         blk_cen = []
#         with open(file, 'r') as fp:
#             raw = json.load(fp)
#             for index in range(len(raw)):
#                 blocks = raw[str(index)]
#                 [cx, cy] = np.mean(blocks['coordinate'], axis=0)
#                 [cx, cy] = [int(cx), int(cy)]
#                 blk_cen.append([cx, cy])
#                 # blk = block_cluster(cen, cx, cy)
#                 blk = block_cluster(contours, cx, cy)
#                 nfm.setblock(blk)
#     mk.plot_cen(blk_cen, name)


def block_detect(contours, cen, box):
    # fm center
    if len(cen) > 0:
        [cx, cy] = np.mean(box, axis=0)
        [cx, cy] = [int(cx), int(cy)]
        # print('center (cx, cy): ({}, {})'.format(cx, cy))
        blk = block_cluster(contours, cx, cy)
        #mk.plot_cen(blk_cen, name)
        return blk


def cnt_count(name, img_path):
    img = cv2.imread(os.path.join(img_path, name), 0)
    # Filter the noise
    bimg = cv2.fastNlMeansDenoising(copy.copy(img), h=8, searchWindowSize=50)
    # Detect the black lines (actually detect well text too)
    bimg = detect_riddes(bimg)
    # Clean up to only keep the vertical and horizontal lines
    mask = get_line_mask(bimg) + get_line_mask(bimg, num_iterations=3, vertical=True)
    # Close the boundaries
    header_mask = close_lines(mask)
    # Get the area contours
    contours = get_enclosing_contours(255-header_mask)
    contours.reverse()
    cen = []
    if len(contours) != 8:
        # over 8: keep biggest 8
        # less than 8: defaults
        # DocumentInfo.logger.warning('Number of area contours unusual : {}'.format(len(contours)))
        print('Img {} Number of area contours unusual : {}'.format(name, len(contours)))
    else:
        # save center of contours
        cen = cnt_center(contours)
        # print('Sorted contour center: {}'.format(cen))
        # mk.plot_cen(cen, name)
    return contours, cen


def cnt_center(cnt):
    # sort centers?
    cen = []
    #for i in range(len(cnt)-1, -1, -1):
    for i in range(len(cnt)):
        m = cv2.moments(cnt[i])
        cx = int(m['m10'] / m['m00'])
        cy = int(m['m01'] / m['m00'])
        cen.append([cx, cy])
        #print('contours {}:'.format(i))
        #print('center: (%d, %d)' % (cen[i][0], cen[i][1]))
    #cen.reverse()
    return cen


def block_cluster(contours, cx, cy):
    blk_cnt = 0
    for i in range(len(contours)):
        # False: whether the point is inside 1 or outside -1 or on the contour 0.
        d = cv2.pointPolygonTest(contours[i], (cx, cy), False)
        if d >= 0:
            blk_cnt = i
            break
    return blk_cnt + 1  # block 1-8


# def block_cluster(cen, cx, cy):
#     blk = 0
#     dis = 10000
#     for i in range(len(cen)):
#         d = math.sqrt((cen[i][0]-cx)**2 + (cen[i][1]-cy)**2)
#         if d < dis:
#             blk = i
#             dis = d
#     return blk+1  # block 1-8


def get_enclosing_contours(binary):
    _, contours, hierarchy = cv2.findContours(binary.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    results = []
    if len(contours) > 0:
        for cnt, h in zip(contours, hierarchy[0]):
            if h[3] < 0:
                results.append(cnt)
    return results


# newfm = fm.Fragment()
# img_path = 'E:/workplace/pycharm/block_extraction/images/text_section'
# json_path = 'E:/workplace/pycharm/block_extraction/results'
# name = '13B_111.jpg' #7C_37
# [contours, cen] = cnt_count(name, img_path)
# block_detect(newfm, name, contours, cen, json_path)

# newfm = fm.Fragment()
# fragments = []
# temp = copy.copy(fmtoblock(newfm, 'author', 'Shiyue Nie', [(1, 0), (1, 1), (0, 1), (0, 0)]))
# fragments.append(temp)
# temp = copy.copy(fmtoblock(newfm, 'place', 'Lausanne', [(2, 3), (1, 3), (1, 1), (2, 1)]))
# fragments.append(temp)
#
# raw = listtodict(fragments)
#
# savejson('try', raw)




