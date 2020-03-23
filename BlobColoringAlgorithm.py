#  This algorithm is based on the Hoshen-Kopelman algorithm

import cv2 as cv
import numpy as np

img = cv.imread('blobs.jpg', 0)
img = cv.threshold(img, 125, 255, cv.THRESH_BINARY)[1]  # Loads the image in binary
labels = np.zeros_like(img)
labels.fill(255)  # Creates a white canvas with same size as loaded image
largest_label = 0  # Starting label+1


# Merges labels that are connecting
def merge():
    # Todo: This code can be better
    continues = True
    z = labels[x-1][y]
    old = labels[x][y-1]
    i = 1
    while(continues):
        if(labels[x][y-i] != old or y-i < 0):
            continues = False
        else:
            labels[x][y-i] = z
            i = i + 1


# Makes the gray image into a more visually apealling image
def change_colors(labelinput):
    blank = np.zeros_like(img)
    blank.fill(255)
    newblobs = cv.merge((labelinput, blank, blank))
    for x in range(len(newblobs)):
        for y in range(len(newblobs[x])):
            if(newblobs[x][y][0] == 255):
                newblobs[x][y] = np.array([0, 0, 0])
    return newblobs


# Loops through every pixel
for x in range(len(img)):
    for y in range(len(img[x])):
        if(img[x][y] == 0):
            left = img[x-1][y]  # Looks on the pixels left the pixel
            above = img[x][y-1]  # Looks on the pixels above the pixel
            if(left == 255 and above == 255):
                largest_label = largest_label + 1
                labels[x][y] = largest_label
            elif(left != 255 and above == 255):
                labels[x][y] = labels[x-1][y]
            elif(left == 255 and above != 255):
                labels[x][y] = labels[x][y-1]
            else:
                merge()  # Merge the labels 
                labels[x][y] = labels[x-1][y]


newcolor = change_colors(labels)
newcolor = cv.cvtColor(newcolor, cv.COLOR_HSV2BGR)
cv.imshow("blobs.jpg", img)  # Shows original image
cv.imshow("labels", newcolor)  # Shows labelled image
cv.waitKey()
