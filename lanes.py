import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

    # Step 2 Reduce Noise

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Step 3 find edges outlines dramatic changes
    canny = cv2.Canny(blur, 50, 150)
    return canny


def display_lines(image,lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line.reshape(4)
            cv2.line(line_image,(x1,y1),(x2,y2),(255,55,121), 10)
    return line_image

def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
        [(200, height), (1100, height), (550, 250)]
    ])
    mask = np.zeros_like(image)   # same as image as black
    cv2.fillPoly(mask,polygons, 255)
    masked_image = cv2.bitwise_and(image,mask)  #
    return masked_image





image = cv2.imread('test_image.jpg')

# Turn Image to Gray Scale
lane_image = np.copy(image)   # make copy important
canny= canny(lane_image)
cropped_image = region_of_interest(canny)
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]),minLineLength=40, maxLineGap=5)
line_image = display_lines(lane_image,lines)
combo_image = cv2.addWeighted(lane_image,0.8,line_image,1,1)
cv2.imshow("result",combo_image)
cv2.waitKey(0)





