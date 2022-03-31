import cv2
import numpy as np


#read image
image = cv2.imread('img/testcircle_false.jpg')
#correct answers
correctAnswer = [2,4]
circles = []
amount = 0


#variables for circle blob
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 300
#filter by how Circular the circles are
params.filterByCircularity = True
params.minCircularity = 0.4
#convexity
params.filterByConvexity = True
params.minConvexity = 0.2
#threshhold
params.thresholdStep = 5
params.minThreshold = 200
params.maxThreshold = 255
#shape
params.filterByInertia = True
params.minInertiaRatio = 0.1
#blob detector :D
detector = cv2.SimpleBlobDetector_create(params)

#variables rectangles
counter = 0
parts = []
areas = []
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
canny = cv2.Canny(blurred, 50, 255, 1)

rectangle = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rectangle = rectangle[0] if len(rectangle) == 2 else rectangle[1]

#draw detected rectangles
for rect in rectangle:
    x,y,w,h = cv2.boundingRect(rect)
    if(((x+w)-x) >= 50):
        cv2.rectangle(image, (x, y), (x + w, y + h), (255,50,0), 1)
        #split rows
        parts.append(image[y:y + h, x:x + w])

for i in range(0,len(parts)):
    #convert image
    gray = cv2.cvtColor(parts[i], cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    canny = cv2.Canny(blurred, 50, 255, 1)
    #draw area
    areaOfIntrest = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    areaOfIntrest = areaOfIntrest[0] if len(areaOfIntrest) == 2 else areaOfIntrest[1]
    print(str(i))
    for area in areaOfIntrest:
        x,y,w,h = cv2.boundingRect(area)
        if(((x+w)-x) >= 70):
            cv2.rectangle(parts[i], (x, y), (x + w, y + h), (50,255,0), 1)
            areas.append(parts[i][y:y + h, x:x + w])

for i in range(0,len(parts)):
    #convert image
    bilateral_filtered_image = cv2.bilateralFilter(parts[i], 5, 255, 255)
    edge_detected_image = cv2.Canny(bilateral_filtered_image, 50, 255)
    #detect circles
    keypoints = detector.detect(edge_detected_image)
    print(str(keypoints[0].pt[0]))
    #draw around blobs
    blank = np.zeros((1, 1))
    blobs = cv2.drawKeypoints(parts[i], keypoints, blank, (0, 0, 255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    #test parts
    cv2.imshow('test' + str(counter), blobs)
    counter += 1
    print(str(i))
            


#show results
cv2.imshow("Original Image",image)
#cv2.imshow("Circular Blobs Only", blobs)
#remove results
cv2.waitKey(0)
cv2.destroyAllWindows()