import cv2
import imutils
import numpy as np

cap = cv2.VideoCapture("20180910_144521.mp4")

#lower = np.array([135,190,191])
#upper = np.array([195,260,239])

#lower = np.array([105,10,150])
#upper = np.array([195,260,239])

#lower = np.array([105,10,150])
#upper = np.array([255,260,239])

lower = np.array([100,5,150])
upper = np.array([200,200,200])

while True:
    
    ok, frame = cap.read()
    frame = imutils.resize(frame, width=350)  # resize do tamanho do video original
    frameClone = frame.copy()

    #roi = frame[80: 550 , 200: 300]
    
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#HSV onverter da escala RGB (ou BGR) para HSV
    

    blur = cv2.medianBlur(frame_hsv ,7) #  filtro de mediana para remoção de alguns ruídos.
    mask = cv2.inRange(blur, lower, upper)

    _,mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

        area = cv2.contourArea(cnt)
        if(area > 100):
           x,y,w,h = cv2.boundingRect(cnt)
           roi = frameClone[y:y+h, x:x+w]
           cv2.rectangle(frameClone,(x,y),(x+w,y+h), (0,255,0),3)


    #res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("HSV", blur)
    cv2.imshow("roi", roi)
    cv2.imshow("frameClone", frameClone)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == 113:
        break
    

cap.release()
cv2.destroyAllWindows()
  


