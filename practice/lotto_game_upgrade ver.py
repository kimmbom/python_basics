#연금복권 p(1/3)
import random

list_year=[]
j_num=random.randint(1,5) #조번호(제일 앞 칸)
for i in range(6):
    r_num=random.randint(0,9) #5개의 랜덤숫자
    list_year.append(r_num)

    print(j_num) #조번호 출력
    print(list_year) #6개의 랜덤숫자

#연금복권 p(2/3-3/3)
from tkinter import*
import random
def delProcess():
    a0.delete(0,END)
    a1.delete(0,END)
    a2.delete(0,END)
    a3.delete(0,END)
    a4.delete(0,END)
    a5.delete(0,END)
    a6.delete(0,END)
    

         
def process():
    delProcess() 
    rand_num0=(random.randint(1,5))
    rand_num1=(random.randint(0,9))
    rand_num2=(random.randint(0,9))
    rand_num3=(random.randint(0,9))
    rand_num4=(random.randint(0,9))
    rand_num5=(random.randint(0,9))
    rand_num6=(random.randint(0,9))

    a0.insert(0,str(rand_num0))
    a1.insert(0,str(rand_num1))
    a2.insert(0,str(rand_num2))
    a3.insert(0,str(rand_num3))
    a4.insert(0,str(rand_num4))
    a5.insert(0,str(rand_num5))
    a6.insert(0,str(rand_num6))

window=Tk()

window.title('연금복권')
window.geometry('290x70')

l1=Label(window,text='연금복권 프로그램')
l1.grid(row=0,column=0,columnspan=8)

a0=Entry(window,width=5)
a0_label=Label(window,text='조')
a1=Entry(window,width=5)
a2=Entry(window,width=5)
a3=Entry(window,width=5)
a4=Entry(window,width=5)
a5=Entry(window,width=5)
a6=Entry(window,width=5)

a0.grid(row=1,column=0)
a0_label.grid(row=1,column=1)
a1.grid(row=1,column=2)
a2.grid(row=1,column=3)
a3.grid(row=1,column=4)
a4.grid(row=1,column=5)
a5.grid(row=1,column=6)
a6.grid(row=1,column=7)

button1=Button(window,text='번호 생성!',width=18,command=process)
button2=Button(window,text='초기화',width=18,command= delProcess)
button1.grid(row=6,column=0,columnspan=4)
button2.grid(row=6,column=4,columnspan=4)

window.mainloop()

