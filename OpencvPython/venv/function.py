import cv2
import numpy as np

# read image from file
img = cv2.imread("1.jpeg")
kernel = np.ones((5, 5), np.uint8)


# convert image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# convert gray image to blur image using GaussianBlur() function
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# find the edge of image using  Canny() function
imgCanny = cv2.Canny(img,100,100)
# increase the thickness of edge
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.waitKey(0)
