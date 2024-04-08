T = int(input())  # 테스트 케이스의 개수 입력 받기

for case in range(1, T+1):
    A, B = map(int, input().split())  # A와 B 입력 받기
    C = A + B  # A와 B의 합 계산
    print("Case #{}: {} + {} = {}".format(case, A, B, C))  # 결과 출력