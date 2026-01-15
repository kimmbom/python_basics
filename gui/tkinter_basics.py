#
from tkinter import *

window=Tk()
button=Button(window,text='클릭하세요')
button.pack()
window.mainloop()

#
from tkinter import*

def process():
 print('안녕하세요')
 
window=Tk()
button=Button(window,text='클릭하세요',command=process)
button.pack()

window.mainloop()


#
from tkinter import*

def paint(event):
    x1,y1= (event.x-1),(event.y+1)
    x2,y2= (event.x-1),(event.y+1)
    canvas.create_oval(x1,y1,x2,y2)

window=Tk()
canvas=Canvas(window)
canvas.pack()
canvas.bind("<B1-Motion>",paint)
window.mainloop()

#
from tkinter import*
window=Tk()

w=Label(window,text='박스#1',bg='red',fg='white')
w.place(x=0,y=0)
w=Label(window,text='박스#2',bg='green',fg='black')
w.place(x=20,y=20)
w=Label(window,text='박스#3',bg='blue',fg='white')
w.place(x=40,y=40)

window.mainloop()

#위치 변경... 겹침
from tkinter import*
window=Tk()

w=Label(window,text='박스#1',bg='red',fg='white')
w.place(x=0,y=0)
w=Label(window,text='박스#2',bg='green',fg='black')
w.place(x=10,y=10)
w=Label(window,text='박스#3',bg='blue',fg='white')
w.place(x=40,y=40)

window.mainloop()

#
from tkinter import*

# def process():
#    e2.insert(0,'100')

def process():
    temperature=float(e1.get())
    mytemp=(temperature-32)*5/9
    e2.insert(0,str(mytemp))
 #위치.insert(o,'내용')0...맨 앞에//END...맨 마지막
 
 
# #all about button
from tkinter import*
def bt4_func():
    print('b4를 클릭!')

def label_click():
    label1.config(text='레이블을 클릭!')

    global photo2
    photo2=PhotoImage(file="C:\\Users\\min_m\\OneDrive\\그림\\Screenshots\\k.png")
    label2.config(image=photo2)

root=Tk()

root.title('제가 한 번 벼락치기 해볼게요')
root.geometry('1000x3000+100+100')
root.resizable(False,False)
photo1=PhotoImage(file="C:\\Users\\min_m\\OneDrive\\그림\\Screenshots\\스크린샷 2025-12-15 190723.png")

label1=Label(root,text='정성찬')
label1.pack()

label2=Label(root,text='label2임')
label2.pack()

bt1=Button(root,image=photo1)
bt2=Button(root,text='b2',fg='red',bg='skyblue',command=label_click) #b2를 누르면 사진이 나옴+위쪽에 label2 도출
bt3=Button(root,text='b3',padx=10,pady=20)
bt4=Button(root,text='b4',width=10,height=20,command=bt4_func)
bt1.pack()
bt2.pack(padx=10,pady=20)
bt3.pack()
bt4.pack()

root.mainloop()


#
window=Tk()
window.geometry('300x300')

l1=Label(window,text='화씨',font='helvetica 16 italic') # 폰트 변경
l2=Label(window,text='섭씨',font='helvetica 16 italic')
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)

e1=Entry(window,bg='green',fg='white') #색 변경
e2=Entry(window,bg='green',fg='white')
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b1=Button(window,text='화씨->섭씨',command=process)
b2=Button(window,text='섭씨->화씨')
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)

window.mainloop()