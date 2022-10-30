# cv2 module is used here to work on the image related things
import cv2
# 
import pyautogui
# GetSystemMetrics module is used to set resolution if the screen
from win32api import GetSystemMetrics
# numpy is an array processing package which is used to store the things in the form of array
import numpy as np
# time module is used to work with the time related tasks 
import time

# setting the resolution of the screen
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim = (width,height)

f = cv2.VideoWriter_fourcc(*'XVID') #used to make the video format

output = cv2.VideoWriter('test.mp4',f,30.0,dim) #setting the name of the video,format,fps and dimension

now_start_time = time.time() #save the current time 
dur = 10
end_time = time.time() + dur 

while True:
    image = pyautogui.screenshot() # take the screenshot
    frame_1 = np.array(image) # store in the form of array
    frame = cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)
    c_time = time.time()
    if c_time > end_time:
        break
    output.write(frame)
output.release() #to release the video
print("Successfully recorded")