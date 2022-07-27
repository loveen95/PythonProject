## 함수(Function)
# : 프로그램에서 사용할 기능을 미리 정의해서 구현한것(또 다른 의미의 프로그램 내의 작은 프로그램)
# python의 함수 정의(생성) 
# def 함수이름([인자List]):
#     함수 기능에 대한 정의1
#     함수 기능에 대한 정의2
#     함수 기능에 대한 정의3
#     ......
# - 함수 사용에 있어서 설명이 필요한 경우, 함수 내부터 주석을 사용하여 기술(여러줄 주석)
# - 함수를 만들때에 함수의 기능을 바로 알수 있는 이름으로 정의하길 권장함.
# - 미리 만들어 놓은 함수를 호출시에는 "함수이름([인자])"로 호출
# - 정의 생성된 함수의 반환값이 있는 경우 "return" 명령어를 사용 
# - 함수에 반환 값이 있을수도 있고, 없을수도 있다. 있는 경우 return을 사용, 없는 경우에 리턴을 사용하면 함수가 종료. 
# - 함수가 필요하다면 인자값을 전달할수 있다. 전달된 인자값은 함수 정의 시에 만든 "매게변수"에 그값이 저장된다. 이후에 함수 정의부에서
#   해당내용을 가지고 구동

# 예제1] 사용자가 입력한 값을 출력하는 함수 구현
'''
from cgitb import text

# 함수 정의부 
def pr(): 
    txt = input("입력값 :")
    print()
    print("입력한 내용은 :" ,txt)
    
# 함수 호출
pr()

# 실습 - 입력값을 받아서 사칙연산하는 프로그램 함수를 사용. 
#       그 함수의 이름은 calc()로 구현해보세요.
#       (메인에서 calc()로 호출하면 모든 동작이 기능하도록 설정)
import os
def calc():
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

calc()
'''
# 예제2] 함수의 인자값 사용 - 사용자가 입력한 값을 출력하는 함수 구현
# 사용자로부터 입력받은 값을 인자값으로 처리하는 함수
'''
# 함수 정의
def pr2(str1): 
    print("입력한 내용 :",str1)
    
# 메인
txt = input("입력 :")
print()
pr2(txt)

# 실습 - 입력값을 받아서 사칙연산하는 프로그램 함수를 사용하여 동작하게 만드세요.
# 함수명은 "calc([문자열인자값])"로 사용하세요.

import os
def calc(calc):
    if '+' in calc:
        num1,num2 = calc.split('+')
        num1 = int(num1);num2=int(num2)
        print("계산 결과는 :", num1+num2)
    elif '-' in calc:
        num1,num2 = calc.split("-")
        num1 = int(num1);num2=int(num2)
        print("계산 결과는 :", num1-num2)
    elif '*' in calc:
        num1,num2 = calc.split("*")
        num1 = int(num1);num2=int(num2)
        print("계산 결과는 :", num1*num2)     
    elif '/' in calc:
        num1,num2 = calc.split("/")
        num1 = int(num1);num2=int(num2)
        print("계산 결과는 :", num1/num2)
    else : 
        print("수식입력이 잘못됐습니다. \n 다시 입력하세요!!")
        
    print("계산기 프로그램을 종료합니다.")
while True: 
    os.system('clear')
    txt = input("계산할 수식을 입력해주세요>>>")
    calc(txt)
    sel = input("계속하시겠습니까? y/n :")
    if sel == 'n':
        break
print("프로그램을 종료합니다!!")
'''

# 예제3] 함수의 인자값 사용 - 사용자가 입력한 값을 출력하는 함수 구현
# 사용자로부터 입력받은 값을 인자값으로 처리하는 함수
# 함수에 리턴을 사용하여 반환값을 처리하는 예제

# 함수 정의
# def pr3(str1): 
#     '''연산 결과 후에 반환값을 전달하는 함수'''
#     return "입력한 문자열은 :" + str1   
    
# # 메인
# txt = input("입력 :")
# print()
# pr_out = pr3(txt)
# print(pr_out)

'''
# 실습 - 위내용을 토대로 계산결과를 반환값으로 처리하는 함수로 변환
# 함수명은 "calc([문자열인자값])"로 사용하세요.
import os
def calc(calc):
    if '+' in calc:
        num1,num2 = calc.split('+')
        num1 = int(num1);num2=int(num2)  
        return num1+num2
    elif '-' in calc:
        num1,num2 = calc.split("-")
        num1 = int(num1);num2=int(num2)
        return num1-num2
    elif '*' in calc:
        num1,num2 = calc.split("*")
        num1 = int(num1);num2=int(num2)
        return num1*num2  
    elif '/' in calc:
        num1,num2 = calc.split("/")
        num1 = int(num1);num2=int(num2)
        return num1/num2
    else : 
        return 0
        
while True: 
    os.system('clear')
    txt = input("계산할 수식을 입력해주세요>>>")
    result = calc(txt)
    print(type(result))
    if result:
        print("계산결과는 :",result)
    else :
        print("입력이 잘못됐습니다\n 다시입력해주세여!!")
    sel = input("계속하시겠습니까? y/n :")
    if sel == 'n':
        break
print("프로그램을 종료합니다!!")
'''

# 두수에 대한 한번의 계산식을 입력받아서 결괄 출력하는 코드를 이용
# 다음과 같이 해보세요
# - 사용자가 계산을 입력. 이것을 이용해서 처리
# - calc()가 인자값으로 두 정수와 계산식(기초:+,-,*,/)를 인자로 받아 처리하는 함수를 만들어 동작시키세요
'''
import os
def calc(num1,num2,giho):
    if '+' in giho:
        return num1+num2
    elif '-' in giho:
        return num1-num2
    elif '*' in giho:
        return num1*num2
    elif '/' in giho:
        return num1/num2
    else : 
        return 0
# 메인        
while True: 
    os.system('clear')
    txt = input("계산할 수식을 입력해주세요>>>")
    if '+' in txt:
        su1,su2 = txt.split('+')
        su1 = int(su1);su2 = int(su2)
        giho = '+'
    elif '-' in txt:
        su1,su2 = txt.split('-')
        su1 = int(su1);su2 = int(su2)
        giho = '-' 
    elif '*' in txt:
        su1,su2 = txt.split('*')
        su1 = int(su1);su2 = int(su2)
        giho = '*'
    elif '/' in txt:
        su1,su2 = txt.split('/')
        su1 = int(su1);su2 = int(su2)
        giho = '/'
    else : 
        print("입력이 잘못됐습니다\n 다시입력해주세여!!")
        os.system('pause')
        continue
    result = calc(su1,su2,giho)
    if result != 0: # 수식이 잘못된 경우
        if type(result) is not float: 
            print("계산결과는 :",result)
        else : 
            print("계산결과 : {:2f}".format(result))
    sel = input("계속하시겠습니까? y/n :")
    if sel == 'n':
        break
print("프로그램을 종료합니다!!")
'''
## 함수 인자 기본값(default)설정
# default란 ?입력 인자값이 없는 경우에 기본적으로 적용되어지는 값을 의미함
# 형식)
# def 함수이름(param1,param2=1):
#     함수정의문1
#     함수정의문2
# 이렇게 정의된 함수가 있는 경우 param2는 기본값으로 '1'을 가지고 있는 것이다.
# 즉, 인자값으로 param으로 전달되지 않아도 기본값으로 '1'을 가진다.

# 예제4] 함수 인자의 기본값 설정(인자1) 
from audioop import reverse


def pr4(par1=10):
    print(par1)
# 메인
pr4(10)
pr4(20)
pr4(3)
pr4()  

# 인자를 2개 가진 경우(모두 default인 경우)
def pr5(par1=1,par2=20):
    print(par1,par2)

# 메인
pr5(100,200)
pr5(100)
pr5(200)
pr5(par2=200)
pr5()
print()
# 인자가 두개 이상인 경우, 기본값이 1개인 경우
def pr6(par1,par2=20):
    print(par1,par2)
    
pr6(100,200)
pr6(100)
pr6(200)
# pr6()     # TypeError: 인자는 반드시 전달되어야 한다.

# 인자의 기본 값이 맨 앞에 있는 경우
# def pr7(par1=10,par2): # SyntaxError : 기본값 뒤에는 일반 인자가 존재 X ,디폴드 값은 뒤로 빼야한다.
#     print(par1,par2)

# [Quiz]
# 1. 짝, 홀수를 구분하는 함수를 작성

'''
def hj(num):
    if num % 2 == 0:
       return '짝수'
    else :
        return '홀수'    
su = int(input("1.정수입력: "))
result = hj(su)
print(result)

# 2. '3'의 배수를 판별하는 함수를 작성
def multi(num):
    if not num % 3:
        return True
    else : 
        return False
su2 = int(input("2.정수입력: "))
if multi(su2):
    print("3의 배수입니다.")
else : 
    print("3의 배수가 아닙니다.")
        
   

# 3. 계산기를 입력, 출력, 연산기능으로 나눠서 실행되게 작성해주세요.
# 입력 => 계산처리 => 출력
def calc(num1,num2,giho):
    if giho == '+':
        return num1+num2
    elif giho == '-':
        return num1-num2
    elif giho == '*':
        return num1*num2
    elif giho == '/':
        return num1/num2
def output(num1,num2,giho,result):   
    print(num1,giho,num2,"=",result)
def input():
    num1,giho,num2 = int(input("첫번째 정수 입력:")),input("계산기호입력(+,-,*,/) :"),int(input("두번째 정수 입력:"))

    result = calc(num1,num2,giho)
    output(num1,num2,giho,result)
    
input()
'''
# 4. 거꾸로 수를 반환하는 함수를 계산, 출력 기능으로 나눠서 작성해주세요.
#    예) 123 => 321
'''
def re(result): 
    tmp,su =0,0
    while True :
        tmp = result % 10
        result = result // 10
        su = (su+tmp)* 10
        if not result:
            return su // 10
def dis():
    result,su = 0,0
    result =int(input("정수 입력: "))
    su = re(result)
    print("변환전값: {}, 변환후값: {}".format(result,su))
        
dis() 
'''
# 5. 예제] 친구이름 관리를 함수로 기능을 나눠서 작성하세여.
# 1. 친구목록 보기, 2. 친구추가, 3. 친구삭제, 4. 친구수정, 0. 종료
'''  
def look(lt): #친구 목록 보기
    print("="*15,"친구목록보기","="*15)
    if lt != []:
        for i in range(len(lt)): 
            print(f"{i} : {lt[i]}")
    else : 
        print("등록된 친구가 없습니다.")
def add(lt):
    name = input("추가할 이름을 입력하세요>>")
    lt.append(name)
def dl(lt): #친구 목록 삭제
    name = input("삭제할 이름을 입력하세요 :")
    if name in lt:
        lt.remove(name)
    else: 
        print("삭제할 친구가 없습니다.")   
def up(lt): # 친구 목록 수정
    name = input("수정할 이름을 입력하세요.")
    if name in lt:
        idx = lt.index(name)
    else :
        print("수정할 친구가 없습니다.")
        return
    name2 = input("변경 이름을 입력하세요.")
    lt[idx] = name2
# 메인 
import os
while True:
    os.system("clear")
    print("="*15,"친구관리 프로그램","="*15)
    print("1.친구목록보기\n2.친구추가\n3.친구삭제\n4.친구수정\n0.종료")
    sel = input("번호를 선택하세요")
    if sel =='1':
        look(lt)
        os.system('pause')
    elif sel == '2':
        add(lt)
        os.system('pause')
    elif sel == '3':
        dl(lt)
        os.system('pause')
    elif sel == '4':
        up(lt)
        os.system('pause')
    elif sel == '0':
        print("종료되었습니다.")
        break
    else:
        print("입력하신 숫자가 없습니다.")
        os.system('pause')
 '''     
# 문제) 알바 시급 프로그램 작성(default인자값 사용)
# 시급 : 8500원, 하루 8시간, 한달 30일(기본값)
# 다음과 같이 출력되게 만드세요
# (출력 결과)
# <<시급 계산 프로그램>>
# 1. 기본급
# 2. 일한 날짜 입력
# 번호 입력 >>
'''
def alba(month=30):
    time = 8; price= 8500
    re = time * price * month
    return re
def dis():
    num = input("<<시급 계산 프로그램>>\n1.기본급\n2.일한 날짜입력\n번호입력>> ")
    if num == '1': 
        result = alba()
    elif num == '2':
        month = int(input("일한 일수 입력 :"))
        result = alba(month)
    print("당신의 급여는 {:,}원 입니다.".format(result))
    
 
dis() 
'''
# 인자값 처리 방식 1 => 연속된 자료를 처리하는 함수의 인자 처리 방식
def pr8(a,b,c):
    print(a,b,c)
# 메인   
pr8(10,20,30)  

# '*'를 이용하여 리스트 또는 튜플같은 자료를 연속된 인자의 값으로 처리
# 리스트 또는 튜플의 변수값을 받아서 "unpacking" 하는 방식으로 인자를 전달
x = [100,200,300]
y = [10,20]
z = 1,2,3,4 
pr8(*x)     #100 200 300   
pr8(*y,30)
# pr8(*z) # TypeError : 인자의 개수와 전달되는 개수는 같아야 한다.             

# 인자값 처리 방식 2 => 가변 인자값 처리...
# - 고정인자 => 인자값을 반드시 정해진 값으로 1:1로 인자를 전해야하는 인자(일반)
# - 가변인자 => 인자값을 정해진 개수로 전달하지 않고, 가변적으로 전달 가능한 인자
# 가변인자 설정은 함수 정의시에 매게변수(인자)앞에 "*"를 사용한다.

#전달된 인자 값들의 합을 구하는 예제
def sum_func(*par):
    result = 0
    print(par,type(par))
    for su in par:
        result += su
    return result

def dis(): 
    sum = 0
    sum = sum_func()
    print(sum)
    sum = sum_func(10,20,30)
    print("인자가 세개(10,20,30)인 경우 결과 :",sum)
    sum = sum_func(10,20,30,40,50)
    print("인자가 다섯개(10,20,30,40,50)인 경우 결과 :",sum)
# 메인
dis()

# 주의) 인자값 처리함에 있어서 고정인자와 가변인자를 동시에 사용하는 경우, 고정인자를 먼저 처리하고 가변인자는 마지막에 사용해야함
# "**"를 사용하는 경우 딕셔너리에 대한 packing을 시도한다는 뜻
def dic_func(**par):
    print(par,type(par))
    for k in par:
        print("{}:{}".format(k,par[k]))
# 메인
dic_func(피카츄='1마리',파이리='두마리',꼬부기='없음',라이칸=1)

dic = {
    'sep' : '-',       # print('test','test',sep='-',end='\n\ntest') 와 같다.
    'end' : '\n\ntest\n',    
}
lst = ['test1','test2']
print('test','test',**dic)
print(*lst,**dic) 



