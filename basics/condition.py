#조건문
score=59
if(score>=90):
 print("합격입니다")
print("수고하셨습니다")

score=int(input("점수를 입력하시오"))
if(score>=90):
 print("합격입니다")
print("수고하셨습니다")


#
score=40
if(score>=60): 
    print("합격")
elif(score==40):
   print("너 40점...!")    
else:
    print("불합격")

print("수고하셨습니다.") 


#
language=int(input("언어를 선택하시오(한국어==1,영어==2,독어==3)"))
if(language==1):
   print("안녕")
elif(language==2):
   print("hi")
elif(language==3):
   print("bonjour")
elif(language==4):
   print("잘못입력하셨습니다.")


#if...elif...else 헷갈릴 때 이거 봐!!
score = 85

if (score >= 90):
    print("A 학점")
elif (score >= 80):
    print("B 학점")
elif (score >= 70):
    print("C 학점")
else:
    print("F 학점")


#
num=int(input("점수를 입력하시오."))
if(num%2!=1):
   print("짝수입니다.")
else:
   print("홀수입니다.")


#if 중첩
num=int(input("점수를 입력하시오."))
if(num>=0):
   if(num==0):
      print("0점 입니다.")
   else:
      print("양수입니다.")
else:
   print("음수입니다.")


#lab01... 직각 삼각형 판별
a=int(input("a를 입력하시오."))
b=int(input("b를 입력하시오."))
c=int(input("c를 입력하시오."))

if((a**2)+(b**2)==(c**2)):
   print("직각삼각형입니다.")
else:
   print("직각삼각형이 아닙니다.")


#lab02. 등급 판별
score=int(input('점수 입력하세요'))
if(90<=score and score <=100):
    print('A등급 입니다.')
elif(80<=score and score<90):
    print('B등급 입니다.')
elif(70<=score and score<80):
    print('C등급 입니다.')
elif(60<=score and score<70):
    print('D등급 입니다.')
else:
    print('F등급 입니다.')
print('수고하셨습니다.')