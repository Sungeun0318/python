
# 비교 연산자 : ==, !=, >, <, >=, <=
# 문자열 비교 : 가나다/abc 순으로 아퓨에 있는 것이 작은 값
print("가방" == "가방") # True
print("가방" != "하마") # True
print("가방" > "하마") # False # '가' 유니코드로 표현 했을 때 '하'보다 작은 값이기 때문에 False


# 범위 논리
x = 25
print(10 < x < 30) # True
print(40 < x < 60) # False

# 불 연산자 : and/이면서/그리고, or/또는/이거나, not/부정/반대
print(not True) # False
print(True and True) # True
print(True and False) # False
print(True or False) # True

# 파이썬 조건문/분기문, if 조건 : 
number = int(input("정수를 입력하세요: "))

#
if number > 0:
    print("양수입니다.") # java와 다르게 들여쓰기 이용하여 실행문 구분한다.


if number < 0:
    print("음수입니다.")


if number == 0:
    print("0입니다.")






  