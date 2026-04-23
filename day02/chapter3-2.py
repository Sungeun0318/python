# if ~ else
number = int(input("숫자를 입력하세요: "))
if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")


# if ~ elif ~ elif ~ else, java : else if
number = int(input("숫자를 입력하세요: "))
if number % 2 == 0:
    print("짝수입니다.")
elif number % 2 == 1:
    print("홀수입니다.")
else:
    print("짝수/홀수 모두 아닙니다.")

# 조건 3개 이상 : [1] if if vs [2] if elif
x=int(input("x값을 입력하세요: "))
y=int(input("y값을 입력하세요: "))
if x > 4:
    if y > 2:
        print(x * y)
else:
    print("조건 2")