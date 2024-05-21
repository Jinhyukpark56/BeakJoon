# lambda 함수의 기본 형식 : lsit.sort(key=lambda x:(정렬 대상) or sorted(list.key = lambda x:(정렬 대상)))

n = int(input())
students = []

for _ in range(n):
    students.append(input().split())
    
students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int([3]), x[0]))

for student in students:
    print(student[0])
