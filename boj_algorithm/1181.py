n= int(input())
lst = [str(input()) for i in range(n)]
    
lst = list(set(lst))
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)
    