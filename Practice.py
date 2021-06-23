def profile(name, age, *language):
   print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
   for lang in language:
       print(lang, end=" ")


profile("A", 20, "python", "java", "c", "c++", "c#")
profile("B", 23, "kotlin", "swift", "", "", "")