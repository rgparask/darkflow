import numpy as np
import cv2
import edgeDetector as ed

cv2.namedWindow("edges")
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while(True):
    ret, frame = cap.read()
    edges = ed.detectEdges(frame)
    cv2.imshow("edges", edges)
    cv2.waitKey(1)
