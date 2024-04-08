a = int(input()) 

for i in  range(a): 
    
    l = list(map(str, input().split())) 
    
    result = eval(l[0])

    for j in range(len(l)):
        if l[j] == "@":
          result = result * 3
        elif l[j] == "%":
          result = result + 5
        elif l[j] == "#":
          result = result -7
    print("%0.2f" %result)
