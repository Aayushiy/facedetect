import cv2
face_cascade =cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
def detect(gr,frame):
    faces = face_cascade.detectMultiScale(gr,scaleFactor =1.05,minNeighbors=5)
    for x,y,w,h in faces:
        #drawing box and labelling
     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
     cv2.putText((frame), "Face", (x+100,y+h+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3, cv2.LINE_AA)


    return frame 
    
a=cv2.VideoCapture(0)
while True:
    check,frame=a.read()
    print(frame)
    gr=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas=detect(gr,frame)
    cv2.imshow("Happy",canvas)
    t=cv2.waitKey(1)
    if t==ord("q"):
        break

canvas=detect(gr,frame)
a.release()
cv2.destroyAllWindows()
