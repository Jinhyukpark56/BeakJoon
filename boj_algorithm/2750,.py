n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))
    
for j in range(1, len(arr)):
    key = arr[j]
    i = j-1
    while i >= 0 and arr[i] > key:
        arr[i+1] = arr[i]
        i -= 1
    arr[i+1] = key

for i in arr:
    print(i)