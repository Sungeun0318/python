
# 문자열의 format() 함수, 자바의 System.out.printf("%s", 10)
string_a = "{}".format(10)
print(string_a, type(string_a))

format_a = "{}만 원".format(5000)
print(format_a)
format_b = "{} {} {}".format(1, "유재석", True)
print(format_b)

# 특정 칸에 출력하기, {:자릿수d} : 정수, {:0자릿수d}, {:자릿수f} : 실수, {:자릿수s} : 문자열
output_a = "{:5d}".format(52) # {} 안에서 공백 주의 // 52
print(output_a)
output_b = "{:05d}".format(52) # 0으로 채우기
print(output_b)

# 기호 붙여 출력하기, {:+d}
output_c = "{:+d}".format(52)
print(output_c)
output_d = "{:+d}".format(-52)
print(output_d)


# 부동소수점 출력하기
output_e = "{:10f}".format(52.273)
print(output_e)
output_f = "{:+015f}".format(52.273) # +기호, 0으로 채움, 15자릿수, f 실수
print(output_f)
output_g = "{:15.3f}".format(52.2735) # .소수자릿수f
print(output_g)

# 의미없는 소수점 제거하기
output_h = "{:g}".format(52.0)
print(type(output_h))

# 대소문자 바꾸기 
a = "Hello Python"
print(a.upper()) # 대문자
print(a.lower()) # 소문자
print(a.swapcase()) # 대소문자 바꾸기
print(a.capitalize()) # 첫 글자만 대문자, 나머지는 소문자
print(a.title()) # 각 단어의 첫 글자만 대문자

# 공백 제거하기
b = "   Hello Python   "
print(b.strip()) # 양쪽 공백 제거
print(b.lstrip()) # 왼쪽 공백 제거
print(b.rstrip()) # 오른쪽 공백 제거

# 문자열 찾기
out_a = "안녕안녕하세요".find("안녕")
print(out_a) # 가장 먼저 나오는 "안녕"의 인덱스 반환
out_b = "안녕안녕하세요".rfind("안녕")
print(out_b) # 가장 나중에 나오는 "안녕"의 인덱스 반환
out_c = "안녕안녕하세요".find("잘가")
print(out_c) # 찾는 문자열이 없으면 -1 반환

print("안녕" in "안녕하세요") # True 
print("잘가" in "안녕하세요") # False

# 문자열 자르기, split(기준문자)
out_d = "10 20 30 40 50".split("30") # "하"를 기준으로 문자열 자르기
print(out_d)

# f-문자열 vs .format()
print(f'{10} {20} {30}') # f-문자열|
print('{} {} {}'.format(10, 20, 30)) # .format()

# 구의 부피와 겉넓이 계산하기
pi = 3.14159
radius = float(input("구의 반지름을 입력하세요: "))
result1 = (4/3) * pi * radius**3
result2 = 4 * pi * radius**2
print(f"구의 부피는: {result1:.2f}")
print(f"구의 겉넓이는: {result2:.2f}")


# 피타고라스의 정리 계산하기
a = float(input("직각삼각형의 밑변의 길이를 입력하세요: "))
b = float(input("직각삼각형의 높이의 길이를 입력하세요: "))
c = (a**2 + b**2) ** 0.5
print(f"직각삼각형의 빗변의 길이는: {c:.2f}")