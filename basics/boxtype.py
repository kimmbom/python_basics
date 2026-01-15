from tkinter import*
root=Tk()
root.title('라디오 박스')
choice1=IntVar()
choice2=IntVar()
Label(root,text='가장 선호하는 프로그래밍 언어를 선택하시오.',justify=LEFT,padx=20).pack()
Radiobutton(root,text='Python',padx=20,variable=choice1,value=1).pack(anchor=W)  #Python vs C
Radiobutton(root,text='C',padx=20,variable=choice1,value=2).pack(anchor=W) 
Radiobutton(root,text='Java',padx=20,variable=choice2,value=3).pack(anchor=W)  #Java vs Swift 
Radiobutton(root,text='Swift',padx=20,variable=choice2,value=4).pack(anchor=W) 
root.mainloop()

#Python vs C vs Java vs Swift (W ver)
from tkinter import*
root=Tk()
root.title('라디오 박스')
choice1=IntVar()

Label(root,text='가장 선호하는 프로그래밍 언어를 선택하시오.',justify=LEFT,padx=20).pack()
Radiobutton(root,text='Python',padx=20,variable=choice1,value=1).pack(anchor=W) 
Radiobutton(root,text='C',padx=20,variable=choice1,value=2).pack(anchor=W) 
Radiobutton(root,text='Java',padx=20,variable=choice1,value=3).pack(anchor=W)  
Radiobutton(root,text='Swift',padx=20,variable=choice1,value=4).pack(anchor=W) 
root.mainloop()


#Python vs C vs Java vs Swift (E ver)
from tkinter import*
root=Tk()
root.title('라디오 박스')
choice1=IntVar()

Label(root,text='가장 선호하는 프로그래밍 언어를 선택하시오.',justify=LEFT,padx=20).pack()
Radiobutton(root,text='Python',padx=20,variable=choice1,value=1).pack(anchor=E) 
Radiobutton(root,text='C',padx=20,variable=choice1,value=2).pack(anchor=E) 
Radiobutton(root,text='Java',padx=20,variable=choice1,value=3).pack(anchor=E)  
Radiobutton(root,text='Swift',padx=20,variable=choice1,value=4).pack(anchor=E) 
root.mainloop()



#python 선택시 value1 값이 choice1에 들어가게 됨. 1234로 어떤 것을 선택했는지 역을 알 수 있음
from tkinter import*
root=Tk()
root.title('라디오 박스')
choice1=IntVar()


def radio_sel():
    if choice1.get()==1:
        print('Python 선택')
    elif choice1.get()==2:
        print('C 선택')
    elif choice1.get()==3:
        print('Java 선택')
    elif choice1.get()==4:
        print('Swift 선택')


Label(root,text='가장 선호하는 프로그래밍 언어를 선택하시오.',justify=LEFT,padx=20).pack()
Radiobutton(root,text='Python',padx=20,variable=choice1,value=1,command=radio_sel).pack(anchor=W)  
Radiobutton(root,text='C',padx=20,variable=choice1,value=2,command=radio_sel).pack(anchor=W) 
Radiobutton(root,text='Java',padx=20,variable=choice1,value=3,command=radio_sel).pack(anchor=W)  
Radiobutton(root,text='Swift',padx=20,variable=choice1,value=4,command=radio_sel).pack(anchor=W) 
root.mainloop()

#msgbox 나타내기
from tkinter import*
root=Tk()
root.title('라디오 박스')
choice1=IntVar()

import tkinter.messagebox as mbox
def radio_sel():
    if choice1.get()==1:  #.get ==정보를 가져와
        print('Python 선택')
        mbox.showinfo('Python','Python 선택')
    elif choice1.get()==2:
        print('C 선택')
        mbox.showerror('C','C언어 선택')

    elif choice1.get()==3:
        print('Java 선택')
        mbox.showwarning('Java','Java 선택')

    elif choice1.get()==4:
        print('Swift 선택')
        mbox.showinfo('Swift','Swift 선택')



Label(root,text='가장 선호하는 프로그래밍 언어를 선택하시오.',justify=LEFT,padx=20).pack()
Radiobutton(root,text='Python',padx=20,variable=choice1,value=1,command=radio_sel).pack(anchor=W)  
Radiobutton(root,text='C',padx=20,variable=choice1,value=2,command=radio_sel).pack(anchor=W) 
Radiobutton(root,text='Java',padx=20,variable=choice1,value=3,command=radio_sel).pack(anchor=W)  
Radiobutton(root,text='Swift',padx=20,variable=choice1,value=4,command=radio_sel).pack(anchor=W) 
root.mainloop()


#radio box... 중복 X//check box... 중복 0
from tkinter import*

root=Tk()
Label(root,text='선호하는 언어를 모두 선택하시오.').grid(row=0,sticky=W)

value1=IntVar()
value2=IntVar()
value3=IntVar()
value4=IntVar()

Checkbutton(root,text='Python',variable=value1).grid(row=1,sticky=W)
Checkbutton(root,text='C',variable=value2).grid(row=2,sticky=W)
Checkbutton(root,text='Java',variable=value3).grid(row=3,sticky=W)
Checkbutton(root,text='Swift',variable=value4).grid(row=4,sticky=W)

root.mainloop()

#radio box... 중복 X//check box... 중복 0
from tkinter import*
from tkinter import messagebox as mb

def check_result_Status():
    et.delete(0,END)
    if (chk1.get()==1 and chk2.get()==1):
        et.insert(0,'피자랑 치킨')
    elif (chk1.get()==1 ):
        et.insert(0,'피자')
    elif (chk2.get()==1 ):
        et.insert(0,'치킨')

def check_pizza_Status():
    if (chk1.get()==1):
        mb.showinfo('체크확인','피자를 선택하셨네요!')

def check_chicken_Status():
    if (chk2.get()==1):
        mb.showinfo('체크확인','치킨 선택하셨네요!')

bm=Tk()
bm.title('tkinter 체크 박스')
bm.geometry('300x120')

l1=Label(bm,text='좋아하는 음식 선택')
l1.grid(row=0,column=0)

chk1=IntVar()
chk2=IntVar()

cb1=Checkbutton(bm,text='피자',variable=chk1,command=check_pizza_Status)
cb1.grid(row=1,column=0)
cb2=Checkbutton(bm,text='치킨',variable=chk2,command=check_chicken_Status)
cb2.grid(row=2,column=0)

button=Button(bm,text='결과',width=10,command=check_result_Status)
button.grid(row=3,column=0)
et=Entry(bm,width=10)  #entry 위젯...et
et.grid(row=4,column=0)

bm.mainloop()

#radio box... 중복 X//check box... 중복 0
from tkinter import*
from tkinter import messagebox as mb

def check_result_Status():
    et.delete(0,END)
    if (chk1.get()==1 and chk2.get()==1):
        et.insert(0,'피자랑 치킨')
    elif (chk1.get()==1 ):
        et.insert(0,'피자')
    elif (chk2.get()==1 ):
        et.insert(0,'치킨')

def check_pizza_Status():
    if (chk1.get()==1):
        mb.showinfo('체크확인','피자를 선택하셨네요!')

def check_chicken_Status():
    if (chk2.get()==1):
        mb.showinfo('체크확인','치킨 선택하셨네요!')

bm=Tk()
bm.title('tkinter 체크 박스')
bm.geometry('300x120')

l1=Label(bm,text='좋아하는 음식 선택')
l1.grid(row=0,column=0)

chk1=IntVar()
chk2=IntVar()

cb1=Checkbutton(bm,text='피자',variable=chk1,command=check_pizza_Status)
cb1.grid(row=1,column=0)
cb2=Checkbutton(bm,text='치킨',variable=chk2,command=check_chicken_Status)
cb2.grid(row=2,column=0)

button=Button(bm,text='결과',width=10,command=check_result_Status)
button.grid(row=3,column=0)
et=Entry(bm,width=10)  
et.grid(row=4,column=0)

bm.mainloop()