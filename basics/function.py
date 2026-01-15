def print_address():
 print('서울특별시 종로구 1번지')
 print('파이썬 빌딩 7층')
 print('홍길동')

print_address()


#위에꺼 수정 ver
def print_address(name):
 print('서울특별시 종로구 1번지')
 print('파이썬 빌딩 7층')
 print(name)

print_address('홍길동')
print_address('김코드')
print_address('나함수')


#함수에 여러개의 인수 전달
def get_sum(start,end):
 sum=0
 for i in range(start,end+1):
  sum+=i
print('sum=',sum)

get_sum(1,10)
get_sum(1,20)

#기본값 있는 함수
def inc(a,step=1):
 print(a+step)

inc(10)
inc(10,50)

#return...함수 종료 
def f():
  print('a')
  return
  print('b') #b 실행 안됨

#return...값을 밖으로 내보내기
def ff(a,b):
  return a+b
result=ff(3,5)
print(result)


#함수의 값 반환하기...return(저장0)
def calculate_area(radius):
 area=3.14*radius**2
 return area
c_area=calculate_area(5.0)
print(c_area)

#함수의 값 반환하기...return(저장X==출력X)
def calculate_area(radius):
 area=3.14*radius**2
 return area
calculate_area(5.0)

#. return 여러개 가능함!
def get_input():
    return 2,3
x,y=get_input()
print(x,',',y)

#. leehi-only..ㅠㅠㅠ큐ㅠㅠ
def judge(num):
 if num%2==0:
  print('짝수')
  return 
 print('홀수')

num=int(input('자연수를 입력하시오.'))
judge(num)

##번외...return이 여러개
def check_num(n):
  if n>0:
    print('양수')
    return
  if n<0:
    print('음수')
    return
  print('0이다')

check_num(9)
check_num(0)
check_num(-7)

        
#지역변수 예제
def calculate_area():
 result=3.14*r**2
 return result  #result=지역변수
 
r=float(input('반지름을 입력하시오.')) #r=전역변수
area=calculate_area()
print(area)

#p
# def calculate_area():
#  result=3.14*r**2

# r=float(input('반지름을 입력하시오.'))
# calculate_area()
# print(result) #result는 지역변수라서 함수가 종료되면 같이 날아감.


#어설픈s... 오류는 안나지만, 값이 0으로 나옴... result는 지역변수라서 함수가 종료되면 같이 날아감. 그래서 0으로 대입된 result랑 함수 안에 있는 result랑 다르게 읽힘!
result=0 #전역 result
def calculate_area():
 result=3.14*r**2
 print('지역 result=',result) #지역 result

r=float(input('반지름을 입력하시오.')) #전역 r
calculate_area()
print(result) #전역 result==0


#완벽한 s... global 코드
result=0
def calculate_area():
 global result #전역 result를 함수 안에서도 지역변수로 사용할게!... return값이 없어도 이미 전역변수 result에 계산된 값 저장! 그래서 따로타 변수에 저장할 필요xx
 result=3.14*r**2


r=float(input('반지름을 입력하시오.')) 
calculate_area()
print(result) #global result 때문에 이미 값 0에서 값 변경됨

#디폴트 인수
def greet (name,msg):
    print('안녕',name+msg)
greet('철수','좋은아침')

def greet (name,msg):
    print('안녕',name+','+msg)
greet('철수')

def greet (name,msg='잘 지내시죠?'):
    print('안녕',name+','+msg)
greet('철수')

#회문판별
def p_text(text):
    i=0
    while(i<len(text)//2):
        if((text[i])!=(text[len(text)-i-1])):
            return False
        i=i+1
    return True

text=input('텍스트 입력')
state=p_text(text)

if(state==True):
    print('회문입니다.')
else:
    print('회문이 아닙니다.')


#팩토리얼 계산 코드
def aa(a):
    fact=1
    for i in range(1,a+1):
     fact=fact*i
    return fact

x=int(input('숫자 입력:'))   
print('합계:',aa(x))

#재귀함수 사용 ver
def fact(n):
   if(n<=1):
      return 1
   return n*fact(n-1)

num=int(input('숫자 입력:'))
print('합계:',fact(num))

# 정렬 코드
num=[]

def sort(num):
    length=len(num)

    for i in range(0,length-1):
      min_idx=i
      for j in range(i+1,length):
         if (num[j]<num[min_idx]):
            min_idx=j

      temp=num[i]
      num[i]=num[min_idx]
      num[min_idx]=temp
      
for i in range(5):
    num.append(int(input('숫자 입력:')))

print('정렬 전 숫자 상태:',num)

sort(num)
print('정렬 후 숫자 상태:',num)

#키워드 인수...위치인자로 시작**해서 파이썬이 따라감
def calc(x,y):
    return x-y
print(calc(10,20))
print(calc(20,10))

def calc(x,y):
    return x-y
print(calc(x=10,y=20))
print(calc(y=10,x=20))

def calc(x,y,z):
 return x+y+z

print(calc(10,y=20,z=30))

#키워드 인수...error 뜨는 이유? 키워드로 시작**했기 떄문에... 시작 방식에 따라 error여부가 정해지는 듯.
# def calc(x,y,z):
#  return x+y+z

# print(calc(x=10,20,30))

#다빈치 게임ppp
import random

x=0 #전역변수 선언
def random_gen():
 global x  #전역변수 x도 지역변수에 쓰겠다!
 x=random.randint(1,100)
 print('x=',x) #함수가 정의만 되어있고,호출한 적이 없음.
 return x

print('랜덤숫자:',random_gen())
num=int(input('숫자를 입력하시오.'))

if(x<num):
    print('높음')
elif(x>num):
    print('낮음')
else:
    print('맞춤')


#lab02... 다항식의 함수로 계산/두 개 다 입력받을 때
def ddd(x,y):
  print((-y)**3+2*x**2*y)
x=int(input('x값 입력:'))
y=int(input('y값 입력:'))
ddd(x,y)
#다른 ver.
result=0
x=int(input('x값 입력:'))
y=int(input('y값 입력:'))
def cc(x,y):
    global result
    result=(-y)**3+(2*(x**2)*y)
cc(x,y)
print(result)
    

#lab03..천둥번개 우르르쾅.쾅.쾅.
def ttt(a):
    return a*340
   
x=int(input('측정시간(초)입력:'))
result=ttt(x)   #print('거리=',ttt(x))
print(result) 

def lightning(num):
   result=num*340
   return result
sec=int(input('시간(초) 입력:'))

print('거리=',lightning(sec))


#lab04...온도 변환/한 개만 입력 받을 때 
def aaa(f):
  c=(f-32)*5/9
  print('섭씨온도:',c)

num=int(input('화씨온도:'))
aaa(num)

#lab05... 거리 구하기// 입력받는 변수 값 뭔지 잘 보라고
def bbb(x1,x2,y1,y2):
  result=(((x2-x1)**2)+((y2-y1)**2))**(1/2)
  print('두 점 사이의 거리:',result)

x1=int(input('x1:'))
x2=int(input('x2:'))
y1=int(input('y1:'))
y2=int(input('y2:'))

bbb(x1,x2,y1,y2)

def kk(x1,x2,y1,y2):
   result=((x2-x1)**2+(y2-y1)**2)**(1/2)
   print('두 점 사이의 거리:', result)

a=int(input('x1:'))
b=int(input('x2:'))
c=int(input('y1:'))
d=int(input('y2:'))

kk(x1=a,x2=b,y1=c,y2=d)

#lab06...계산대 프로그램/파이썬 입장에서 순차적으로 적어야지==> 변수에 대한 계산식을 먼저 입력--> print문에 해당 변수만 입력하면 출력되잖아!
def www(x,y):
 print('받아야 할 금액:',x-y)
 remain_500=(x-y)//500
 print('500원 개수:',remain_500)
 remain_100=((x-y)-(remain_500*500))//100
 print('100원 개수',remain_100)
 remain_50=((x-y)-((remain_500*500)+(remain_100*100)))//50
 print('50원 개수:',remain_50)
 remain_10=((x-y)-((remain_500*500)+(remain_100*100)+(remain_50)*50))//10
 print('10원 개수:',remain_10)
  
x=int(input('투입한 돈:'))
y=int(input('물건가격:'))
www(x,y)

#이렇게도 가능
a=int(input('투입한 돈을 입력하시오.'))
b=int(input('물건 가격을 입력하시오.'))

def cal(x,y):
    return_500=(y-x)//500
    return_100=(y-(x+(500*return_500)))//100
    return_50=(y-(x+(500*return_500)+(100*return_100)))//50
    return_10=(y-(x+(500*return_500)+(100*return_100)+(50*return_50)))//10
    print('500원 동전개수:',return_500)
    print('100원 동전개수:',return_100)
    print('50원 동전개수:',return_50)
    print('10원 동전개수:',return_10)
   
cal(b,a)


