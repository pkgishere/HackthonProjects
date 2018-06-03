import cv2
import numpy

def haar_face_detection(output_data):
    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

    ret, frame = cap.read()

    current_img = frame
    gray = cv2.cvtColor(current_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.1,
                                          minNeighbors=5,
                                          minSize=(30,30),
                                          flags = cv2.CASCADE_SCALE_IMAGE)

    biggest_face = 0
    big_x = 0
    big_y = 0
    big_w = 0
    big_h = 0
    for (x,y,w,h) in faces:
        if w*h > biggest_face:
            biggest_face = w*h
            big_x = x
            big_y = y
            big_w = w
            big_h = h

    cv2.rectangle(current_img,(big_x,big_y),(big_x+big_w,big_y+big_h),(255,0,0),2)
    roi_gray = gray[big_y:big_y+big_h, big_x:big_x+big_w]
    roi_color = current_img[big_y:big_y+big_h, big_x:big_x+big_w]
    #cv2.imwrite('data/haar_test.jpg', current_img)

    if output_data == 'center_face_position':
        return big_x + (big_w/2), big_y + (big_h/2)

    if output_data == 'cropped_face':
        cv2.imwrite('data/haar_test.jpg', roi_color)

    
