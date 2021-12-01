from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.title("Face Detector")
        self.root.geometry("1366x768+0+0")

        btn = Button(self.root,command=self.face_recog,cursor="hand2", text="FACE DETECTOR", width=15,font=("times new roman", 15, "bold"), bg="red", fg="white")
        btn.place(x=600, y=300, width=200, height=60)

    def mark_attendance(self,n,r,d):
        with open("jay.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            namelist=[]
            for line in mydatalist:
                entry=line.split(".")
                namelist.append(entry[0])
                if ((n not in namelist) and (r not in namelist) and (d not in namelist)):
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtstring=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{n},{r},{d},{dtstring},{d1},Present")
                # f"\n{n},{r},{d},{dtstring},{d1},Present"


    def face_recog(self):
        def draw_boundary(img,classifier,scalefactor,minineighbors,color,text,clf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scalefactor,minineighbors)
            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_img[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="Jayeshcnair1",database="mydata")
                my_cursor = conn.cursor()

                my_cursor.execute("select name from student where enrollment="+str(id))
                n=my_cursor.fetchone()
                # n = str(n)
                n="+".join(n)

                my_cursor.execute("select enrollment from student where enrollment=" + str(id))
                r = my_cursor.fetchone()
                # r = str(r)
                r = "+".join(r)

                my_cursor.execute("select department from student where enrollment=" + str(id))
                d = my_cursor.fetchone()
                # d = str(d)
                d = "+".join(d)
                # f"name:{n}"
                # f"enrollment:{r}"
                # f"department:{d}"
                if confidence>77:
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)
                    cv2.putText(img, f"Enrollment:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)
                    self.mark_attendance(n,r,d)
                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0,0, 255), 3)
                    cv2.putText(img, "Unknown face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord=[x,y,w,h]
            return coord

        def recognize(img,clf,facecascade):
            coord=draw_boundary(img,facecascade,1.1,10,(255,25,255),"Face",clf)
            return img

        facecascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0) #,cv2.CAP_DSHOW

        while True:
            ret,img=video_cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            img=recognize(img,clf,facecascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Face recognition successful")




if __name__=="__main__":
    root=Tk()
    Face_Recognition(root)
    root.mainloop()