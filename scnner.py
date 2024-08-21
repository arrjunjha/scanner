import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        
        if barcode.polygon:  # Check if polygon points are available
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        else:
            # Use the bounding rectangle if polygon is not available
            pts2 = barcode.rect
            cv2.rectangle(img, (pts2[0], pts2[1]), 
                          (pts2[0] + pts2[2], pts2[1] + pts2[3]), 
                          (255, 0, 255), 5)

        pts2 = barcode.rect
        cv2.putText(img, myData, (pts2[0], pts2[1] - 10), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255, 0, 255), 2)

    cv2.imshow('Result', img)
    cv2.waitKey(1)
