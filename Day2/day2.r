# **print() , paste() - 여러 자료 븉여서 출력하기(주의 자료형이 다른것을 붙이지 못함)
print(x)
print(x,i)
paste('I', 'am', 'a', 'student') 
# print('I', 'am', 'a', 'student') 에러....
# ceiling()-올림, floor()-내림-> ceiling(1.4), floor(1.4) 
# 내장 함수
# max() , min(), sqrt()-루트 연산, abs()-절대값

max(c(11,5,36,3,4,8,33))
min(c(11,5,36,3,4,8,33))
sqrt(2) 
abs(-100)
ceiling(1.4)
floor(1.4)
round(1.456,2)

## 문자열
# 1. 문자열 
str <- "Hello R!"
print(str) 

# 2. 여러줄 문자열
str2 <- "안녕, 친구야!!,
오늘도 좋은 하루가 되길 바래,
밖에 날씨는 어때?,
졸리다...." 
print(str2)
# [1] "안녕, 친구야!!,\n오늘도 좋은 하루가 되길 바래,\n밖에 날씨는 어때?,\n졸리다...." 

# 3. 동일하게 "\n"표현되도록 출력하고 싶다면.... cat() 
str3 <- "안녕, 친구야!!,
오늘도 좋은 하루가 되길 바래,
밖에 날씨는 어때?,
졸리다...." 
cat(str3) 

# 4. 문자열 길이 : nchar(str)
nchar(str)
nchar(str3) 

# 5. 문자열 내에 글자 확인 함수 : grepl() 
str4 <- "Hello World!! Hi, R~"
grepl("H",str4) # True
grepl("Hi",str4)
grepl("Hello",str4)
grepl("Hallow",str4)

# 6. 문자열의 결함: paste()
str5 <- "Hello" 
str6 <- "R~" 
paste(str5,str6) 

## escape 문자 : \\,\n,\t,\r,\b 

# 조건문 : if
# if(조건) {
#    조건 실행문...
#}

# 조건문 : if
# if(조건) {
#    조건 실행문
# }else{   
#    else조건 실행문...
#} 

## x가 10 일경우 ,if 문을 사용하여 2의 배수이면"2의 배수",6배수 이면 "6의 배수"라고 출력되게 if를 사용해보세요. 


# intext <- readline("입력하세요 :")
# num <- as.numeric(intext) 
# if (num%%2 == 0){
#     print("2의 배수!!")
# }
# if (num %%6 == 0) {
#    print("6의 배수")
# }

## 반복문 : while, for 
# next(continue) 
i <- 0
while (i < 6){
    i <- i + 1
    if (i==3){
        next
    }
    print(i)
} 

# for 문도 비슷하게 사용이 가능함.
dice <- c(1,2,3,4,5,6)
for (x in dice){
    print(x)
}

x <- 1 
for (i in 2:10){
    x <- x*i
    print(x) 
}

## 함수만들기(function명령어 사용)
# 함수명 <- function(인자리스트){
#   함수정의부
#}

# return() 함수 실행 결과를 리턴
# 함수 호출 : 함수명(인자)
bh <- function(yb){
    x <- 1 
    for (i in 2:yb){
        x <- x * i
        
    }
    return(x)
}
# 함수 호출
bh(10)

# 함수 중첩 예시
Nested <- function(x,y){
    a <- x+y
    return(a)
}
Nested(Nested(2,2),Nested(3,3))

## 함수 중첩 예시2
Outer_func <- function(x){
    Inner_func <- function(y){
        a <- x + y
        return(a)

    }
    return(Inner_func)
}
output <- Outer_func(3) # x값
output(15) # y값

#### 숫자를 입력받아 그 숫자를 역으로 출력하는 프로그램을 함수로 만드세요.



reverse <- function(x){
    result <-0
    while(True){
        temp <- x %% 10 
        x <- x %/% 10
        result <- (result+ temp) * 10
        if (x == 0){
            break
        }
    }
    return(result%/%10)
}


### 두수를 입력받아 그 평균을 구하는 함수를 만드세요. 
num2 <- readline("첫번째 숫자 :")
num3 <- readline("두번째 숫자 :")



# 재귀 함수 : 재귀함수는 자신이 자신을 참조하여동작하는 함수 
tri <- function(k){
    if(k > 0) {
        result <- k + tri(k - 1)
        print(result)
    }else {
        result <- 0
        return(result)
    }
}
tri(5)


fact <- function(k) {
    if(k > 1){
        result <- k* fact(k - 1)
        print(result)
    }else {
       result <- 1
       return(result)
    }
}
fact(5) 

## 전역변수 설정하기
# 일반 변수 설정
txt <- "awesome"
my_function <- function(){
    txt <- "fantastic"
    paste("R is ",txt)
}

my_function()
print(txt)

# 전역 변수 설정
my_function <- function(){
    txt <<- "fantastic"
    paste("R is",txt)
}
my_function()
print(txt)

## 벡터 : 같은 자료형의 연속된 리스트(배열) 
fruits <- c("banana","apple","orange")
fruits[2] 

# 숫자 벡터
numbers1 <-c(1,2,3,4,5)
numbers1[5] 

# 연속된 숫자의 백터 생성
numbers2 <- 1:10 
numbers2 
numbers2[9] 

# 연속된 값의 표현은 정수 단위로 증가합니다. 
numbers3 <- 1.5:6.5
numbers3  

# 연속된 값의 숫자 벡터 경우 단위 증가시 사용되지 않는 경우 
numbers4 <- 1.5:6.4 # [1] 1.5 2.5 3.5 4.5 5.5 마지막 값은 출력이 안됨
numbers4

# 논리값 벡터
log = c(TRUE,FALSE,TRUE,FALSE)
log 
# 벡터 길이 알아오기(요소 갯수 알아오기)
length(numbers4)

fruits <- c("banana","apple","orange","mango","lemon")
length(fruits)

### 벡터의 문자열이나 숫자를 정렬하여 처리하는 함수 : sort() 
sort(fruits) # "apple"  "banana" "lemon"  "mango"  "orange"
sort(numbers1)  # 1,2,3,4,5

# 벡터 함수의 사용 인덱스 참조1: c()
fruits <- c("banana","apple","orange","mango","lemon")
fruits[c(1,3,5)] # "banana" "orange" "lemon"  

# 인덱스 참조2 
fruits <- c("banana","apple","orange","mango","lemon")
# 선택 제외(-인덱스로 제거하여 출력) 
fruits[-1] # "apple"  "orange" "mango"  "lemon"   # "-"는 파이썬과 달리 해당 인덱스 제거를 뜻한다.
fruits[-3] # "banana" "apple"  "mango"  "lemon" 
fruits[c(-1,-3)] # "apple" "mango" "lemon"           

# 벡터의 반복 : rep() 
# 요소의 반복 
repeat_each <- rep(c(1,2,3),each = 3)
repeat_each

# 벡터의 반복
repeat_times <- rep(c(1,2,3), times = 3)
repeat_times 

# 요소의 개별 반복
repeat_ind <- rep(c(1,2,3),times = c(5,3,2))
repeat_ind 

# 순차적인 벡터 생성
number1 <- 1:10
number1 
# seq() 함수 사용 : 인자(from(시작), to(끝), by(단위,간격))
number2 <- seq(from=0,to=100,by=20)
number2  

for (i in seq(from=0,to=100,by=20)){
    print(i)
}

### Lists : list()함수 사용
# 문자열 리스트 
strlist <- list('사과','바나나','딸기')
strlist 

# 숫자형 리스트
numlist <- list(12,34,24,55)
numlist 

tlist <- list("사과",c(10,20,30),'바나나','체리')
tlist[2]

# 리스트내 값 참조
strlist <- list('사과','바나나','딸기') 
"사과" %in% strlist

# 리스트내에 값 추가 : append() 
strlist <- list('사과','바나나','딸기') 
strlist <- append(strlist,"메론",after = 2)
strlist

# after가 없다면? 마지막에 추가
strlist <- list('사과','바나나','딸기') 
strlist <- append(strlist,"메론",after = 2)
strlist <- append(strlist,"포도")
strlist

# 리스트 값 제거 :
strlist <- strlist[-1] 
strlist

# 리스트 범위로 값을 출력
strlist
strlist[2:5] 

# 리스트 결합
list <- list("a","b","c")
list2 <- list(1,2,3) 
list3 <- c(list,list2)
print(list3) 

## Matrices() - matrix() 를 사용, nrow,ncol값으로 정렬 지정
## 행렬 생성1

tmatrix <- matrix(c(1,2,3,4,5,6),ncol = 2,nrow = 3) 
tmatrix 


## 행렬 생성2 
t2matrix <- matrix(c("apple","banana","cherry","orange"),nrow = 2,ncol = 2)
t2matrix

## 행렬에 대한 접근 "[]"를 이용하여 접근 
t2matrix[1,2]
t2matrix[2,]
t2matrix[,2]
t2matrix[,]

##하나 이상의 행렬에 접근 
t3matrix <- matrix(c("apple","banana","cherry","orange","grape","pineapple","pear","melon","fig"),nrow = 3,ncol = 3)
t3matrix 
t3matrix[c(1,2),]
t3matrix[-3,]
t3matrix[,c(1,3)]

## 행렬에 값을추가 (컬럼 추가) : cbind() 
newmatrix <- cbind(t3matrix,c("strawberry","blueberry","rasberry"))
newmatrix
## ## 행렬에 값을추가 (컬럼 추가) : rbind() 
newmatrix <- rbind(t3matrix,c("strawberry","blueberry","rasberry"))
newmatrix 

# 행렬값 제거 : 음수 인덱스 표시
r1matrix <- newmatrix[-c(1,2),-c(3,4)]
r1matrix

## 행렬값 확인
"apple" %in% r1matrix
"apple" %in% newmatrix

## 행렬의 row와 column 알아오기 : dim()함수
dim(t2matrix)
dim(t3matrix)
dim(tmatrix)
dim(newmatrix) 

# 행렬의 길이 
lmatrix <- matrix(c("apple","banana","cherry","orange"),nrow = 2,ncol = 2)
length(lmatrix) 

# 행렬에 반복문을 사용하여 rows column값으로 행렬값을 불어와 보세요 ,
# t4matrix <- matrix(c("apple","banana","cherry","orange"),nrow = 2,ncol = 2)
# t3matrix 
t4matrix <- matrix(c("apple","banana","cherry","orange"),nrow = 2,ncol = 2)
for (t in 1:nrow(t4matrix)) {
    for (c in 1:ncol(t4matrix)){
        print(t4matrix[t,c])  
    }

}
# 행렬 합치기
matrix1 <- matrix(c("apple","banana","cherry","grape"),nrow = 2,ncol = 2)
matrix2 <- matrix(c("orange","mango","pineapple","watermelon"),nrow = 2,ncol = 2)

# row로 더하기 : rbind() 
mat_combind <- rbind(matrix1,matrix2)
mat_combind

## Array  배열
tarray <- c(1:24) 
tarray 
class(tarray) 

multiarray <- array(tarray,dim=c(4,3,3)) 
multiarray  
# * dim(4,3,3) : 4는 rows, 3은 columns,3은 행렬의 갯수(생성할 행렬의)
# dim(nrow,ncol,생성 개수) 

# Arrays 값 접근
multiarray[2,2,2] 

# c()함수를 이용한 접근

t2array <- c(1:24) 
## 첫번째 행렬의 첫번째 row 에 접근
tmulti <- array(t2array,dim=c(4,3,2))
tmulti[c(1),,1] 

## 첫번째 행렬의 첫번째 column 에 접근
tmulti <- array(t2array,dim=c(4,3,2))
tmulti[,c(1),1] 

3 %in% tmulti 

## row 와 column 확인
dim(tmulti) 

## Array 길이 
length(tmulti) 

# 반복문 사용 
for (x in tmulti){
    print(x)
}

## dataframe (data.frame())
## 데이터 프레임은 데이터릉 테이블 형채로 표현하는 자료형
## 데이터 프레임 안의 데이터 타입은 서로 달라도 됩니다.

Data_frame <- data.frame(   # 키:값은 = 로 대입한다.
    Training = c("Strength","Stamina","Other"), 
    Pulse = c(100,150,120),
    Duration = c(60,30,45)

)
Data_frame   
## summary () : 데이터 프레임 값을 요약해서 보여줌
summary(Data_frame) # 데이터 프레임의 값을 요약해서 출력

Data_frame[1] 
Data_frame['Training']
Data_frame$Training 

## Row추가 : rbind() 


Data_frame <- data.frame(   # 키:값은 = 로 대입한다.
    Training = c("Strength","Stamina","Other"), 
    Pulse = c(100,150,120),
    Duration = c(60,30,45)

)
New_Row_DF <- rbind(Data_frame,c("Speed",110,110))
New_Row_DF 

## column 추가 : cbind()
Data_frame <- data.frame(   # 키:값은 = 로 대입한다.
    Training = c("Strength","Stamina","Other"), 
    Pulse = c(100,150,120),
    Duration = c(60,30,45)

)
New_Col_DF <- cbind(Data_frame,Steps=c(1000,6000,2000))
New_Col_DF 

## row와 column제거 
Data_frame <- data.frame(   # 키:값은 = 로 대입한다.
    Training = c("Strength","Stamina","Other"), 
    Pulse = c(100,150,120),
    Duration = c(60,30,45)

)
Data_frame_new <- Data_frame[-c(1),-c(1)]
Data_frame_new

# ncol,nrow()
ncol(Data_frame)
nrow(Data_frame) 

# 요소 개수(길이)
length(Data_frame)

# 결합 : rbind()
Data_frame1 <- data.frame(   # 키:값은 = 로 대입한다.
    Training = c("Strength","Stamina","Other"), 
    Pulse = c(100,150,120),
    Duration = c(60,30,45)

) 
Data_frame2 <- data.frame(   # 키:값은 = 로 대입한다.
    Training = c("Stamina","Stamina","Strength"), 
    Pulse = c(140,150,160),
    Duration = c(30,30,20)

) 
New_Data_frame <- rbind(Data_frame1,Data_frame2)
New_Data_frame 
# 결합 : cbind() 
Data_frame3 <- data.frame(   # 키:값은 = 로 대입한다.
    Training = c("Strength","Stamina","Other"), 
    Pulse = c(100,150,120),
    Duration = c(60,30,45)

) 
Data_frame4 <- data.frame(   # 키:값은 = 로 대입한다.
    Steps = c(3000,6000,2000),
    Calories = c(300,400,300)

)  
New_Data_frame1 <- cbind(Data_frame3,Data_frame4)
New_Data_frame1 

# Factors (factor()) : 범주형 자료일때에 사영
## : 정해진 범위 내에서 카테고리 별로 분석을 하기 위해서 사용되는 데이터 자료형
## 예) 성별 : 남성/여성, 음악 : 락, 팝, 클래식 , 재즈, 운동 : 스테미나, 근력 

music_genre <- factor(c('Jazz','Rock','pop','classic','classic','Rock','Jazz'))
music_genre 

# levels : levels() - > 카테고리로 출력 
levels(music_genre)
# length 요소의 갯수
length(music_genre)

# 요소 접근
music_genre[3]

# 요소의 변경
music_genre[3] <- "Rock"
music_genre[3]

# 주의) factor는 정해진 범주내에서 카테고리별로 분석을 위해서 사용하기 때문에 사전에 정의되어 있지 않은 값으로 변경시 에러발생
music_genre[3] <- 'Opera' 
music_genre <- factor(c('Jazz','Rock','pop','classic','classic','Rock','Jazz'),
levels = c('Classic','Jazz','Pop','Rock','Opera'))
music_genre[3] <- 'Opera'
music_genre[3]

## 순열과 조합
# 순열 : 서로 다른 것들이 있는 경우 그중에서 몇개를 뽑아서 줄을 세우는 경우의 수 여기서 줄을 세운다는 표현은 순서를 고려한다는 의미

# 팩토리얼 구하는 코드
fact <- function(n){
    x <- 1 
    for (i in 2:n){
        x <- x *i 

    }
    return(x)
}
fact(10)

####################################
x <- c(1,2,3,4,5) 
count <- 0
for (i in 1:5){
    x2 <- x[x != i] # i에 저장된 값 빼고, x2에 저장
    for (j in 1:4){
        print(c(i, x2[j]))
        count <- count + 1 
    }            

}
# (1,2) (1,3),(1,4),(1,5),(2,1),(2,3),(2,4),(2,5)..... 
print(count) 

# =>> 공식을 이용한 경우npr = n!/(n-r)! 
perm <- function(n,r){
    return(fact(n)/fact(n-r))
}
perm(5,4) 

### 조합은 순서를 고려하지 않는다...... (1,2),(2,1) 
# 순서를 고려하지 않기 때문에 같은 값이 있다면, 이것은 하나의 값으로 처리됨. 

# nPr/r! = nCr ,이유는 순서의 쌍이 같은 값으로 구성되기 때문이다.
# 1,2,3 세숫자의 순열은 3! = 6이다.... 
# (1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1) 

# 하지만 조합은 1개만 존재한다. 왜? 모두 1,2,3이 포함되어 있으니까....

## 조합을 계산하는 코드 
x <- c(1,2,3,4,5) 
count <- 0
for (i in 1:4){
    for (j in (i+1):5){
        print(c(i,j))
        count <- count + 1
    }
}
print(count) 

## nPr = n!/(n-r)! 
## nCr = nPr/r! => n!/(n-r)!/r! 

comb <- function(n,r) {
    return(fact(n)/fact(n-r)/fact(r)) 
}
comb(45,6)   

# 순열, 조합, 상트페티르부트크의 역설   

