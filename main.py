
import cv2
import time

imagePath = "C:/Users/moyas/Documents/programsForMe/apps/clowdWatch/data/dest/image.jpg"

def store():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(imagePath, frame)
        print("画像保存したよ～")
    else:
        print("エラーだよ。画像とれてないよ。")

if __name__ == "__main__":
    while True:
        store()
        time.sleep(5)
