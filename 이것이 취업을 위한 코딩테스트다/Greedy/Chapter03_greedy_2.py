n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
print(data)

first = data[n - 1]
second = data[n - 2]

sum = 0
cnt = 0
for i in range(m):
  if cnt == 3:
    sum += second
    cnt = 0
  else: 
    sum += first
  cnt += 1

print(sum)

''' 단순하게 푸는 답안 예시 '''
# 이 방법은 M의 크기가 100억 이상처럼 커진다면 시간 초과 판정 받음
'''
n, m, k = map(int, input().split())
data = list(map(int, input.split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
  for i in range(k): # 가장 큰 수를 k번 더하기
    if m == 0: # m이 0이라면 반복문 탈출
      break
    result += first
    m -= 1 # 더할 때마다 1씩 빼기

  if m == 0: # m이 0이라면 반복문 탈출
    break

  result += second # 두 번째로 큰 수를 한 번 더하기
  m -= 1 # 더할 때마다 1씩 빼기

print(result) # 최종 답안 출력
'''

''' 가장 효율적인 답안 '''
# 반복되는 수열에 대해서 파악
'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수 계산 (수열)
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)
'''