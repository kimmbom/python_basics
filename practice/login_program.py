#로그인 p
from tkinter import *

## 선언
def print_fields():  #아이디와 비밀번호 입력값을 가져와서 출력
    print('아이디:',e1.get(),'비밀번호:',e2.get())


def del_fields(): # 아이디와 비밀번호 입력값 삭제
    e1.delete(0,END) 
    e2.delete(0,END)

root=Tk()  # Tkinter 윈도우 생성

#아이디와 비밀번호 라벨 생성 및 배치
Label(root,text='아이디').grid(row=0,column=0)
Label(root,text='비밀번호').grid(row=1,column=0)
#Label().grid=생성+배치

#아이디와 비밀번호 입력 위젯 생성 및 배치
e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
#Entry(root).grid(row=0,column=1)
#Entry(root).grid(row=1,column=1)
# 나중에 e1.get()형태로 값 가지려면 합쳐서 적으면 오류발생

#로그인 및 취소 버튼 생성 및 배치
Button(root,text='로그인',command=print_fields).grid(row=2,column=0)
Button(root,text='취소',command=del_fields).grid(row=2,column=1)

root.mainloop()
