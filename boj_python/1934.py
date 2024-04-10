n = int(input())
for _ in range(n):
    k =[]
    a,b = map(int, input().split())
    for i in range(1,min(a,b)+1):
        if a%i == 0 and b%i == 0:
            k.append(i)
    print(a*b//max(k))