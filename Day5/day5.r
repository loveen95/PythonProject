### 통계적 추정(STATISTICAL INFERENCE)
# 통계학을 배우는 이유?
# 통계학은 실제 전체 집단에 대한 특성을 알고 싶을때, 그게 현실적으로 가능할까?
# 실제로 전체 집단에 대한 자료를 구하는거는 쉽지 않은 일이다.
# 집단 전체가 아닌 일부 표본집을 집단을 통해서 전체에 대해서 추론을 하는 것이다.
## 예) 선거철 여론조사
## 우리는 올바른 통계적 추론 방법을 사용하는 것이 매우 중요하다.

## 통계척 추정의 종류
# 통계학에서 모집단(population)과 표본(sample)을 구분한다.
#
# - 모집단은 우리가 여러번 언급한 관심을 가진 전체 집단 ex) 주사위 경우의 수
# - 표본은 모집단의 일부를 의미. 여기서 표본이란 임의 표본을 말한다(random sample)
# 임의 표본은 모집단의 모든 구성원에게 표본에 포함될 기회를 똑같이 주고 추출한 표본
# 그리고, 특정 단위가 선택될 확률은 다른 단위가 선택될 확률과 독립적이다.(영향을 받지 않는다)
# "독립적이면서도 동일하게 분포된(independent and identically distributed - iid)"라고 표현한다.

# 모집단에서 표본을 얻으면, 그것을 바탕으로 모집단에 대해서 추정을 하는데,
# 통계적 추론으로 1)점추정(point estmation)과 2)구간추정(interval estmation)이 있다.

## 점추정
# 점추정은 관심을 갖고 있는 숫자, 모집단의 평균, 비율 등 하나의 숫자로 "찍는"것을 말한다.
# 모집단의 평균과 비율을 얘기하고 모평균, 모비율로 말하는 방식으로 모집단의 수치를 표시한다.
# 같은 방식으로 표본 집단의 평균도 표본평균, 표본비율이라고 부른다.
# 모집단의 특정 값을 알기 위해서는 표본에서 같은 특정 값을 사용하여 추정하는 것이 맞다.
# 표본집단의 특정갑 예로 평균을 점추정하여 모집단의 평균을 구하는 것이다.
## 예) "한국의 20대 여성"이라는 모집단의 키 평균울 추정한다면, 100의 표본을 추출하여 키의 표준평균을 계산한다음,
##     그것을 모평균의 추정치로 사용하는 방식. 같은 방식으로 모비율에 대한 추정, 표준 편차에 대한 추정도 가능하다.

## 표집오차(sample error),표준오차(standard error)
# 모집단에서 임의 표본을 추출한다는 것은 각각의 단위에 뽑힐 확률 기회가 무작위적으로 주어진다는것을 의미함.
# 이는 추출할때마다 표본이 달라지고, 표본평균이나 표본비율도 달라질수 있다.
# 이런 현상을 통계학에서는 "표집오차(sample error)"라고 한다.
# 이 표집오차로 인해서 표본의 평균, 비율은 매번 일치하지 않을 경우가 대부분인 것을 알수 있다.
# 하지만, 일치하지 않는 정도는 어떤 범위 내로 정해져 있을것이다. 이 범위 정도를 "표준오차(standard error)"라고 한다.
# 이 표준오차가 작은 추정방식일수록 좋은 추정 방식이 된다.

## 구간추정
# 위에서 말한 표준오차를 알고 있다면, 구간추정을 할수 있습니다.
# 점추정이 하나의 숫자를 찍는것과 달리 구간추정은 모수치가 대략 어디에서 어디 사이에 있을 것이라고 예상하게 해줍니다.
# 예로 선거에서 특정 후보의 지지율을 단순히 40%라고 하지 않고, 38.5 ~ 41.5%에 있다고 하는 경우를 구간추정이라고 볼수있다.
# 점추정과 다른점은 하나의 숫자를 전달하는게 아닌 불확실성의 정도를 함께 전달하고 있어서 더 바람직한 경우가 많다는 점이다.
# 여기서 "신뢰구간"또는 "신뢰도"라는 말을 했다면, 보통 구간추정을 했다는 의미다.

## 모평균의 추정
# 표본평균은 모평균에 대해서 즐겨 사용한 점추정치로 여러가지 좋은 성질을 가지고 있다.
# 1) 불편성(unbiasedness): 어디에 치우치지 않는다.
#    모집단에서 추출을 계속하면서 표본평균을 계산한다면, 그 기댓값은 모평균에 일치한다.
# 예로 앞에서 이야기한 "20대 한국 여성"이라는 모집단의 키의 평균을 구하는 것을 생각해보자.
# 이미 키의 평균은 정해져 있을 것이지만, 우리는 정확히 알지 못한다면 모집단에서
# 임의의 100명식 표본을 추출하여 평균을 계산하는것을 반복한다.
# 그리고, 표본 100명의 평균을 계산한 다음에 다시 모집단으로 돌려보낸다. 즉, 복원 추출을 한다는 의미이다.
# 이렇게 1000번을 시뮬레이션을 한다음에 1000개의 표본평균을 얻을수 있다.
# 이 값들의 평균을 구하면, 이것이 바로 평균의 평균이다.
# 불편성은 이렇게 평균을 한없이 모으면 그 값들의 평균은 모평균과 일치한다는것을 의미한다.
# 불편성은 표본평균을 모평균에대한 추정치로 사용할 때에 모평균에 비해 작거나 큰 값으로 치우치는 경향이 없다는것을 보장한다.
# 이 추정치를 "불편 추정치"라고 한다.
# 반면에 음이나 양의 방향으로 치우치는 경향이 있는 추정치를 "편의 추정치"라고 한다.

# 2) 최소분산(minimum variance)
# 표본평균 말고도 모평균에 대해 불편추정치를 만들수 있는데, 자료를 많이 모았다고 해도, 그중 첫번째 값만 떼어 모평균에 대한
# 추정치로 사용할 수 있다. 그러면 그 기댓값이나 평균은 모평균과 같을수 있다.
# 하지만, 이런 방식은 표본평균에 비해 변동성이 훨씬 크다.
# 수학적인 증명이 있으나 여기서는 단순히 자료의 수가 적으면 정보의 양도 적다는 것을 의미한다.
# 위에 이야기한 표본평균은 모평균에 대한 불편추정치중 변동성이 가장 작다.
# 모평균과 가장 가깝다는 의미이고, 이것이 "최소분산"의 의미이다.
# 여기서 분산은 변동성을 측정하는 단위의 하나라고 이해하면 된다.

### R을 이용한 표본평균 시뮬레이션하기
# 불편성은 직접 시뮬레이션을 하지 않으면 이해하기 쉽지 않다.
# 모집단이 특정 자료가 아니라 확률분포라고 가정한다.
# 확률분포는 자료가 무한히 많은 모집단처럼 간주하기도 한다.
# 평균이 170이고, 표준편차가 15인 확률분표, N(170,15^2)를 모집단으로 생각한다.
# 이것은 어떤 가상 집단의 키의 분포라고 생각할수 있다.
# 이 모집단에서 표준평균을 추출작업을 반복하여 값을 구한다.

# 난수 생성기 시드 고정
set.seed(1234)  # 참고사항 : 시드값은 아무거나 넣어도 상관없다. 대신 같은 값이면 고정된 결과가 나옴

# 표본평균의 개수
n_sim <- 10000

# 각 표본의 크기
sample_size <- 100
means <- c()

for (i in 1:n_sim) {
    data <- rnorm(sample_size, 170, 15)
    means <- c(means, mean(data))
}
hist(means,xlab="X", ylab="N", main="", prob=T, breaks=50 )
curve(dnorm(x,170,15/sqrt(sample_size)), 160, 180, add=T, lty=2, lwd=2, col="red") 

# 출력된 그래프를 확인하면, 완벽하지는 않지만, 표본평균에 분포는 대충 종형 곡선에 가까운것을 확인할수 있다.
# 이것은 앞에서 말한 표본평균의 분포는 정규분포를 따른다는 "중심극한정리"의 결과이다.
# 시뮬레이션 횟수를 더 늘리면 곡선이 실제 자료의 점점더 잘 들어맞게 된다.
# 통계학에서는 "fit이 좋아진다"라고 한다.
# 이분포의 표준편차는 모집단의 표준편차인 15를 표본의 크기인 100의 제곱근 즉 10으로 나눈것과 같다.
# 일반적으로 표본평균의 표준편차는 모집단의 표준편차에 비해 "표본의 크기의 제곱근"의 역배수 만큼 작다.
# 즉, 여기서는 표준표본의 표준편차는 1.5가 된다.
# 실질적으로 모표준편차를 모르기 때문에 다른 방식으로 추정한뒤에 대신 사용해야 한다.

# 이 시뮬레이션을 하기 전에 표본평균은 모평균에 대한 불편추정치라고 했다.
# 이게 사실이면 표본평균은 모평균에 매우 가까워야한다.

# 위 시뮬레이션에서 표본평균의 평균을 구하면,
mean(means)  # 170.0066
# 표본평균의 평균은 모평균과 거의 일치하는 것을 확인할수 있다.
# 또한, 정규분포는 매우 유용한 성질을 가지고 있다.
# 평균에서 +-(2 x 표준편차)영역 안에 95%가량의 자료가 포함된다는 것이다.
# 여기서 표본평균의 경우에도 (2 x 표준오차)라고 할수 있다.

se <- 15/sqrt(sample_size)  # standard error
means_within_2se <- (means > 170 - 2*se) & (means < 170 + 2*se)
sum(means_within_2se) # 9514

# standard error는 표준편차를 각 표본의 크기에 대한 루트값으로 나눈것이다.
# 위에서 계산한 것과 같이 1.5가 나온다.

# 두번째, 표본평균이 위에 170 +- (2 x 표준오차)안에 포함되는지 여부를 각각 알아본뒤에
# means_within_2se에 저장하고 있다. 이때에 결과는 TRUE 또는 FALSE가 저장된다.
# 각각의 TRUE는 1로 FALSE는 0으로 취급되기때문에, 이들의 합을 구하면 전체 시행 횟수에 따른
# 얼마나 TRUE가 나왔는지를 알수 있게 된다. 그리고 그 값은 95.14%로 95%라는 값과 대략 일치한다.

# 모평균에 대한 구간 추정
# 표본평균이 정규분포를 따른다는 것은 수학적 증명이 시뮬레이션으로 확인했다.
# 이것을 통계학적으로 표현하면, 자료가 평균이 m, 표준편차가s인 어떤 분포를 따른다고 한다면
# 이 분포의 크기인 n인 표본을 추출하여 표본평균을 구하는 일을 반복할때에 n이 커짐에 따라 표본평균은 근사적으로
# 다음과 같은 정규분포를 따른 것으로 알려져 있다.

# N(m,s^2/n)
# 표본평균의 분산, s^2/n은 자료의 크기에 반비례하여 작아진다.(큰 수의 법칙)
# 이 사실을 활용하여 다음이 성립할수 있다.

# 원래는 X위에 바를 그어서 표현하나, 지금은 그냥 대문자 S로 표현(표본평균을)

# P(m - 2 x s/sqrt(n)< X < m + 2 x s/sqrt(n)) ~= 0.95
# 이것은 표본평균이 모평균으로 부터 +-(2 x 표준오차)안에 있을 확률은 95%이다를 수학적으로 표현한 것이다.

# 첫번째 부등식, m - 2 x s/sqrt(n) < X ,m이하의 부분을 넘기면,
# m < X + 2 x s/sqrt(n)가 된다.
# 두번째 부등식, X < m + 2 x s/sqrt(n) 도 첫번째와 같은 방식으로 처리하면
# m > X - 2 x s/sqrt(n)이 된다.
# 첫번째 두번째 부등식의 결과를 합치면
# X - 2 x s/sqrt(n) < m < X + 2 x s/sqrt(n)

# P(X - 2 x s/sqrt(n) < m < X + 2 x s/sqrt(n)) ~= 0.95

# 여기서 "무작위"인것, 즉 표본을 추출할때마다 모평균이 아닌 표준평균임을 주목한다.
# 즉, 위에 평균이 m이고, 표준편차가 s인 모집단의 표본평균을 계속 모으면
# 그 중 95%에서 m은 평균에서 (2 x 표준오차)안에 들어온다는것을 의미한다.
# 신뢰구간은 이와 같이 표본평균 +-(2 x 표준오차)는 모평균에 대한 95% 신뢰구간이라고 한다.
# 이것을 달리 말하면, 모집단에서 계속 표집하면서 95% 신뢰구간을 만들면 그 중에 95%는 모평균을 포함한다는 것을 의미한다.

# R로 95%신뢰구간의 성질 확인하기

# 난수 생성기 시드 고정
set.seed(1234)

# 표본평균 개수
n_sim <- 10000
# 각 표본의 크기
sample_size <- 100
m <- 170
s <- 15
se <- s/sqrt(sample_size)
X_bar_in_CI <- c()

# 정규 분포에서 표집후 평균을 저장
for (i in 1:n_sim){
    data <- rnorm(sample_size,m,s)
    X_bar <- mean(data) # 표본평균
    if((X_bar - 2*se < m) & (X_bar + 2*se > m)){
        X_bar_in_CI <- c(X_bar_in_CI,TRUE)
    }else{
        X_bar_in_CI <- c(X_bar_in_CI,FALSE)
    }
}

# 신뢰구간 안에 모평균이 포함된 비율
mean(X_bar_in_CI) 

## 계산값을 확인하면 95% 에 가까운 숫자가 나온다.
## 작성한 신뢰구간, (X_bar - 2*se,X_bar + 2*se)가 실제로 95%의 경우에 모평균을 포함한다는것을 확인해준다.

## 신뢰구간의 사용에 대한 팁
# - 지금까지 이야기한 모평균에 대한 95% 신뢰구간은 표본평균에 대해 대칭
#   따라서 양끝값을 더한뒤 2로 나누면 표본평균이 얼마인지 알수 있다. 160 + 180 = 340 / 2 = 170
# - 신뢰도(앞서 이야기한 95% 신뢰구간..)가 높아질 수록 구간의 길이는 길어진다.
#   높은 확률로 모평균을 잡아내려면 신뢰구간을 넓게 잡아야 그 안에 떨어질 확률이 높아질 것이다.
#   하지만, 신뢰구간의 길이가 길수록 신뢰구간 자체의 유효성은 떨어진다.
#   즉 신뢰가 높다고 해서 꼭 좋은것은 아니다.
# - 신뢰도로 추정할때 표본크기가 커질수록 신뢰구간의 길이는 짧아진다.(=표준오차가 적다)
#   수학적으로 신뢰구간의 길이는 표준오차에 비례하게 된다.
#   모평균에 대한 95%신뢰구간의 경우 대략(4 x 표준오차) 정도 된다. 그런데 표준오차 자체가 모표준편차를 sqrt(n)으로
#   나눈것이고, n이 커질수록 표본오차가 작아지기 때문에 결국 신뢰구간의 길이도 짧아진다.
#   직관적으로 표본 크기를 늘릴수록 신뢰구간의 길이는 짧아지게 되고 이는 더 정밀한 구간 추정을 할수 있다는 의미가 된다.
#   하지만 표본크기를 늘리는 것을 돈과 그밖의 자원 문제가 생기기 때문에 적당한 선에서 타협점을 찾을수 밖에 없다.


#### 부트스트랩
# 현대 통계학자들이 진보된 계산 기술을 받아들여 기존 수학 공식을 이용한 방식이 잘 통하지 않는 경우에도
# 폭넓게 적용할수 있는 보다 강력한 추론 기법을 의미
# 부트스트랩을 활용하면 앞에서 살펴봤던 신뢰구간 공식이든 뭐든 전혀 사용하지 않고,
# 컴퓨터 시뮬레이션 만으로도 평균을 추정하고 신뢰구간을 만들 수 있다.

## 부트스트랩 원리
# 앞서 관심을 가진 모집단, "20대 한국 남성"등 이런 모집단에 전수 자료애 접근할 수 없기 때문에 표본을 추출하고,
# 그것을 가지고 통계적 추정을 한다고 이야기 했다.
# 모집단의 대한 특정 가정하에서 표본을 계속 추출한다고 했을때 실제로 관측한 표본이 그중에 어느 위치에 있는지를 생각했다.
# 이런 발상을 전환하여 우리가 갖고 있는 표본 자체가 일종의 모집단인 것처럼 여길수는 없을까?
# 이 가정을 받아들이면 그 가상의 모집단에서 표본을 추출하여 평균을 계산하고 그것들을 모아 분포를 만들수 있다.
# 이것은 우리가 컴퓨터로 지금까지 해왔던 방식으로 쉽게 할수 있는 작업이다.
# 이것이 바로 "부트스트랩 방식"이다. 비복원추출이 원칙이다.

## 부트스트랩의 장점
# 추정이 필요한 수학공식을 모르거나 애초에 존재하지 않아도 관심이 있는 대상, 즉 평균이나
# 중앙값등에 대한 분포를 만들고 신뢰구간도 만들 수 있다.
# 앞서 시뮬레이션 방식을 이용하여 만들게 된다.
# 표본평균의 경우 표본평균이 중심극한정리에 의해 근사적으로 정규분포에 따른다는점을 이용하여 95% 신뢰구간을 만들때,
# 표본평균 +- (2 x 표준오차)공식을 사용했다.
# 이것은 중심극한정리가 적용되지 않는 대상 또는 구간 추정 공식을 모르는 대상에 대해서는 적용할수 없다.
# 부트스트랩을 사용하면 신뢰구간을 간편하게 얻을 수 있다.

## R에 내장된 데이터세트를 이용하여 부트스트랩 방식을 실습하자.
## 자료는 붓꽃(iris)
iris 
class(iris)  #data.frame
head(iris)
## 부트스트랩으로 모평균 추정하기(자료 : iris)
# iris는 데이터세트로 총 5가지 변수를 가지고 있다.
# 150개의 데이터가 각각 꽃잎(petal),꽃받침(sepal),각 길이(length)와 너비(width), 종(species)로 기록된 자료

# 여기서는 종이 setosa종의 꽃잎 길이의 모평균에 대해서 점추정과 구간 추정을 해본다.
# 꽃잎 길이 변수는 데이터세트 안에 Petal.Length라는 이름으로 저장되어있다.
# 추정 공식을 사용하면 모평균에 대한 점추정치는 표본평균과 같고, 구간 추정치는 이것에 (2 x 표준오차)를 더하거나 뺀 것으로
# 만들수 있다.
# 여기 예제는 sqrt(50)으로 나눈것과 같다.
# 여기서는 한가지 주의할 점이 있다. 앞에서 보았던 예제들은 모집단의 표준편차를 정확히 안다고 가정했다.
# 지금 setosa종의 모표준편차를 안다고 가정할수 없다. 그러므로 여기서는 표본에서 추정한 표준편차를 사용한다.
# 정규분포 추정 공식을 바로 이용할수 없다. 이렇게 되면 정규분포를 근사하는 분포인 t분포를 사용해야 한다.
# 하지만 t분포는 표본 크기가 충분히 크면 정규분포에 가까워지고, 이를 적용가능하지만 안쓰고, 정규분포 추정공식을 사용할것이다.

# 먼저, setosa종의자료만 따로 추출하기
# 이때 실행함수는 subset()을 사용한다. subset() : 부분집합을 만들어 저장하는 함수
y <- subset(iris, Species == 'setosa')$Petal.Length

# 이 값들의 평균을 쉽게 구할수 있다.(모평균의 대한 점추정치)
mean(y)  #1.462

# 다음으로 95% 신뢰구간을 만들어보자. 그럴려면 표준편차를 구해야한다.
# R은 표준편차(standard deviation)를 구하는 함수를 가지고 있다. 앞글자를 따서 sd()
sd(y)  # 표준편차 : 0.173664

# 이제 이 값을 당분간 모표준편차처럼 사용한다.
# 표준오차를 구하고, 신뢰구간을 만들려면 다음과 같이 처리한다.

n <- length(y)
ci_lower <- mean(y) - 2 * sd(y) / sqrt(n)
ci_upper <- mean(y) + 2 * sd(y) / sqrt(n)
print(ci_lower)  # 1.41288
print(ci_upper)  # 1.51112

### 이제 모평균에 대한 구간 추정 공식을 모른다고 치고, 부트스트랩 방식으르 추정한다!!!(중요*****)
## 앞에서 부트스트랩은 가상의 모집단인 표본에서 반복 추출하는 방식이기 때문에 이를 위한 시뮬레이션 코드를 작성해야한다!!!!!(중요*****)

n_sim <- 10000
means <- c()
for (i in 1:n_sim){
    bs_sample <- sample(y,length(y),replace = T)  #부트스트랩은 표본 길이만큼 복원추출을 한다는게 중요하다!
    sample_mean <- mean(bs_sample)
    means <- c(means,sample_mean)
}

head(means,12L)

# 여기서 중요한 것은 sample이다.
# 첫번째 입력값인 y로부터 무작위로 표본추출을 하는데, 표본의 크기가 두번째 입력값과 같다.
# 여기서 부트스트랩에서 중요한 것은 원자료에서 표본을 추출할때 정확히 같은 크기 만큼 추출해야 한다는점이 중요하다!!!
# 세번쨰로 replace=TRUE로 복원추출을 해야한다는것(필수)!!

## 이렇게 구해진 means를 이용하여 신뢰구간을 만들수 있다.
# 95% 신뢰구간은 값들을 정렬했을 때 가운데의 95%에 해당하는 값들의 범위를 의미한다.
# 이것은 상위, 하위 2.5%에 해당하는 값들을 찾으면 그것들로 신뢰구간 상한, 하한을 구할수 있다.
# 이때 사용하는 함수가 quantile()함수이다.
# 이 함수는 자료를 작은것부터 큰 것 순으로 나열할때 주어진 비율의 해당하는 값이 무엇인지 알려준다.

quantile(means,.025)  # 하위 2.5%    # 구간 추정
quantile(means,.975)  # 상위 2.5%    # 구간 추정

# 결과적으로 95% 신뢰구간인 1.41, 1.51과 거의 일치한다.
# 부트스트랩은 수학적인 공식을 전혀 사용하지 않고, 오로지 컴퓨터와 시뮬레이션의 힘으로 값을 추정했다는 것이다.

## t분포(모표준편차를 모를때 표준정규분포 대신에 사용하는 일종의 근사)
# t분포는 표준정규분포와 매우 비슷하다. 종형 모양의 가깝고0에 대해 대칭적이지만 분포 끝부분의 더 많은 자료가 흩어져 있는게 특징이다.
# 이는 꼬리의 두께는 자유도(degree of freedom)에 의해 결정되고 정규분포가 평균과 표준편차 두개의 값으로 결정되는것과 달리
# t분포는 자유도만으로 결정된다.
# 자유도는 낮을 수록 꼬리가 두꺼워지고, 높을수록 얇아져 t분포는 결국 표준정규분포에 가까워진다.
# t분포의 자유도는 표본 크기에서 1을 뺀것 즉 (n - 1)과 같다.
# 이것을 사용하여 다시 95%구간을 추정할수 있다.
# t분포의 상한과 하한을 구하기 위해서 qt()를 사용한다.

y <- subset(iris, Species == 'setosa')$Petal.Length
n <- length(y)

c(mean(y) + qt(.025,df=n-1)*sd(y)/sqrt(n),mean(y) + qt(.975,df=n-1)*sd(y)/sqrt(n))

#    상한       하한
# 1.412645 1.511355

## 부트스트랩으로 모표준편차 추정하기
# 추정공식을 아직 모르는 대상에 대해서 구간 추정하는것을 확인한다. 모표준편차....


y <- subset(iris, Species == 'setosa')$Petal.Length

n_sim <- 10000
sds <- c() 

for (i in 1:n_sim){
    bs_sample <- sample(y, length(y),replace = TRUE)
    sample_sd <- sd(bs_sample)
    sds <- c(sds,sample_sd)

}
c(quantile(sds,.025),quantile(sds,.975))

## 구간 추정 공식을 이용한 결과를 확인한다. 모표준편차에 대한 구간 추정 공식을 생략
sqrt(var(y)*(n-1) / qchisq(.975,n-1))
sqrt(var(y)*(n-1) / qchisq(.025,n-1))

## 공식에 의한 값은 실제로 부트스트랩을 사용한 경우와 비교했을때에 큰 차이가 나지 않는다.
# 이는 각종 수학적 가정과 표본크기등의 문제 때문에 복잡하니 생략한다.
# 중요한것은 구간 추정법을 모르는 대상도 점추정법만 알면 복원추출을 통해 구간 추정을 할수 있다는 점이다.
# 이게 바로 부트스트랩을 사용하는 이유이다.

## 통계적 가설 검정
# 과학자들이 매일 통계적 가설 검증을 활용한다. 새로운 코로나19 백신이 개발되어 백신의 효과가 있는지 알고싶다면,
# 이를 입증하기 위해서 백신을 접종한 사람과 그렇지 않은 사람들을 비교했을 때에 전자가 유의미하게 병에 걸릴 확률이 낮아야 한다.
# 두 집단에서 발병자료를 수집하고, 질병 발생률에 차이가 없다고 가정했을 때(백신의 효과가 없다고 가정 했을때)
# 일반적으로 관측될 만한 자료인지 아닌지 확인한다. 만약 수집된 자료가 백신이 효과가 없다는 가정하에 관측되기 매우 힘든
# 결과라면, 즉 백신을 맞은 집단에서 그렇지 않은 집단에 비해서 질병 발생률이 훨씬 낮다면 원래 가정인 "백신이 효과가 없다"
# 라는 주장을 기각하고 효과가 있다는 결론을 내린다.
# 그렇지 않고 자료가 두 집단 사이 차이가 없다고 가정 했을 때도 충분히 그럴듯 하다면 백신은 없다는 주장을 기각하지 못한다.

# 통계적 가설 검증에서는 "효과가 있다","차이가 있다" 등의 직접 입증하는 것이 아니라 그런 효과가 차이가 없다는
# 주장을 반박하는 방식으로 과학적 주장을 간접적으로 입증하는 방식으로 취약한다. "~~~없다"는 주장,
# 즉 과학자가 자료를 통해서 기각하려는 주장을 통계학에서 "영가설"이라고 부른다. "귀무가설"이라고도 한다.
# 영가설을 기각하기 위한 통계학에서 사용하느 일반적 도구는 P값 (p-value)이지만 생략한다.
# 대신 지금까지 살펴본 신뢰 구간을 바탕으로 이야기 한다.
# 가설 검증에서는 p값을 사용하든 신뢰구간을 사용하든 똑같은 결과가 나온다는 것을 수학적으로 증명할수 있지만, 하지 않는다.

# iris자료를 통해서 setosa종의 Petal.Length의 모평균에 대한 추정치가 95%신뢰도에서 [1.41,1.51]것을 확인했다.
# 뒤집어서 생각하면 이 신뢰구간을 이 구간밖에 있는 값을 별로 그럴듯 하지 않다는 이야기이다.
# 즉 Petal.Length 평균 값이 1.3이라는 주장은 이 신뢰구간에 비추어 생각해 볼때 별로 그럴듯한 가설이 아니다.
# 모평균이 1.3이라는 주장은 기각할수 있는 것이 된다. 모평균이 1.3이라는 주장이 바로 영가설이 된다.
# 모평균이 1.5는 신뢰구간 안에 들어있기 때문에 모평균이라고 주장할수 있다.

# 여기서 알수 있는 것은 신뢰구간의 성질을 알 수 있다.
# 모평균1.3은 신뢰구간 95%확률 영역안에 없다는 말이다. 만약 모평균이 1.3인 상황에서 만들어졌다면 95%신뢰구간안에 포함되어 있었겠지만
# 그러지 않다는 점이다. 95% 값이 옳은데도 불구하고 5%의 확률로 그릇되게 기각될 수 있다는 것을 말한다.(신뢰도 95%의 의미)
# 이렇게 영가설이 옳은데도 자료의 생성과정에 개입되는 우연성 때문에 영가설이 잘못 기각되는 상황을 우리는 "1종오류(type 1 error)"라고 부른다.
# 이것은 가설검증에서 사용되는 신뢰구간의 신뢰도를 100%에서 뺀것과 같다.

### 부트스트랩 신뢰구간을 활용한 가설검증
# 앞에 iris 데이터 세트에서 versicolor종과 virginica종의 Petal.Length 모평균 사이에 차이가 있는지 검증해본다.
# 이를 입증하기 위해서 실제로 관측된 두 종의 Petal.Length 자료가 영가설하에 그럴듯한지 판단해야 한다.
# 만약 답이 "그렇지 않다"면 영가설은 기각하고 모평균이 다르다는 결론을 낼수 있다.

# 프로그래밍 구현에서 두 종의 Petal.Length의 모평균이 같다면 두종에서 각각 표본을 뽑아서 계산한 표본평균들 간의 차이도 대체로 0에 가까울 것이다.
# 그리고 이를 반복적으로 해서 모평균에 차이에 대한 신뢰구간을 어떻게든 만들면 대부분의 신뢰구간은 0을 포함할것이다.
# 문제는 모평균의 차이에 대한 신뢰구간을 만드는 방법이나 수학 공식에 대해서 전혀 이야기 되고 있지 않다는 것이다.
# 이런 상황에선 부트스랩을 이용하여 극복해야한다.
# 두 종의 자료를 iris에서 각각 원래 표본과 같은 크기의 표본을 복원 추출하고, 표본평균을 각각 계산한 뒤에 그 차이를 모을거다.
# 그리고 신뢰구간을 작성옥 0이 그 구간안에 포함되는지 확인하면 된다.

# 각각의 자료를 추출
x <- subset(iris,Species =='virginica')$Petal.Length
y <- subset(iris,Species =='versicolor')$Petal.Length

iris
# 시뮬레이션 
n_sim <- 10000

# 두 평균의 차이
difs <- c()

# 시뮬레이션 작업
for (i in 1:n_sim){
    # 표본 추출
    bs_virginaca <- sample(x,length(x),replace = TRUE)
    bs_versicolor <- sample(y,length(y),replace = TRUE)
    # 차이 값(표본평균 간 차이값)
    mean_dif = mean(bs_virginaca) - mean(bs_versicolor)
    difs = c(difs, mean_dif)

}

c(quantile(difs,.025), quantile(difs,.975))
# 모평균의 차이에 대한 95% 부트스트랩 신뢰 구간은 대략 [1.10, 1.49]
# 그리고 이 신뢰구간은 0을 포함하지 않기 때문에 두 종의 Petal.Length의 모평균이 같다는 영가설은 95%신뢰 수준에서 기각할수 있다.

c(quantile(difs,.005), quantile(difs,.995))
# 모평균의 차이에 대한 99% 부트스트랩 신뢰 구간은 대략 [1.03, 1.53]
# 이결과는 결국 신뢰구간에 0이 포함하지 않기 때문에 두 종의 Petal.Length의 모평균이 같다는 영가설은 역시 99%신뢰 수준에서 기각할수 있다.

### 예측정확도의 역설

