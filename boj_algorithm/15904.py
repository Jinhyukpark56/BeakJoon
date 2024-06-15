s = input().replace(' ','')
ans = 'UCPC'
index = 0
for i in s :
    if i == ans[index]:
        index += 1
    if index == 4:
        print('I love UCPC')
        break
else:
    print('I hate UCPC')