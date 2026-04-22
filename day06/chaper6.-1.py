
# 예외 처리 : 예외가 발생할 상황을 예측하고 모두 조건문으로 처리하는 것은 매우 힘들다.
# 예외가 발생하면 프로그램이 강제로 종료되지 않게 흐름 제어 하기 = 예외처리

# try ~ except ; 

try :
    # 예외가 벌샹헐 곳 같은 코드
    int(input('정수입력 : ')) # 7 : 정상, a : 예외발생
except :
    # 만약에 예외가 발생했을 떄
    print('정수만 입력하세요')
    
# pass : 예외처리가 아닌 일단 생략할 경우
list_input_a = ["52", "273", "43", "스파이","103"]
list_number = []
for item in list_input_a :
    try :
        float(item)
        list_number.append(item)
    except :
        pass
print (list_number)

try :
    number_input_a = int(input)('정수입력 : ')
except :
    print("정수를 입력하세요.")
else :
    print(number_input_a)
    

# finally : 무조건 실행할 코드 
try :
    number_input_a = int(input('정수입력하세요'))
except :
    print("정수를 입력하세요")
else :
    print("예외가 발생하지 않았다.")
finally :
    print("무조건 실행되는 코드")
    
