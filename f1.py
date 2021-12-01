from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from flask import Flask
app1 = Flask(__name__)
@app1.route('/')
class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1920x1080+0+0")
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Jayesh\Desktop\face-recog-pycharm\images\283242.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root, bg="skyblue")
        frame.place(x=540, y=170, width=340, height=450)

        img1=Image.open(r"C:\Users\Jayesh\Desktop\face-recog-pycharm\images\login.jpg")
        img1=img1.resize((150,150),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="skyblue",borderwidth=2)
        lblimg1.place(x=660,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",22,"bold"),fg="black",bg="skyblue")
        get_str.place(x=95,y=110)

        username=Label(frame,text="USERNAME",font=("times new roman",15,"bold"),fg="black",bg="skyblue")
        username.place(x=110,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password = Label(frame, text="PASSWORD", font=("times new roman", 15, "bold"), fg="black", bg="skyblue")
        password.place(x=110, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        # loginbtn = Button(frame, text="LOGIN",command=self.login, font=("times new roman", 15, "bold"), fg="black", bg="lightblue",activeforeground="black",activebackground="lightblue")
        # loginbtn.place(x=125, y=300)
        #
        # Registerbtn = Button(frame,command=self.register_window, text="Register", font=("times new roman", 15, "bold"),borderwidth=0,fg="black", bg="skyblue",activeforeground="black",activebackground="lightblue")
        # Registerbtn.place(x=40, y=350)
        #
        # forgetbtn = Button(frame,command=self.forget_password, text="Forget Password", font=("times new roman", 15, "bold"),borderwidth=0, fg="black", bg="skyblue",activeforeground="black",activebackground="lightblue")
        # forgetbtn.place(x=40, y=380)

if __name__=="__main__":
    # root=Tk()
    # app=Login_Window(app1)
    # root.mainloop()
    app1.run(debug=True, port=8000)