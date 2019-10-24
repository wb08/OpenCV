import cv2
import numpy as np
image=cv2.imread('balls.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
boundary = [
	((144,102,211), (163,255,255)),
	((104,99,12), (144,255,255)),
	((0,53,248), (9,175,255)),
	((40,89,120), (114,255,255)),
    ((0,199,123),(7,255,255)),
    ((19,138,223),(48,255,255))
]
i=0
for (lower,upper) in boundary:
    lower = np.array(lower, np.uint8)
    upper = np.array(upper, np.uint8)


    mask = cv2.inRange(gray, lower ,upper )
    output = cv2.bitwise_and(image, image, mask=mask)


    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)
    cv2.imwrite('ballsd{}.jpg'.format(i),output)
    i+=1