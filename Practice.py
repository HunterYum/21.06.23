#온도
temp = int(input("기온 : "))
if 30<= temp:
    print("너무 더움")
elif 10 <= temp and temp < 30:
    print("괜찮음")
elif 0 <= temp and temp <10:
    print("추움")
else:
    print("너무 추움")