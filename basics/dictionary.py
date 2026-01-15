phone_book={} #Dictionary는 중괄호임...vs 리스트는 대괄호
phone_book["홍길동"]="010-1234-5678"
phone_book["이순신"]="010-1111-2222"
phone_book["강감찬"]="010-3333-4444"
print(phone_book) 

dict={'홍길동':1234,'강감찬':5678,'세종대왕':12+1} #세종대왕 파트 집중...계산가능
print(dict)

#딕셔너리 탐색하기
phone_book={'홍길동':'010-1234-5678',
            '강감찬':'010-1235-5679',
            '홍남동':'010-1234-5600'}
print(phone_book['강감찬']) #=> 010-1235-5679


#dict 탐색하기1...현재 dict안에 어떤 key들이 있는지 알고 싶을 때 사용/key값들만 쫘르륵 출력시킴
phone_book={'홍길동':'010-1234-5678',
             '강감찬':'010-1235-5679',
            '홍남동':'010-1234-5600'}
print(phone_book.keys())


#dict 탐색하기2...dict에 사용되는 모든 value값들을 찾기
phone_book={'홍길동':'010-1234-5678',
             '강감찬':'010-1235-5679',
             '홍남동':'010-1234-5600'}
print(phone_book.values())


# 출력 정리하기
phone_book={'홍길동':'010-1234-5678',
             '강감찬':'010-1235-5679',
             '홍남동':'010-1234-5600'}
for key in sorted(phone_book.keys()): #key값들을 오름차순으로 정렬..가나다순
    print(key,phone_book[key])        # phone_book[key]== value값을 의미



#dict 수정...del,pop코드 사용해서// pop이 어떤 형식으로 삐지는지 공부하기
phone_book={'홍길동':'010-1234-5678',
             '강감찬':'010-1235-5679',
            '홍남동':'010-1234-5600'}
del phone_book['홍길동']
print(phone_book)

print(phone_book.pop('홍남동'))
print(phone_book)

# #dict 삭제... all 삭제vs...del== 특정 부분 삭제
phone_book={'홍길동':'010-1234-5678',
             '강감찬':'010-1235-5679',
             '홍남동':'010-1234-5600'}
phone_book.clear() #모든 부분 삭제
print(phone_book)


#예제
english_dict={}
english_dict['one']='하나'
english_dict['two']='둘'
english_dict['three']='셋'

word=input("단어를 입력하시오:")
print(english_dict[word])

#oct.27.2025
#편의점 알바생 체험하기
items={'커피':7,'펜':0,'종이컵':10,'우유':5,'콜라':4,'라면':11}

print('판매 전 재고',items)

sell=input('판매한 물건을 입력하시오.')

if sell in items:
    if(items[sell]==0):
     print('판매할 수 없습니다.') #순서가 중요... 판매할 수 있는지를 먼저 판단하는 if문이 앞에 있어야 함
    else:
     items[sell]-=1
  
else:
    print('판매 제품이 아닙니다.')
print('판매 후 재고',items)


#우주여행을 떠나요~
ppp={'수성':91700000,'금성':41400000,'화성':78400000,'목성':628700000}
x=input('행성이름:')
y=int(input('이동속도:'))
print('이동시간:',ppp[x]/y) #시간=거리/속도


#upgrade verr.
City={'서울':300,'대전':150,'독도':500}
Move={'도보':4,'택시':100,'비행기':800}
x=input('어디로 갈건가요?')

if x in City:
   y=input('이동수단은 무엇인가요?')
   print('총 걸리는 시간은',City[x]/Move[y])
else:
   print('위치가 해당되지 않습니다.')


#딕셔너리와 반복문 궁합
p_book={'홍':123,'강':567,'이':888}
for i in p_book.keys():
    print(i)
for i in p_book.values():
    print(i)

