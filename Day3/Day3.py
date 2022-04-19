'''
[문제1]윤년 구하기
윤년을 구하는 코드를 작성하시오.
4의 배수는 윤년이 된다. 그 외에는 평년 
4의 배수면서 100의 배수인 경우는 평년이다. 그외에는 윤년
4그리고 100의 배수이면서 400의 배수인 경우 윤년이다. 그외에는 평년 
출력예제 : 2017년은 평년입니다.

year = int(input("년도를 입력하세요.")) 

if year % 4 == 0 :
    if year % 100 == 0 : 
        print ("{}년은 평년입니다.".format(year)) 
        if  year % 400 == 0 : 
            print("{}년은 윤년입니다.".format(year))
        else :
            print ("{}년은 평년입니다.".format(year))
    else :
        print ("{}년은 윤년입니다.".format(year))
else :
    print ("{}년은 평년입니다.".format(year))     
    '''   
'''
[문제2]
-이름, 학번, 3과목의 성적을 입력받아 합계와 평균을 구하고, 
평균이 90이상이면 'A', 80이상'B', 70이상'C', 60이상'D', 60미만이면'F'를 출력하시오.

name = input("이름을 입력하세요.")
num = int(input("학번을 입력하세요."))
stu1 = int(input("국어 점수를 입력하세요."))
stu2 = int(input("영어 점수를 입력하세요."))
stu3 = int(input("수학 점수를 입력하세요."))
sum = stu1 + stu2 + stu3 
pre = sum / 3 
if pre >= 90:
    print(f"{name}님의 학점은 A입니다.")
elif pre >= 80 and pre < 90:
    print(f"{name}님의 학점은 B입니다.")
elif pre >= 70 and pre < 80:
    print(f"{name}님의 학점은 C입니다.")
elif pre >= 60 and pre < 70:
    print(f"{name}님의 학점은 D입니다.")
else : 
    print(f"{name}님의 학점은 F입니다.")   
'''
'''
[문제3]
-커피의 개당 가격은 2000원이다. 10개를 초과하면 초과하는 양에 대해서만 개당 1500원씩 받는다.
-커피의 개수를 입력받아 금액을 출력하시오.

coffee1 = 0
num = int(input("커피의 개수를 입력하시오."))  

if num <= 10 :
    coffee1 = 2000
    sum = coffee1 * num
elif num > 10 :
    coffee1 = 1500
    sum = coffee1 * num
print(f"커피의 금액은 {sum}입니다.") 
'''

'''
[문제4]
-정수를 입력받아 아래와 같이 출력하시오.
3의 배수이면서, 4의 배수입니다.
3의 배수입니다.
4의 배수입니다.
3의 배수도, 4의 배수도 아닙니다.
0은 3의 배수도 4의 배수도 아닙니다.

num = int(input("정수를 입력하세요."))
if num == 0 :
    print("0 은 3의 배수도 4의 배수도 아닙니다.")
elif num % 3 == 0 and num % 4 == 0 :
        print("3의 배수이면서 4의 배수입니다.")
elif num % 3 == 0:
    print("3의 배수입니다.") 
elif num % 4 == 0:
    print("4의 배수입니다.")        
else :
    print("3의 배수도 4의 배수도 아닙니다.")   
# 다중 if문을 사용하여 여러 조건식을 볼 경우에 범위가 작은 조건식을 먼저 정의한다!!!!!
'''


## for 문
# : 가장 대표적인 반복 구문 중 하나로 주어진 조건에 따른 회차만큼 반복
# (형식)
# for 변수명 in range(반복횟수):
#           종속문장1(for)
#           종속문장2(for)
# (메인 프로그램 실행 코드 진행)
for i in range(10):
    print("A",i)
# range(시작 값, 끝 값, 증감 값) : 파이썬의 내장 함수
# 사용법(range())
# 1. range(종료 값) 시작값 0, 증감 값 +1 기본 값으로 생략
#   :0부터 시작해서 종료값 이전까지의 값의 범위를 가짐.
#    ex) range(10) => [0,1,2,3,4,5,6,7,8,9]
# 2. range(시작값,종료값)
#   :시작값부터 종료값 이전까지의 값의 범위     
#   ex) range(5,10) => [5,6,7,8,9]
# 3. range(시작값,종료값,증감값)
#   : 시작 값 부터 종료값 이전까지 값의 증감값 간격의 값 범위
#  ex) range(0,10,2) => [0,2,4,6,8]
#  ex) range(10,0,-2) => [10,8,6,4,2]
'''
# range(종료값) 예제1
for x in range(10): #[0,1,2,3,4,5,6,7,8,9] , 초기값 : 0, 증가값 : 1, 조건식 : x < 10 
    print(x,end=' ') #print()end 인자값 설정하면 출력후
                     # 마지막에 사용될 문자를 지정 할 수 있음
                     # 사용 : end='문자열', 기본값은 end='\n'
print() 

# 예제2]for문 (range(시작값, 종료 값))
for x in range(5,10): #[5,6,7,8,9],초기값 : 5, 증가값 : 1, 조건식 : x < 10 
    print(x,end=' ') 
print() 

# 예제3]for문 (range(시작값, 종료 값, 증/감값)) -증가값
for x in range(0,10,2): #[0,2,4,6,8],초기값 : 0, 증가값 : +2, 조건식 : x < 10 
    print(x,end=' ') 
print()

# 예제4]for문 (range(시작값, 종료 값, 증/감값)) -증감값
for x in range(10,0,-2): #[10,8,6,4,2],초기값 : 10, 증감값 : -2, 조건식 : x > 0 
    print(x,end=' ') 
print()     

# 예제5]for문 - 문자열
sum = 0
for x in 'string': #['s','t','r','i','n','g'] 
    print(x,end='')
    sum += 1 
print(); print(sum) 

# 예제6]for문 - list, tuple, dictionary...
i = 0
for x in [1,4,78,'test','A',1.80,100]:
    print(x,end=' ')
    i += 1 
print("\n",i,"번 반복함")

# 예제7]이중 for문 : for문을 중첩해서 사용하는 것 
sum = 0
for x in range(10): #상위 for문 [0,1,2,3,4,5,6,7,8,9]   #하위 for문이 10번 돌아갈때 상위 for문이 한번 돌아감.
    for y in range(10):  #하위 for문 [0,1,2,3,4,5,6,7,8,9]
        sum += 1 #sum = sum + 1
print(sum)  


중첩for문(이중for문)은 상위 for한번 실행할때에 하위 for문은 자신에게 주어진 반복 횟수만큼 실행 
(하위for문)
'''
'''
# 예제8]이중 for문 
sum = 0
for x in range(1,5,3): #[1,4] 값으로 두번 반복함 -> 초기값: 1 , 조건식 1 < 5 증가값 : 3     
    for y in range(5,0,-1):  #[5,4,3,2,1] 번 반복함 -> 
        print("{}상위 for문의 x 값, {}하위 for문의 y의 값 ".format(x,y))
        sum += 1 
print(sum,"횟수만큼 반복함!!") 

# 문제1] 중첩for문을 이용하여 구구단 표를 작성
# (출력예시)
# 2 x 1 = 2    
# 2 x 2 = 4  
# 2 x 3 = 6  
# 2 x 4 = 8 .....
sum = 0
for x in range(2,10):
    print("{}단".format(x))
    for y in range(1,10):
        sum = x*y
        print(x,"X",y,"=", sum)

# 문제2] 중첩for문을 이용하여 구구단 표를 작성
# (출력예시)
# 2 x 1 = 2   3 x 1 = 3 
# 2 x 2 = 4   3 x 2 = 6 
# 2 x 3 = 6   3 x 3 = 9 
# ...         ...

for x in range(1,10):  
    for y in range(2,10):      
        print("{}x{}={:<3}".format(x,y,x*y),end=' ')
        print()
print()

# 문제3] 중첩for문을 이용하여 구구단 표를 작성
# (출력예시)
# 상위 for문이 0일때, 하위 for문 : 0 0 0 0 0
# 상위 for문이 1일때, 하위 for문 : 0 1 2 3 4
# 상위 for문이 2일때, 하위 for문 : 0 2 4 6 8
# 상위 for문이 3일때, 하위 for문 : 0 3 6 9 12
# 상위 for문이 4일때, 하위 for문 : 0 4 8 12 16

for x in range(5) :
    print("상위 for문이 {}일 때, 하위 for문 :".format(x),end=' ')
    for y in range(5):
        print("{}".format(x*y),end=' ')
    print()

    
#문제4) 이중 for문을 사용하여 다음과 같이 출력되게 만들어보세요.
# 1) 1   2   3    4    5
#    6   7   8    9    10
#    11   12   13    14    15
for x in range(5) :
    for y in range(1,6) :
        print(x*5+y,end="\t")
    print()
print()
# 2) 25 24 23 22 21
#    20 19 18 17 16
#       ..........
#     5  4  3  2  1 

for x in range(5,0,-1):
    for y in range(5):      
        print(x*5-y,end=" ")
    print()
print()
        
# 3) 1  2  3  4  5
#    2  3  4  5  1
#    3  4  5  1  2 
#    4  5  1  2  3 
#    5  1  2  3  4 
for x in range(5):
    for y in range(5):    
        print((x+y)%5+1,end=" ")
    print()
print()
'''
##while
# : 조건식이 참인 경우에 반복하는 반복문
# (형식)
# while(조건식):
#   종속문장1
#   종속문장2
# (메인 프로그램 코드 실행)
# 예)
# while x <10:
#   종속문장1
#   종속문장2
#     x = x+1 # x += 1 =>조건식에 변화를 주는 값이 필요함.
# (메인 프로그램 코드 실행)

#예제 1] while구문을 이용한 반복문(짝수의 합, 홀수의 합)
'''
i = 1   #초기값
odd_sum = 0
even_sum = 0
while i <= 10:  #조건
    if i % 2==0:
        even_sum += i
    else:
        odd_sum += i
    i += 1 #i = i + 1 # 증감식
print("짝수의 합 : {}, 홀수의 합 : {}".format(even_sum,odd_sum))

#while ~else 를 사용 : while 의 조건이 False가 되는 경우에 else가 실행됨.
# i = 0
# while i < 5: 
#     print("{}번 종속문장 실행".format(i))
#     i += i
# else:
#     print("조건식이 거짓인 경우에 실행 문장")
# print("메인 프로그램 실행 코드")
'''
'''
while의 무한 반복 :while 구문의 조건을 항상 참이 되게 설정한 후에 반복문 내에 제어를 위한 명령어를 실행하는 반복구문
제어를 실행하는 명령어 (반복문에 대한 제어)
1. break => 반복의 종료
2. continue => 반복시 조건 문으로 이동
(형식)
while True:
    종속문장1
    종속문장2
    (종료하기 위한 조건과 명령어 : break)
위와 같은 코드에서는 break를 사용하지 않으면 무한반복함.
무한히 반복되면서 다음으로 코드 진행되지 않기 때문에 정지한것같이 보이게 됨. 때문에 반복에서 벗어나기 위해서 
"break "명령어를 적절히 사용해야함

(break 사용예)
while True:
    종속문장1 
    break
    종속문장2
(메인프로그램 코드)
프로그램 흐름 : 1) while 의 조건식 2) 종속문장1 3)continue
             4) while 의 조건식 5) 종속문장1 6)continue
             7) while 의 조건식....
종속문장2는 실행하지 않음



while True:
    a= int(input("정수 입력[0]시 종료:"))
    if a == 0:
        break
    print("입력값 출력 : " ,a)

#continue 이용
a = 0
while a < 5:
    a += 1
    if a == 3:
        continue
    print("a={}".format(a)) 
'''
#문제 1]
'''
쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다. 
쥐 한마리가 하루 20g씩 쌀을 먹고 있다.
10일마다 쥐의 수가 2배씩 증가하고 있다면,
며칠만에 창고의 쌀이 모두 쥐의 먹이가 될까? 
또, 이때에 쥐는 총 몇마리가 되어 있을까? 
(쌀 한통은 1kg, 쥐는 쌀은 먹은후 2배로 증가하는 조건)
[결과]: 80일 , 512 마리
'''   
# day = 1
# num = 2
# rice = 100*1000

# while True: 
#     rice -= 20*num     
#     if day % 10 == 0: #10일 마다
#         num *= 
#     if rice <= 0: #쌀이 없다면~
#         break 
#     day += 1
# print("결과: {}일, {}마리".format(day,num)) 

'''
# 문제2] 1~100까지의 합을 구하는 코드를 작성
sum = 0
for x in range(1,101) :
    sum += x
print(sum)
                                                                #마지막에 더해진 값 = x+=1 이 반복됐을때 가장 마지막에 증가한 값
#문제3] 1부터 1씩 증가하는 값에 대해 누적합을 구할때 10,000보다 큰 누적합 값에 대해 마지막에 더해진 값이 얼마인지 구하시오
x = 1  
sum = 0 
while True: 
    sum += x # 누적합
    if sum > 10000:
        break; # 누적 값
    x +=1 
print(x,"은 마지막 값") 

#문제4] 1부터 100사이의 소수(prime number)를 출력하고 개수를 구하시오(2진 알고리즘)
count = 0         # 소수는 0,1를 제외한 자기자신으로 밖에 안나눠지는 수이다.
for x in range(2,101): 
    flag = True # flag가 True이면 소수 - 2진 알고리즘, flag 기법 
    ##소수 판별....
    for y in range(2,x):
        if x % y == 0 :
            flag = False   # False 는 즉 소수가 아니란 뜻
            break
    if flag:  #flag가 트루이므로 이때 변수 count에 1를 하나씩 더한다.
        print(x,end=" ")
        count += 1    
print()
print(f"1~100사이의 소수의 갯수는 {count}입니다.")
'''
        
