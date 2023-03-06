import cv2
import random  
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('natu.png')
#  --->just toggle the commented code to uncomment and viseversa
#  ----> to open a web cam
# cam=cv2.VideoCapture(0)
while True:
    # is_OK,img=cam.read()
    grayscaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)
    for x,y,w,h in face_coordinates:
        a=random.randint(0,250)
        b=random.randint(0,250)
        c=random.randint(0,250)
        print(x,y,w,h)
        cv2.rectangle(img,(x,y),(x+w,y+h),(a,b,c),2)
        cv2.imshow("manikanta",img)
    keys=cv2.waitKey(1) 
    if keys==81 or keys==113:
        break
# cam.release()
print("Code Completed")