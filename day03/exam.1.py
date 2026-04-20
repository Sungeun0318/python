key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]

print(character)





limit = 10000
i = 1


while True :
    sum_value += i
    if sum_value > limit :
        break
    i += i
# while sum_value <= limit:
#     sum_value += i
#     i += 1
print("{}를 더할 때 {}을 넘으며 그때의 값은 {} 입니다.".format(i-1, limit, sum_value))