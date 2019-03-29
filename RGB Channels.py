import cv2

image= cv2.imread('captura.png')

r=image.copy()
r[:,:,0] = 0
r[:,:,1] = 0

g=image.copy()
g[:,:,0] = 0
g[:,:,2] = 0

b=image.copy()
b[:,:,1] = 0
b[:,:,2] = 0

cv2.imshow('R-RGB',r)
cv2.imshow('G-RGB',g)
cv2.imshow('B-RGB',b)

cv2.waitKey(0)
