# p.103
print(273)      # print() vs console.log() vs system.out.println()
print(52.273)

# 타입 확인, type(자료) 
print(type(52)) # type() : 자료형을 알려주는 함수
print(type(52.273))

# 지수 표현식 : 10의 거듭제곱으로 표현하는 방법 / 지수 승 표현 방법 / 자료e지수승
0.52273e2 # 52.273
0.52273e-1 # 0.052273

# 연산자 
print(5+7) # 12
print(5-7) # 2 
print(5*7) # 35
print(15/4) # 0.7142857142857143
print(3//2) # 1 몫 연산자
print(5%7) # 5 나머지 연산자
print(2**3) # 8 거듭제곱 연산자
# pi : 3.141592653589793

# 사용자 입력, input(), 주의할 점 : 콘솔에 입력하는 구조로 무조건 *문자열*로 반환 된다.
input("인사말을 입력하세요 >")
 
string = input("인사말을 입력하세요 >")
print(string)

print(type(string)) # str

# 문자열을 숫자로 변환하기, Integer.parseInt() vs parseInt() vs int() , 사용처 : input, HTTP 문자열 통신
# 타입을 변환해야하는 이유 : 자료를 사용할 때 서로다른 타입간의 예외가 발생할 수 있다.
string_a = input("입력A >")
int_a = int(string_a) # 문자열을 정수로 변환하는 함수
print(type(int_a)) # int

string_b = int(input("입력B >")) # 밥먹기(공부하기()) : 공부하고 밥먹기
print(type(string_b)) # int

string_c = float(input("입력C >"))
print(type(string_c)) # float

# 숫자를 문자열로 바꾸기, 
pi = 3.141592
string_d = str(pi)
print(type(string_d)) # str

