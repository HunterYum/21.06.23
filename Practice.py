class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기")
    n1 = int(input("첫번째 숫자 : "))
    n2 = int(input("두번째 숫자 : "))
    if n1 >= 10 or n2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(n1, n2))
    print("{0}/{1} = {2}".format(n1, n2, int(n1/n2)))

except ValueError:
    print("잘못된 값 입력. 한 자리 숫자만 입력 바람.")
except BigNumberError as err:
    print("에러 발생. 한 자리 숫자만 입력")
    print(err)

finally:
    print("계산기 종료")