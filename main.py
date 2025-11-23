# main.py
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="日本語勉強 🍡", page_icon="🎌", layout="centered")

st.title("やさしい にほんご🍙")
st.caption("문자 → 단어 → 문장 → 문화, 4단계로 배우는 일본어 학습앱")
st.caption("2025.장윤하.All rights reserved.")

with st.expander("무엇을 배울 수 있나요?💡"):
    st.markdown("""
- **문자학습**: 히라가나/가타카나 읽기·쓰기 연습  
- **단어학습**: 플래시카드 + 선택형 테스트  
- **문장학습**: 빈칸 채우기·쓰기 연습  
- **문화학습**: 일본 문화 퀴즈와 미니레슨 🎎
""")

# 간단한 사용 통계(세션)
if 'visits' not in st.session_state:
    st.session_state.visits = 0
st.session_state.visits += 1

st.sidebar.header("앱 메뉴")
st.sidebar.write("페이지는 좌측 상단 Streamlit의 Pages 메뉴에서 이동하세요.")
st.sidebar.markdown("---")
st.sidebar.write(f"방문: {st.session_state.visits}번")
st.sidebar.write(f"오늘: {datetime.now().strftime('%Y-%m-%d')}")

st.markdown("### 시작하기 ✨")
st.markdown("좌측 상단의 페이지 탭에서 `문자학습`, `단어학습`, `문장학습`, `문화학습` 중 탭을 골라 학습을 시작하세요! 🎌")
st.markdown("---")
st.write("즐겁게 배우세요 — がんばってね！😊")
