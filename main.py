
import pyautogui as pg
from PIL import Image,ImageGrab
import time


def hit(key):
    pg.press(key)

def isColloid(data):
    for i in range(600,660):
        for j in range(670,710):
            if data[i, j] < 100:
                return True
    return False        
   

if __name__ ==  "__main__":

    print("Starting  in 5s")
    print("Go to ->  chrome://dino")
    time.sleep(5)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isColloid(data):
            hit("up")


    # for i in range(500,580):
    #     for j in range(670,710):
    #         data[i,j] = 0        

    # for i in range(370,480):
    #     for j in range(635,710):
    #         data[i,j] = 0

    # image.show()