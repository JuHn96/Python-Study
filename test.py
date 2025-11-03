menu = {
    "1": "회원가입",
    "2": "로그인",
    "3": "종료"
    }
    
# 메뉴 출력
for key, value in menu.items():
    print(f"{key}. {value}")
    
choice = "2"

if choice == "1":
    print(menu[choice])
elif choice == "2":
    print(menu[choice])
elif choice == "3":
    print(menu[choice])
else:
    print("잘못된 선택입니다.")
