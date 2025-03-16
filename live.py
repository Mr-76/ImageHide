import cv2
import numpy as np
from PIL import Image
import time




#will try to display but can jsut crash cause of the constant writes of the image...


image_path = 'modified_fruit.jpg'
cv2.namedWindow("Live Image Viewer", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Live Image Viewer", 800, 600)
while True:
    img = Image.open(image_path)
    img_data = np.array(img)
    cv2.imshow("Live Image Viewer", img_data)
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

