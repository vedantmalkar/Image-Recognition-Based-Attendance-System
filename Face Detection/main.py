import cv2 as cv
cam = cv.VideoCapture(0)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

while True:
    imTrue, frame = cam.read()
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    detection_coordinates = haar_cascade.detectMultiScale(grey,scaleFactor=2 ,minNeighbors=3)

    for (x,y,w,h) in detection_coordinates:
        cv.rectangle(frame,(x,y),(x+w,y+h), (0,0,255),thickness=2)
        cropped = frame[y:y+h+4 , x:x+w+4]

    cv.imshow('Camera', frame)
    cv.imshow('Cropped', cropped)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
