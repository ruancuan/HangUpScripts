# coding:utf-8
import os
from PIL import ImageGrab,Image
import pytesseract
import threading
import pyautogui
import time

pos=[600,465,1222,659]
target0=r'继续学习'
target1=r'在吗'
target2=r'离开'
target3=r'学分'
target4=r'走开'

def t1():
    print('Start:')

#定时
def t2():
    t1()
    while 1:
        print('执行--')
        fun()
        time.sleep(10)

def fun():
    file_path='C:\PythonLearn\Scripts\AutoLearn\Image.jpg'
    pic=ImageGrab.grab(pos)
    pic.save(file_path)
    print('图片保存成功')
    text=pytesseract.image_to_string(Image.open(file_path),lang='chi_sim').encode('utf-8')
    result0=text.rfind(target0)>0
    result1=text.rfind(target1)>0
    result2=text.rfind(target2)>0
    result3=text.rfind(target3)>0
    result4=text.rfind(target4)>0
    print(text)
    end=result0|result1|result2|result3|result4
    if end:
        pyautogui.click(x=900,y=600,button='left')

if __name__=='__main__':
    t=threading.Thread(target=t2)
    t.start()
