phonebook = {
    "엄마": "010-1234-5678",
    "아빠": "010-2345-6789",
    "친구": "010-3456-7890"}
    
name = "엄마"

# 여기에 코드 작성
# name에 해당하는 전화번호 출력
print(phonebook.get(name))

# 원하는 이름 입력하여 전화번호 조회
user_name = input("이름을 입력하세요(예시 - 엄마, 아빠, 친구):")
print(f"{user_name}: {phonebook.get(user_name)}")