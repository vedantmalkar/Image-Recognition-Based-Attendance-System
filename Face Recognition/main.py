import cv2 as cv
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
cascade_path = os.path.join(script_dir, 'haar_face.xml')

if not os.path.exists(cascade_path):
    print(f"Error: The file '{cascade_path}' is missing or not found!")
    exit()

haar_cascade = cv.CascadeClassifier(cascade_path)

if haar_cascade.empty():
    print("Error: Haar cascade xml file not loaded.")
    exit()

cam = cv.VideoCapture(0)

while True:
    imTrue, frame = cam.read()
    
    if not imTrue:
        print("Error: Failed to capture image.")
        break

    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    detection_coordinates = haar_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=3)

    font = cv.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255, 255, 255)
    thickness = 2

    for (x, y, w, h) in detection_coordinates:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
        cropped = frame[y:y + h, x:x + w]
        
        org = (int(x), int(y) - 10)
        cv.putText(frame, "test", org, font, fontScale, color, thickness)

    if len(detection_coordinates) > 0:
        print("Face detected")
        cv.imshow('Cropped', cropped)  
    else:
        print("Face not detected")

    cv.imshow('Camera', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
