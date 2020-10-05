#!/usr/bin/env python
# coding: utf-8
def image(title, name):
    cv2.imshow(title, name)
    cv2.waitKey(0)

# HoughCircles function
def houghCircles(img, or_img):
    #Applying Grayscale filter to image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray_img,cv2.HOUGH_GRADIENT,1,30,param1=40,param2=30,minRadius=52,maxRadius=110)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(or_img,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(or_img,(i[0],i[1]),2,(255,0,0),2)
    number=circles.shape[1]
    return number


#importing libraries
#importing libraries
import numpy as np
import cv2


#Reading the image
img = cv2.imread('./dolar_original.png') 

#Result 1
image('dolar_original.jpg', img)

#Applying Grayscale filter to image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Result 2
image('Gray', gray_img)

#Converting the image to a binary standard using threshold
ret, thresh = cv2.threshold(gray_img, 55, 240, cv2.THRESH_BINARY_INV)

#Result 3
image('Threshold', thresh)

#Morphological filter
kernel = np.ones((3, 3), np.uint16)
morphology = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=3)
#Result 4
image('Threshold', morphology)

# SimpleBlobDetector
# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

#params.minDistBetweenBlobs = 120
params.filterByInertia = False
params.filterByConvexity = True
params.minConvexity = 0.9
params.maxConvexity = 1.0
params.filterByColor = False
params.filterByCircularity = False
params.filterByArea = True
params.maxArea = 50000
params.minThreshold = 150
params.maxThreshold = 230

detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(morphology)
numbers = len(keypoints)

# Draw detected blobs as red circles.
im_with_keypoints = cv2.drawKeypoints(morphology, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#Result 5
image('Result_5', im_with_keypoints)

#Result 6
print('Number of coins detected = ', numbers)

#Applying the Circle function to draw the centers and edges of the coins on the original image.
num = houghCircles(im_with_keypoints, img)

#Result 7
image('Result', img)
#Saving the final image
cv2.imwrite('./image_result/dolar_result.png',img)

