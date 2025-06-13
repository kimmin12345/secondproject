import streamlit as st
import random

# 🎨 페이지 꾸미기
st.set_page_config(
    page_title="가위✌️바위✊보🖐️ 게임",
    page_icon="🎮",
    layout="centered"
)

st.markdown("# 🎮 컴퓨터와 가위✌️바위✊보🖐️ 한 판 승부!")
st.markdown("## 🤖 당신의 운을 시험해보세요!")

st.markdown("### ✨ 선택하세요!")

choices = {
    "가위 ✌️": "scissors",
    "바위 ✊": "rock",
    "보 🖐️": "paper"
}

user_choice = st.radio(
    "무엇을 낼까요?", 
    list(choices.keys()),
    horizontal=True
)

if st.button("👉 대결 시작!"):
    user_pick = choices[user_choice]
    computer_pick = random.choice(list(choices.values()))
    
    # 역 매핑
    emoji_dict = {
        "rock": "바위 ✊",
        "paper": "보 🖐️",
        "scissors": "가위 ✌️"
    }

    st.markdown("---")
    st.markdown(f"👤 당신의 선택: **{user_choice}**")
    st.markdown(f"🖥️ 컴퓨터의 선택: **{emoji_dict[computer_pick]}**")
    st.markdown("---")
    
    # 승부 로직
    if user_pick == computer_pick:
        st.success("😮 비겼어요! 역시 실력자시군요!")
    elif (user_pick == "rock" and computer_pick == "scissors") or \
         (user_pick == "scissors" and computer_pick == "paper") or \
         (user_pick == "paper" and computer_pick == "rock"):
        st.balloons()
        st.success("🎉 이겼어요! 축하드립니다!")
    else:
        st.error("😢 졌어요... 다음엔 이길 수 있어요!")

st.markdown("---")
st.markdown("🌀 계속해서 컴퓨터와 대
