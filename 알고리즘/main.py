# 알고리즘 # 

# 팰린드롬(palindrome) : "토마토","기러기"처럼 거꾸로 읽어도 똑같은 단어 
# 문제) 문자열 word가 팔린드롬인지를 확인하는 함수 is_palindrome를 작성하시오.
#       조건 - 반드시 for문을 사용할 것,(append,insert메소드 del함수)작성 금지 
def is_palindrome(word):
  list_word = list(word)    
  for i in range(len(word)//2):
    if list_word[i] == list_word[-i-1]: 
      continue
    else:
      return False
  return True 
    
print(is_palindrome("racecar")) # True
print(is_palindrome("stars")) # False 
print(is_palindrome("토마토")) # True
print(is_palindrome("kayak")) # True
print(is_palindrome("hello")) # False  

# 선형 탐색 : 왼쪽부터 처음부터 끝까지 순서대로 하나씩 탐색 
# 문제) 선형 탐색 알고리즘을 이용해서 어떤 원소가 리스트 안에 포함 되어 있는지 확인 하는 함수를 작성하시오.
#      조건 - 0번 인덱스부터 순서대로 하나씩 확인해서 리스트 안에 포함 되어 있으면 그 위치(인덱스)를 리턴,
#            존재 하지 않는 값이면 None을 리턴   
def linear_search(element, some_list):
  for i in range(len(some_list)):
    if element == some_list[i]:
      return i
    else: 
      continue
  return None 
print(linear_search(2, [2, 3, 5, 7, 11])) # 0
print(linear_search(0, [2, 3, 5, 7, 11])) # None
print(linear_search(5, [2, 3, 5, 7, 11])) # 2
print(linear_search(3, [2, 3, 5, 7, 11])) # 1
print(linear_search(11, [2, 3, 5, 7, 11])) # 4       

# 이진 탐색 : 중간으로 나눠서 해당하지 않는 값을 절반씩 버리면서 탐색하는 방법(정렬된 리스트만 가능)  
# 문제) 이진 탐색 알고리즘을 이용하여 어떤 원소가 리스트 안에 몇번째 인덱스에 위치하는지 탐색하시오.
#      조건 - 존재하지 않으면 None을 리턴하고, 이진 탐색은 *정렬된 리스트*만 사용 가능함.
def binary_search(element, some_list):
  start_index = 0
  end_index = len(some_list) - 1
    
  while start_index <= end_index:
    midpoint = (start_index + end_index) // 2
    if some_list[midpoint] == element:
      return midpoint
    elif some_list[midpoint] > element:
      end_index = midpoint - 1
    else:
      start_index = midpoint + 1
  return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))  

# 정렬(Sorting) : 리스트의 원소들을 특정 순서로 정리하는 것, 알고리즘의 기초!!
# <정렬의 종류>
# 선택 정렬(Selection Sort) : 선택된 값과 나머지 데이터중에 비교하여 알맞은 자리를 찾는 알고리즘(각 위치에 어떤 값이 들어갈지 찾는다.)
# 삽입 정렬(Insertion Sort) : 정렬이 필요한 요소를 뽑아내어 이를 다시 적당한 곳으로 삽입하는 알고리즘(각 값이 어떤 위치에 들어갈지 찾는다.)
# 퀵 정렬(Quick Sort) : 데이터 집합 내에 임의의 기준(pivot)값을 정하고 해당 피벗으로 집합을 기준으로 두개의 부분 집합으로 나눈다. 한쪽 부분에는 피봇값보다 작은 값들만, 
#                     다른 한쪽은 큰 값들만 넣고 더이상 쪼갤 부분 집합이 없을 때까지 각각의 부분 집합에 대해 피벗/쪼개기를 재귀적으로 사용 
# 힙 정렬 : 트리 기반으로 최대 힙 트리 or 최소 힙 트리를 구성해 정렬을 하는 방법(완전 이진 트리여야 함)
# 버블 정렬(Bubble Sort) : 거품이 수면으로 올라오는 듯 인접한 두수를 비교하여 오름차순 or 내림차순으로 정렬 
# 병합 정렬(Merge Sort) : 둘 이상의 부분 집합으로 가르고, 각 부분집합을 정렬한 다음 부분집합들을 다시 정렬된 형태로 합치는 방식
# 기수 정렬(Radix Sort) : 낮은 자리수부터 비교해가며 정렬한다. 비교연산을 하지 않아 빠르지만, 또 다른 메모리 공간을 필요로 한다는게 단점이다. 
#                       데이터 전체크기에 기수 테이블의 크기만한 메모리가 더 필요하다.


# 알고리즘의 평가
# 평가의 두 기준 - 시간과 공간
# 시간 복잡도(Time Complexity) : 데이터가 많아질수록 걸리는 시간이 얼마나 급격히 증가하는지를 나타낸다.
# 거듭제곱(Exponentiation) : 2^0은? ==> 2^1/2 == 2/2 == 1, 2^-1제곱은? ==> 2^0/2 == 1/2 
# 로그 : 거듭제곱의 반대 개념
# 점근 표기법(Big-O) : 소요 시간 20n + 40의 점근 표기법은? ==>  O(n) 
#                 : 소요시간 2n^2 + 8n + 157의 점근 표기법은? ==> O(n^2)
#                 - 즉 n의 가장 영향력을 많이 받는 숫자만 남기면서 표기한다. n이 가장 크다고 가정한다.
#                 - 점근 표기법으로 알고리즘을 평가 할때 주의해야 할점 : 주로n을 사용하지만 n에 특별한 의미를 둘 필요는 없다.
#                   또한 코드의 모든 줄은 O(1)이 아니다. sort나 sorted메소드를 사용하면 O(n lg n)의 정렬이 이루어지고, 
#                   리스트에서 in 키워드를 통해 값의 존재 여부를 확인하면 내부적으로 O(n)의 선형 탐색이 이루어진다.
#                   그 외 리스트의 길이를 n이라고 가정할때 인덱싱, append(), len()은 O(1)을 사용하고, 
#                   reverse(), insert(index, element), del, min & max등은 O(n)로 동작한다. 
#                   Dictionary에서 값 찾기, 값 넣어주기/덮어쓰기, 값 삭제등은 O(1)로 동작한다.
# 주요 시간 복잡도 총정리
# 선형 탐색 알고리즘 O(n), 이진 탐색 알고리즘 O(lg n)
# 이 중 O(1), O(lg n), O(n), O(n lg n), O(n^2), O(n^3)가 많이 사용된다. 
# O(1)은 인풋의 크기가 소요 시간에 영향이 없다는 뜻, 반복문이 없으면 대체로 O(1)이다. 
# O(n)은 반복문이 있고, 반복되는 횟수가 인풋의 크기와 비레하면 일반적으로 O(n)이다. n/2번 반복한다면 O(1/2n)이지만, 1/2를 버려서 O(n)이 된다.
# O(n^2)은 반복문 안에 반복문이있고, 두 반복문 다 인풋의 크기에 비례하는 경우, O(n^2)라고 한다.
# O(n^3)은 인풋의 크기에 비례하는 반복문이 세번 충첩되면 O(n^3)가 된다.
def print_powers_of_two(n):
  i = 1
  while i < n: 
    print(i) 
    i = i * 2
# n이 128이면 i가 1일때부터 2,4,8,16,32,64 총 7번 실행
def print_powers_of_two_1(n):
  j = n
  while j > 1:
    print(j)
    j = j / 2 
# j가 128일때부터 64,32,16,8,4,2까지 총 7번 실행 
# 두 경우 모두 O(lg n)이다.

# O(n lg n)은 O(n)과 O(lg n)이 겹쳐진 것이다.
def print_powers_of_two_repeatedly(n):
  for i in range(n): # 반복 횟수: n에 비례
    r = 1
    while r < n: # 반복 횟수 : lg n에 비례
      print(i, r)
      r = r * 2
# while문이 for문 안에 중첩되어 있기 때문에 위 코드의 시간 복잡도는 O(n lg n)이다.

# 공간 복잡도(Space Complexity): 인풋 크기에 비례해서 알고리즘이 사용하는 메모리 공간을 나타낸다.
#                             물론 공간 복잡도도 점근표기법으로 표현할수 있기 때문에 간편하게 Big-O표기법을 사용할수 있다.
def product(a, b, c):
  result = a * b * c
  return result 
# 파라미터 a,b,c가 차지하는 공간을 제외하면 추가적으로 변수 result가 공간을 차지한다. 
# result가 차지하는 메모리 공간은 인풋과 무관하기 때문에 함수 product의 공간 복잡도는 O(1)이다.    

def get_every_other(my_list):
  every_other = my_list[::2]
  return every_other 
# 파라미터 my_list가 차지하는 공간을 제외하면 every_other가 공간을 차지한다. 
# 리스트 every_other에는 my_list의 짝수 인덱스 값들이 복사돼서 들어간다. 약 n/2개의 값이 들어가는데, 
# O(n/2)는 O(n)으로 값을 나타낼수 있기 때문에, get_every_other 함수의 공간 복잡도는 O(n)이다.

def largest_product(my_list):
  products = []
  for a in my_list:
    for b in my_list:
      products.append(a * b) 
# 파라미터 my_list가 차지하는 공간을 제외하면 변수 products, a, b가 공간을 차지한다.
# a와 b는 그냥 정수 값을 담기 때문에 O(1)이다.  
# products에는 my_list에서 가능한 모든 조합의 곱이 들어간다. 총 n^2의 값이 들어간다. 
# 즉, 함수 largest_product의 공간 복잡도는 O(n^2)이다. 


# 유용한 파이썬 기능 정리 #
# str
my_str = str(257138)
print(my_str)                # => 257138
# str함수를 사용하면 숫자를 문자열로 바꿀수 있다. 
# 시간복잡도는 O(log n)이 된다.  

# append 메소드를 사용하면 리스트 끝에 새로운 값이 추가된다. 시간 복잡도는 O(1)이다.
# insert, del, index, reverse는 모두 O(n)이다.  

# sort, sorted
my_list = [7, 5, 2, 3, 6]
print(sorted(my_list))       # => [2, 3, 5, 6, 7]
print(my_list)               # => [7, 5, 2, 3, 6]

my_list.sort()
print(my_list)               # => [2, 3, 5, 6, 7]
# sort메소드와 sorted함수는 리스트를 정렬시켜 준다. 
# sorted함수를 사용하면 정렬된 새로운 리스트가 리턴되고, sort메소드는 그 리스트 자체를 정렬시켜 준다는 차이점이 있다.
# 두 메소드의 시간복잡도는 모두 O(n lg n)이다. 

# slicing 
my_list = [7,5,2,3,6]
print(my_list[1:4])          # => [5, 2, 3]
print(my_list[:4])           # => [7, 5, 2, 3]
print(my_list[1:])           # => [5, 2, 3, 6]
print(my_list[:])            # => [7, 5, 2, 3, 6]
print(my_list[::2])          # => [7, 2, 6]
# 슬라이싱의 시간 복잡도는 슬라이싱의 범위 길이에 비례한다.
# my_list[a:b]를 하면 시간 복잡도는 O(b-a)이다. 

# len
my_list = [7, 5, 2, 3, 6]
my_dict = {'a': 2, 'b': 3, 'c': 5, 'd': 7}
my_string = 'hello world'

print(len(my_list))          # => 5
print(len(my_dict))          # => 4
print(len(my_string))        # => 11
# len함수를 사용하면 리스트, 사전, 문자열 등의 길이가 리턴된다. 시간 복잡도는 O(1)이다.







