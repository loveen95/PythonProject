# 2차(원)리스트
# : 리스트 안에 멤버 중에 리스트가 존재하는 경우 사용되는 방식
# 리스트 안에 있는 리스트 멤버에 대한 참조 방식

# 예1] 2차 리스트 변수 값 참조
aa = [[1,2,3,4], # aa[0]
     [5,6,7,8], # aa[1]
     [9,10,11,12]] # aa[2]
print(len(aa)) # 3개
print(aa) # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for x in range(len(aa)): ##aa 리스트의 멤버수 : 3
    for y in range(len(aa[x])): #aa 멤버 리스트의 멤버의 갯수 : 4
        print(aa[x][y],end='\t')
    print()

#예제 2] 2차 리스트 생성 및 출력
ls_1 = []; ls_2 = []; value = 1
#2차 리스트 생성
for x in range(3): #상위 리스트 멤버 갯수
    for y in range(4) : # 하위 리스트 멤버의 갯수 : 4 
        ls_1.append(value)
        value += 1
        #lst, ls_1 = [1,2,3,4]
        #2nd, ls_1 = [5,6,7,8]
        #3rd, ls_1 = [9,10,11,12]
    ls_2.append(ls_1) #lst, [[1,2,3,4]] 
                      #2nd,[[1,2,3,4],[5,6,7,8]] 
                      #3rd,[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    ls_1 = []
print(ls_2)
#출력(읽기) 
for x in range(len(ls_2)): 
    for y in range(len(ls_2[x])): 
        print(ls_2[x][y],end='\t')
    print()

# 문제 1] numbers =[10,20,30,40,50,60,70]
# 위 리스트의 모든 값을 더한 결과를 출력하세요.

# numbers = [10,20,30,40,50,60,70]
# sum = 0
# for x in range(numbers):
#     sum += x
# print(sum)

# 문제2] 1~45 까지의 임의의 중복 없이 6 개 생성하여 출력
from random import random,randint,randrange
from tkinter import W
lotto =[]
cnt = 0
while True :
    su = int(random()*45)+1
    if su not in lotto:  # su not in lotto 로또에 포함되지 않는다면 True
        lotto.append(su)
        cnt += 1
        if cnt == 6 :
           break
lotto.sort()
print(lotto)

# 문제3] lst_sec= [['홍길동''남',36], ['김수양', '여', 32],['박담수', '남', 28]]
# 위 2차 리스트 자료를 다음과 같은 형식으로 출력
# 이름 : 홍길동
# 성별 : 남
# 나이 : 36
lst_sec = [['홍길동','남',36], ['김수양', '여', 32],['박담수', '남', 28]]

for x in range(len(lst_sec)):
    for y in range(1):
        print(f"이름: {lst_sec[x][y]}")
        y += 1
        print(f"성별: {lst_sec[x][y]}")
        y += 1
        print(f"나이: {lst_sec[x][y]}")
        y += 1
    print() 
print()
# 문제 4]
gugu = []
for x in range(2,10): #2,3,4,5,6,7,8,9
    gugu.append([]) 
    for y in range(1,10):
        gugu[x-2].append(x*y)
print(gugu)
for x in range(2,10):
    for y in range(1,10):
        print("{}x{}={:<3}".format(x,y,gugu[x-2][y-1]),end='')
    print()
    
#===============================================================
### list 내포(List comprehension): 리스트 안에서 for 와 if 를 사용하는 문법
#
# 형식1 (for)
# 변수 = [실행문 for 변수 in 열거형 객체]
# for문의 실행 결과가 변수 리스트에 append 처리가 되어 진다.
x = [2,4,1,5,7] ##멤버를 **2로 처리하고 싶다면....
lst = []
for i in x:
    i **=  2 
    lst.append(i)
print(lst)

# 형식 1
lst1 = [i**2 for i in x] # x열거형 자료(list) 의 멤버들을 i**2한 처리결과로 append한다.   
print(lst1) 

# 형식 2(for와 if문을 같이 사용하는 경우 )
# 변수 = [실행문 for 변수 in 열거형 객체 if 조건문]
lst1 = [i**2 for i in x if i % 2 == 0]
print(lst1)
# 예제] 1~10 -> 2의 배수 추출 -> i*2 -> list 에 저장
num = list(range(1,11)) # num리스트[1,2,3,4,5,6,7,8,9,10]
lst2 = [i*2 for i in num if i % 2 == 0]
print(lst2) 
#===========================================================================================
#문제]
'''
print("1.친구리스트 출력\n 2.친구 추가 \n 3.친구 삭제 \n 4.이름 변경\n 0.종료")
choice = int(input("메뉴를 선택하세요 :"))
name = ['홍길동','이윤빈','민병학','주세인','김상래']
idx = [] 
for x in range(1):
    if choice == 1:
        print(name)
    elif choice == 2:
        name1 = input("이름을 입력하시오 : ")
        name.append(name1)
        
    elif choice ==3:
        name1 = input("이름을 입력하시오 : ")
        if name1 in name:
            name.remove()
        else : 
            print("삭제할 친구가 없습니다.")
    elif choice == 4:
        name2 = input("이름을 입력하세요:")
        if name2 in name:
            idx = name.index(name2)
        else : 
            print("수정할 친구가 없습니다.")
            continue
        mod_name = input("변경할 이름 입력하시오:")
                
print(name)
'''
'''
# 튜플
: 리스트와 비슷한 자료형으로 튜플 안에 댜향한 형태의값을 사용할 수 있음
(형식)
튜플변수명 = (value1,value2,value3,...)
리스트와 튜플의 차이점 
1. 리스트는 "[]"를 사용하지만 튜플은 "()"를 사용한다. 
2. 리슨트는 그 값을 생성 , 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀수 없다 !!!!!!!!
3. 튜플은 멤버(요소)의 값이 1개인 경우 반드시 뒤에 ","를 붙여야한다.
    예) tu =(1,)
4. 튜플은 가장 외각에 있는 "()"는 생략이 가능함
# 튜플의 인덱싱
: 튜플도 리스트와같이 인덱싱을 통해서 값에 접근
# 튜플의 슬라이싱
: 튜플의 특정 범위의 값에 접근하기 위한 방법으로 리스트와 동일하게 사용
'''
tu = (1,2,3,4,5)
print(tu,type(tu))
print(tu[0])
# print(tu[5])  범위 벗어난 error
print(tu[4])
print(tu[-1])
print(tu[:3])
print(tu[3:])
tu1 = '문자열',100,123.456 #()생략가능
print(tu1,type(tu1))
tu2 = (10) # ","이 없으므로 int형이다.
print(type(tu2)) # <class 'int'> 
tu3 = (10,)
print(type(tu3)) # <class 'tuple'>   # 튜플의 경우 값이 하나인 경우엔 ","를 써야한다. 
tu4 = 10,
print(type(tu4)) # <class 'tuple'> #()생략 가능

# 예제2] 튜플의 특성
# tu =(1,2,3,4,5)
# tu[0] = 100 # error 튜플은 자르는건 가능하지만 값을 바꾸는건 안된다. !!!!!!!!!!
# print(tu)

# 튜플의 결합1(병합)
a = 1,2,3
b = 4,5,6
c = a + b
print(c)
# 튜플의 결합2(확장)
tu1 = 1,2,3
tu2 = 4,5,6
tu1= tu1 + tu2 
print(tu1)

tu3 = tu1[2:]
print(tu3)

# packing 과 unpacking
# : 튜플과 같은 자료형으로 묶어서 사용하는 것을 packing 
# 반대로 묶어진 튜플과 같은 자료형을 나눠서 사용하는 것을 unpacking 
# 예 ] (1,2),(3,4)
# packing => pack = ((1,2),(3,4)) 
# unpacking => a,b = pack 
pack = 10,20,30
a,b,c = 10, 20, 30 #unpacking
print(a,b,c)
lst =[100,200,300]
a,b,c = lst
print(a,b,c)
st = 'abc'
a,b,c = st
print(a,b,c)

# 튜플의 함수
# -index(value)
# -count(value)

# 예제 4
tu = (100,200,'함수',100,'개수')
print(tu.index(200))
print(tu.index(100))
print(tu.count(100))

'''
1.numbers = (10,20,30,40,50,60,70)
위 튜플 자료에서 30과 40을 따로 num1, num2 변수에 할당

'''
numbers = (10,20,30,40,50,60,70)
num1 = numbers[2]
num2 = numbers[3]
print(num1,num2)

'''
2. menu = (('칼국수',6000),('비빔밥',5500),('돼지국밥',7000))
칼국수 - 6,000원
비빔밥 - 6,000원
돼지국밥 - 7,000원
양식으로 출력
'''
menu = (('칼국수',6000),('비빔밥',5500),('돼지국밥',7000))
for x in range(len(menu)):
    print("{}-{}원".format(menu[x][0],menu[x][1])) 
print()   
# 풀이: 메뉴의 길이는 3, menu[x]는 0,1,2인덱스로 증가하고 튜플안에 튜플은 3가지가 있다.
#      메뉴의 [x][0] = '칼국수', [x][1] = '6000' 이다. #0번째 인덱스
#      메뉴의 [x][0] = '비빔밥', [x][1] = '5500' 이다. #1번째 인덱스
#      메뉴의 [x][0] = '돼지국밥', [x][1] = '7000' 이다.#2번째 인덱스

#[튜플 종합문제]
# 1. 여러개의 값을 패킹 시킨후 저장되어 있는 값을 빼내어 출력하시오. 
num = (1,2,3,4,5)
lst = []
for i in range(1):
    lst += num
    print(lst)
    
# 2. 아래와 같이 출력
infor = (('회사정보'),('제품명'),('가격정보'),('출시일'))
lst = ['삼성전자','갤럭시','1000원','미정']
for x in range(4):
    print(" "*5," {}  :  {}".format(infor[x],lst[x]))  
print()
# 3. 위에서 출력한 내용을 업데이트 하시오.
infor = (('회사정보'),('제품명'),('가격정보'),('출시일'))
lst = ['삼성전자','갤럭시','1000원','미정'] 
price = lst.index('1000원') #인덱스 부분을 price 에 저장한다.
runch = lst.index('미정')    #인덱스 부분을 runch 에 저장한다.
lst.remove('1000원')  #value'1000원'을 삭제한다.
lst.remove('미정')    #value'미정'을 삭제한다.
lst.insert(price,"110원") #insert(인덱스,value)를 지정하는데 인덱스의 변수가 price이므로 price 인덱스에 value'110'을 insert한다.
lst.insert(runch,"이번 달 말") 
for x in range(4):
    print(" "*5," {}  :  {}".format(infor[x],lst[x])) 

# dictionary 
# 1. 리스트와 비슷한 자료형 . List 는 요소에 대한 접근시 첨자(index)를 사용
# 2. 딕셔너리도 첨자를 사용하는데 사용하는 첨자는 "key"를 사용
# 3. 딕셔너리는 키가 가르키는 곳에 값(value-data)이 존재함
#   키 값을 사용 하는 장점 : 
#       1) 빠른 탐색 - 빠름
#       2) 편리함
# 4. 딕셔너리를 정의할때는 "{}"를 사용함
# 5. 특정 슬롯을 대해서 참조할때 key-value 를 입력하거나, 딕셔너리 안에 있는 요소를 참조할 경우에"[]"를 사용한다.
# (형식)
# 변수명 = {} 
# 변수명 = {key1:value1, key2:value2......}
# dict()를 이용해서 선언하는 경우, 
# 변수명 = dict([(k1,v2),(k2,v2),(k3,v3)])
# (접근방식)
# dic = {key:value}
# dic[key] = value1
# print(dic[key]) => value1이 나옴. 
print(dict([('a',100),(1,'test')]))
dic = {'a':100, 1:'test'}
print(dic['a']) # ['a']의 value값 : 100 이 나온다. 
print(dic[1]) # 딕셔너리의 [1]번째의 value값 : 'test'이 나온다.

dic = {'a':1,'b':2}
print(dic['a'])
dic['b'] = 5*dic['a']
print(dic['b'])

#예 2] 딕셔너리에 for문을 사용하는 경우
for k in dic: 
    print(k)
    print("키 값:{}, 키를 이용한 참조값 : {}".format(k,dic[k]))
    
#예 3] 딕셔너리와 리스트를 같이 사용하는 경우
d1 = {'음료':['탄산','우유','물','과일'],
      '식사':['김밥','라면','돈까스','비빔밥']}
for key in d1:
    print(d1[key])
    for i in d1[key]:
        print(i,end=" ")
    print()
    for j in range(4):
        print(d1[key][j],end=" ")
    print()

# 예 4] 리스트 안에 딕셔너리를 넣는 경우 
ld =  [{'name':"홍길동",'age':18},
    {'name':"이윤빈",'age':28}]
for dic in ld :
    print(dic['name'],dic['age'])
    
#예 5] 딕셔너리안에 딕셔너리를 넣는 경우 
dd = {'홍길동':{'age':18,'blood':"A"},
       '이윤빈':{'age':18,'blood':"B"}}
for name in dd :
    print(name,dd[name]['age'],dd[name]['blood'])
'''
# 딕셔너리에 사용하는 함수들
- update(dict): 사전형 자료에 값을 추가(key:value)
- fromkeys(iter[,value]): iter에 리스트, 튜플의 값을 딕셔너리의 키로 사용하는 딕셔너리를 생성하여 반환
- clear() : 사전형의 모든 "키:값"을 삭제하여 빈 사전형 자료로 만듦
- keys() : 사전형 자료에서 모든 키를 반환하는 함수
- get(key[,value]) : 사전형의 키를 사용하여 값을 얻어오는 함수
- values : 사전형 자료에서 모든 값을 반환하는 함수 
- items() : 사전형의 모든 "키:값"의 쌍으로 튜플(*)로 반환 
- pop(key) : 사전형의 자료의 키를 통해서 값을 반환한 후에 삭제
- popitem() : 사전형 자료의 마지막 "키:값"쌍을 튜플로 반환후 삭제
'''
# update()
dic ={'a':1,'b':2}
dic.update({'d':4})
print(dic['a'])
print(dic['d'])
print(dic)
# fromkeys(iter,value)
ke = ['a','b','c']
dic1= {}.fromkeys(ke)
dic2= {}.fromkeys(ke,1)
print(dic1)
print(dic2)
# get(key[,value]) *******
dic = {'a':1,'b':2,'c':3}
value = dic.get('b')
print(value)
print(dic.get('d'))
print(dic.get('d','not exist key'))
print(dic.get('c','not exist key'))


# keys()
dic = {'a':1,'b':2,'c':3}
for key in dic.keys():
    print(key,end=' ')
print(type(dic.keys()))
print(dic.keys())
print()

# values()
dic = {'a':1,'b':2,'c':3}
for values in dic.values():
    print(values,end=' ')
print()
print(dic.values())

# items()
dic = {'a':1,'b':2,'c':3}
for key, value in dic.items():
    print("{}:{}".format(key,value),end=" ")
print()

# pop(key)
dic = {'a':1,'b':2,'c':3}
value= dic.pop('b')
print(value)
print(dic)

# popitem()
dic = {'a':1,'b':2,'c':3}
tu1= dic.popitem()
print(dic)
print(tu1)

# clear()
dic = {'a':1,'b':2,'c':3}
print(dic)
dic.clear()
print(dic)

# 문제1 
# 1. 이름, 전화번호, 이메일 주소를 키로 사용하는 사전 자료를 생성하시오.
d = {'이름':"홍길동",'전화번호':'010-0000-0000','이메일':'xxxx@naver.com'}
# 문제2
import os
ld = [] 
while True: 
    dic2 = {}
    dic2.update({'이름':input("이름 입력 :")})
    dic2.update({'전화번호':input("전화번호 입력 :")})
    dic2.update({'이메일':input("이메일 입력 :")})
    ld.append(dic2)
    if (input("계속 하시겠습니까?(y/n)")=='n'):
        break
    os.system("clear")
    
# 문제3
for d in ld :
    print(f"이름 : {d['이름']}")   
    print(f"전화번호 : {d['전화번호']}")   
    print(f"이메일 : {d['이메일']}")   
    print()

