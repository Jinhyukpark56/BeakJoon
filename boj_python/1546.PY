n = int(input())

num = list(map(int, input().split()))
avg_list = []
for i in range(n):
    num_max = max(num)
    avg_list.append((num[i] / num_max) * 100)

avg_sum = sum(avg_list)
avg_real = avg_sum / n
print(avg_real)
        
