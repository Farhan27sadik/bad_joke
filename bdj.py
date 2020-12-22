import pyautogui
import time
import PyPDF2
from random import random

book = open('book.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()

    for line in text.split('\n'):
        time.sleep(random()+1)
        pyautogui.typewrite(line+'\n')
        pyautogui.press('enter')
