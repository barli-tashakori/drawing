import cv2

img=cv2.imread("pardazesh tasvir\messi and ronaldo.jpg",0)
inverted=1.01-img
blurred=cv2.GaussianBlur(inverted,(21,21),0)
inverted_blurred=1.01-blurred
sketch=img/inverted_blurred
sketch=sketch*1.01
cv2.imshow("result",sketch)
cv2.waitKey()