import cv2

grey_img = cv2.imread ("image/1(1).jpg", 0)
img = cv2.imread ("image/1(1).jpg", 1)

resized = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Display Image', img)
cv2.imshow("resized pic", resized)
print(img.shape)
print("Top left", img[0, 0])
print("Top right", img[0, 400])
print("Bottom left", img[90, 0])
print("Bottom right", img[90, 400])
white = img [:, :, 0]
green = img [:, :, 1]
red = img [:, :, 2]
cv2.imshow("red pic", red)
cv2.imshow("color pic", img)
cv2.waitKey(0)
cv2.destroyAllWindows()