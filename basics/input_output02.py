#정수.소수.실수 구분
x=100
y="100" 
z=15.5
print(type(x))
print(type(y))
print(type(z))

#100과 "100"구별... ppt 다시보고 수정 후 공부>>>i got it!
x=input("정수를 입력하시오.")
y=input("정수를 입력하시오.")
print(x+y)

#문자열을 숫자로 변환 
t=input('정수 입력')
x=int(t)

t=input('정수를 입력하시오.')
y=int(t)

print(x+y)


# 변환 upgrade ver
x=int(input('정수입력'))
y=int(input('정수입력'))

print(x+y)


#index...위치인자
a="hello"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
#print(a[5])...error

#index... 공백 응용ver. 기호 체크해서 공부하기
s="hello world"
print(s[5])

#문자열 사이에 변수 값 삽입...%s
price=10000
print(' 상품의 가격은 %s원 입니다.'%price)

#문단 나누기...\n의 기능
poom="이렇게 정다운\n너 하나 나하나는\n 어디서 무엇이 되어\n다시 만나라."
print(poom)


#\와 같은 기능을 하는 작은 따옴표 3개
poom='''안녕하세요.
집
가고 싶어요.'''
print(poom)


 #Lab01... 대화 스크립트
print('안녕하세요')
x=input('이름이 뭐예요?')
print('만나서 반갑습니다.',x,'님')
print(x,'님, 이름의길이는',len(x), '이군요.')
y=int(input('나이가 어떻게 돼요?'))
print('내년이면',str(y+1),'세가 되시는군요.')

#Lab02... 거스름돈 구하기 기본 ver
x=int(input('투입한 돈:'))
y=int(input('물건의 가격:'))
remain_money=x-y
remain_500=remain_money//500
remain_100=(remain_money-(500*remain_500))//100
print('500원 짜리 동전의 개수는',remain_500,'이다.')
print('100원 짜리 동전의 개수는',remain_100,'이다.')
#Lab03...거스름돈 구하기 upgrade ver
x=int(input('투입한 돈:'))
y=int(input('물건가격:'))
remain_money=x-y
remain_500=remain_money//500
remain_100=(remain_money-(500*remain_500))//100
remain_50=(remain_money-((500*remain_500)+100*remain_100))//50
remain_10=(remain_money-((500*remain_500)+100*remain_100+50*remain_50))//10
print('거스름돈:',remain_money)
print('500원은:',remain_500)
print('100원은:',remain_100)
print('50원은:',remain_50)
print('10원은:',remain_10)