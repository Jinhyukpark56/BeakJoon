n = int(input())
ans = [1, 2] * (n//2)
if n%2:
	ans += [3]
print(*ans)