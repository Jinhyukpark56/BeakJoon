# 그리디 알고리즘 유형 

n = int(input())

k = 0
while n >= 0 :
    if n % 5 == 0: # 5의 배수이면
        k +=(n // 5)# 5로 나눈 몫을 구해 정수를 만듬
        print(k)
        break
    n -= 3
    k += 1# 5의 배수가 될 때까지 n-3, k+1 (n=설탕,k=설탕봉지)
else :
    print(-1)