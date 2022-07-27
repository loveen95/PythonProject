# 1. 다음과 같은 메뉴와 가격을 key value로 사용하여 사전형 자료를 만들어 보세요.(변수명은 menu)
# 칼국수(6000원), 비빔밥(5500원), 돼지국밥(7000원), 돈까스(7000원), 김밥(2000원), 라면(2500원)

# 2. 위에서 만든 사전형 자료 menu 변수에서 가격이 6000원 미만에 해당 하는 메뉴와 가격을 출력하는 코드를 작성하세요 .
# 3. 사용자 입력으로 메뉴와 가격을 입력받아 메뉴 변수에 자료를 추가할수 있도록 하시오.(동일한 메뉴는 가격만 변경)
# 4. 메뉴를 자동으로 선택하여 출력하게 만들어 보세요.

# 1 
'''
import os
menu = {'칼국수':6000,'비빔밥':5500,'돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}
print(menu)
# 2 

for me in menu:
    if menu[me] < 6000:
        print (f"{me}:{menu[me]}원")
print()
# 3
add_menu = input("메뉴를 입력하세요")
add_pc = int(input("가격를 입력하세요"))
if add_menu in menu:
    menu[add_menu] = add_pc
else:
    menu.update({add_menu:add_pc})   
# 4 
sel = input("메뉴를 자동으로 출력하시겠습니까?(y/n)")
if sel == 'Y' or sel != 'n':
    for me in menu:
        print(me,menu[me],'원')
    print()
'''
# set클래스 
# 여러개의 자료를 비순서로 적재하는 가변길이 비순차 자료구조
# 변수 = {값1, 값2, 값3,.....}
#
# 특징
# - 중복허용 x
# - 순서가 없기 때문에 색인 인덱스를 사용할수가 없다. 
# - 객체에서 제공하는 함수를 이용하여 추가, 삭제 및 집합 연산 등이 가능함
# 1) 중복 불가

from email import message
from multiprocessing.reduction import DupFd
from re import A


se = {1,2,3,4,1} # 숫자인 경우에는 정렬 표시됨.
print(len(se)) 
print(se)

st = set('hello') # set() : 셋 타입을 생성하는 함수 
print(len(st))
print(st)
# 2) 요소 반복
for d in se:
    print(d, end=' ')
print()

for s in st:
    print(s, end=' ') # 문자는 임의로 들어간다.
print()

# 3) 집합 관련 함수
# - union([set타입 자료 ]) : 합집합
# - differ([set타입 자료-뺄집합]) : 차집합  
# - intersection() : 교집합
# - add() : 집합에 값(원소)을 추가하는 함수
# - discard() : 집합에 있는 원소를 제거

se2 = {2,4,6,8}
print(se.union(se2))
print(se.difference(se2))
print(se.intersection(se2))
se.add(7)
print(se)

st2 = set('world') 
print(st.union(st2))
print(st.difference(st2))
print(st.intersection(st2))
st.add('test')
print(st)

# 값의 타입은 상관하지 않는다.
lst = ['test','user','server','date'] 
print(lst)
print(set(lst))

# set 은 중복된 원소(값)를 제거 할때 많이 사용한다.(많이 사용하진 않음)
'''
# python의 문자열 # 
: 파이썬의 사용하는 문자열 처리

(특징)
1) 인덱싱을 이용한 참조가 가능함.
string = 'python string'
          0123456789...(인덱스값)
print(string[0])
print(string[7]) 
print(string[-1]) #g
  
2) 슬라이싱을 이용한 참조도 가능하다.
print(string[:6]) #python
print(string[0::2]) # pto tig

3) 문자열 반복문(for)
st = 'python string for'
print(string)
for x in st: 
    print(x,end =' ')
print() 

'''


#### 문자열 힘수!!!!!!####
'''
 - find(str) : 문자열에서 특정 문자열을 찾아서 해당 문자의 index값을 반환
 - count(str) : 문자열에서 특정 문자열을 찾아서 해당 문자열의 수를 반환
 - lower() : 문자열에서 영문 대문자를 소문자로 변경하여 반환
 - upper() : 문자열에서 영문 소문자를 대문자로 변경하여 반환
 - strip() : 문자열에서 양쪽 공백 또는 문자를 제거 반환
 - lstrip() : 문자열에서 왼쪽 공백 또는 문자를 제거하여 반환
 - rstip() : 문자열에서 오른쪽 공백 또는 문자를 제거하여 반환
 - replace(old, new) : 문자열에서 왼쪽(old)문자열을 찾아서, 오른쪽(new) 문자열로 변경
 - split() : 문자열을 특정 문자를 기준으로 분리 -> 반환값은 리스트
 
'''
'''
# fide 예제
st = 'python string'
print(st.find('string'))
# find(str, 시작인덱스, 끝인덱스)
print(st.find('t',3))
# find()가 문자열을 찾지 못한 경우의 반환값 : -1
print(st.find('t',9)) # -1

# count()
st= 'python string'
print(st.count('t'))

# count(str, 시작인덱스, 끝인덱스)
print(st.count('t',6))

# lower() 
st = 'PYTHON STRING'
print(st.lower())
print(st)
st1 = st.lower()
print(st1)

# upper()     
st = 'python string'
print(st.upper())
print(st)
st2 = st.upper
print(st2)

# strip() : 양쪽에 인자로 전달 받은 문자열을 제거, 인자값이 없는 경우, 공백 제거
st = '       python     '
print(st)
print(f"[{st}]")
st1 = st.strip() 
print(f"[{st1}]") 

# lstrip() : 
st2 = st.lstrip()
print(f"[{st2}]")

# rstrip() : 
st3 = st.rstrip()
print(f"[{st3}]")

# replace(old,new)
st = 'python string'
st1 = st.replace('string','문자열')
print(st1)

# split() : ****중요!!!!! 문자열을 str에 있는 문자를 기준으로 분리 - > 리스트로 저장(반환)
st = 'python string'
st1 = st.split() # 아무것도 안넣으면 공백을 기준으로....
print(st1)  # ['python', 'string']
# split()을 이용한 입력 문자 값 분리!!!
values = input("입력 :").split()
print(values, type(values))
'''
#예제 1 . 결합 및 연산
a = 'Hava a'
print(a)
b = ' Nice day'
c = a+b
print(c)
print(c*3)
a += ' Nice Day!!'
print(a) 

#예제 2
str1 = 'Python is Easy 괜찬? 아니야? 아님 말고 말해요!!'
print(str1)
print(str1.upper())
print(str1.lower())

# swapcase() : 영문 대소문자를 변경 대문자 -> 소문자 , 소문자 -> 대문자
print(str1.swapcase()) 
str2 = str1.lower()
# title() : 영문 단어의 시작을 대문자로 변경 
print(str2.title()) # Python Is Easy

# 문제 1. 
# 1)아래의 문장 주어진 조건에 맞게 변경
# "Never-eVer 100gIVe Up"
# "Never-Ever 100Give Up"

st = "Never-eVer 100gIVe Up"
print(st.title())
# 2)Have a nice day 문자열에서 다음 알아오기
# 'a', 'day', 'dak' 의 갯수 알아오기
st = "Have a nice day"
print(st.count('a'))
print(st.count('day'))
print(st.count('dak'))
# 문제 2. "Is is a fun python class"문자열의 길이, 문자 ''의 개수, 's'의 개수를 출력하는 코딩(함수x)
st = "Is is a fun python class"
num = 0
num1 = 0
num2 = 0
for x in st: 
    num += 1
    if x == 'a':
        num1 += 1
    elif x == 's':
        num2 += 1
print(num,num1,num2)

# 문제 3. "Have a nice day"문자열을 가지고 다음을 처리하세요.
# 1) 각각 파인드와 인덱스를 사용하여 "day"문자위치를 찾으세요.
st = "Have a nice day"
st1 = st.find('day')
print(st1)
print(st.index('day'))

# 2) 각각 파인드와 인덱스를 사용하여 "kkk" 문자의 위치를 찾으세요.
st1 = st.find('kkk')
print(st1)
# print(st.index('kkk')) # error
# 3) 파인드를 사용하여 첫번째, 두번째, 세번째, 네번째 'a'의 위치를 출력하세요.
'''
idx = st.find('a')
print(idx)
idx = st.find('a'+1)
print(idx)
idx = st.find('a'+1)
print(idx)
idx = st.find('a'+1)
print(idx) '''

# [Quiz] : 리스트 정의하여 첨자 위치 저장
# a 의 총 개수와 첨자의 위치를 출력하시오
# st = 'Have a nice day Have a nice day Have a nice day'
# a 개수 : 9
# 첨자 : [1,5,13,17,21,29,33,37,45]
st = 'Have a nice day Have a nice day Have a nice day'
num = 0
lst = []
while True:
    num = st.find('a',num)
    if num != -1:
        lst.append(num)
        num += 1
    else :
        break
print("a의 개수",st.count('a'))
print("첨자:",lst)

# strip(): 
st = "파이썬파"    
print(st)                  #파이썬파
print(st.strip("파"))       #이썬
print(st.lstrip("파"))      #이썬파
print(st.rstrip("파"))      #파이썬

# replace() 함수 사용
st = "2015-6-05"
print(st)                  
print(st.replace("2015","2022"))       
print(st[0:4])      
print(st.replace(st[0:4],'2022'))  

#split(str) : 특정 문자(str)를 기준으로 문자열을 나누는 함수 -> 리스트로 반환
st = "Never Ever Give Up" 
a = st.split()
print(st)
print(a,type(a))

st2= "하나:둘:셋"
st3 = "1,2,3"
b = st2.split(":")
c = st3.split(",")
print(b,type(b))
print(c,type(c))

st4 = "하나둘셋넷"
d = st4.split()
print(d,type(d))

# splitlines() : 개행('\n')을 기준으로 문자열을 나누는 함수 -> 리스트로 반환
st = "Never\nEver\nGive\nUp" 
print(st)
print(st.splitlines()) #['Never', 'Ever', 'Give', 'Up']

# 여러줄 문자열 처리 : '''~''',"""~"""
st = """
    Never Ever Give Up
    Never Ever Give Up
    Never Ever Give Up
    Never Ever Give Up
    Never Ever Give Up
"""
print(st)
a = st.splitlines()
print(a)

# join() : 지정한 문자열을 기준으로 문자열 데이터를 결합 - 반환값 str
st = '123'
print(st.join('%%'))  # %123% 
print('%'.join(st))   # 1%2%3 

# 아래의 리스트를 문자열로 변경해보세요. 
lst = ['I', 'am', 'a', 'student']
print(' '.join(lst)) #I am a student

lst1 = ["", "123", "456"]
print("".join(lst1)) 
print("-".join(lst1),type("-".join(lst1)))
# st = "2015-06-05"
lst = ['2015','06','05']
st = "-".join(lst)
print(st)

# 문제 1 . input() 함수로 이름과 나이를 입력 받을때 한번에 입력받아 처리하고 출력하는 코드를 작성하시오
# 예)
# 이름과 나이를 입력하세요 : 홍길동 18
# =>이름 : 홍길동 , 나이 : 18살
'''
name_age = input("이름과 나이를 입력하세요 >>").split()
num = name_age
print(f"이름:{num[0]}, 나이 : {num[1]}살")
# 문제 2. input() 함수로 입력받은 수의 더하기, 빼기, 곱하기, 나누기의 간단한 수식을 처리할수 있도록 코드를 작성하시오.
#    예) 계산식을 입력하세요 : 5 + 5
#        계산결과 : 10
import os

result = 0
while True: 
    os.system('clear')
    num = input("계산식을 입력하세요>>") 
    if '+' in num:
        num1, num2 = num.split('+')
        num1 = int(num1); num2=int(num2)
        print("계산결과 :",num1 + num2)
    elif '-' in num:
        num1, num2 = num.split('-')
        num1 = int(num1); num2=int(num2)
        print("계산결과 :",num1 - num2)     
    elif '*' in num:
        num1, num2 = num.split('*')
        num1 = int(num1); num2=int(num2)
        print("계산결과 :",num1 * num2)  
    elif '/' in num:
        num1, num2 = num.split('/')
        num1 = int(num1); num2=int(num2)
        print("계산결과 :",num1 / num2)   
    else : 
        print("수식입력이 잘못됬습니다. 계속하시겠습니까? (y/n)")
    sel = input()
    if sel == 'n':
        break 
print("계산기 프로그램을 종료합니다.")
'''

# 알고리즘 #
# 알고리즘이란, 어떤 문제를 해결하기 위한 일련의 절차를 의미함. 프로그래밍이 논리적인 절차를 의미하는 로직을 기초로 삼고 있기때문에
# 이를 통해서 문제를 해결하는 것을 말함

# 알고리즘 조건
# - 입력 : 외부에서 제공되는 자료가 있을수 있다.
# - 출력 : 적어도 한가지 이상의 결과가 나올수 있다. 
# - 명백성 : 각 명령들은 애매한 부분이 없이 간단 명령해야 한다.
# - 유한성 : 반드시 종료 조건이 있어야 한다.
# - 효과성 : 모든 명령들은 명백하고 실행 가능한 것이어야 한다.

# 최대값 / 최소값(max/min)
# : 전체 자료의 원소들 중에 큰 값과 가장 작은 값을 선별하는 기본 알고리즘

# 1. 입력 자료 생성
import random
dataset = []
for i in range(10):
    r = random.randint(1,100)
    dataset.append(r)
print(dataset)
# 2. 변수 초기화
vmax = vmin = dataset[0]
# 3. 최대/최소값 구하기
for i in dataset:
    if vmax < i:
        vmax = i
    if vmin > i:
        vmin = i       
# 결과 출력
print("max =",vmax,"min =",vmin)

# 정렬(sort)
dataset = [3,5,1,2,4]
for i in range(0, len(dataset)-1):
    for j in range(i+1,len(dataset)):
        if dataset[i] > dataset[j]:# swqp 조건
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp
    print(i,"번째",dataset)
'''
결과
0 번째 [1, 5, 3, 2, 4]
1 번째 [1, 2, 5, 3, 4]
2 번째 [1, 2, 3, 5, 4]
3 번째 [1, 2, 3, 4, 5]
'''    
'''   
## 검색(search)
# 검색 알고리즘은 순차검색과 이진검색(반으로 나눠서 범위안에 있는지 없는지 확인하는 이분법)
dataset = [5,10,18,22,35,55,75,103]

value = int(input("검색할 값 입력 :"))
low = 0 # start 위치 
high = len(dataset)-1 # end 위치
loc = 0 # 최종위치 
state = False # 상태변수

while (low <= high) :
    mid = (low+high) // 2 # 
    
    if dataset[mid] > value : # 중앙값이 큰 경우
        high = mid - 1 
    elif dataset[mid] < value : # 중앙값이 작은 경우
        low = mid + 1
    else : # 찾은 경우 
        loc = mid
        state = True
        break
if state : 
    print("찾은 위치값 :", loc,"번째")
else : 
    print("찾는 값이 없습니다.") 

''' 



#===================================================================================================#
# 숙제] 2장 4번과 3,4장의 연습문제 풀어서 다음주 월요일까지 제출 #
# kdw335552@nate.com





