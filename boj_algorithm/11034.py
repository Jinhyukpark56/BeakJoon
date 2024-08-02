while True:
    try:
        lst = list(map(int,input().split(" ")))
        print(max(lst[1]-lst[0],lst[2]-lst[1])-1)
    except EOFError:
        break