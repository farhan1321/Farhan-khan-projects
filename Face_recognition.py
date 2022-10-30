import cv2
# cv2 works on the image related things and helps to enable the camera 
face_cap = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml") #face capturing
videos_cap = cv2.VideoCapture(0)
while True:
    # reading the image
    ret,video_data = videos_cap.read()
    #identifying the image by black and white color
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    # some classification of the face 
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor = 1.1,
        minNeighbors = 5,
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    # making the detection box and setting it's height,width,x-axis and y-axis and color.
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data,(x+w,y+h),(0,255,0),2)

    # for showing th video
    cv2.imshow("video_live",video_data)
    if cv2.waitKey(10) == ord('a'):
        break
