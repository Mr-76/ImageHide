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


new_img = np.array(img) #Load image as array
index = 0 #index to jump
placing_of_chars = {} #map of x and y to get chars back from image
pointsofnoise = 100 #limiter of points of noise
for x in range(len(ascii_values)): #loop in the number of chars of the message
    if (index < len(ascii_values)-1):
        randomX = random.randint(0, width - 1)
        randomY = random.randint(0, height - 1)
        new_img[randomY, randomX] = [ascii_values[index], ascii_values[index+1],ascii_values[index+2]]
        placing_of_chars[index] = (randomX,randomY) #makes you get the order and coord of the ascii values
        index+=3 #well can be any number of char but 3 by 3 makes it use the rgb values inside each pixel.
    else:
        #Still need to verify if the random value was alredy used to store a char
        for x in range(pointsofnoise): #loop in the number of chars of the message
            randomX = random.randint(0, width - 1)
            randomY = random.randint(0, height - 1)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            new_img[randomY, randomX] = [r,g,b]
print(placing_of_chars)
modified_image = Image.fromarray(new_img)
modified_image.save('modified_fruit.jpg')
