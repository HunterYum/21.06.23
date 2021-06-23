import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름" : "A", "나이" : 20, "취미" : ["축구", "농구", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #프로필에 있는 정보를 파일에 저장
# profile_file.close()

profile_file = open("profile.pickle", 'rb')
profile = pickle.load(profile_file)
print(profile)
profile_file.close()