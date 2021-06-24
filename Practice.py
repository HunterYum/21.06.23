try:
    print("나누기 전용 계산기")
    ns = []
    ns.append(int(input("첫 번째 숫자 : ")))
    ns.append(int(input("두 번째 숫자 : ")))
    ns.append(int(ns[0]/ns[1]))
    print("{0}/{1} = {2}".format(ns[0], ns[1], ns[1]/ns[2]))
except ValueError:
    print("오류 발생")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알수없음")
    print(err)