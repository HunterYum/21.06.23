#함수 정의 후 호출
def open_account():
    print("새로운 계좌 생성됨")
open_account()

#입금
def deposit(balance, money):
    print("입금 완료. 잔액 : {0}".format(balance + money))
    return balance + money

balance = 0
balance = deposit(balance, 1000)
print(balance)

def withdraw(balance, money):
    if balance >= money:
        print("출금 완료. 잔액 : {0}".format(balance - money))
        return balance - money
    else:
        print("출금 불가능. 잔액 : {0}". format(balance))
        return balance

balance = withdraw(balance, 500)

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

comminssion, balance = withdraw_night(balance, 500)
print("수수료 {0}원, 잔액 : {1}".format(comminssion, balance))