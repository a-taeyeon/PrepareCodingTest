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

''' 답안 예시 '''
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