import cv2
# load in the top image
top_img = cv2.imread('6.png')
top_img = cv2.cvtColor(top_img, cv2.COLOR_RGB2GRAY)
#top_img = top_img.reshape(28,28,1)
new_shape1 = (22, 22)
top_img = cv2.resize(top_img, new_shape1)
top_img = top_img.reshape(22,22,1)
top_img_w, top_img_h, channel1 = top_img.shape
# load in the bottom image
bottom_img = cv2.imread('black.jpg')
binary_threshold = 100
bottom_img = cv2.cvtColor(bottom_img, cv2.COLOR_RGB2GRAY)
new_shape2 = (28, 28)
bottom_img = cv2.resize(bottom_img, new_shape2)
bottom_img = bottom_img.reshape(28,28,1)
# get the size or use 150x150 if it's constant
bottom_img_w, bottom_img_h,channel2 = bottom_img.shape

# offset the top image so it's placed in the middle of the bottom image
offset_w = (bottom_img_w - top_img_w) // 2
offset_h = (bottom_img_h - top_img_h) // 2
# embed top_img on top of bottom_img
bottom_img[offset_w:offset_w+top_img_w,offset_h:offset_h+top_img_h]=top_img

cv2.imwrite("./N.png",bottom_img)
