import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="🎮 가위✌️바위✊보🖐️ 게임",
    page_icon="✂️🪨📄",
    layout="centered"
)

# 제목
st.markdown("# 🥳 컴퓨터와 가위✌️바위✊보🖐️ 대결! 🥳")
st.markdown("## 당신의 운명을 시험해보세요! 🤖 VS 👤")

# 선택지 딕셔너리
choices = {
    "가위 ✌️": "scissors",
    "바위 ✊": "rock",
    "보 🖐️": "paper"
}

# 사용자 선택 UI
user_choice = st.radio(
    "👉 무엇을 낼까요?",
    options=list(choices.keys()),
    horizontal=True
)

# 대결 시작 버튼
if st.button("⚔️ 대결 시작!"):
    user_pick = choices[user_choice]
    computer_pick = random.choice(list(choices.values()))
    
    # 컴퓨터, 사용자 선택 이모지 매핑
    emoji_map = {
        "rock": "바위 ✊",
        "paper": "보 🖐️",
        "scissors": "가위 ✌️"
    }
    
    # 결과 출력
    st.markdown("---")
    st.markdown(f"👤 당신의 선택: **{user_choice}**")
    st.markdown(f"🤖 컴퓨터의 선택: **{emoji_map[computer_pick]}**")
    st.markdown("---")
    
    # 승부 판단
    if user_pick == computer_pick:
        st.info("🤝 비겼습니다! 다시 도전해보세요!")
    elif (user_pick == "rock" and computer_pick == "scissors") or \
         (user_pick == "scissors" and computer_pick == "paper") or \
         (user_pick == "paper" and computer_pick == "rock"):
        st.balloons()
        st.success("🎉 축하합니다! 이겼어요!")
    else:
        st.error("😢 아쉽지만 졌습니다... 다음엔 꼭 이겨요!")

st.markdown("---")
st.markdown("🌀 계속해서 컴퓨터와 가위✌️바위✊보🖐️로 대결하세요! 행운을 빕니다! 🍀")
