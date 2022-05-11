# R 사용 문법
# 변수 사용하기(대입 연산은 "=" 대신 "<-"or "->"를 사용함)
# - 하나의 값을 변수 저장하기
x <- 5
x * x
10 -> y
y + y

# 2. 여러개의 값을 변수에 저장하기 (배열과 같은 자료 사용하기) 
x <- c(5, 6) # 벡터 변수, 여러개의 값을 하나의 변수 저장
print(x)  
# 여러개의 값을 가진 변수의 일부값을 참조시 index를 사용
# r의 인덱스의 시작값은 1부터 시작!!!
x[1]
x[2]

##  변수 이름 규칙
# - 변수 이름은 영문, 숫자, ".", "_"를 사용
# - 하지만, "."을 앞에 사용할수 있음. 이때 뒤에 숫자는 안된다.
# - 변수 앞에 숫자나 "_"를 사용할수 없다.
# - 변수명은 대소문자 구분
# - 예약어를 사용할 수 없음


## 데이터 타입
# numeric : 숫자(10.5, 55, 768) 
# integer : integer타입 (숫자 L을 붙여서 표현) (1L, 55L, 100L) 
# complex : 복소수형(i를 붙여서 구분)
# character : 문자 또는 문자열 자료
# logical : 논리형 자료 (TRUE, FALSE)

## 타입 보는 명령어(함수) : class() 
class(10L)    # integer 
class(10.7)   # numeric
class("th")   # character
class('test') # character
class(TRUE)   # logical 

## 형변환 : as .numeric(), as.integer(), as.complex() 
x <- 1L 
y <- 2 

a <- as.numeric(x) 
class(a) 

b <- as.integer(y)
class(b)

### 연산자(산술)
# +, -, *, /, ^(제곱), %%(나머지), %/%(정수 나누기)
a + b
a - b
a * b
a / b 
a ^ b
a %% b
a %/% b 

### <-, <<-, ->, ->> 
# "<<-" 전역 선언 , <- 대입처리

# 비교 연산자
# ==, !=, >, <, >=, <=

10 == 10
10 != 10 

## 논리 연산자 
# &, &&, |, ||, ! 
10 == 10 && 10 == 10 
10 == 10 || 10 == 10 
!(10 == 10)   

### 이외연산자
# : 순서대로 순자를 생성하는 연산자 ex) 1:10 -> X
# X는 (1,2,3,4,5,6,7,8,9,10)
# %in% : 데이터들(벡터)내에 값이 있는지 확인
# %*% : 매트릭 곱하기

1 : 10 -> x
x 
i <- 5 
i %in% x    

