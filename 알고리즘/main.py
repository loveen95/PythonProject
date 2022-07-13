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
#      조건 - 존재하지 않으면 None을 리턴하고, 이진 탐색은 정렬된 리스트만 사용 가능함.
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