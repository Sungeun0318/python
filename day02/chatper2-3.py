# 변수 : 하나의 자료 저장하는 (메모리) 공간
pi = 3.141592 # = 같다 의미가 아니라 우변의 값을 좌변에 넣겠다.

print(pi) # 변수 참조, 변수가 갖는 자료 반환
print(pi + pi)

print(pi + "입니다.") # 예외가 발생한다.
print(pi, "입니다") # 연결

# 타입의 유연성 = 동적 타입, 단점 : 타입 식별이 어렵다.
# 자바 또는 C언어, int pi = 3
# 파이썬, pi = 3 

# 복합 대입 연산자
number = 100
number += 10
print(number) # 110
number -= 10
print(number) # 100
number *= 10
print(number) # 1000
number /= 10
print(number) # 100.0
number //= 10
print(number) # 10.0
number %= 3
print(number) # 1.0
number **= 3
print(number) # 1.0