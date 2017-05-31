import os
import numpy as np
import cv2

fgbg = cv2.createBackgroundSubtractorMOG2()
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 800, 600)
for file in os.listdir("C:\Users\Paul\Desktop\SS2017\SMBAD\source\scripts\weather-image\data"):
    if file.endswith("jpg"):
        frame = cv2.imread(file)
        fgmask = fgbg.apply(frame)
        print file
        cv2.imshow('frame',frame)
        cv2.destroyAllWindows()