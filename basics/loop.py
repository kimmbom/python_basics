#while문
i=0
while(i<10):
    print(i, "반복합니다")
    i=i+1 #i값은 1씩 더해져서 증가

#
count=1
sum=0
while(count<=100):
    sum=sum+count
    count=count+1
print("1부터 100까지의 합은", sum,"입니다.")


#간단 로그인 시스템
count=3
password=""

while(password!="pythonisfun"):
    password=input("암호를 입력하시오:")
    count=count-1
    if(count==0):
      print("계정 5분 잠금")
      break

#반복문... for 문 과 range()함수
for i in range(5):
    print(i,"환영합니다.")#0,1,2,3,4회 반복(0부터 시작함)...괄호 안에 있는 숫자의 -1한 값까지만 반복된다는 뜻
for i in range(1,11):
    print(i,"환영.")#... 1~10
for i in range(1,5,2):
    print(i,"환영합니다.") #... 1~4 반복한다는 뜻에 마지막의 숫자 2는 1~4까지의 증감의 폭

#출력을 가로로 하려면... end="" 사용
for i in range(10,6,-1):
    print(i,end="")

sum=0
y=int(input("어디부터 합 할 건지 입력하시오."))
x=int(input("어디까지 합 할 건지 입력하시오."))
for i in range(y,x):
    sum +=i
print("y부터 x까지의 합은",sum,"입니다.")


n=int(input("정수를 입력하시오."))
fact=1

for a in range(1,n+1):
    fact=fact*a

print(n,"!은",fact,"이다")
#fact값이 1인 이유... 
#a라는 변수가 1~n까지 적용

#
for i in range(5):
    for j in range(10):
        print("*",end="")
    print("")

#
for i in range(1,6):
    for j in range(1,i+1):
         print("*",end="")
    print("")
    #행을 1열로 I값으로 세워두고/ j값에 i대입
#
for i in range(1,6):
    for j in range(6,i,-1):
         print("*",end="")
    print("")


#예제
sign=True

while (sign):
    light=input("신호등 색상을 입력하시오.")
    if (light== 'blue'):
        sign=False

print("전진!")


#break문
while(True):
    light=input("신호등 색상을 입력하시오.")
    if (light== 'blue'):
       break
print('go!')


#continue 
for n in range(10):
    print(n,"n%2값",n%2) 
    if (n%2==0):    
        continue    
    print(n)

for n in range(11):
    if(n%2==1):
        continue
    print(n)