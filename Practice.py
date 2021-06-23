#날씨
weather = input("오늘 날씨(비, 눈, 미세먼지 등) : ")
if weather == "비" or "눈":
    print("우산 챙길 것")
elif weather == "미세먼지" :
    print("마스크 챙길 것")
else :
    print("그냥 갈 것")