
# 딕셔너리 란? 키를 기반으로 값을 저장하는 것 
# vs JS(JSON) vs JAVA(map/dto)

# [1] tjsdjs
dict_a = {"name" : "어벤져스 엔드게임", "type" : "히어로 무비"}

# [2] 호출
print(dict_a)
# print(dict_a.name) # JS에서는 가능하지만 오류 발생
print(dict_a["name"])
print(dict_a.get("name")) # JAVA MAP 처럼 호출 가능
# print(dict_a["orgin"]) # 없는 키이면 오류 발생 

# [3] 딕셔너리 값 추가 하기, 딕셔너리['key'] = value
dict_a["price"] = 1000   
print(dict_a) # {'name' : '어벤져스 엔드게임', 'type' : '히어로 무비', 'price' : 1000}

dict_a['price'] = 2000 # 만약에 존재하면 key이면 value 수정 # key는 중복없음
print(dict_a)

# [4] 딕셔너리 키/값 제거하기, del 딕셔너리명['key']
del dict_a['price']
print(dict_a)

# 반복문과 딕셔너리 관계 
# for 키 변수 in 딕셔너리 : 
#    코드 

for 키 in dict_a : 
    print(키, ':', dict_a[키])


pets = [{"name" : "구름", "age" : 5}, {"name" : "초코", "age" : 3}]

print("# 우리 동네 애완 동물들")
for pet in pets:
    print(f"{pet['name']} {pet['age']}살")

numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)


character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:    # 딕셔너리 내 key 값이 딕셔너리이면
        for key2 in character[key] :
            print(key2, ":", character[key][key2])

    elif type(character[key]) is list:  # 딕셔너리 내 key 값이 리스트이면
        for key3 in character[key] :
            print(key, ":", key3)
            
    else :   # 딕셔너리 내 값이 리터럴이면
        print(key,":", character[key])

