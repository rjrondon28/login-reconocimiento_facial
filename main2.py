import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('ejemplo.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMulScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
	cv.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
cv2.inshow('img', img)
cv2.waitKey()