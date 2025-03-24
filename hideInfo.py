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


def writer_image(ascii_values,new_img,message):
    for x in range(len(ascii_values)-3 ): #loop in the number of chars of the message
        randomX = random.randint(0, width - 1)
        randomY = random.randint(0, height - 1)
        new_img[randomY, randomX] = [ascii_values[x], ascii_values[x+1],ascii_values[x+2]]
        placing_of_chars[x] = (randomX,randomY) #makes you get the order and coord of the ascii values
#        index+=3 #well can be any number of char but 3 by 3 makes it use the rgb values inside each pixel.

    return new_img

def writer_noise(new_im,pointsofnoise):
    #Still need to verify if the random value was alredy used to store a char
    for x in range(pointsofnoise): #loop in the number of chars of the message
        randomX = random.randint(0, width - 1)
        randomY = random.randint(0, height - 1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        new_im[randomY, randomX] = [r,g,b]
    return new_im

#find the pixel with the closest value to the tuple of values
#based on absolute diff
def isClose(tuple_rgb_string,new_img):
    #set starting diff as 0 and 0 
    #calculate abs diff np[x,y] = ((ch1,ch2,ch3) - (r,g,b))
    #returns the closest position also need tell that a position was alrey used.
    for y in range(len(new_img)):
        for x in range(len(new_img[0])):
            print(y)
            print(x)


    print("hello")
    return (x,y)
writer_image(ascii_values,new_img,message)
writer_noise(new_img,10000)


isClose(1,new_img)

print(placing_of_chars)
modified_image = Image.fromarray(new_img)
modified_image.save('modified_fruit.jpg')

