import numpy as np
import cv2

def detectEdges(frame):    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 210)
    return edges


