from tkinter import * 
import requests
from datetime import datetime , timedelta
import json
import io

root = Tk()
root.title("大阪COVID19情報")
root.geometry("640x480") # 가로*세로크기
root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 +y좌표
root.resizable(False,False)  # x너비, y높이 값 변경 불가 (창 크기 변경붚가)

# ------------------------------------------------------------------------------------------  기본 셋팅

def close_window():
  root.destroy()


def execute():
  requestUrl = "https://api.opendata.go.jp/osaka-fu/patients-summary?apikey=n1gVGU0wkLZOSmCWDQDcB9gD0JdXp1TO"
  requestHeaders = {
    "Accept": "application/json"
  }


  request = requests.get(requestUrl, headers=requestHeaders)
  val = json.loads(request.content)
  

  Todate = datetime.today().year + datetime.today().month + datetime.today().day

  # 오늘날짜
  Todate = datetime.today().strftime("%Y-%m-%d")

  # 어제날짜
  yesterday = datetime.today() - timedelta(1)
  sum = 0

  Photo = PhotoImage(file = "C:/Users/bsjapan/Documents/Source_Python/.vscode/git/Tkinter_Ex/img2.png")
  btn = Button(root, image = Photo, command = close_window)
  btn.pack()

  for i in val:
    if Todate == str(val[sum]["日付"]):
            
        lbl = Label(root, text = " **  大阪府COVID19現状リスト(RealTime)  **")
        lbl.pack()
        tit = Label(root, text = " **  Yesterday  **")
        tit.pack()


        lbl1 = Label(root, text = "日付:" + val[sum-1]["日付"])
        lbl1.pack()

        lbl2 = Label(root, text = "検査件数:" + val[sum-1]["検査件数"])
        lbl2.pack()

        lbl3 = Label(root, text = "陽性人数:" + val[sum-1]["陽性人数"])
        lbl3.pack()

        lbl4 = Label(root, text = "陽性累計:" + val[sum-1]["陽性累計"])
        lbl4.pack()

        lbl5 = Label(root, text = "現在陽性者数:" + val[sum-1]["現在陽性者数"])
        lbl5.pack()

        lbl6 = Label(root, text = "退院:" + val[sum-1]["退院"])
        lbl6.pack()

        lbl7 = Label(root, text = "退院済累計:" + val[sum-1]["退院済累計"])
        lbl7.pack()

        lbl8 = Label(root, text = "退院判明:" + val[sum-1]["退院判明"])
        lbl8.pack()

        lbl9 = Label(root, text = "退院判明累計:" + val[sum-1]["退院判明累計"])
        lbl9.pack()

        lbl10 = Label(root, text = "死亡:" + val[sum-1]["死亡"])
        lbl10.pack()

        lbl11 = Label(root, text = "リンク不明者:" + val[sum-1]["リンク不明者"])

        lbl11.pack()

      # today /////////////////////

        lbl1 = Label(root, text = "日付:" + val[sum]["日付"])
        lbl1.pack()

        lbl2 = Label(root, text = "検査件数:" + val[sum]["検査件数"])
        lbl2.pack()

        lbl3 = Label(root, text = "陽性人数:" + val[sum]["陽性人数"])
        lbl3.pack()

        lbl4 = Label(root, text = "陽性累計:" + val[sum]["陽性累計"])
        lbl4.pack()

        lbl5 = Label(root, text = "現在陽性者数:" + val[sum]["現在陽性者数"])
        lbl5.pack()

        lbl6 = Label(root, text = "退院:" + val[sum]["退院"])
        lbl6.pack()

        lbl7 = Label(root, text = "退院済累計:" + val[sum]["退院済累計"])
        lbl7.pack()

        lbl8 = Label(root, text = "退院判明:" + val[sum]["退院判明"])
        lbl8.pack()

        lbl9 = Label(root, text = "退院判明累計:" + val[sum]["退院判明累計"])
        lbl9.pack()

        lbl10 = Label(root, text = "死亡:" + val[sum]["死亡"])
        lbl10.pack()

        lbl11 = Label(root, text = "リンク不明者:" + val[sum]["リンク不明者"])
        lbl11.pack()
        sum += 1  

  else :
    sum += 1
   
  # print ("**  Copyright@2021,B.S.Japan // Osaka-Fu Covid19(RealTime)  **")

if __name__ == "__main__":
  execute()

    
root.mainloop()    
  

 
