# @Project : block_extraction
# @Filename: __init__.py
# @Date    : 2017-03-24
# @Author  : Shiyue Nie


import cv2
import os.path
import format.shared
import format.fragment
from format.section_cut import TextSection
from format.base import DocumentInfo


def single_frag(img, name):
    basename = os.path.join('E:\workplace\pycharm\\block_extraction\images\cardboard', name)
    output_folder = 'E:\workplace\pycharm\\block_extraction\images\\text_section'
    side = 'recto'
    doc_info = DocumentInfo(basename, output_folder, side)
    # img = cv2.imread(basename)
    # print('Img height and width: %d and %d' % (img.shape[0], img.shape[1]))
    text_img = TextSection(doc_info, img)

    text_img.extract_text()
    text_img.save_text_section(os.path.join(output_folder, name))


def piles_frag():
    folder = 'E:\workplace\pycharm\\block_extraction\images\cardboard'
    images, img_name = load_images_from_folder(folder)
    for ind in range(len(images)):
        single_frag(images[ind], img_name[ind])


def load_images_from_folder(folder):
    images = []
    img_name = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
            img_name.append(filename)
    return images, img_name

piles_frag()

