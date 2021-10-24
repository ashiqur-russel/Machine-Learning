import cv2 as cv

""" img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img) """


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


# Redaing videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resize = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow("Video Resize", frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
