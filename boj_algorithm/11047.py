# 그리디 알고리즘 유형

# 1. 계산대 안에 있는 돈의 수와 거슬러 줄 돈을 구한다.
n,k=map(int,input().split())

# 2. 게산대에 있는 화폐들을 리스트의 형태로 입력받는다.

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

# coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

# 3. 만약 '계산대 안에 있는 화폐'보다 '거슬러 줄 돈'이 크다면
# 돈을 거슬러 준다.
answer = 0
for coin in coins:
    if k >= coin:
        answer += k // coin # 몫만큼 더하기
        k %= coin # 나머지 할당
        if k <= 0: # 만약 k가 0이면 반복문 탈출.
            break

print(answer) # 거슬러 준 동전 + 화폐의 수
        
    