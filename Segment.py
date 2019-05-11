import os
import cv2
import numpy as np

sour_dir = "./origin/"   # picture to be detected
dst_dir = "./"            # destination directory
min_val = 10
min_range = 30

# load in the bottom image for future reshape
bottom_img = cv2.imread('black.jpg')
binary_threshold = 100
bottom_img = cv2.cvtColor(bottom_img, cv2.COLOR_RGB2GRAY)
new_shape2 = (28, 28)
bottom_img = cv2.resize(bottom_img, new_shape2)
bottom_img = bottom_img.reshape(28,28,1)
bottom_img_w, bottom_img_h,channel2 = bottom_img.shape

count = 0
def frame_peek(array_vals, minimun_val, minimun_range):
    start_i = None
    end_i = None
    peek_ranges = []
    for i, val in enumerate(array_vals):
        if val > minimun_val and start_i is None:
            start_i = i
        elif val > minimun_val and start_i is not None:
            pass
        elif val < minimun_val and start_i is not None:
            if i - start_i >= minimun_range:
                end_i = i
                print(end_i - start_i)
                peek_ranges.append((start_i, end_i))
                start_i = None
                end_i = None
        elif val < minimun_val and start_i is None:
            pass

    return peek_ranges

def Segmentation(img, peek_range):
    global count
    for i, peek_range in enumerate(peek_ranges):
        for vertical_range in vertical_peek_ranges2d[i]:
            x = vertical_range[0]
            y = peek_range[0]
            w = vertical_range[1] - x
            h = peek_range[1] - y
            pt1 = (x, y)
            pt2 = (x + w, y + h)
            count += 1
            img1 = img[y:peek_range[1], x:vertical_range[1]]
            new_shape = (22, 22)
            img1 = cv2.resize(img1, new_shape)
            img_gray = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
            img_gray = img_gray.reshape(22,22,1)
            top_img_w, top_img_h, channel1 = img_gray.shape
            binary_threshold = 100
            cv2.threshold(img_gray, binary_threshold, 255, cv2.THRESH_BINARY_INV, img_gray)
            # offset the top image so it's placed in the middle of the bottom image
            offset_w = (bottom_img_w - top_img_w) // 2
            offset_h = (bottom_img_h - top_img_h) // 2
            # embed top_img on top of bottom_img
            bottom_img[offset_w:offset_w+top_img_w,offset_h:offset_h+top_img_h]=img_gray
            cv2.imwrite(dst_dir + str(count) + ".png", bottom_img)

for fileName in os.listdir(sour_dir):
    img = cv2.imread(sour_dir + fileName)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    new_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                               cv2.THRESH_BINARY_INV, 11, 2)
    horizontal_sum = np.sum(new_threshold, axis=1)
    peek_ranges = frame_peek(horizontal_sum, min_val, min_range)
    line_seg_adaptive_threshold = np.copy(new_threshold)
    for i, peek_range in enumerate(peek_ranges):
        x = 0
        y = peek_range[0]
        w = line_seg_adaptive_threshold.shape[1]
        h = peek_range[1] - y
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        cv2.rectangle(line_seg_adaptive_threshold, pt1, pt2, 255)
    vertical_peek_ranges2d = []

    for peek_range in peek_ranges:
        start_y = peek_range[0]
        end_y = peek_range[1]
        line_img = new_threshold[start_y:end_y, :]
        vertical_sum = np.sum(line_img, axis=0)
        vertical_peek_ranges = frame_peek(
            vertical_sum, min_val, min_range)
        vertical_peek_ranges2d.append(vertical_peek_ranges)

Segmentation(img, peek_range)
