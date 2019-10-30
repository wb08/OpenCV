import cv2
import imutils
from PIL import Image
import os

def resized_image(image,width,height):
    img = Image.open(image)
    base_name, ext = os.path.splitext(image)
    image_copy=str(base_name)+'_copy'+str(ext)
    width = width
    height = height
    resized_img = img.resize((width, height), Image.ANTIALIAS)
    save_resized_img = resized_img.save(image_copy)

    return image_copy

def no_need(*arg):
    pass

cv2.namedWindow("result")
cv2.namedWindow("settings")
cv2.createTrackbar('thresh', 'settings', 0, 255, no_need)
cv2.createTrackbar('maxval', 'settings', 255, 255, no_need)
image = resized_image('korobka.jpg', 300, 500)
image_str = str(image)

while True:
    image = cv2.imread(image_str)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresh = cv2.getTrackbarPos('thresh', 'settings')
    maxval = cv2.getTrackbarPos('maxval', 'settings')

    ret = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY_INV)[1]

    cnts = cv2.findContours(ret.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    output = image.copy()

    for c in cnts:
        cv2.drawContours(output, [c], -1, (240, 0, 159), 3)

    cv2.imshow("result", output)
    cv2.imshow("settings", ret)
    ch = cv2.waitKey(5)
    if ch == 27:
        print('thresh:'+str(thresh))
        print('maxval:'+str(maxval))
        break
