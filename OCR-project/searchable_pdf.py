# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 08:08:18 2021

@author: serha
"""

import pandas as pd
#first install tabula library and jdk from the command line and set it to environment variable
import tabula

pdf1='C:/Users/serha/OneDrive/Masaüstü/MyRepo/OCR-project/input/Allianz boyali police.pdf'
pdf2='C:/Users/serha/OneDrive/Masaüstü/MyRepo/OCR-project/input/Axa_poliçe_boyali.pdf'
pdf3='C:/Users/serha/OneDrive/Masaüstü/MyRepo/OCR-project/input/Demir_boyali_police.pdf'
pdf4='C:/Users/serha/OneDrive/Masaüstü/MyRepo/OCR-project/input/NN_boyali_police.pdf'

pdf_path = "C:/Users/serha/OneDrive/Masaüstü/MyRepo/OCR-project/input/Demir_boyali_police.pdf"

dfs = tabula.read_pdf(pdf_path, pages = 'all', stream=True)
print(len(dfs))
dfs[0]


# text extract ediyor ama bazi kisimlari almiyor, e.g. bazi tabular datalari gormedi
# ve bazi tabular datalari eksik aldi. tabular data uzerindeki police basligini gormedi
from tika import parser # pip install tika
raw = parser.from_file('input/Demir_boyali_police.pdf')
print(raw['content'])
raw['content']

# cogu karakteri tanimiyor, kalitesiz extraction
import textract
text = textract.process('input/Demir_boyali_police.pdf')
#text = textract.process('input/Demir_boyali_police.pdf', method='tesseract', language='nor')
text = textract.process('path/to/pdf/file', method='pdfminer')
print(text)


# cogu karakteri tanimiyor, kalitesiz extraction
import PyPDF2
pdfFileObj = open('input/Demir_boyali_police.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(8)
pageObj.extractText()
