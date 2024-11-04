import cv2

img_left = cv2.imread('left_image.jpg')
img_right = cv2.imread('right_image.jpg')

if img_left.shape[0] != img_right.shape[0] or img_left.shape[1] != img_right.shape[1]:
    img_right = cv2.resize(img_right, (img_left.shape[1], img_left.shape[0]))

left_red = img_left.copy()
left_red[:, :, 1] = 0
left_red[:, :, 2] = 0

right_cyan = img_right.copy()
right_cyan[:, :, 0] = 0

anaglyph_img = left_red + right_cyan

cv2.imshow('Anaglyph Image', anaglyph_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

