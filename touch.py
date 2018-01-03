#-*- encode:utf-8 -*-
#/bin/python
import commands
import time
import sys
import cv2
from numpy import *
def send_command(command):
    commands.getstatusoutput(command)
def process_img(image):
    # transfer image from rgb to gray
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # calculate the sobel of x and y axis.
    gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)
    # blur and threshold the image
    blurred = cv2.blur(gradient, (9, 9))
    (_, thresh) = cv2.threshold(blurred, 45, 255, cv2.THRESH_BINARY)

    return thresh
def find_chesspiece(origin, compare):
    #load image which will be compared
    d, w, h = compare.shape[::-1]
    compare_thresh = process_img(compare)

    origin_thresh = process_img(origin)
    result = cv2.matchTemplate(origin_thresh, compare_thresh, method=cv2.TM_SQDIFF)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    x = (top_left[0] + bottom_right[0]) / 2
    y = bottom_right[1]

    return x, y
def normalize_image(image):
    thresh = process_img(image)
    w, h = thresh.shape[::-1]
    max_x = w / 8
    max_y = h / 8
    mat = zeros((max_y, max_x))
    for i in range(0, max_y):
        for j in range(0, max_x):
            startx = j * 8
            starty = i * 8
            colored=0
            nocolor=0
            for y in range(0, 8):
                for x in range(0, 8):
                    if (thresh[starty + y][startx + x]) > 0:
                        colored += 1
                    else:
                        nocolor += 1
            if nocolor == 0:
                mat[i, j] = 1
                continue
            if colored / nocolor >= 1:
                mat[i, j] = 1
            else:
                mat[i, j] = 0
    return mat
def find_next_pos(image):
    mat = normalize_image(image)
    top_x = 0
    top_y = 0
    is_found = False
    for i in range(mat.shape[0] / 4, mat.shape[0]):
        for j in range(0, mat.shape[1]):
            if mat[i][j] == 1:
                top_x = j
                top_y = i
                is_found = True
                break
        if is_found:
            break
    ignore_cnt = 5
    bottom_y = 0
    for i in range(top_y + ignore_cnt, mat.shape[1]):
        if mat[i][top_x] == 1:
            bottom_y = i
            break
    return (top_x * 8, (top_y + bottom_y) / 2 * 8)
compare = cv2.imread('compare.png')
origin = cv2.imread('current.png')
chess_x, chess_y = find_chesspiece(origin, compare)
print "chess position:(%d, %d)" % (chess_x, chess_y)
grid_x, grid_y = find_next_pos(origin)
print "grid position:(%d, %d)" % (grid_x, grid_y)
distance = ((chess_x - grid_x)**2 + (chess_y - grid_y)**2)**0.5
print "distance:%f" % distance
time_span = distance / 1432
print "time:%f" % time_span
send_command('sh ./start_touch.sh')
time.sleep(float(time_span))
send_command('sh ./finish_touch.sh')
