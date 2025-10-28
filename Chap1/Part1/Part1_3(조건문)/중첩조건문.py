age = 25
has_ticket = True

if age >= 18:
    if has_ticket:
        print("입장 가능")
    else:
        print("티켓이 필요합니다")
else:
    print("미성년자는 입장 불가")