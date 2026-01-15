#로또 p
from random import shuffle # shuffle 사용

game_num=int(input('로또 게임 횟수 입력:'))

for i in range(game_num):
    balls=[x+1  for x in range(45)] #1-45개의 숫자가 balls에 저장
    #print(balls) #저장된 balls값 출력

    ret=[] #ret이라는 공백 리스트
    for j in range(6): #6회 반복(6개 숫자 뽑기)
        shuffle(balls) #숫자 섞기
        number=balls.pop() #balls에 있는 숫자하나 뺸 것을 추출--> number에 저장
        ret.append(number) #number 숫자를 ret[]에 추가
    ret.sort() #오름차순 정렬
    print("로또 번호[%2d]:"%(i+1),end='') #가로로 숫자 출력
    print(ret)

# 로또 p with tkinter
from tkinter import * 
from random import shuffle

def generation_random():
    
    ent_1.delete(0, END)
    ent_2.delete(0, END)
    ent_3.delete(0, END)
    ent_4.delete(0, END)
    ent_5.delete(0, END)
    ent_6.delete(0, END)

    for i in range(1):
        balls=[x+1  for x in range(45)] 
        

        ret=[] 
        for j in range(6): 
            shuffle(balls) 
            number=balls.pop()
            ret.append(number) 
        ret.sort() 
        print("로또 번호[%2d]:"%(i+1),end='') 
        print(ret)

    ent_1.insert(0,ret[0])
    ent_2.insert(0,ret[1])
    ent_3.insert(0,ret[2])
    ent_4.insert(0,ret[3])
    ent_5.insert(0,ret[4])
    ent_6.insert(0,ret[5])


windows=Tk()

#global 코드
la_title=Label(windows,text='로또 생성 프로그램')
la_num1=Label(windows,text='숫자1')
la_num2=Label(windows,text='숫자2')
la_num3=Label(windows,text='숫자3')
la_num4=Label(windows,text='숫자4')
la_num5=Label(windows,text='숫자5')
la_num6=Label(windows,text='숫자6')

#label 배치
la_title.grid(row=0,column=0,columnspan=6)
la_num1.grid(row=1,column=0)
la_num2.grid(row=1,column=1)
la_num3.grid(row=1,column=2)
la_num4.grid(row=1,column=3)
la_num5.grid(row=1,column=4)
la_num6.grid(row=1,column=5)

#entry 코드
ent_1=Entry(windows)
ent_2=Entry(windows)
ent_3=Entry(windows)
ent_4=Entry(windows)
ent_5=Entry(windows)
ent_6=Entry(windows)


#entry 배치
ent_1.grid(row=2,column=0)
ent_2.grid(row=2,column=1)
ent_3.grid(row=2,column=2)
ent_4.grid(row=2,column=3)
ent_5.grid(row=2,column=4)
ent_6.grid(row=2,column=5)

lotto=Button(windows, text='로또 생성 버튼',command=generation_random)
lotto.grid(row=3,column=0,columnspan=6)

windows.mainloop()