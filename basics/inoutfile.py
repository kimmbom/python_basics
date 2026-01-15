#예외
try:
    age=int(input('나이를 입력하시오.'))
except:
    print('입력이 정확하지 않습니다.')
else:
   if(age<=18):
     print('미성년자는 출입금지입니다.')
   else:
     print('환영')


try:
   infile=open("D:\\python\\hangman.txt","r")
   lines=infile.read()
   print(lines)
except FileNotFoundError:
   print('오류발생')
finally: #무조건 실행:중간에 오류발생해도 실행됨
   print('무조건 실행')
#infile.close()


try:
   num1=int(input('첫 번째 숫자 입력:'))
   num2=int(input('두 번째 숫자 입력:'))
   result=num1/num2
except ValueError:
   print('다시 입력')
except ZeroDivisionError:
   print('0으로 잘못나누셨습니다.')
except Exception as e:
   print('알 수 없는 오류 발생')
else:
   print('나눗셈 결과:',result)
finally:
   print('프로그램 종료')

#mc/dc 처리
#            a.b.c          result2
# test case1 t t t          t
# test case2 t t f          t
# test case3 t f t          t
# test case4 t f f          f
# test case5 f t t          t
# test case6 f t f          f
# test case7 f f t          t
# test case9 f f f          f

# a(2.6)
# b(2.4)
# c(3.4)(5.6)(7.8)
# mc/dc...2.4.6.7.8
# mc/dc...2.4.5.6
# mc/dc...2.3.4.6


# a:score>=90
# b:score<=100
# if( a and b):
#     a b rr
# tc1 t t t
# tc2 t f f
# tc3 f t f

# a(1.3)
# b(1.2)
# mc/dc...(1.2.3)==3가지



# if(a<5) or (b>3) or (c!=5):
   
#            a.b.c          result2
# test case1 t t t          t
# test case2 t t f          t
# test case3 t f t          t
# test case4 t f f          t
# test case5 f t t          t
# test case6 f t f          t
# test case7 f f t          t
# test case8 f f f          f

# a(4.8)
# b(6.8)
# c(7.8)

# mc/dc(4867)



#담백한 정석 in
infile= open('C:\\Users\\min_m\\OneDrive\\Desktop\\phones.txt','r',encoding='utf8')
lines=infile.read()
print(lines)
infile.close()



#r...한 줄씩 in
infile= open('C:\\Users\\min_m\\OneDrive\\Desktop\\phones.txt','r',encoding='utf8')
lines=infile.readline()
print(lines)

lines=infile.readline()
print(lines)

infile.close()



#r... 반복문써서 in
infile= open('C:\\Users\\min_m\\OneDrive\\Desktop\\phones.txt','r',encoding='utf8')

for line in infile:                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    line=line.rstrip()
    print(line)

infile.close()


#a... 추가 out
outfile= open('C:\\Users\\min_m\\OneDrive\\Desktop\\phones.txt','a',encoding='utf8')

outfile.write('정성찬 010.123\n')
outfile.write('난난살 010.153\n')
outfile.write('나나나 070.123\n')

outfile.close()


#w... 새로 바꾸기 out
outfile= open('C:\\Users\\min_m\\OneDrive\\Desktop\\phones.txt','w',encoding='utf8')

outfile.write('정성찬 010.123\n')
outfile.write('난넉살 010.153\n')
outfile.write('강희건 070.123\n')

outfile.close()
 
#split 코드
a="we're not a commercial for everyone else."
print(a.split())

#split 응용 ver.
a="we're not a commercial for everyone else."
print(a.split())
b=[]
b=a.split()
print(b[0])
print(b[1])
print(b[2])
print(b[3])

#csv 파일 불러오기
import csv
f=open("C:\\Users\\min_m\\OneDrive\\input.csv",'r')
data=csv.reader(f)

for line in data:
   print(line)

f.close()

#해커 빙의
infilename=input('입력 파일 이름:')
outfilename=input('출력 파일 이름:')

infile=open(infilename,"r",encoding='utf8')
outfile=open(outfilename,"w")

s=infile.read()

outfile.write(s)

infile.close()
outfile.close()

#lab02
infilename=input('입력파일이름:')
outfilename=input('출력파일이름:')

infile=open(infilename,'r',encoding='utf8')
outfile=open(outfilename,'w')


for i in range(10):
    if (i%2==0):
        s=infile.readline()
        outfile.write(s)
    else:
        s=infile.readline()


infile.close()
outfile.close() 

# | 함수              | 읽는 단위      | 예시 결과                     |
# | --------------- | ---------- | ------------------------- |
# | **read()**      | 전체         | `"Hello\nPython\n"`       |
# | **readline()**  | 한 줄        | `"Hello\n"`               |
# | **readlines()** | 모든 줄 → 리스트 | `["Hello\n", "Python\n"]` |
