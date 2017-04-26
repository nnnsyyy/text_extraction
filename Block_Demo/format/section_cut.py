# @Project : block_extraction
# @Filename: section_cut
# @Date    : 2017-03-29
# @Author  : Shiyue Nie

import os.path
import cv2
import numpy as np

from . import shared
from .base import DocumentInfo


class TextSection:
    def __init__(self, document_info: DocumentInfo, document=None):
        self.document_info = document_info
        if document is not None:
            self.cardboard = document
        else:
            self.cardboard = cv2.imread(os.path.join(self.document_info.output_folder,
                                                     shared.RECTO_CARDBOARD_DEFAULT_FILENAME))
        # self._image = None
        # self._image_bounds = None
        self._text_section = None

    def extract_text(self):
        doc = self.cardboard
        ratio = doc.shape[0] / shared.RESIZE_HEIGHT
        doc = cv2.resize(doc, (int(doc.shape[1] / ratio), int(shared.RESIZE_HEIGHT)))

        # cut top 26% of doc
        text_section_height = int(0.26 * doc.shape[0])
        self._text_section = doc[:text_section_height, :]

    def save_text_section(self, path=None):
        assert self._text_section is not None
        if path is None:
            self.document_info.check_output_folder()
            cv2.imwrite(os.path.join(self.document_info.output_folder, shared.TEXT_SECTION_DEFAULT_FILENAME),
                        self._text_section)
        else:
            cv2.imwrite(path, self._text_section)

