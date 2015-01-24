

############################################
## Import OpenCV
import numpy as np
import cv2
# Initialize camera
cap = cv2.VideoCapture(1)
############################################

# Sample Pixel --> A - [213,154,150] , B - [113,154,150]
param1 = [ 80,100,150]
param2 = [130,200,255]

############################################
## Video Loop

while(1):
    
    ## Read the image
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    ## Do the processing
    lower = np.array(param1)    ## Convert the parameters into a form that OpenCV can understand
    upper = np.array(param2)
    mask  = cv2.inRange(hsv, lower, upper)
    res   = cv2.bitwise_and(frame, frame, mask= mask)
    ## Show the image
    cv2.imshow('image',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    

    ## End the video loop
    if cv2.waitKey(1) == 27:  ## 27 - ASCII for escape key
        break
############################################

############################################
## Close and exit
cap.release()
cv2.destroyAllWindows()
############################################
