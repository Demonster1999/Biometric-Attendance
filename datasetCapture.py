import cv2 # image processing library
import os

def assurePathExists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

faceId = input('Enter Your ID : ')

# start capturing video
cap = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face
faceDetector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Intialize sample face image
count = 0

assurePathExists("dataset/")

# Start looping
while(True):
    # Capture video frame
    ret, imageFrame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces in rectangles
    faces = faceDetector.detectMultiScale(gray, 1.3, 5)

    # Loops for each faces
    for (x,y,w,h) in faces:

        # Crop the image frame into rectangle
        cv2.rectangle(imageFrame, (x,y), (x+w,y+h), (255,0,0), 2)

        # Increment sample face image
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(faceId) + '.' + str(count) + '.jpg', gray[y:y+h, x:x+w])

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', imageFrame)

    # To stop taking video, press 'q' for atleast 100ms
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    # If image taken reach 30, stop taking video
    elif count >= 30:
        print('Successfully Captured')
        break

# Stop Video
cap.release()

# Close all started windows
cv2.destroyAllWindows()
