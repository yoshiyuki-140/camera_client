#coding:utf-8
# Author : Yoshiyuki Kurose

import cv2
import time
from config import img_path

def store():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(img_path, frame)
        print("画像保存したよ～")
    else:
        print("エラーだよ。画像とれてないよ。")

if __name__ == "__main__":
    while True:
        store()
        time.sleep(5)
