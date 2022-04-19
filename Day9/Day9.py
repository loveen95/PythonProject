## Builtins 함수(내장 함수)
# help() # 함수, 객체에 대한 설명 (도움말)
# print() # 터미널 화면에 결과를 출력
# input() # 표준 입력을 받은 결과를 처리 
# sum() # 인자값 으로 여러개의 숫자를 받아서 합을 함수
# max() # 값들중에서 가장 큰 수를 반환
# min() # 인자 값들 중에서 가장 작은 수를 반환 
# pow() # 인자값들 통해서 제곱 처리하는 함수
# 내장 함수들은 도움말 -> in module builtins....(p.118)
# import ** : 모듈을 불러오는 명령어
# import builtins 
# dir(builtins) 내장 클래스, 내장 함수 목록을 보여줌
# 
# import builtins
# print(dir(builtins)) 
# 1. abs(x): x를 대상으로 절댓값을 반환하는 함수 
'''
print(abs(10))
print(abs(-10)) 

# 2. all(iterable) : 모든 요소가 True면, 트루를 반환 
lst1 = [1,3,4,7,-9,38]
lst2 = [0,1,2,3,4,5,6,7]
print(all(lst1))
print(all(lst2))

# 3. any(iterable) : 하나 이상의 요소가 True일때 True를 반환 
lst3 = [0,False,'',[]]
lst4 = [1,False,0,-15.3]
print(any(lst3))
print(any(lst4)) 

# 4. bin(number) -> 10진수 정수를 2진수로 변환, 표현식 0b
#    oct(number) -> hex(number) -> 0x

# 5. dir(x) : 객체 x에서 제공하는 변수, 내장함수, 내장 클래스 목록을 반환
print(dir(lst3))

# 6. eval(expr) : 문자열 수식을 인수로 받아서 계산 가능한 파이썬 수식으로 변환
print(eval("10 + 20"))
#print(eval(10+"10+30")) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(eval("20 + 30")+10)

# 7. ord(charactor): charactor를 아스키 코드값(문자 코드 값으로) 으로 반환  
# ' ' -> 0x20(32), 0 -> 0x30(48), A -> 0x41(65), a -> 0x61(97)
print(ord("0")) # 0x30(48) 
print(ord('a')) # 0x61
print(ord('A')) # 0x41
print(ord('가')) # 0xac00

# 8. chr(number) : number는 코드값을 
print(chr(0x30))
print(chr(0xac00))

# 9. pow(x,y) :x에 대한y의 제곱을 계산하여 반환
print(pow(2,3)) 
print(pow(10,3))
print(pow(10,-1)) #0.1
print(pow(-8,-2)) #0.015625

# 10. round(number,자릿수) : 올림값 처리 
print(round(3.14159)) # 3
print(round(3.14159,3)) # 3.142

# 11. sorted(iterable) : 반복 가능한 원소들을 오름차순 또는 내림차순으로 정렬 결과 반환
# 12. zip(iterable) : 반복 가능한 객체와 객체간의 원소들을 묶어서 튜플로 반환
zi = zip([1,3,5],[2,4,6])
print(list(zi))    

## 파이썬의 모듈 및 패키지의 사용
#  module이란? 함수, 변수, 클래스들을 모아놓은 파일
#  (모듈은 만들어 놓은 다른 파이썬 프로그램에서 불러와 사용이 가능함.)
# 모듈을 만드는 방법 : *.py확장자를 이용하여 만들수 있음 
# 모듈을 불러오는 방법 : import 명령어를 사용하여 모듈을불러와 사용함
# (표준 라이브러리를 불러와 사용할때에는 import 사용함)
# 시간과 관련있는 모듈들 ....
import datetime,time
import imp 

# datetime 모듈은 시간에 대해서 가공된 정보를 처리 
s = datetime.datetime.now()  # 현재 시간을 알아오는 함수
print(s) 
t = time.localtime()  # 현재 동작중인 지역의 시간
print(t)
print(t.tm_year) # 2022
print(t.tm_mday) # 29

start = time.time() # 1970.01.01.00시를 기점.... 
print(start) 
time.sleep(5)
end = time.time()
print(end)
'''
# 모듈을 불러와 사용하기
# (형식1)
# import 모듈명-> 모듈내에 있는 함수, 클래스, 변수들을 호출
# 사용할때에는 모듈명. 함수(변수,클래스)
from operator import indexOf
import calc #as를 사용하여 별칭으로 호출가능 예) import calc as c
a= 100
b = 200
c = 10
sum = calc.sum(a,b)
sub = calc.sub(a,b)
mul = calc.mul(a,b)
div = calc.div(a,b)
print(sum)
print(sub)
print(mul)
print(div)
calc.result = (sum+sub)-int((mul/div))
print("(a+b)+(b-a))-((b*a)/(b-a))의 결과: ",calc.result) 

# (형식2)
# from 모듈 import*

from calc import* # 테스트용으로 사용하는 경우가 많음
a = 10
b = 20
c = 30
sum_re = sum(a,b)
sub_re = sub(a,b)
mul_re = mul(a,b)
div_re = div(a,b)
result = sub_re+ sum_re + mul_re+ int(div_re)
print(sum_re)
print(sub_re)
print(mul_re)
print(div_re)
print(result)

# 패키지 생성후 사용하기
# 패키지란? 여러 동작과 관련된 모듈을 모아 놓은 것을 의미함 
# (패키지 생성 순서)
# 1. 패키지로 사용할 폴더를 생성
# 2. 패키지 폴더에 묶어서 사용할 모듈을 저장
#   (주의사항 파이썬 3.3이하 버전에서는 폴더에"__init__.py"로 명을 해야함)
# 3. 
from testpack import sub,sum,mul,div 
print(sum.sum(100,200))
print(sub.sub(100,200)) 
print(mul.mul(100,200))
print(div.div(100,200))
'''
# python 파일 입출력 사용 
# - 디스크에 파일을 읽어들이거나 
# - 디스크에 파일을 생성하여 저장하는 기능을 의미함 
# - 많은 양의 데이터를 처리(저장) 할때에 유용하게 사용됨
# ex) 홈페이지 이미지, 데이터, 음악, 파일 정보등을 저장할때......

# [과정- 순서]
# 1. open 함수를 이용하여 파일(객체)을 열기
# 2. read(읽기)또는 write(쓰기)관련 함수를 이용하여 파일에 대해서 작업 진행 및 처리하는 단계 
# 3. open으로 열린 파일내용을 close함수를 사용하여 닫는다.

# 1. open 함수 사용 
file = open("data/test_text.txt",mode='w',encoding='utf-8')
# /data/test_text_txt파일에 대한 fileIO생성.... 

# -"a" => 모드 영역
# open 함수 사용시 모드(mode='') 설정 값
# r(read-읽기) => 파일이 있는 경우, 해당 파일에 대해 읽기 동작을 실행 
#                파일이 없는 경우 , 에러를 출력(File Not Found!!)
# w(write-쓰기) => 파일이 있는 경우, 파일에 있는 내용을 삭제후 새롭게 쓰기
#                파일이 없는 경우, 파일을 생성하고, 쓰기를 진행
# a(append-추가) => 파일이 있는 경우, 마지막에 추가로 쓰기 작업을 진행
#                 파일이 없는 경우, 파일을 생성하고, 쓰기를 진행
#                => 파일이 있는 경우, 생성 에러를 발생
#                파일이 없는 경우, 파일을 생성하고, 쓰기를 진행
# *mode에 '+'를 사용하는 경우, 추가 기능이 사용됨(읽기와 쓰기 가능함)
# ** 모드에 t => text 작업, b => binary 작업
# - encoding : 문자 설정
# 2. open으로 생성된 내용을 토대로 작업이 진행
str1 = input("파일에 저장할 내용 입력 :")
i = file.write(str1)
print("file.write()의 반환 값 : ",i)
# 3. 작업한 파일의 내용을 close()로 종료
file.close()
# 파일 읽기 
# 1.open
rfile = open("data/test_text.txt","r",encoding="utf8")
# 2. 작업
readbuffer = rfile.read()
print(readbuffer)  
# 3. close
rfile.close()
'''
'''
[quiz] 파일명 : data/quiz1.txt
1. 본인의 인적사항을 파일에 저장후 출력
(이름, 나이, 주소)
- 당신의 이름: 홍길동 
- 홍길동님의 나이는: 20살
- 홍길동 님의 주소는 : 산골짜기

[출력결과]=> 파일에 저장된 결과를 출력 
홍길동
20살 
산골짜기
'''
'''
# 파일 입력
# 1.open
file = open("data/quiz1.txt", mode='a', encoding='utf8')
# 2.work
name = input("당신의 이름 :")
age = input(f"{name}의 나이는 : ")
address = input(f"{name}의 주소는 :")
file.write(name+"\n"+age+"\n"+address)
# 3.close
file.close()

# 파일 출력
rfile = open("data/quiz1.txt","r",encoding="utf8")
buff = rfile.read()
print(buff) 
rfile.close() 

# [예제2] readline() => 데이터를 일어 들일때에 '\n'을 기준으로 데이터를 읽어들이는 함수
rfile2 = open("data/quiz1.txt",'r',encoding='utf8')
while True:
    buff = rfile2.readline() 
    if buff == '': # 문자열의 마지막을 의미함.
        print("\n 더이상 값이 존재하지 않습니다.")
        rfile2.close()
        break
    print(buff,end='')
# [예제3]readlines()=> "\n"을 기준으로 데이터를 읽어들이는 함수,
# 읽어들인 문장들은 리스트에 저장하는 함수
rfile3 = open("data/quiz1.txt",'r',encoding='utf8')
buf3 = rfile3.readlines()
print(buf3,type(buf3))
rfile3.close()

# 문자열 리스트에 "\n"을 제거하여 저장하세요....
for i in range(len(buf3)):
    buf3[i] = buf3[i].strip('\n')
    print(buf3[i])
print(buf3)

# 예제5] 문자의 암호화(한글자)
readstr, content = "",""
key = 100 # 암호화 연산을 위한 값
choice = input("1.파일저장\n2.파일불러오기\n번호선택>>>")
fileName =input("파일명 입력: ")
if choice == '1' :
    content = input("단일 문자 입력 :")
    # 1.open
    sfile = open("data/"+fileName,"w", encoding="utf8")
    # 2.작업
    chNum = ord(content)
    chNum = chNum + key 
    content = chr(chNum) 
    sfile.write(content)
    # 3.close
    sfile.close
elif choice == '2': 
    rfile = open("data/"+fileName,"r",encoding='utf8')
    readstr = rfile.read()
    chNum = ord(readstr)
    chNum = chNum - key
    readstr = chr(chNum)
    print("파일에 저장된 값: ",readstr)
    rfile.close()
    '''
     
'''
[문제1]
위 예제를 이용하여 문자열을 암호화 시켜주세요.
- 현재 단일 문자만 저장이 가능
- 문자열을 암호화 하여 파일에 저장 할수 있도록 코드를 수정
- 반대로 암호회된 문자열을 복호화 하여 화면에 출력할수 있도록 코드를 수정
'''
'''
import os
readstr, savestr, printstr = '', '', ''
key = 100
while True:
    os.system('cls')
    choice = input('1.파일 저장\n2.파일 불러오기\n0.종료하기\n번호선택 : ')
    fileName = input('파일명 입력 : ')
    
    if choice == '1':
        sfile = open('data/'+fileName, 'w', encoding='utf-8')
        contents = input('문자열 입력 : ')
        for i in contents:
            chNum = ord(i)
            chNum += key
            savestr += chr(chNum)
        sfile.write(savestr)
        sfile.close()
        
    elif choice == '2':
        rfile = open('data/'+fileName, 'r', encoding='utf-8')
        readstr = rfile.read()
        for i in readstr:
            chNum = ord(i)
            chNum -= key
            printstr += chr(chNum)
        print('파일에 저장된 값 : ', printstr)
        rfile.close()
        os.system('pause')
    
    elif choice == '0':
        print('프로그램을 종료합니다.')
        break
    
    else:
        print('입력값 오류, 다시입력하세요!!!')
        os.system('pause')
        '''
'''
[문제2]
위 예제를 이용하여 문서파일에 저장할 입력내용을 암호화 시켜주세요.
- 문자열을 암호화 하여 파일에 저장할수 있도록 코드를 수정
 (문자열을 반복적으로 입력 할수 있게 만들어서 처리 후 암호화) 
- 반대로 암호회된 문자열을 복호화 하여 화면에 출력할수 있도록 코드를 수정

import os
readstr, savestr, printstr = '','','' 
key = 10 
while True:
    os.system
    choice = input("1.파일저장\n2.파일불러오기\n0.종료\n번호선택>>>")
    if choice == '1' :
        # 1.open
        fileName = input("파일명 입력: ")
        sfile = open("data/"+fileName,"a", encoding="utf8")
        while True:
            content = input("문자열 입력 :") 
            for i in content:
                chNum = ord(i)
                chNum += key 
                savestr += chr(chNum) 
            savestr += '\n'
            sel = input("문자열 입력을 계속 하겠씁니까? y/n")
            if sel == 'n':      
                sfile.write(savestr)
                sfile.close()
                break
    elif choice == '2': 
        rfile = open("data/"+fileName,"r",encoding='utf8')
        while True:
            readstr = rfile.readline()
            if readstr == '0':
                rfile.close()
                break 
            for i in readstr:
                chNum = ord(i)
                chNum -= key
                printstr += chr(chNum)
            printstr += '\n'
        print(f"파일{fileName}에 있는 내용\n{printstr}")
        os.system('pause')
    elif choice== '0' : 
        print("프로그램을 종료합니다.")
    else : 
        print("입력값 오류 다시입력하세요.")
        os.system('pause')
''' 
'''
# open()모드에 +옵션 사용하기
fileName = input("파일명입력:")
file = open(fileName,"r+",encoding="utf8")
readstr = file.read()
print(readstr,end="")
writestr = input("\n문서에 추가할 내용을 입력하세요")
file.write(writestr+"\n")
file.close()

# 모드 옵션
# t = > 텍스트(문서)=> 생략가능
# b => 바이너리(2진데이터)

# 문제] file 입출력을 이용하여 특정 파일을 복사하는 프로그램 코드를 작성
# 복사할 대상 (원본): data/data/test.jpg
# 복사할 위치(복사본) : data/test_copy.jpg

fileName = input("복사할 대상 (원본) :")
copy_name = input("복사할 파일 위치 (복사본) :")
# open
rfile = open("data/"+fileName,"r",encoding="utf8")
wfile = open("data/"+copy_name,"a",encoding="utf-8")
# work
rbuffer = rfile.read()
i = wfile.write(rbuffer)
if i !=0 or i != -1:
    print("복사가 성공했습니다. 파일크기는{:,}bytes입니다.".format(i))
else : 
    print("복사에 실패했습니다.")
'''
# 예외처리 : 프로그램에서 벌어지는 예외적 상황
# 예 ) 
# 파일을 읽고자 할때 , 그파일이 존재하지않는 경우(FileNotFound)
# 어떤 값을 0으로 나누고자 할때 (ZeroDivision)
# 배열의 인덱스 범위를 벗어났을 경우
# 사용자의 요구대로 진행이 되지 않았을 경우 
# (예외처리 형식)
# try : #예외처리 시작(검증)
#   예외처리 검증구문1
#   예외처리 검증구문2
# except (예외처리 코드 - 에러코드):
#   예외처리 검증구문1
#   예외처리 검증구문1
# finally:
#   마지막에 실행할 코드 1 
# 예1]
''' 
try:
    num1 = int(input("첫번째 정수:"))
    num2 = int(input("두번째 정수:"))
    div = num1/num2
    print("나눗셈 결과 :",div)
except ValueError:
    print("정수값 입력하세요!")
except ZeroDivisionError:
    print("숫자 0으로 나눌수 없어요!")
print("예외처리 이후 프로그램 진행...")

# 예2] try:~except~else 구문
# try : #예외처리 시작(검증)
#   예외처리 검증구문1
#   예외처리 검증구문2
# except (예외코드): # 예외발생시 동작
# ....
# else: # 예외 발생 안한 경우 실행
#   예외 발생 안한 경우 코드1
#   예외 발생 안한 경우 코드2

try : #예외처리 시작(검증)
    num = int(input("수 입력:"))
except ValueError:
    print("정수만 입력하세요!")
    # 예외발생시 동작
else: # 예외 발생 안한 경우 실행
    print("입력값 출력{}".format(num))

# 예3] 파일관련 예외처리(파일이 없는 경우)
fileName= input("파일명 입력 :")
try : #예외처리 시작(검증)
    file = open(fileName,"r",encoding="utf-8")
    buf = file.read()
    print(buf)
except FileNotFoundError:
    print("지정한 파일이나 디렉터리가 존재하지 않습니다.")
    # 예외발생시 동작
except Exception as e:
    print(e,"에러가 발생했습니다.")
else: # 예외 발생 안한 경우 실행 # finally==>항상 실행
    file.close()
    print("문제없이 잘 실행")
''' 

# 문제] 나이를 입력받는 프로그램을 만들때에 잘못된 값을 입력시 예외처리를 만들어보세요.
# - 입력값 에러 : ValueError=>소수점 이하, 문자를 입력
# - 입력값이 0보다 작은 경우, 강제로 예외작업을 해야함.
#           =>raise Exception("예외 사항")

try : #예외처리 시작(검증)
    age = int(input("나이를 입력하세요>>"))
    if age <= 0 :
        raise Exception("예외사항 발생")
except ValueError:
    print("양의 정수를 입력하세요!!!")
except Exception as e:  
    print(e,"0보다 작은 나이는 존재하지 않습니다.")    
    # 예외발생시 동작
else: # 예외 발생 안한 경우 실행
    print("입력하신 나이는 {}살입니다.".format(age))
finally: 
    print("프로그램을 종료합니다.")