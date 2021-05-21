import tkinter as tk
from tkinter import *

class Fullscreen_Example:
    def __init__(self):
        self.window = tk.Tk()
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.w, self.h))
        
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

        # root = tk()
        self.window.title("確定申告書-金額算出")
        
        y_position = 47
         
        for i in range(11) :
            
           
            x_position = 20
            
            label = Label(self.window, text = i)
            label.pack()
            label.place(x=x_position, y=y_position)
            # x_position += 10
            y_position += 27


        y_position = 20    
        list = ["경비과목","임대료","수도관열비","광고선전비","여비교통비","통신비","접대교재비","외주공사비","소모품비","감가삼각비","재세공과금","합   계"]    
        for j in list :
            x_pos = 40
            
            label2 = Label(self.window, text = j,fg = "blue")
            label2.pack()
            label2.place(x=x_pos, y=y_position)
            
            y_position += 27
            
            
        #  ////////////////////////////////////////////////////             텍스트 입력을 구현

        def getTextInput():
            result=text_input.get("1.0","end")
            print(result)

        y_positi = 40
        label3 = Label(self.window, text = "실제금액",fg = "red")
        label3.pack()
        label3.place(x=200, y=20) 
        for k in range(12) :
            
           
            x_positi = 120

            text_input=tk.Text(self.window, width=30,height=5,fg = "blue")
            text_input.pack()
            text_input.place(x=x_positi, y=y_positi)  
            y_positi += 27

# ////////////////////////////////////////        실제금액 입력란 끝 /////////////////////
        y_positio = 40
        label4 = Label(self.window, text = "감면금액(40%)",fg = "blue")
        label4.pack()
        label4.place(x=450, y=20) 
        for k in range(12) :
            
           
            x_positio = 380

            text_input2=tk.Text(self.window, width=30,height=5,fg = "blue")
            text_input2.pack()
            text_input2.place(x=x_positio, y=y_positio)  
            y_positio += 27

# ////////////////////////////////////////        감면 입력란 끝 /////////////////////


        y_p = 40
        label5 = Label(self.window, text = "영수증상의 경비",fg = "blue")
        label5.pack()
        label5.place(x=700, y=20) 
        for k in range(12) :
            
           
            x_p = 650

            text_input3=tk.Text(self.window, width=30,height=5,fg = "blue")
            text_input3.pack()
            text_input3.place(x=x_p, y=y_p)  
            y_p += 27

# ////////////////////////////////////////  인정되는경비 끝 /////////////////////

# /////////////////////////////////// 각 항목 변수 할당하고 계산시작 해서 합계값출력 ////////////

        def quit():
            tk.destroy()


        Photo77 = PhotoImage(file = "C:/Users/bsjapan/Documents/Source_Python/.vscode/git/Tkinter_Ex/img.png")
        btnRead77=tk.Button(self.window, image=Photo77,command = quit)
        btnRead77.pack()
        btnRead77.place(x=900, y=27)  


























        #///////////////////////////// 실제금액 출력 /////////////////////
        # y_position = 20    
        # list = ["실제금액","실제금액","실제금액","실제금액","실제금액","실제금액","실제금액","실제금액","실제금액","실제금액","실제금액","합계"]    
        # for j in list :
        #     x_pos = 350
            
        #     label2 = Label(self.window, text = j)
        #     label2.pack()
        #     label2.place(x=x_pos, y=y_position)
            
        #     y_position += 27







        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

if __name__ == '__main__':
    app = Fullscreen_Example()  







# root.geometry("640x480") # 가로*세로크기
# root.geometry("1280x1024+50+10") # 가로 * 세로 + x좌표 +y좌표

# root.resizable(False,False)  # x너비, y높이 값 변경 불가 (창 크기 변경붚가)

# ------------------------------------------------------------------------------------------  기본 셋팅


# ####  버튼을 동작시키는 사용자정의 함수
# def btncmd() :
#     print ("버튼에 명령을 넣어줍니다.")

# ##########################################    

# Photo = PhotoImage(file = "Tkinter_Ex/img.png")
# btn7 = Button(root, image = Photo, command = btncmd)
# btn7.pack()


############## 레이블 ############################

# label1 = Label(root, text = "안녕하세요반갑습니다.")
# label1.pack()


# Photo = PhotoImage(file = "Tkinter_Ex/img2.png")
# label2 = Label(root, image = Photo )
# label2.pack()

# ##################  레이블 텍스트 바꾸기

# def change():
#     label1.config(text = " 이와 같이 텍스트가 바뀝니다.")
#     Photo2 = PhotoImage(file = "Tkinter_Ex/img.png")
#     label2.config(image = Photo2)

# btn1 = Button(root, text = "Click", command = change)    
# btn1.pack()

# ##############################################################

# root.mainloop()

