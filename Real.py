#!/usr/bin/env python
# coding: utf-8


def image(title, name):
    cv2.imshow(title, name)
    cv2.waitKey(0)

#HoughCircles function
def houghCircles(img, or_img):
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=150)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(or_img,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(or_img,(i[0],i[1]),2,(0,0,255),2)
    number=circles.shape[1]
    return number


#importing libraries
import cv2 
import numpy as np

#Reading the image
img = cv2.imread('./real_original.jpg',1) 

#Result 1
image('real_original.jpg', img)

#Converting the image to gray
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Result 2
image('gray', gray_img)

#Applying a filter to blur the image
blur_img = cv2.medianBlur(gray_img, 57)

#Result 3
image('Blur', blur_img)

#Applying the Circle function to draw the centers and edges of the coins on the original image.
num = houghCircles(blur_img, img)

#Result 4
print('Number of coins detected = ', num)

#Result 5
cv2.imwrite('./image_result/real_result.jpg',img)
image('Blur', img)



