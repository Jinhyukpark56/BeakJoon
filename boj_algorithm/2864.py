a,b = input('').split()

a1 = a.replace('6','5')
b1 = b.replace('6','5')

a2 = a.replace('5','6')
b2 = b.replace('5','6')

print(int(a1)+int(b1), int(a2)+int(b2))