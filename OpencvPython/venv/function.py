import cv2

# read image from file
img = cv2.imread("1.jpeg")
# convert image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# convert gray image to blur image using GaussianBlur() function
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.waitKey(0)
