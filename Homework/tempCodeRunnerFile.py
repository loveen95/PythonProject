# [5장 문제 1]
from itertools import count
from turtle import width
def star(height):
    floor = count = 0
    while floor < height:
        floor += 1
        print("*"*floor)
        count += floor
    return count
height = int(input("height :"))
print("star 개수 :%d" % star(height)) 

# [5장 문제 2]
def Bank_account(bal):
    balance = bal 
    def getBalance():
        return balance
    def deposit(money):
        nonlocal balance    
        if money < 0: 
            print("금액 확인")
            return
        balance += money       
    def withdraw(money):
        nonlocal balance
        if balance < money :
            print("잔액이 부족합니다.")
            return
        balance -= money      
    return getBalance, deposit, withdraw 

acc = Bank_account(int(input("최초의 계좌 잔액을 입력하세요")))
print("현재 계좌의 잔액은{}원입니다.".format(acc.getBalance()))
add = int(input("입금액을 입력하세요"))
print("{}원 입금후 잔액은 {}원입니다.".format(add,acc.deposit(add)))
draw = (int(input("출금액을 입력하세요")))
print("{}원 출금후 잔액은 {}원 입니다.".format(draw,acc.withdraw(draw)))

# [5장 문제 3]
def Factorial(n):
    if n == 1:
        return 1
    else :
        result = n * Factorial(n-1)
        print(n,end=' ')
        return result
result_fact = Factorial(5)
print("팩토리얼 결과 :",result_fact)

# [6장 문제 1]
class Rectangle:
    width = 0 
    height = 0
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area_calc(self):
        calc = self.height * self.width
        return calc
    def circum_calc(self):
        circum = (self.height+self.width)*2
        return circum 
    
print("사각형의 넓이와 둘레를 계산합니다.")
w = Rectangle(int(input("사각형의 가로 입력 :")),int(input("사각형의 세로 입력 :")))
print("------------------------------------")
print("사각형의 넓이 :{}".format(w.area_calc()))
print("사각형의 둘레 :{}".format(w.circum_calc()))
print("------------------------------------")

# [6장 문제 2]
from statistics import mean
from math import sqrt

class Scattering:
    def __init__(self,x):
        self.x = x
    def var_func(self):
        avg = mean(self.x)
        diff = [(i-avg)**2 for i in self.x]
        self.var = sum(diff) / (len(self.x)-1)
        return self.var
    def std_func(self):
        st = sqrt(self.var)
        return st
x = [5,9,1,7,4,6]
scat = Scattering(x)
var = scat.var_func()
st = scat.std_func()
print("분산 :",var)
print("표준편차 :",st)

# [6장 문제 3]

