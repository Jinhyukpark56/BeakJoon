# (1)과 (2)의 위치에 들어갈 세 자리 자연수를 입력받습니다.
num1 = int(input())
num2 = int(input())

# (3)부터 (6)까지의 값을 계산합니다.
result3 = num1 * (num2 % 10)  # (3) 위치 값 계산
result4 = num1 * (num2 // 10 % 10)  # (4) 위치 값 계산
result5 = num1 * (num2 // 100 % 10)  # (5) 위치 값 계산
result6 = num1 * num2  # (6) 위치 값 계산

# 계산된 결과를 출력합니다.
print(result3)
print(result4)
print(result5)
print(result6)