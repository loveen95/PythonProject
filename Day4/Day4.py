'''
for x in '*':
    for y in range(1,6):
        print(x*y)  # 1*1,1*2,1*3,1*4,1*5         
print()
for x in range(5,0,-1):    # 5 4 3 2 1 
    for y in '*':
        print(x*y)    #5*1 4*1 3*1 2*1 1*1
print()
for x in '*':
    for y in range(1,6):      #1,2,3,4,5
        print("{:>10}".format(x*y))  # 오른쪽 정렬 
print()
for x in range(5,0,-1):
    for y in '*':
        print("{:>10}".format(x*y))
print()
'''

# 1.
for i in range(5): # 0,1,2,3,4 
    for y in range(i+1): 
        print("*",end="") 
    print() #줄바꿈
print()
# 2.
for i in range(5): # 0,1,2,3,4
    for y in range(5-i):
        print("*",end="") 
    print() #줄바꿈
print()
# 3.
for i in range(5): # 0,1,2,3,4
    for j in range(4-i): #공백을 처리하는 반복문
        print(" ",end="")
    for y in range(i+1):
        print("*",end="") 
    print() #줄바꿈
print()
# 4.
import os # os모듈은 파이썬에서 제공하는 기본 라이브러리 모듈로 os와 관련된 함수들이 저장된 모듈
          # system()=> os의 시스템 명령어를 사용 할 수 있게함.
import time # 시간과 관련된 파이썬에서 제공하는 기본 라이브러리 모듈
# 5.
i, j = 0, 0; num =1 
while num: #True와 같다.
    os.system('clear') # 맥은 'clear'  window는 'cls'
    ln = int(input("홀수 줄수를 입력하세요>>"))  # 7
    sp = ln // 2      # 7 // 2 == 3 
    st = 1   
    flag = True 
    for i in range(ln): 
        for j in range(sp):print(end=' ') #빈 공간
        for j in range(st):print(end='*') #별 찍기
        print() #줄바꿈
        if i ==(ln//2): flag = False
        if flag: sp -= 1; st += 2
        else: sp += 1; st -= 2
    num = int(input("계속 하시겠습니까?(0.종료, 1.계속):")) #num 변수값의 변화가 생겼다. 
   
## 랜덤함수
# : 임의의 값(난수)을 출력하는 함수 
#   난수는 생성된 임의의 값을 의미한다.
#   랜덤함수를 사용하기 위해 모듈을 사용: random    
#   모듈 사용 방법 : import [모듈명]
#   ex) import random #랜덤 모듈 전체를 로딩
#   ex) from [모듈] import [모듈에 있는 내용(변수,클래스,메소드 등등)] #모듈내의 일부 정보를 로드
#       from random import random #랜덤 모듈 내에 random()함수를 로드
# 두방식은 기능 사용방식에 차이가 존재함
# import [모듈]인 경우, [모듈명].[사용할 값]
# from [모듈] import[모듈에 사용값]인 경우, [모듈에 사용값]을 그대로 사용 
from random import random
from re import T
print(random()) # 랜덤 모듈에 있는 random()함수
                # 0.0~ 1.0 미만의 값을 출력(float)
# 0.0 ~ 10.0 미만의 임의의 값을 출력                   
print(random()*10) 
# 0 ~ 10 미만의 값을 출력(int)  # random의 기본 반환값은 float 이다.
print(int(random()*10))
# 1 ~ 10까지의 값을 출력(int)
print(int(random()*10)+1)

# 예제1] 1~45까지의 임의 값 6 개를 출력
for x in range(6):
    print(int(random()*45)+1,end=' ')
print()
# 문제1] 1~100까지 랜덤 값을 6개 출력하는 코드를 작성
for x in range(6):
    print(int(random()*100)+1,end=' ')
print()
# 문제2] 1~100까지 랜덤 값을 반복하여 출력하되, 출력값이 50이 출력되는 순간 반복이 종료되는 코드를 작성
while True:
    su = int(random()*100)+1
    print(su,end=' ')
    if su == 50:
        break
print()
# 문제3] 1~15까지의 랜덤값을 중복 없이 3개 생성하여 출력하는 코드 작성
num1, num2, num3 = 0, 0, 0
while True:
    su = int(random()*15)+1
    if num1 != su:
        num1 =su
        break
while True:
    su = int(random()*15)+1
    if num1 != su and num2 != su:
        num2 = su 
        break
while True:
    su = int(random()*15)+1
    if num1 != su and num2 != su and num3 != su:
        num3 = su
        break
print(f"{num1} {num2} {num3}")

# random 모듈내의 있는 다른 형태의 random 함수들...
# -randint() : 임의의 값을 출력하는 int값 랜덤 함수
# 사용방법
#    randint(a,b)
#    a : 시작값, b :마지막 값 => 시작값부터 마지막값까지 랜덤
# 예제1] 1~6까지의 숫자
from random import randint
print(randint(1,6))
# 예제2]
print(randint(100,200))

# random 모듈내의 있는 다른 형태의 random 함수들...
# -randrange() : 범위 내에 있는 임의의 값을 출력
# 사용방법
#    randrange(5,10)
#    => 5~10 미만의 값을 출력 (5,6,7,8,9 중 하나)
#    randrange(5,10,2)
#    => 5~10 미만의 2씩 증가 값을 출력 (5,7,9 중 하나)
# 예제3] 1~6까지의 숫자
from random import randrange
print(randrange(10))
print(randrange(5,10))
print(randrange(5,10,2))

# random 모듈내의 있는 다른 형태의 random 함수들...
# -choice() : 이 함수의 특징은 리스트와 같은 형태의 자료 중 일부를 랜덤하게 추출하는 함수
# 사용방법
#    dice[1,2,3,4,5,6] #리스트형
#    choice(5,10,2)
# 예제4]
'''
import random
dice = [1,2,3,4,5,6]
st = 'hello world!'
x = random.choice(st)
print("dice에서 출력 된 값 :",x)
#or
from random import choice,randint,randrange
dice = [1,2,3,4,5,6]
st = 'hello world!'
x = choice(st)
print("dice에서 출력 된 값 :",x)
#문제4] 1~99까지의 랜덤 값 중에 짝수는 True 홀수면 False출력하는 프로그램
from random import random 
num = int(random()*99)+1
if num % 2 == 0:
    print(f"True{num}")       
else:
    print(f"False{num}")
'''
'''
ASCII코드
미국 표준 문자 코드로 7bite(0~127)로 하나의 문자를 표현 할수 있음
아스키 코드는 통신상 기본 문자 코드로 사용되고 있음.
(특징)
1. 프린트 가능한 문자 총95자, 나머지 33개 문자는 프린트가 불가능한 문자.
   프린트 가능한 문자의시작 0x20(32)->"공백"부터 시작, 0x7e(126)까지임
2. 숫자는 0x30(48)="0"에서부터 0x39(57)="9"까지 값을 가진 10개의 코드
3. 영문 대문자는 0x41(65)=>"A"에서부터 0x5A(90)="Z"까지
4. 영문 소문자는 0x61(97)=>"a"에서 0x7A(122)="z"까지
5. 아스키 코드는 문자이나 숫자(정수)로 표현이 가능함

숫자를 문자(ASCII)코드로 변경하는 함수 : chr()
 ()안에 코드 값을 전달하면 그 값을 문자로 출력하는 함수
'''
print(chr(65))   # A
print(chr(0x41)) # A
#문제5] 'A'~ 'Z'까지의 임의 문자 3자리를 출력하는 코드를 작성하세요.
from random import random,randint,randrange,choice
for x in range(3):
    ch = int(random()*26)+65
    print(chr(ch),end=" ")
'''
#List
리스트 자료형이란?
    -데이터 목록을 다루는 자료형
    -리스트를 정의할대는 "[]"를 사용한다.
    -리스트 안에는 어떤 종류의 자료형이든 상관없이 저장 가능

List자료형의 기본 사용(정의)

(정의)
    변수명 =[] #비어있는 리스트를 선언
    변수명 = [value1, value2, value3, value4,....]
    (value들의 타입은 상관없이 가능)
(List()를 이용한 리스트 생성)
    변수명 = list() #비어있는 리스트를 선언
    변수명 = list("Hello") #[H,e,l,l,o]
    변수명 = list(range(5)) # [0,1,2,3,4]
'''
# 예제1] 리스트 선언 및 값에 대한 처리
'''
lst = [1,2,3,4,5,6,7,8]
print(type(lst))

# 생성된 리스트에 대한 특정 값 참조 : index(인덱스)값을 이용
# indexing 방법 : 변수명[인덱스값] #주의)인덱스 값의 시작은 0부터 시작
print(lst[0])
print(lst[3])

# 인덱싱을 이용한 리스트값 변경
lst[0] = lst[5] 
print(lst)

#리스트 자료의 길이(요소[멤버]의 갯수):len()
print("lst의 길이 :",len(lst))

# 리스트의 결합1(병합)
ls2 = [9,10]
print(lst+ls2) 
ls3 = ls2+lst
print(ls3)

# 리스트의 결합2(확장)
lst = lst + ls2
print(lst)

# 리스트의 반복
print(ls2 * 3 )

# max(): 최댓값, min(): 최소값
print(max(lst)) # 10
print(min(lst)) # 2
print(sum(lst)) # 60
print(pow(2,2)) # 4

#변수를 선언, 3개의 정수를 입력받아 합을 출력
#출력결과 >> "합계" = xx <"합계"문자도 변수로 저장하여 사용>
num1 = int(input("숫자1 입력"))
num2 = int(input("숫자2 입력")) 
num3 = int(input("숫자3 입력"))
sum1 = [num1,num2,num3]
stt = '합계'
print(f"{stt}=",sum(sum1))

# 예제2] 리스트의 멤버를 변수처럼 사용
lst = [0,0,0,'합계']
lst[0] = int(input("숫자1 입력"))
lst[1] = int(input("숫자2 입력")) 
lst[2] = int(input("숫자3 입력"))
sum1 = lst[0] + lst[1] + lst[2]
print(f"{lst[3]}= {sum1}")
'''
# list인덱싱
# : 인덱스 값을 이용한 참조 
lst= [1,2,3,4,5,6,7,8]
# 양의 index : 0,1,2,3,4,5,6,7
# 음의 index : -8, -7, -6, -5, -4, -3, -2, -1

# 예제1]
print("lst[]",lst)
print("lst[-1] :",lst[-1])
print("lst[-2] :",lst[-2])
print("lst[-3] :",lst[-3])

#sclicing 방식을 이용한 시퀀스 객체(자료)접근
# : 리스트와 같은 시퀀스 자료 값들의 범위로 접근하기 위해서 사용하는 방법으로 자료의 일부를 잘라서 새롭게 생성하는 것을 의미
#(형식)
#   변수명[시작인덱스:끝인덱스]
#   변수명[시작인덱스:끝인덱스:증감값]
#예] lst = [1,2,3,4,5,6]
#   index   0 1 2 3 4 5
#    (-)   -6 -5 -4 -3 -2 -1
# lst[0:3] => [1,2,3], lst[0,3,2]= [1,3]
lst = [1,2,3,4,5,6]
print(lst[0:3])
print(lst[0:3:2])
print(lst[-6:-3])
print(lst[-1:-3:-1])

## 인덱스 생략
print(lst[:3]) # 시작값 생략
print(lst[3:]) # 끝값 생략
print(lst[:])  # 둘다 생략

# 슬라이싱 후 새로운 리스트 생성
sl = lst[3:6]
print(sl)
sl2 = lst[1:5:3]
print(sl2)
sl3 = lst[5::-1]
print(sl3) # [6,5,4,3,2,1]
sl4 = lst[-3:-1]
print(sl4) # [4,5]



'''
##### 리스트 함수들######....(외우시오!!)
- append(value) : 리스트 끝에 값을 추가(멤버 추가)
- extend(iter) : 리스트 끝에 list, tuple, dict의 값을 하나씩 추가
- insert(idx,value) : 인덱스에 있는 인덱스 위치에 특정 값을 추가하는 함수
===================리스트의 값을 추가하는 메서드==============================
- pop([idx]) : 인덱스를 지정하지 않으면, 마지막 인덱스 값을 반환후 삭제. 
               인덱스 값을 지정하면 해당 인덱스 값을 반환후 삭제 
- remove(value) : 특정 값을 찾아서 삭제하는 함수 
- clear() : 리스트의 모든 멤버를 삭제하고 , 빈 리스트로 만드는 함수
===================리스트의 모든 멤버를 삭제하고, 빈 리스트로 만드는 함수===========
- count(value) : 리스트내에 특정 값의 개수를 반환하는 함수
- index(value) : 리스트내에 특정 값의 인덱스 값을 반환하는 함수
- reverse() : 리스트의 멤버의 순서를 뒤집어서 나열하는 함수
- sort([reverse=False]) : 리스트의 값을 오름차순(False), 내림차순(True)정렬해주는 함수

'''
# append()
lst1 = [1,2,3,4,5,6,7,8]
lst1.append('a')
print(lst1)
lst1.append([9,10])
print(lst1)
print(lst1[-1]) #하나의 요소로 보기때문에 [9,10] 이 나온다.

# extend() : 리스트 뒤에 추가할 리스트, 듀플, 딕셔너리 자료를 멤버에 개별적 추가
lst1 = [1,2,3,4,5,6,7,8]
lst1.extend('abcdef')
print(lst1)  #하나씩 잘라서 

# insert(idx,value) : 인덱스 위치에 값을 추가
lst1 = [1,2,3,4,5,6,7,8]
lst1.insert(3,'a')  
print(lst1) #3에 있던 값은 사라지지 않고 밀려서 출력된다. [1, 2, 3, 'a', 4, 5, 6, 7, 8]

# pop([idx]) 
lst1 = [1,2,3,4,5]
a = lst1.pop()
print(a)
print(lst1)
b = lst1.pop(2)
print(b)
print(lst1)  

# remove()
lst1 = [1,2,3,2,3,4,2,4,5]
lst1.remove(2)
print(lst1) #첫번째 2 가 삭제됨
lst1.remove(2)
print(lst1) #두번째 2 가 삭제됨
lst1.remove(2)
print(lst1) #세번째 2 가 삭제됨

# clear()
lst1 = [1,2,3,4,5,6,7]
lst1.clear()
print(lst1)

# count() : 특정 값의 개수를 입력
lst1 = [1,2,3,2,5,6,2,8]
su = lst1.count(2)
print(lst1)
print("2의 값을 가진 멤버의 갯수 :", su)

# index(value) : 특정 값의 인덱스 값을 반환
lst1 = [1,2,3,2,5,6,2,8]
idx = lst1.index(2,4) #start와 stop설정을 안해놓으면 자동으로 처음과 끝으로 설정된다. 
print("idx의 값을 확인:",idx)

# reverse() : 리스트 멤버 순서를 반전(정렬x)
lst1 = [9,10,3,2,6,1,7,8,4,5]
print("reverse() 사용전 :" ,lst1)
lst1.reverse() 
print("reverse() 사용후 :",lst1) 

# sort() : 리스트를 정렬하는 함수
# - 오름차순(작은 -> 큰값) => reverse=False(생략:기본값)
# - 내림차순(큰 -> 작은값) => reverse=True 
lst1 = [9,10,3,2,6,1,7,8,4,5]
lst1.sort() #오름차순
print("오름차순 정렬 :", lst1)
lst1.sort(reverse=True)
print("내림차순 정렬 :", lst1)
# sort 사용시 주의사항
# 1. 숫자 형식 또는 문자 형식은 분리해서 정렬해야 한다. 
# 2. 정수와 숫자는 같은 숫자이기 때문에 정렬이 가능하다.
# 3. 정렬된 리스트를 새롭게 만들고 싶은 경우,sorted()를 사용 # sorted의 반환값은 list이다.
       # lst2 = sorted(lst1)
       # print(lst1,id(lst1),'\n',lst2,id(lst2))
       # lst3 = sorted("I am a student".split())
       # print(lst3) # ['I', 'a', 'am', 'student'] # 아스키 코드로 정렬을 하기 때문에 순서가 이렇게 나옴 
       # lst4 = sorted("I am a student".split(),key=str.lower)
       # print(lst4) #['a', 'am', 'I', 'student'] 
#**split() : 문자열을 분리하는 함수 (많이 씀!)
# : "()" 안에 아무것도 넣어주지 않으면, 공백(스페이스,탭,엔터)을 기준으로 문자열을 나눠서 사용함. 만약 split(';')을 사용하면,
# ';'를 기준으로 문자열을 나누겠다는 의미이다. 

# copy 기능
# - shallow copy : 서로 다른 변수가 같은 위치에 있는 데이터를 가르키는 경우
# - deep copy : 두개의 변수가 별도의 공간을 가리키는 경우 
# 예) shallow copy
lst1 = [1,2,3,4,5]
lst2 = lst1
print("lst1의 값 :",lst1,"lst1의 주소값 :",id(lst1)) 
print("lst2의 값 :",lst2,"lst1의 주소값 :",id(lst2))#shallow copy
lst1[1] = 'a'
print(lst1)
print(lst2)
# 예) deep copy
lst1 = [1,2,3,4,5]
lst2 = list(lst1) #list() 는 새로운 리스트 생성하는 메서드
lst1[1]='a'
print(lst1,id(lst1))
print(lst2,id(lst2)) 

# 복사 기능을 제공하는 copy 모듈을 불러서 사용
import copy 
lst1 = [1,2,3,4,5]
lst2 = copy.deepcopy(lst1) # deepcopy()
lst3 = lst1 #shallowcopy()
print(lst1,lst2)
print(id(lst1),'\t',id(lst1),'\t',id(lst3))
lst2[0]= 100
print(lst1,lst2) 

# [Quiz1]: 리스트 초기값[30,30,10] 설정후 
# 아래와 같이 출력 되도록 코드를 작성하세요. 
# 현재 리스트 :[30,20,10]
# append(40) 후의 리스트 : [30.20,10,40]
# pop() 으로 추출한 값 : 40
# pop()후의 리스트 : [30,20,10]
# sort() 후의 리스트 : [10,20,30]
# reverse() 후의 리스트 : [30,20,10]
lst1 = [30,20,10]
print("현재 리스트:",lst1)
lst1.append(40)
print("append(40) 후의 리스트:", lst1)
a = lst1.pop(3)
print("pop() 으로 추출한 값 :",a )
print("pop() 후의 리스트 :",lst1 )
lst1.sort(reverse=False)
print("sort() 후의 리스트 :",lst1)
lst1.reverse()
print("reverse() 후의 리스트 :",lst1)

# [Quiz2] :리스트 초기값[30,20,10] 설정후 아래와같이 출력 되도록 코드 작성하시오
# 현재 리스트 : [30,20,10]
# 10의 값의 위치 : 2
# insert(2,200) : [30,20,200,10]
# remove(200) : [30, 20, 10]
# extend([555,666,555]) 후의 리스트 : [30,20,10,555,666,555]
# 555 값의 개수 : 2
lst1 = [30,20,10]
print("현재 리스트:",lst1)
a = lst1.index(10)
print("10의 값의 위치 :",a)
lst1.insert(2,200)
print("insert()후의 리스트 :",lst1)
lst1.remove(200)
print("remove()후의 리스트 :",lst1)
lst1.extend([555,666,555])
print("extend([555,666,555]) 후의 리스트 :" ,lst1)
a = lst1.count(555)
print("555값의 개수 :",a)

