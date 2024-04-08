T = int(input())  # 테스트 케이스의 개수 입력 받기

for case in range(1, T+1):
    A, B = map(int, input().split())  # A와 B 입력 받기
    print("Case #{}: {}".format(case, A + B))  # 결과 출력