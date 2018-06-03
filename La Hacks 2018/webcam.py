import cv2

def capture_picture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('data/test.jpg', frame)


#def capture_video():
#    cap = cv2.VideoCapture(0)

#    while True:
#        ret, frame = cap.read()
#        if ret:
#            cv2.imshow('test', frame)
#        if cv2.waitKey(1) == 27:
#            break
#    cv2.destroyAllWindows()
