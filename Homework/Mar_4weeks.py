# [2장 문제4]
world1 = input("첫번째단어 :") 
world2 = input("두번째단어 :") 
world3 = input("세번째단어 :")
abbr = world1[0] + world2[0] + world3[0] 
print("========================")      
print(f"약자 : {abbr}")

# [3장 문제1-A]
kg = int(input("짐의 무게는 얼마입니까?"))
if kg < 10 : 
    print("수수료는 없습니다.")
else : 
    print("수수료는 10,000입니다.")
    
# [3장 문제1-B]
kg = int(input("짐의 무게는 얼마입니까?"))
price = 0
if kg >= 10:
    price = (kg // 10) * 10000
    print("수수료는 {}원 입니다.".format(price))
else : 
    print("수수료는 없습니다.")
    
# [3장 문제2]
import random 
print(">>숫자 맞추기 게임 시작<<")
com = random.randint(1,10)
while True : 
    my = int(input("예상 숫자를 입력하시오>>"))
    if my > com : 
        print("더 작은 수를 입력")
    elif my < com :
        print("더 큰 수를 입력")
    else : 
        print("성공!!~~")
        break
print()

# [3장 문제3]
sum = 0
print ("수열 =", end=' ')
for x in range(1,101):
    if x % 3 == 0 and x % 2 != 0:
        print (x,end=' ')
        sum += x
print(f"\n누적합 = {sum}")          

# [3장 문제4]
multiline="""안녕하세요. 파이썬 세계로 오신걸 환영합니다. 파이썬은 비단뱀 처럼 매력적인 언어입니다."""
print("<출력결과>")
count= 0
a = []
b = []
for x in multiline.split('\n'):
    a.append(x)
    for y in x.split(' '):
        b.append(y)
        count += 1
print(a)
print("단어수 : ",count)

# [4장 문제1]
lst = [10,1,5,2]
result = lst*2
print("단계 1 :",result)
result.append(lst[0]*2)
print("단계 2 :",result)
result2 = result[1:8:2]
print("단계 3 :",result2)

# [4장 문제2-A]
vector = int(input("vector 수 :"))
lst = [] 
for x in range(vector):
    num = int(input())
    lst.append(num)
print("vector 크기 :",len(lst))

# [4장 문제2-B]
vector = int(input("vector 수 :"))
lst = [] 
for x in range(vector):
    num = int(input())
    lst.append(num)
if int(input()) in lst:
    print("YES")
else : 
    print("NO") 

# [4장 문제3-A]
message = ['spam','ham','spam','ham','spam']
dummy = [1 if lst =='spam' else 0 for lst in message]
print(dummy)

# [4장 문제3-B]
spam_list = [lst for lst in message if lst == 'spam']
print(spam_list)

# [4장 문제4]
position = ['과장','부장','대리','사장','대리','과장']
no_repeat = list(set(position))
num1, num2, num3, num4 = 0,0,0,0
for x in position:
    if x == '과장':
        num1 += 1
    elif x == '부장':
        num2 += 1
    elif x == '대리':
        num3 += 1
    elif x == '사장':
        num4 += 1
   
print("중복되지 않은 직위 :",no_repeat)
print("직위별 빈도수: '과장':{},'부장':{},'대리':{},'사장':{}".format(num1,num2,num3,num4))