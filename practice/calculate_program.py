#계산기...pack ver
from tkinter import*
from math import*


#eval함수를 호출하여서 사용자가 입력한 수식을 계산한다. 
#레이블의 configure()을 호출해서 레이블의 텍스트를 변경한다.

def calculate(event): #함수안에 envent라는 매개변수가 들어감
    label.configure(text='정답:'+str(eval(entry.get()))) 
    # 아래의 결과값을 덮어쓰고**--enter--정답으로 바뀜


root=Tk()

Label(root,text='파이썬 수식 입력:').pack()

entry=Entry(root)


#이벤트 처리 부분을 참고한다.
#<Return>==엔터키
#Entry 위젯에서 엔터키를 치면, calculate()가 호출되게 연결. 
entry.bind('<Return>',calculate)
entry.pack()

label=Label(root,text='결과:')
label.pack()

root.mainloop()



#계산기...grid ver
from tkinter import*
from math import*


#eval함수를 호출하여서 사용자가 입력한 수식을 계산한다. 
#레이블의 configure()을 호출해서 레이블의 텍스트를 변경한다.

def calculate(event=None): #함수안에 event라는 매개변수가 들어감//#none..실행버튼을 누르면 이벤트에 전달해줄 것이 없어 라는 뚯..default parameter느낌
    label.configure(text='정답:'+str(eval(entry.get()))) # 아래의 결과값을 덮어쓰고**--enter--정답으로 바뀜

root=Tk()

Label(root,text='파이썬 수식 입력:').grid(row=0,column=0)

entry=Entry(root)

#Entry 위젯에서 엔터키를 치면, calculate()가 호출되게 연결. 이벤트 처리 부분을 참고한다.
entry.bind('<Escape>',calculate) #return=enter #Esacpe=esc
entry.grid(row=0,column=0)

#버튼 추가
button=Button(root,text='실행',command=calculate)
button.grid(row=1,column=0)

label=Label(root,text='결과:')
label.grid(row=2,column=0)

root.mainloop()


#dec.01.2025
# 계산기 p
from tkinter import *
 
flag=True
   
def click(key):
    global flag
    if flag==False:
         entry.delete(0,END)
         flag=True


    if(key=='='):
        try:
            result=eval(entry.get())
            entry.delete(0,END)
            entry.insert(END,str(result))
            flag=False
            
        except:
            entry.insert(END,'오류!')
    elif key=='C':
        entry.delete(0,END)
        flag=True
    else:
        entry.insert(END,key)

root=Tk()
root.title('버튼식계산기')

buttons=['7','8','9','+','C','4','5','6','-','','1','2','3','*','','0','.','=','/','']


i=0
for b in buttons:
    emd=lambda x=b: click(x)
    b=Button(root,text=b,width=5,relief='ridge',command=emd)
    b.grid(row=i//5+1,column=i%5)
    i+=1

entry=Entry(root,width=33,bg='yellow')
entry.grid(row=0,column=0,columnspan=5)
root.mainloop()