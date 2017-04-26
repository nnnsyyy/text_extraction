# @Project : block_extraction
# @Filename: block
# @Date    : 2017-03-24
# @Author  : Shiyue Nie

# import format.fragment as fm
# fm shorts for fragment
import json
import os
import random
# import copy


tag_list = ['place', 'author', 'institution', 'description',
            'collection', 'collection_num', 'others']


def listtodict(nfm):
    dicfm = {k: v for k, v in enumerate(nfm)}
    # print('Dict: ')
    # print(dicfm)
    return dicfm


def fmtoblock(nfm, ntranscription, ncoordinate, ntag=None):
    if ntag is None:
        ntag = random.choice(tag_list)
    return nfm.setfragment(ntag, ntranscription, ncoordinate)


# def savejson(name, raw):
#     file = os.path.join('E:\workplace\pycharm\\block_extraction\\results', name)
#     suffix = '.json'
#     with open(file+suffix, 'w') as fp:
#         json.dump(raw, fp, indent=4)


def save_img_text(name, fm_list):
    raw = listtodict(fm_list)
    fname = os.path.splitext(name)[0] + '.json'
    file = os.path.join('E:/workplace/pycharm/block_extraction/results', fname)
    with open(file, 'w') as fp:
        json.dump(raw, fp, indent=4)



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




