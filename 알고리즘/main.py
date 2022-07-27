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
# 거듭제곱(Exponentiation) : 
# 로그 : 거듭제곱의 반대 개념 

