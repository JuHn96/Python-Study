# def calculate_average(scores):
#     return sum(scores) / len(scores)

# print(calculate_average([85, 90, 78, 92, 88]))


def calculate_average(*scores):
    return sum(scores) / len(scores)

scores = []  # 점수를 저장할 리스트

while True:
    user_input = input("점수를 입력하세요 (종료하려면 'stop'): ")
    if user_input.lower() == 'stop':
        break
    try:
        score = float(user_input)
        scores.append(score)  # 리스트에 추가
    except ValueError:
        print("유효한 점수를 입력하세요.")

# 입력된 점수가 하나라도 있을 때만 평균 계산
if scores:
    avg = calculate_average(*scores)  # 언패킹해서 함수에 전달
    print(f"평균 점수 : {avg:.2f}")
else:
    print("입력된 점수가 없습니다.")
