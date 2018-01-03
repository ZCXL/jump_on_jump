#-*- encode:utf-8 -*-
#/bin/python
import cv2
image=cv2.imread('current.png')
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
#resized = cv2.resize(thresh, (0, 0), 0.125, 0.125, cv2.INTER_NEAREST)
fx=0.125
fy=0.125
resized = cv2.resize(thresh, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_NEAREST)
cv2.imwrite('current_gradx.png', resized)
'''
for i in range(0, 5):
    for j in range(0, 5):
        startx = j * 288
        starty = i * 288 + 680
        f=open('./data/%d_%d' % (i, j), 'w')
        print startx, starty
        for k in range(0, 36):
            for l in range(0, 36):
                starty_1 = starty + k * 8
                startx_1 = startx + l * 8
                colored=0
                nocolor=0
                for x in range(0, 8):
                    for y in range(0, 8):
                        if thresh[starty_1 + x][startx_1 + y] > 0:
                            colored+=1
                        else:
                            nocolor+=1
                if nocolor == 0:
                    f.write('1')
                    continue
                if colored / nocolor >= 1:
                    f.write('1')
                else:
                    f.write('0')
            f.write("\n")
        f.close()
f=open("./data/current", 'w')
for i in range(0, 180):
    for j in range(0, 180):
        startx = j * 8
        starty = i * 8 + 680
        colored=0
        nocolor=0
        for y in range(0, 8):
            for x in range(0, 8):
                if (thresh[starty + y][startx + x]) > 0:
                    colored+= 1
                else:
                    nocolor+=1
        if nocolor == 0:
            f.write('1')
            continue
        if colored / nocolor >= 1:
            f.write('1')
        else:
            f.write('0')
    f.write('\n')
f.close()
'''
