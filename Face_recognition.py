import cv2
# cv2 works on the image related things ab=nd helps to enable the camera 
face_cap = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")
videos_cap = cv2.VideoCapture(0)
while True:
    ret,video_data = videos_cap.read()
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor = 1.1,
        minNeighbors = 5,
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data,(x+w,y+h),(0,255,0),2)

    cv2.imshow("video_live",video_data)
    if cv2.waitKey(10) == ord('a'):
        break