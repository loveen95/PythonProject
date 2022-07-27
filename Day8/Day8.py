### 변수의 범위
# 변수를 특정 지역에서만 사용되는 지역변수(블럭 내 사용)와 상관없이 전 영역에서 사용되는 전역변수로 분류 변수의 scope-범위
# 특정영역(블럭)은 함수 또는 블럭(if,for,while등)등을 의미함.
# 전역변수 - global, 지역변수 - local

# 예제1] - 지역변수의 영역: 블럭에서만 동작한다
from calendar import prweek
from importlib.resources import read_text
from itertools import count
from re import A
import re
from typing import Iterable


var2 = 2 # 전역변수
def func(arg):
    var1=1
    print(var1,var2,arg)
# 메인
func(var2)
# print(var1) # 함수의 블럭내에 선언된 변수 - 함수가 종료되면서 사라짐(지역변수) 

# 예제2] 블럭에서 전역변수를 사용
var2 = 2 # 전역변수
def func(arg):
    global var2  # 전역변수 var2 호출 
    var2 = 10    # 전역변수 var2 = 10
    print(var2,arg+2)
# 메인
func(var2) 
print(var2) # 전역변수 

# 함수 또는 블럭에서 변수명으로 데이터에 접근시 우선순위 : 가까운 local -> global
# 예제3]
var2 = 2 
def func(arg):
    global var2  
    var2 = 10 
    var1 = 1   
    print(var2,arg+2)
    def func2(var2):
        var2 = 1
        print(var2,arg,var1)
    func2(var2)
# 메인
func(var2) 
print(var2) 

# 중첩함수
# 중첩함수란, 함수내부에 또 다른 함수가 내장된 형태. 내부 함수를 포함한 함수를 외부함수 표현한다.
# (형식)
# def 외부함수(인수):
#       함수 정의문1
#       def 내부함수(인수):
#           함수정의문(내부1)
#           return 값
#       return 내부함수
# 파이썬의 중첩함수는 외부함수나 내부함수를 변수에 저장할수 있다. 
# 이런 특성을 가진 함수를 일급함수(First class Function)라고 한다.
# 특히 내부함수는 외부함수의 return명령문을 입력하여 반환하는 형태의 함수를 클러저(Function clour)라고 한다. 
# 특징은 외부함수가 종료되어도 내부 함수에서 선언된 변수가 메모리에서 소멸되지 않는 상태로 내부함수를 사용할 수 있다. 
def a(): # 외부
    var1 = 1
    print('a 함수')
    def b(): # 내부
        print('b 함수')
        print(var1)
    return b
b = a() # 외부 함수 호출 : a함수 
b()     # 내부 함수 호출 : b함수

###
# outer
data = list(range(1,101))
def outer_func(data):
    dataSet = data # data로 받은 값을 dataSet에다가 저장
     
    # inner
    def total():
        total_val = sum(dataSet)
        return total_val
    def avg(total_val):
        avg_val = total_val / len(dataSet)
        return avg_val 
    return total,avg #inner 반환
# 외부함수 호출
total,avg = outer_func(data)
# 내부함수 호출
total_val = total() # outer_func내에있는 함수 구동 
print('total =',total_val)
avg_val = avg(total_val) 
print('avg =',avg_val)

# 역할
# 외부함수 : 함수에서 사용할 자료를 만들고, 내부함수를 포함하는 역할
# 내부함수 : 외부함수에서 만든 자료를 연산하고 조작하는 역할을 담당.
'''
# [Quiz]
디폴트 매개변수를 이용한 요금 구하는 프로그램 만드기
기본요금은 500원 환승이 없거나 환승 1회까지는 기본 요금
1회를 초과하는 환승의 경우 환승1 회마다 요금의 2배씩 증가된다.
[ex) 환승 2회인 경우 :1000원, 환승 3화일 경우 : 2000원]
[장거리는 10000원으로 처리한다.]
1. 환승안함
2. 환승함   #(몇번 환승하는지는 질의 후 요금 계산)
3. 장거리
<<**함수화 하여 작업하세요>> ->요금 계산하는 함수, 화면에 표시하는 함수
함수 처리시 목적지에 대한 내용도 입력받아서 처리 하세요.
'''
'''
# 함수 정의 : transfer
def transfer(dest,su=1,won=500):
    for i in range(1,su):
        won *= 2
        if won >= 10000:
            won = 10000
    return "{}까지 요금 : {:,}원입니다.".format(dest,won) 

def display():
    dest = ''; su = 0 #목적지와 환승횟수에 대한 초기값
    num = input("1.환승안함\n2.환승함\n3.장거리\n번호선택>>")
    dest = input("목적지 입력 :")     
    if num == '1' :
        result = transfer(dest)
    elif num == '2' :
        su = int(input("몇번 환승하시나요? :"))
        result = transfer(dest,su)
    elif num == '3':
        result = transfer(dest,1,10000)
    else : 
        print("번호 선택이 잘못됐습니다.")
        return
    print(result)
display()
'''
'''
# match ~ case 구문 : 파이썬 3.10.0이후에 도입
# 다른 언어의 switch ~ case 구문과 같은 동작

# 예제1]
def num_check(st):
    match st:
        case 1:
            return "일"
        case 2: 
            return "이"
        case 3: 
            return "삼"
        case _:
            return "선택 범위 밖 숫자"
st1 = int(input("1~3까지의 숫자를 입력하세요 :"))
print("입력값은 :"+num_check(st1)+'입니다.')

# 예제2]
def alpha_check2(check): 
    match check:
        case 'a'|'A':
            return 'A'
        case 'b'|'B':
            return 'B'
        case 'c'|'C':
            return 'C'
        case _:
            return "A~C 이외의 알파벳"
st2 = input("a~c 중 한개를 입력하세요.")
print("입력한 알파벳은 : ",alpha_check2(st2))

## 연습 : 국가명을 입력받아 해당 국가를 폰 번호를 출력하는 함수 구현
# 01 - UnitedState, 33 - France, 34 - Spain , 81 - Japan, 82 - SouthKorea
# 코드가 없는 경우에는 '-1'을 반환값으로 하는 getPhoneCode()를 구현
# (예) getPhoneCode("SouthKorea") -> 82
# Ver1
def getPhoneCode(num):
    match num:
        case 'unitedstates'|'UnitedState':
            return '01'
        case 'france'|'France':
            return '33'
        case 'spain'|'Spain':
            return '34'
        case 'Japan'|'japan':
            return '81'
        case 'SouthKorea'|'southkorea':
            return '82'
        case _ :
            return '-1'
# Ver2        
st3 = input("국가명을 입력하세요.")
print("{}의 폰번호는 {}입니다.".format(st3,getPhoneCode(st3))) 

def getPhoneCode1(country:str) -> int:
    match country.lower():
        case 'unitedstates':
            return 1
        case 'france':
            return 33
        case 'spain':
            return 34
        case 'japan':
            return 81
        case 'southkorea':
            return 82
        case _ :
            return -1  
st4 = input("국가명을 입력하세요.")
print("{}의 폰번호는 {}입니다.".format(st4,getPhoneCode(st4)))   
'''

'''
# lambda 함수
익명 함수로 일시적으로 사용하는 함수를 의미함.
사용은 함수가 생성된 곳에서 필요한 경우, 사용한 후 버리는 함수  
(형식)
lambda 인자 리스트: 표현식
예) lam = lambda x : x**2 
print (lam(8)) ==> 출력결과 : 64  
    lam2 = lambda x,y : x+y
    print(lam2(2,5)) ==> 출력결과 : 7
람다는 어디든지 사용할수 있는 함수
'''
'''
lam = lambda x : x **2
print(lam(8))
lam2 = lambda x,y : x+y
print(lam2(2,5))

# 예1)다음과 같은 함수를 람다로 표현
# 함수
def swap(a,b):
    return b,a 
a = 100
b = 200 
print("swap전 :",a,b)
a,b = swap(a,b)
print("swap후 :",a,b)

# 람다 사용
swap = lambda x,y: [y,x]
a = swap(10,20)
print(a,type(a))

# 예2) 
lam = lambda a: a*10
lam2 = lambda a,b : a+b
noData = lambda : print("인자가 없는 람다")
print(lam(10))
print(lam2(10,20))
noData() 
'''
# 예3)
def str_len(s):
    return len(s)
string = ['bob','charles','alexander3','teddy']
# 알파벳 순서로 정렬 # 문자열의 길이를 기준
#string.sort(key=str_len)
string.sort(key=lambda s:len(s))
print(string)

## 람다가 유용하게 사용되는 3가지 대표적 함수
# filter : 특정 조건을 만족하는 요소만 남기고 필터링 
# map : 각 원소를 주어진 수식에 따라 변경하여 새로운 리스트를 반환
# reduce : 차례대로 앞 2개의 원소를 가지고 연산, 연산 결과가 또 다음 연산의 입력으로 진행됨. 따라서 마지막까지 진행되며
#          최종출력은 하나의 값만 남기게 됨.
# filter(함수,리스트)
# filter(function,iterable) -> 특정 조건에 요 소만 남기고 필터링,
#                              리스트에 있는 내용을 함수에 대입하여 결과값을 처리(True or False)
# 함수 - 짝수만 반환 하는 함수
# 함수 사용
def even(n):
    return n % 2 ==0
print(even(4)) # True 

nums = list(range(1,11))
filter_list = list(filter(even,nums))
print(filter_list) 

# lambda 사용 
filter2_list = list(filter(lambda n: n%2==0,nums))
print(filter2_list)

# map : 특정 조건에 맞는 새로운 리스트를 생성 
# 주어진 리스트,리스트의 제곱을 한 숫자 새로운 리스트 생성
# map(func,iter1) : 각 멤버를 func으로 동작 시킨후에 새롭게 리스트를 생성
nums = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda n : n**2,nums))) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# reduce : 내장함수는 아님, functools 모듈 내에 존재함.  
import functools 
a = [1,2,3,5,8]
print(functools.reduce(lambda x,y:x+y,a))
# 람다를 사용해서 두수의 +,-,*,/의 사칙연산 하는 프로그램을 작성하세요.
sum = lambda x,y : x+y
sub = lambda x,y : x-y
mul = lambda x,y : x*y
div = lambda x,y : x/y
import os 
while True: 
    os.system('clear')
    num1,giho,num2 = int(input("첫번째 정수 입력:")),input("계산기호입력(+,-,*,/) :"),int(input("두번째 정수 입력:"))
    if giho == '+':
        print(sum(num1,num2))
    elif giho == '-': 
        print(sub(num1,num2))
    elif giho == '*':
        print(mul(num1,num2))
    elif giho =='/':
        print(div(num1,num2))
    else : 
        print("수식 값을 잘못 입력했습니다.")
        os.system('pause')
    sel = input("계속하시겠습니까 ? y/n :")
    if sel == 'n':
        break
# 획득자(getter), 지정자(setter), nonlocal
# 내부 함수는 중첩 함수에서 클로저 역할도 하지만 함수 내 자료를 외부로 획득하거나 자료를 수정하는 역할도 함
# 이런 내부 함수들을 획득자(getter), 지정자(setter)라고 부르며 역할과 필요요건은 다음과 같다.
# 획득자 함수 : 함수 내부에 생성한 자료를 외부로 반환하는 함수로 반드시 return명령 갖는다.
# 지정자 함수 : 함수 내부에 생성한 자료를 외부에서 수정하는 함수로 반드시 매게변수를 갖는다.
#            만약 외부함수에서 생성된 자료를 수정할 경우 해당 변수에 nonlocal명령어를 쓴다.  
# (형식)
# def 외부함수():
#     변수명 = 값
#    def 내부함수():
#         nonlocal 변수명
# 예) 획득자와 지정자 함수 그리고 , nonlocal명령어를 이용하여 외부함수에서 생성한 자료를 내부에서 획득하고, 수정하는 예문
def main_func(num): 
    num_val = num
    def getter(): # 획득자 ...return
        return num_val
    def setter(value): # 지정자
        nonlocal num_val # nonlocal명령어
        num_val = value
    return getter,setter # 함수 클러저 반환
# 호출
getter,setter = main_func(100) # num생성

# 획득자 getter 호출
print("num =",getter()) # 획득한 num =100
# 지정자 호출
setter(300) # num값 수정
print("num =",getter()) #num값 수정확인

# 함수 장식자(decoration)는 기존함수 시작부분과 종료부분에 기능을 장식하여 추가해주는 별도의 함수를 의미함
# 즉, 현재 실행되는 함수를 파라미터로 받아서 꾸며줄 내용과 함께 해당 함수를 감싸주는 함수(Wrapping function)
# (형식)
#   @함수 장식자 => 사전에 만들어 있어야함. @wrapping 함수명
#   def 함수명():
#       함수 실행문

# wrapper 함수
def wrap(func):
    def decorated():
        print("반가워요 ~~~!!!!! ") # 시작부분에 삽입
        func() # 인수로 넘어온 함수 실행
        print("안녕 반가웠어!!!~~ 잘가^^") # 종료 부분에 삽입 
    return decorated #클로저 함수 반환
# 장식자 적용할 함수
@wrap
def hello():
    print("hi~~~")
# 함수 호출
hello() 

# 재귀함수(Recursive Function)
# 함수 내부에서 자신의 함수를 반복적으로 호출하는 함수
# 재귀함수는 반복적으로 호출하기때문에 반드시 함수내에 반복을 탈출(exit)조건이 필수이다.
# 재귀함수는 반복적으로 변수를 조금씩 변경하여 연산을 수행하는 알고리즘에서 이용됨 
# 예제로 팩토리얼(Factorial)계산 등을 사례로 들수 있다.

# 예제) count - 1~ n까지 정수를 count(카운트)하는 과정 
# 재귀함수 정의
def counter(n):
    if n == 0:
        print()
        return 0 # 종료 조건
    else : 
        print(n,end='')
        counter(n-1) # 재귀함수 호출
# 함수 호출 1
print("n=0 :",counter(0)) # n = 0, 0
# 함수 호출 2
counter(5)

# 예) 누적합
# 1~n 까지 정수를 카운트한 값을 누적하여 반환하는 경우
# 재귀함수 정의 
def add(n):
    if n == 1: # 종료 조건
        return 1
    else : 
        result = n + add(n-1) # 재귀호출
            
        print(n,end=' ') # stack 영역 : 만약 n=5(시작) => 2,3,4,5
        return result
# 함수 호출
print("n = 1 :",add(1))
print("\nn = 5 :",add(5))    

