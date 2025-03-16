import numpy as np
import cv2
from PIL import Image
import time
import random

img = Image.open('fruit.jpg')
pix = img.load()
(width, height) = img.size

message = "The I took the one less traveled by,And that has made all the difference."

#may need to add padding if the value if not multiple of 3....
ascii_values = [ord(c) for c in message]

new_img = np.array(img)
index = 0
placing_of_chars = {}
pointsofnoise = 0
for y in range(height):
    for x in range(len(ascii_values)):
        if (index < len(ascii_values)-1):
            randomX = random.randint(0, width - 1)
            randomY = random.randint(0, height - 1)
            new_img[randomY, randomX] = [ascii_values[index], ascii_values[index+1],ascii_values[index+2]]
            placing_of_chars[index] = (randomX,randomY)
            time.sleep(0.05) 
            index+=3
        else:
            if (pointsofnoise < 1000):
                pointsofnoise += 1
                randomX = random.randint(0, width - 1)
                randomY = random.randint(0, height - 1)
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                new_img[randomY, randomX] = [r,g,b]
            continue

print(placing_of_chars)
modified_image = Image.fromarray(new_img)
modified_image.save('modified_fruit.jpg')
