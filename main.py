import numpy as np
import cv2

img = np.zeros([710 , 1370 , 3] , np.uint8)
#Background
cv2.rectangle(img , (0 , 0) , (1370 , 550) , (255 , 255 , 85) , -1)
cv2.rectangle(img , (0 , 550) , (1370 , 710) , (75 , 180 , 70) , -1)

#sun
cv2.circle(img , (200 , 150) , 60 , (0 , 255 , 255) , -1)
cv2.circle(img , (200 , 150) , 70 , (220 , 255 , 255) , 1)

#tree
cv2.line(img , (1000 , 550) ,(1000 , 500) , (30,65 , 155) , 15)
triangle2 = np.array([[900 ,500] , [1100 ,500] , [1000, 250]] ,dtype=np.int32)
cv2.fillPoly(img , [triangle2] , (75,180 ,70))
cv2.line(img , (850 , 550) ,(850 , 480) , (30,65 , 155) , 25)
triangle2 = np.array([[750 ,480] , [950 ,480] , [850, 100]] ,dtype=np.int32)
cv2.fillPoly(img , [triangle2] , (75,200 ,70))

cv2.imshow("image ",img)
cv2.waitKey(0)