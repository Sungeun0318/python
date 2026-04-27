user_list = []
login_name = ""
apt_list = []

file_name = "./day08/practice7/user.txt"
apt_file = "아파트_실거래가.csv"


def signup():
    u_id = input("아이디 입력: ")
    u_pw = input("비밀번호 입력: ")
    u_name = input("이름 입력: ")
    u_no = len(user_list) + 1
    new_user = {"no": str(u_no), "id": u_id, "pw": u_pw, "name": u_name}
    user_list.append(new_user)
    with open(file_name, "a", encoding="utf-8") as file:
        file.write("{},{},{},{}\n".format(u_no, u_id, u_pw, u_name))
    print("{}님 가입 완료!".format(u_name))

def login():
    global login_name
    u_id = input("아이디: ")
    u_pw = input("비밀번호: ")
    for user in user_list:
        if user["id"] == u_id and user["pw"] == u_pw:
            login_name = user["name"]
            print("{}님 환영합니다!".format(login_name))
            return
    print("로그인 실패")

def logout():
    global login_name
    login_name = ""
    print("로그아웃 되었습니다.")

def load_apt_data():
    try:
        with open(apt_file, "r", encoding="cp949") as file:
            lines = file.readlines()
            for line in lines[17:]:
                data = line.strip().split('","')
                if len(data) > 10:
                    apt = {
                        "area": data[1],
                        "name": data[5],
                        "price": data[9]
                    }
                    apt_list.append(apt)
    except:
        pass
print(  load_apt_data)

def search_area():
    keyword = input("검색할 지역명을 입력하세요: ")
    print("\n--- 검색 결과 ---")
    count = 0
    for apt in apt_list:
        if keyword in apt["area"]:
            print("지역: {} | 아파트: {} | 금액: {}만원".format(apt["area"], apt["name"], apt["price"]))
            count += 1
    if count == 0:
        print("결과가 없습니다.")
    else:
        print("총 {}건 검색됨".format(count))

print(search_area)
try:
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) == 4:
                user = {"no": data[0], "id": data[1], "pw": data[2], "name": data[3]}
                user_list.append(user)
except:
    pass

load_apt_data()

while True:
    if login_name == "":
        print("1. 회원가입 2. 로그인 3. 종료")
        choice = input("선택: ")
        if choice == "1": signup()
        elif choice == "2": login()
        elif choice == "3": break
    else:
        print("[ {}님 로그인 중 ]".format(login_name))
        print("1. 지역명 검색 2. 로그아웃 3. 종료")
        choice = input("선택: ")
        if choice == "1": search_area()
        elif choice == "2": logout()
        elif choice == "3": break
