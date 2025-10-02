import cv2 as cv
cam = cv.VideoCapture(2)
while True:
    check, frame = cam.read()
    cv.imshow("test" , frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()



