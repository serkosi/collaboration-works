# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:18:28 2021

@author: serha
"""

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# List of available languages
print(pytesseract.get_languages(config=''))


print(pytesseract.image_to_string(Image.open('input/Demir_boyali_police.pdf')))
