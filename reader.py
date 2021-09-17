# -*- coding: utf-8 -*-
"""
created on 14.09.2021 by Serhat Kosif

reading text parts from pdf files

"""
import re
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('input/Capture.PNG')

# Adding custom options
custom_config = r'--oem 3 --psm 6'
pytesseract.image_to_string(img, config=custom_config)

# Here's a list of the supported page segmentation modes by tesseract -
# 0    Orientation and script detection (OSD) only.
# 1    Automatic page segmentation with OSD.
# 2    Automatic page segmentation, but no OSD, or OCR.
# 3    Fully automatic page segmentation, but no OSD. (Default)
# 4    Assume a single column of text of variable sizes.
# 5    Assume a single uniform block of vertically aligned text.
# 6    Assume a single uniform block of text.
# 7    Treat the image as a single text line.
# 8    Treat the image as a single word.
# 9    Treat the image as a single word in a circle.
# 10    Treat the image as a single character.
# 11    Sparse text. Find as much text as possible in no particular order.
# 12    Sparse text with OSD.
# 13    Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.
# To change your page segmentation mode, change the --psm argument in your custom config string to any of the above mentioned mode codes.

custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz --psm 6'
pytesseract.image_to_string(img, config=custom_config)


# Preprocess image functions
    # get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
    #thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    #dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
    #erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

    #opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    #canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

    #skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

    #template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 

gray = get_grayscale(img)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)

plt.imshow(img)
plt.imshow(gray)
plt.imshow(thresh)
plt.imshow(opening)
plt.imshow(canny)

# bounding box for each character
img = cv2.imread('input/Capture2.PNG')
h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)

# bounding box for each word
img = cv2.imread('input/Capture2.PNG')
d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(float(d['conf'][i])) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)

# finding date with bounding box
img2 = cv2.imread('input/Capture2.PNG')
d = pytesseract.image_to_data(img2, output_type=Output.DICT)
keys = list(d.keys())

date_pattern = '^(0[1-9]|[12][0-9]|3[01]).(0[1-9]|1[012]).(19|20)\d\d$'

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(float(d['conf'][i])) > 60:
    	if re.match(date_pattern, d['text'][i]):
	        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
	        img2 = cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img2)
cv2.waitKey(0)













