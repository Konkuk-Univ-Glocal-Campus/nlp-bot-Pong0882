import random

# 랜덤 응답 리스트
random_responses = [
    "그것은 꽤 흥미로운데, 더 말해주세요.",
    "알겠어요. 계속 이야기해 주세요.",
    "왜 그렇게 말하시는 거죠?",
    "요즘 날씨가 웃겨요, 그렇지 않나요?",
    "주제를 바꿔볼까요?",
    "어젯밤 경기 보셨어요?" "오늘 하루 어떻게 보내셨어요?",
    "요즘 무엇에 관심이 있으세요?",
    "최근에 본 책이나 영화에 대해 이야기해 주세요.",
    "가장 좋아하는 여가 활동은 무엇인가요?",
    "가고 싶은 여행지가 있으신가요?",
    "오늘 무엇을 먹었나요?",
    "가장 기억에 남는 추억은 무엇인가요?",
    "가장 좋아하는 음악은 무엇인가요?",
    "누군가에게 가르치고 싶은 것이 있나요?",
    "가장 행복한 순간은 언제였나요?",
]

print("안녕하세요, 저는 Marvin이라고 하는 간단한 로봇입니다.")
print("'종료'를 입력하여 언제든 대화를 종료할 수 있어요.")
print("각 답변을 입력한 후 '엔터' 키를 누르세요.")
print("오늘 기분은 어떠세요?")

while True:
    # 사용자가 텍스트를 입력할 때까지 대기합니다.
    user_input = input("> ")
    if user_input == "종료":
        # 사용자가 '종료'를 입력하면 루프를 빠져나옵니다.
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("대화해 주셔서 즐거웠어요. 안녕히 가세요!")
