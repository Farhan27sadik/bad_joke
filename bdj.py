"""

import pyttsx3
import PyPDF2

book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

"""

import pyautogui
import time

m = 100
while m > 0:
    time.sleep(1)
    pyautogui.typewrite('You have challenged a wrong person!\n')
    pyautogui.press('enter')
    m = m - 1
