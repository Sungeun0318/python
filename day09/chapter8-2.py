
# isinstance(객체, 클래스명), 만약에 해당 객체가 클래스로 만들어졌다면 True, False
# vs 객체 instanceof 클래스명

# [1] 클래스 선언
class Student :
    count = 0   # 클래스변수 vs JAVA : static
    def study(self) :
        print("공부를 합니다.")
    
    def __str__(self): # str() 함수 호출될 때 자동으로 실행되는 함수 
        return "학생"
    
    def __eq__(self, value): # == 호출될 때 자동으로 실행되는 함수
        return 80 == value
    
    def func1(self) :
        return Student.count + 1 # 클래스변수 호출
    
    # cls(클래스) vs self(인스턴스)
    # 클래스 함수 vs JAVA : static 
    @classmethod # 데코레이터
    def print(cls) : # cls(class) 해당 클래스 가리킴.
        print("클래스 함수 호출")
        print(cls.count)
       
    
class Teacher :
    def teach(self) :
        print("학생을 가르칩니다.")
        

# [2] 인스턴스 생성
classroom = [Student(),Student(), Teacher(), Student(), Student()]

# [3] 리스트내 인스턴스들의 타입 확인

for person in classroom :
    if isinstance(person, Student) :
        person.study()
    elif isinstance(person, Teacher) :
        person.teach()
        
# [4] 
print(str(classroom[0])) # 학생
print(classroom[0] == 90) # False
print(classroom[0] == 80) # True

# [5] 클래스 변수 호출
print(Student.count) # 클래스변수는 인스턴스 없이 호출 가능 # 0
print(classroom[0].func1()) # 1

# [6] 클래스 함수 호출, 클래스명.함수명()
Student.print() 