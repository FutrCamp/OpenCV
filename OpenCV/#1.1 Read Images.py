# ----------------------Importing opencv -------------------------

import cv2
# -------------Reading a image ------------------------------------

      # cv2.imread() method loads an image from the specified file
img = cv2.imread("Resources/pic1.jpg")

      # the image will disapear immediately if only above line is used
cv2.imshow("output",img)

cv2.waitKey(0) # 0 means wait infinitely
      # cv2.waitKey(1) #will display a frame for 1 ms
      # cv2.waitKey(10000) #will display a frame for 10000 ms or 10 seconds

#--------------Getting Height, Width, Channels of an Imge------------
# read image
img = cv2.imread("Resources/pic1.jpg")

# get dimensions of image
dimensions = img.shape

# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

print('Image Dimension    : ', dimensions)
print('Image Height       : ', height)
print('Image Width        : ', width)
print('Number of Channels : ', channels)

print(img.shape)

cv2.imshow("Image", img)

cv2.waitKey(0)