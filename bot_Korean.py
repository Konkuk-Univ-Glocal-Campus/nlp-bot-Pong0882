import random

# 이 리스트는 랜덤 응답을 포함합니다 (원하시면 자신의 응답을 추가하거나 번역해서 넣을 수도 있어요)
random_responses = ["그것은 꽤 흥미로운데, 더 말해주세요.",
                    "알겠어요. 계속 이야기해 주세요.",
                    "왜 그렇게 말하시는 거죠?",
                    "요즘 날씨가 웃겨요, 그렇지 않나요?",
                    "주제를 바꿔볼까요?",
                    "어젯밤 경기 보셨어요?"]

print("안녕하세요, 저는 Marvin이라고 하는 간단한 로봇입니다.")
print("'bye'를 입력하여 언제든 대화를 종료할 수 있어요.")
print("각 답변을 입력한 후 '엔터' 키를 누르세요.")
print("오늘 기분은 어떠세요?")

while True:
    # 사용자가 텍스트를 입력할 때까지 대기합니다.
    user_input = input("> ")
    if user_input.lower() == "bye":
        # 사용자가 'bye'를 입력하면 (또는 BYE, ByE, byE 등), 루프를 빠져나옵니다.
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("대화해 주셔서 즐거웠어요. 안녕히 가세요!")
