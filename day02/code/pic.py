import cv2 as cv
img = cv.imread('E:\\CODE\\day02\\code\\02.jpg')
# h w c
# BGR(0,0,255)  RGB  GRAY
# BGR---->GRAY
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print(img.shape)
print(img)
cv.imshow("cv",img)
cv.waitKey(0)
