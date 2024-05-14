n,k = map(int,input().split())

sores = list(map(int,input().split()))

sores.sort(reverse=True)

print(sores[k-1])