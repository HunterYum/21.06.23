#파일 만들기
# score_file = open("score.tex", "w", encoding="utf8")
# print("math : 0", file=score_file)
# print("en : 50", file=score_file)
# score_file.close()

# score_file = open("score.tex", "a", encoding="utf8")
# score_file.write("sci : 88")
# score_file.write("\nco : 100")

# #파일 읽기
# score_file = open("score.tex", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

#파일 글 하나씩 읽기
score_file = open("score.tex", "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

