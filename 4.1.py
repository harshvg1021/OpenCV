import cv2
import numpy
photo = numpy.zeros((800,800,3))
font = cv2.FONT_HERSHEY_SIMPLEX

photo = cv2.rectangle(photo, (240,300),(700,500), [0,255,0], 5 )
photo = cv2.line(photo,(240,300),(470,100), [255,0,0], 5)
photo = cv2.line(photo,(470,100),(700,300), [255,0,0], 5)
photo = cv2.line(photo,(0,500),(240,500), [255,255,255], 5)
photo = cv2.line(photo,(700,500),(800,500), [255,255,255], 5)
photo = cv2.line(photo,(380,375),(560,375), [255,0,0], 5)
photo = cv2.line(photo,(380,375),(380,500), [255,0,0], 5)
photo = cv2.line(photo,(560,375),(560,500), [255,0,0], 5)

cv2.imshow("TASK 4.1 ", photo)
cv2.waitKey()
cv2.destroyAllWindows()
