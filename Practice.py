#커피 대기
customer = "A"
index = 5
while index >=1:
    print("{0}, 커피가 준비 됐습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피 보류")

#무한반복
# index = 1
# while True:
#      print("{0}, 커피가 준비 됐습니다. {1}번 남았습니다.".format(customer, index))
#      index += 1

#whlie문 탈출예제
customer = "A"
person = "unknown"

while person != customer :
     print("{0}, 커피가 준비 됐습니다.".format(customer))
     person = input("이름이")