# @Project : block_extraction
# @Filename: __init__.py
# @Date    : 2017-03-24
# @Author  : Shiyue Nie


import text_block.block as block
import text_block.text as text


def get_img_text():

    # input_path = 'E:\workplace\pycharm\\block_extraction\images\\text_section'
    # output_path = 'E:\workplace\pycharm\\block_extraction\images\\block_plot'
    input_path = 'E:/workplace/pycharm/block_extraction/images/text_section'
    output_path = 'E:/workplace/pycharm/block_extraction/images/block_plot'
    json_path = 'E:/workplace/pycharm/block_extraction/results'

    text.piles_block(input_path, output_path, json_path)


get_img_text()

