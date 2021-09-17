import numpy as np
import pandas as pd
import os
import tabula
from io import StringIO
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#from numpy import asarray
try:
    from PIL import Image
except ImportError:
    import Image

from pytesseract import Output
from pdf2image import convert_from_path, convert_from_bytes

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

files = os.listdir(r'C:/Users/serha/OneDrive/Masaüstü/MyRepo/OCR-project/input/') 

imageslist=[]
for file in files:
    imageslist.append(convert_from_path('C:/Users/serha/OneDrive/Masaüstü/MyRepo/OCR-project/input/' + file))
tabulalist=[]
for file in files:
    tabulalist.append(tabula.read_pdf('C:/Users/serha/OneDrive/Masaüstü/MyRepo/OCR-project/input/' + file, pages = 'all', stream=True))


sigorta_policesi=[]
for i in range(len(imageslist)):
    if i==0:
        texttable=pd.read_table(StringIO(pytesseract.image_to_data(imageslist[i][0], lang='tur')))
        sigorta_policesi.append(texttable['text'][[9,10,11,13,14]].str.cat(sep=' '))
    if i==1:
        texttable=pd.read_table(StringIO(pytesseract.image_to_data(imageslist[i][5], lang='tur')))
        sigorta_policesi.append(texttable['text'][[58,59,60]].str.cat(sep=' '))
    if i==2:
        texttable=pd.read_table(StringIO(pytesseract.image_to_data(imageslist[i][1], lang='tur')))
        sigorta_policesi.append(texttable['text'][[8,9,10,11,13]].str.cat(sep=' '))
    if i==3:
        texttable=pd.read_table(StringIO(pytesseract.image_to_data(imageslist[i][1], lang='tur')))
        sigorta_policesi.append(texttable['text'][[392,393,394,395,396]].str.cat(sep=' '))
        
police_no=[]
for i in range(len(tabulalist)):
    if i==0:
        texttable=pd.read_table(StringIO(pytesseract.image_to_data(imageslist[i][0], lang='tur')))
        police_no.append(texttable['text'][[20]].to_string(header=False, index=False))
    if i==1:
        police_no.append(tabulalist[1][0]["POLİÇE-TECDİT-"][[1]].to_string(header=False, index=False))
    if i==2:
        police_no.append(tabulalist[2][2]["Unnamed: 1"][[0]].to_string(header=False, index=False))

del file, i, texttable



# # Cropping the image and recognise text
# width, height = imageslist[3][0].size
# left, top = 50, 600
# right, bottom = 250, 700
# cropped = imageslist[3][0].crop((left, top, right, bottom))
# cropped.show()
# pytesseract.image_to_data(cropped, lang='tur')
# pytesseract.image_to_string(cropped, lang='tur')

# # SOME TESSERACT CODES
# a=Image.open('C:/Users/serha/OneDrive/Masaüstü/MyRepo/OCR-project/input_image/Capture.PNG')
# images = convert_from_path(pdf_filepath)
# # Get bounding box estimates
# print(pytesseract.image_to_boxes(a))
# print(pytesseract.image_to_boxes(images[0]))
# # Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(a))
# print(pytesseract.image_to_data(images[0]))
# # Get information about orientation and script detection
# print(pytesseract.image_to_osd(a))
# print(pytesseract.image_to_osd(images[0]))
# # Get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr(a, extension='hocr')
# # Get ALTO XML output
# xml = pytesseract.image_to_alto_xml(a)



# # CONVERT IMAGE TO NUMPY ARRAY
# imagearray = asarray(images[0])
# d = pytesseract.image_to_data(imagearray, output_type=Output.DICT)
# n_boxes = len(d['level'])
# for i in range(n_boxes):
#     (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#     data=cv2.rectangle(imagearray, (x, y), (x + w, y + h), (0, 255, 0), 2)
# cv2.imshow('img', imagearray)
# cv2.waitKey(0)



# # SEARCHING CERTAIN KEY WORDS
# listt=[]
# for a in range(2):
#     listt.append(pytesseract.image_to_string(images[a]))
    
# complete_text="".join(listt)

# complete_text.find("POLiCESi")
# complete_text[1781:1789]

# result_string = ''
# list_=["SIGORTASI", "POLiCESi", "Sigortasi"]
# text2=complete_text.split(".")
# for itemIndex in range(len(text2)):
#     for word in list_:
#         if word in text2[itemIndex]:
#             if text2[itemIndex][0] ==' ':
#                 print(text2[itemIndex][1:])
#                 result_string += text2[itemIndex][1:]+'. '
#                 break
#             else:
#                 print(text2[itemIndex])
#                 result_string += text2[itemIndex]
#                 break

