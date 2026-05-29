import streamlit as st
from openai import OpenAI

# OpenAI 연결
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 제목
st.title("💘 AI 연애 코치")

st.write("연애 고민을 입력하면 AI가 코칭해줍니다.")

# 고민 입력
user_input = st.text_area(
    "연애 고민 입력",
    height=200
)

# 버튼
if st.button("코칭 받기"):

    # 입력 체크
    if user_input == "":
        st.warning("고민을 입력해주세요.")
    else:

        with st.spinner("AI가 분석중입니다..."):

            prompt = f"""
            너는 유명한 연애 코치다.

            사용자의 고민을 보고:
            1. 상대 심리
            2. 현재 상황
            3. 추천 행동
            4. 추천 카톡 답장

            을 친절하게 알려줘.

            사용자 고민:
            {user_input}
            """

            # GPT 호출
            response = client.chat.completions.create(
                model="gpt-5",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            result = response.choices[0].message.content

            st.success("분석 완료!")

            st.write(result)
