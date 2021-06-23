# def profile(name, age, main_lang):
#     print("이름 : {0}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile("A", 20, "파이썬")
# profile("B", 23, "자바")

#기본값 사용하기

def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))

profile("A")
profile("B")