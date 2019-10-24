import cv2
import numpy as np


if __name__ == '__main__':
    def no_need(*arg):
        pass

cv2.namedWindow("result")
cv2.namedWindow("settings")


cv2.createTrackbar('H1', 'settings', 0, 185, no_need)
cv2.createTrackbar('S1', 'settings', 0, 255, no_need)
cv2.createTrackbar('V1', 'settings', 0, 255, no_need)
cv2.createTrackbar('H2', 'settings', 185, 185, no_need)
cv2.createTrackbar('S2', 'settings', 255, 255, no_need)
cv2.createTrackbar('V2', 'settings', 255, 255, no_need)


while True:
    image = cv2.imread('balls.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    h1 = cv2.getTrackbarPos('H1', 'settings')
    s1 = cv2.getTrackbarPos('S1', 'settings')
    v1 = cv2.getTrackbarPos('V1', 'settings')
    h2 = cv2.getTrackbarPos('H2', 'settings')
    s2 = cv2.getTrackbarPos('S2', 'settings')
    v2 = cv2.getTrackbarPos('V2', 'settings')

    lower = np.array((h1, s1, v1), np.uint8)
    upper = np.array((h2, s2, v2), np.uint8)
    thresh = cv2.inRange(gray, lower, upper)

    cv2.imshow('result', thresh)

    ch = cv2.waitKey(5)
    if ch == 32:
        color_filtr=[h1, s1, v1, h2, s2, v2]
        try:

            color_filtr_min = 'lower:'+", ".join(repr(e) for e in color_filtr[0:3])
            color_filtr_max = 'upper:' + ", ".join(repr(e) for e in color_filtr[3:6])
            print(color_filtr_min)
            print(color_filtr_max)
            color=input('Enter  color name:')

            with open('color_filtr.txt', 'a') as file:
                file.write(color+"\n")
                file.write("\n"+color_filtr_min+"\n")
                file.write(color_filtr_max+'\n')
                file.write('---------------------------------\n')

        except NameError:
            pass
        break