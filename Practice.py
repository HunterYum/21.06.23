#숫자값에 더하기
student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]
print(student)

#문자를 길이로 변환
students = ["Apple", "Banana", "Cross"]
students = [len(i) for i in students]
print(students)

#문자를 대문자로 변환
students = [i.upper() for i in students]
print(students)