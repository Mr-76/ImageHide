import cv2
import numpy as np

#with this you can clearly see the image noise and info.... if u can find it xd
image1 = cv2.imread('fruit.jpg')
image2 = cv2.imread('modified_fruit.jpg')

if image1.shape != image2.shape:
    raise ValueError("Images must have the same dimensions for subtraction.")

result_image = cv2.absdiff(image1, image2)


cv2.imwrite('subtracted_image.jpg', result_image)
