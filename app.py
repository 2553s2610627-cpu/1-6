import streamlit as st
import random

st.title("💘 연애 코치 앱")

st.write("연애 고민을 입력하면 조언을 해드립니다.")

# 고민 입력
user_input = st.text_area("연애 고민 입력")

# 답변 리스트
answers = [
    """
    ❤️ 상대방은 아직 관심이 있습니다.

    추천 행동:
    너무 조급해하지 말고 여유 있게 대화하세요.

    추천 카톡:
    "오늘 하루 어땠어? 😊"
    """,

    """
    💡 지금은 밀어붙이기보다 분위기를 보는 게 중요합니다.

    추천 행동:
    연락 텀을 조금 조절해보세요.

    추천 카톡:
    "요즘 바쁜가 보네!"
    """,

    """
    🌸 상대방은 편안함을 느끼고 있습니다.

    추천 행동:
    가벼운 약속을 잡아보세요.

    추천 카톡:
    "주말에 맛있는 거 먹으러 갈래?"
    """,

    """
    🔥 호감 가능성이 높습니다.

    추천 행동:
    자신감 있게 표현해보세요.

    추천 카톡:
    "너랑 있으면 재밌어 😊"
    """
]

# 버튼
if st.button("코칭 받기"):

    if user_input == "":
        st.warning("고민을 입력해주세요.")

    else:
        result = random.choice(answers)

        st.success("분석 완료!")

        st.write(result)
