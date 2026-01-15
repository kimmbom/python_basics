heroes=["아이언맨","토르","스칼렛","헐크","스파이더맨"] #출력이 대괄호도 같이 된다는 점 기억
print(heroes)
print(heroes[4])


cart=[]
cart.append("사과")#리스트이름.append("추가하고픈 텍스트")
print(cart)

cart=[]
cart.append("사과")
cart.append("수건")#계속 추가하면 돼.. 항상 마지막에 추가됨
print(cart)

#letters라는 항목에 있는 abcde/abcde들이 copy라는 곳에 들어
letters=["a","b","c","d","e"]
copy=letters[:]
print(copy)

#자리 바꾸는 마법/아직 존재하지 않는 인덱스 번호에 넣거나 변경하면 error
cart=["사과","세차","치약"]
cart[1]="파인애플"
print(cart)


#insert코드...특정위치에 항목을 추가/추가 이후로는 인덱스 번호가 뒤로 밀림
cart=["사과","세차","치약"]
cart.insert(1,"건전지")
print(cart)

#append=추가하는 코드 vs 변경하는 마법vs insert코드

#리스트삭제:remove.. 개수는 추가하면 계속 빠질 수 있음.
cart=["사과","세차","치약"]
cart.remove("사과")
print(cart)

cart=["사과","세차","치약"]
cart.remove("사과")
cart.remove("세차")
print(cart)

cart=["사과","세차","치약"] #if문 사용해서도 삭제 가능/cart에 없는 항목을 넣으면... 들여쓰기 말고 cart란 다 출력됨
if"세차"in cart:
    cart.remove("사과")
print(cart)


#del을 이용한 삭제/인덱스 번호 존재 안하면 error
cart=["사과","세차","치약"]
del cart[2]
print(cart)

#맨 마지막에 있는 항목 빼기+빠진 항목이 item에 들어가있고/ 출력하면 따로 출력됨:pop코드
cart=["사과","세차","치약"]
item=cart.pop()
print(cart)
print(item)

#항목 여러개 일 때 이름으로 index번호 역으로 알기
cart=["사과","세차","치약"]
print(cart.index("세차"))

cart=["사과","세차","치약"]
if"세차"in cart:
    print(cart.index("세차"))

#sorting... 정렬/ 오름차순으로 정렬 ex...ㄱㄴㄷㄹ
heroes=["아이언맨","토르","스칼렛","헐크","스파이더맨"]
heroes.sort()
print(heroes)

#reverse=True:역순 정렬...내림차순으로 정렬
heroes=["아이언맨","토르","스칼렛","헐크","스파이더맨"]
heroes.sort(reverse=True)
print(heroes)





#oct.13.2025
#sorted vs sort...헷갈리지 말기/ 숫자. 알파벳, 한글 우선순위 체크
heroes=["아이언맨","토르","헐크","스파이더맨","a","z","1","8",
"1.1","2.6"] 
new_heroes=sorted(heroes)
print(heroes)
print(new_heroes)

#2차원 리스트... 대괄호 속에 또 대괄호// 그림으로 코드 작성 or 코드 보고 그림 작성할 수 있어야 함 
num=[[10,20,30],[40,50,60]]
print(num)

 #... 특정숫자만 출력 하는 방법/[행][열]
num=[[10,20,30],[40,50,60]]
print(num[1][1]) #50
print(num[1][0]) #40
print(num[1][2]) #60

 #...업그레이드ver
num=[[10,20,30],[40,50,60],[70,80,90]]
print(num[2][1]) #80


#강의 녹음 다시 들으면서 정리하기==> i did~!
heroes=[]
for i in range(5):
    name=input("영웅들의 이름을 입력하시오.")
    heroes.append(name)

for i in heroes:
    print(i,end="")

#2로 나눈 나머지가 1이다==홀수만 출력하시오
num=[100,96,209,22,30,117]
for i in num:
    if i%2==1:
        print(i,end="")

#01문제...중간값찾기
num_list=[]#...sol1
for i in range(3):
    num=int(input("숫자 3개를 입력하시오."))
    num_list.append(num)

num_list.sort() #오름차순 정렬

print("중간값은", num_list[1], "입니다.")

#...sol2
num_list=[]
for i in range(3):
    num=int(input("숫자 3개를 입력하시오."))
    num_list.append(num)

num_list.sort() #오름차순 정렬

print("중간값은: %s 입니다." %(num_list[1]))






















