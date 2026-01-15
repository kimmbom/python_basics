print("hi")
x=100 #=의 뜻은 대입/ 우변의 값을 좌변에 저장한다는 뜻으로 작용
print(x)
x=3
print(x)
z=5
print(z)
name="김보민"
age="22살"
address="대한민국"

#출력해보기
print(name) #이름
print(age) #나이
print(address) #주소

food=("potato pizza")
print(food) #음식
#print문 하나만 써서 3가지 출력시키기
print("안녕하세요 저는 ",name+age,"입니다.","주소는",address,"입니다.")

#변수 값의 출력은 마지막 값으로 출력됨(100이 아니라 200출력)
x=100
x=200
print(x)

#변수를 저장해서 sum을 이용해서 출력하기
x=200
y=100
sum=x+y
print(sum)
z=1 #변수를 추가해서 sum이용해서 출력하기
sum=x+y+z
print(sum)

#낙타 포기법... 대분자나 underbar로 구분짓기
GoodMorning=10
input_output=3

x=100
y=200
sum=x+y
print(x,"와",y,"의 값의 합은",sum,"입니다.")

#문자열 입력받기
a=input("입력:")
print(a)
a=int(input("입력:"))

name=input("이름을 입력하시오.")
print(name,"씨 안녕하세요.")
print("파이썬에 오신걸 환영합니다.")

#Lab01...점수 게산
x=int(input("첫 번째 점수를 입력하시오."))
y=int(input("두 번째 점수를 입력하시오"))
sum=x+y
print("총 점수는", sum ,"입니다.")

#Lab02...원 넓이 계산
pi=3.14
r=int(input("반지름 길이 입력: "))
print("반지름이",r,"인 원의 넓이는",r*r*pi)

#Lab03...천둥번개가 발생한 곳은 어디?
x=int(input("측정시간을 입력하시오")) #숫자문 입력 하려면 int 사용해야함
print("거리는",x*340,"m")

#연산자
print(17**2) 
print(10*2**7) #연산우선순위...괄호>제곱>곱하기
print(2**2**3)

#나누기 연산자
print(17/5) #일반 나눗셈
print(17//5) #몫만 구하는 나눗셈
print(17%5) #나머지만 구하는 나눗셈

#
p=int(input("나누어지는 수를 입력하시오."))
q=int(input("나누는 수를 입력하시오."))
print(p//q)
print(p%q)

#
sec=1000
min=sec//60
remainder=sec%60
print(min,"분",remainder,"초")

#위의 문제 응용ver.
s=int(input("값을 입력하시오.")) 
min=s//60
remainder=s%60
print(min,"분",remainder,"초")

#대입 연산자
x=y=100
print(x)
print(y)

#복합 대입 연산자... 두 식의 의미가 같음.ppt 다시 보기<review>=>i did!
x=x+2
x+=2

#구별하는 연습
x=1000
print("초깃값 x",x)
x+=2
print("x+=2 계산 후의 x",x)
x-=2
print("x-=2 계산 후의 x",x)

#
x=int(input("첫 번째 수"))
y=int(input("두 번째 수"))
z=int(input("세 번째 수"))

avg=(x+y+z)/3
print("평균은",avg,"이다.")

#다항식 계산01
x=-1
y=3
print("다항식의 계산식은:",(-y)**3+2*(x**2)*y)

#다항식 계산02
x=2
y=4
z=4
print("총 다리의 수는",(x*2)+(y*4)+(z*3))

x=int(input("닭은"))
y=int(input("돼지는"))
z=int(input("소는"))
x=2*x
y=4*y
z=4*z
print("총 다리의 수는",x+y+z)

#Lab04...온도 계산
x=int(input("화씨온도를 입력하시오."))
print("섭씨온도는",(x-32)*5/9)

#Lab05...두 점 사이 거리
x1=int(input("첫 번째 값을 입력하시오."))
x2=int(input("두 번째 값을 입력하시오."))
y1=int(input("세 번째 값을 입력하시오."))
y2=int(input("네 번째 값을 입력하시오."))
print(" 두 점 사이의 거리는",((x2-x1)**2)+((y2-y1)**2)**(1/2))