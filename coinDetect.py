import cv2
import numpy as np

img = cv2.imread("Desktop/Projects/coins.jpg")
cv2.startWindowThread()
cv2.namedWindow("canny")
#cv2.namedWindow("coins")
                

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 3)
ret, thresh = cv2.threshold(blur, 170, 255, cv2.THRESH_BINARY)
canny = cv2.Canny(thresh, 170, 255)

contours, heirarchy = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img, contours, -1, (0,255,0), 2)

sortedCon = sorted(contours, key = cv2.contourArea)
i = 1
for i, cont in enumerate(sortedCon):
    x, y, w, h = cv2.boundingRect(cont)
    print(i)
    #print(x, y, w, h)

    X = x + int(w/2)
    Y = y + int(h/2)

    img = cv2.circle(img, (X,Y), 50, (0,255,0), 2)

    img = cv2.putText(img = img, text = str(i+1), org=(X,Y), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale= 1.0, color = (0,255,255), thickness = 2)

cv2.imshow("canny", thresh)
cv2.imshow("coins", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
