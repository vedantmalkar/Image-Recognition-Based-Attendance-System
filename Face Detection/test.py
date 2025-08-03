import cv2 as cv
cam = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier('haar_face.xml')

while True:
    imTrue, frame = cam.read()
    cv.imshow('Camera', frame)
    detection_coordinates = haar_cascade.detectMultiScale(gray,scaleFactor=2 ,minNeighbors=3)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
