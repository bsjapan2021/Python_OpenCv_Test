import pygame      #pygame 모듈을 가져옴 
from tkinter import  *
import time

app_window = Tk() 
app_window.title("有限会社 B.S.Japan - (고객선물용)개발및 홈페이지제작문의 : https://bsjpan.jp  / E-mail : ceo@bsjapan.jp") 
app_window.geometry("765x250") 
app_window.resizable(0,0)

# Tk.attributes('-topmost', True) # 항상 창을 상위에 노출시키는 코드...


text_font= ("Boulder", 68, 'bold')
background = "#0e0738"
foreground= "#FFFFFF"
border_width = 25



label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)


def digital_clock(): 
   #    time.strftime('%Y-%m-%d', time.localtime(time.time()))
   time_live = time.strftime('%Y-%b-%d-%a', time.localtime(time.time())) +'\n'+ time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)






music_file = "1.mp3"   #음악파일을 music_file 변수에 대입

pygame.mixer.init()                    # mixer를 초기화 
pygame.mixer.music.load(music_file)    # 음악 파일을 로드 
pygame.mixer.music.play(0)              # 음악 재생 

clock = pygame.time.Clock()           
while pygame.mixer.music.get_busy():     # 음악파일이 재생되고있을 때 = true
      clock.tick(30)
    #   print ("30초로 시간을 제한합니다.") # 초당30 프레임이상이 안되게 제한

digital_clock()

pygame.mixer.quit()                      # 음악 종료






app_window.mainloop()