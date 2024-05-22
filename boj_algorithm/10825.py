# lambda 함수의 기본 형식 : lsit.sort(key=lambda x:(정렬 대상) or sorted(list.key = lambda x:(정렬 대상)))

N = int(input()) ; arr = []

for _ in range(N):
    a,b,c,d = list(map(str,input().split()))
    arr.append( [a, int(b),int(c),int(d)])

arr.sort(key = lambda x : (-x[1] , x[2],-x[3],x[0]) )

for i in arr :
    print(i[0])
