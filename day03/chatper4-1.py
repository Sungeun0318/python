
# 리스트란? 여러 자료덜을 모아 하나의 자료로 구성 
# [, , , ,]
# 인덱스란? 자료가 저장된 순서, 0번 시작

list_a = [273, 32, "문자열", True]
print(list_a[0]) # 273
# 슬라이싱
print(list_a[1 : 3]) # [32, '문자열']
# print(list_a[4]) # 없는 인덱스는 에러 발생 // print(list_a[4]) # IndexError: list index out of range

# 요소값 변경
list_a[1] = "변경값"
print(list_a) # [273, '변경값', '문자열', True]

# 뒤에서부터 요소 선택
print(list_a[-2]) # 문자열

# 리스트 안에 리스트 사용 가능
print(list_a[2][1]) # 자


list_a[1] = ['변경값', '변경값2']
print(list_a[1][1]) # 변경값2

# 리스트 연산
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# [1] + 연결
print(list_a + list_b) # [1, 2, 3, 4, 5, 6]

# [2] * 반복 
print(list_a * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# [3] len 길이
print(len(list_a)) # 3

# 리스트에 요소 추가
# [4] 요소 추가하기, .append(자료)
list_a.append(4)
print(list_a) # [1, 2, 3, 4]

# [5] 중간에 요소 추가하기, .insert(인덱스, 자료)
list_a.insert(1, 1.5)
print(list_a) # [1, 1.5, 2, 3, 4]

# 리스트 요소 제거 
list_a = [0, 1, 2, 3, 4, 5]

# [6] del 리스트명[인덱스]
del list_a[1]
print(list_a) # [0, 2, 3, 4, 5]

# [7] 리스트명.pop(인덱스)
list_a.pop(2)
print(list_a) # [0, 2, 4, 5]
list_a.pop() # 인덱스 생략 시 마지막 요소 제거
print(list_a) # [0, 2, 4]

# [*] 슬라이싱 이란? 인덱스로 구성된 자료들(문자열/리스트)의 요소 선택 기능
# [시작인덱스 : 끝인덱스 : 단계]
print(list_a[:: -1]) # [4, 2, 0] 역순으로 출력
print(list_a[0 :: 2]) # [0, 4] 0번부터 마지막 인덱스까지 2칸씩 출력

# [8] 리스트명.remove(자료), 해당 자료가 존재하면 삭제
list_a.remove(2)
print(list_a) # [0, 4]

# [9] 리스트명.clear(), 리스트 안의 모든 요소 제거
list_a.clear()
print(list_a) # []

# [10] .sort() 리스트 정렬, .sort(reverse=True) 내림차순 정렬
list_a = [52, 273, 103, 32]
list_a.sort()
print(list_a) # [32, 52, 103, 273]
list_a.sort(reverse=True)
print(list_a) # [273, 103, 52, 32]

# [11] in, 내부에 있는지 확인
print(103 in list_a) # True
print(100 in list_a) # False
print(103 not in list_a) # False
print(100 not in list_a) # True 


number = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in number:
    if len(str(number)) == 3:
        print(f"{number}는 세 자리 수입니다.")
    elif len(str(number)) == 2:
        print(f"{number}는 두 자리 수입니다.")
    else:
        print(f"{number}는 한 자리 수입니다.")


# for number in number:
#     if number % 2 == 0:
#         print(f"{number}는 짝수입니다.")
#     else:
#         print(f"{number}는 홀수입니다.")


# 리스트와 반복문
# for 반복변수 in 반복할 수 있는 자료 : 
#            코드 

리스트명 = [273, 32, 103, 57, 52]

for 요소 in 리스트명:
    print(요소)

for 요소 in "안녕하세요" : 
    print(요소)


# 중첩 리스트 # 중첩 반복문 # 2차원 리스트
list_of_list = [[1, 2, 3],     # 1행 3열
          [4, 5, 6, 7],  # 2행 4열
          [8, 9]         # 3행 2열
]       
for row in list_of_list: 
    print(row) # 각 행 출력
    for col in row: 
        print(col) # 각 열 출력
         

# 전개 연산자, * 
list_a = [1, 2, 3]
print(list_a) # [1, 2, 3] 리스트 그 자체 
print(*list_a) # 리스트 그 자체가 아닌, 1 2 3 # 리스트는 첫번째 인덱스를 참조한다.
print(1, 2, 3) # 1 2 3

print([list_a, list_a]) # [[1, 2, 3], [1, 2, 3]] 리스트를 요소로 하는 새로운 리스트 생성
print([*list_a, *list_a]) # [1, 2, 3, 1, 2, 3] 리스트를 전개하여 새로운 리스트로 생성


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[(number-1) % 3].append(number)

print(output)












