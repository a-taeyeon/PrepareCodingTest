n, m = map(int, input().split())

col_min = list()
for i in range(n):
  cards = list(map(int, input().split()))
  col_min.append(min(cards))

print(max(col_min))


# min()함수를 이용하는 답안 예시
'''
n, m = map(int, input().split())

result = 0
for i in range(n):
  data = list(map(int, input().split()))
  #현재 줄에서 '가장 작은 수' 찾기
  min_value = min(data)
  #'가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)
'''

# 2중 반복문 구조를 이용하는 답안 예시
'''
n, m = map(int, input().split())

result = 0
for i in range(n):
  data = list(map(int, input().split()))
  #현재 줄에서 '가장 작은 수' 찾기
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)
    #'가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)
'''