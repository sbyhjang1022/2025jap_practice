# pages/2_단어학습.py
import streamlit as st
from data import VOCAB
import random

st.set_page_config(page_title="단어학습 🧋", page_icon="🍡")
st.title("② 단어학습 — 기본 단어 플래시카드 & 퀴즈 🃏")

st.write("플래시카드로 외운 뒤, 퀴즈로 확인해보세요. ✨")

# Flashcard
if 'card_idx' not in st.session_state:
    st.session_state.card_idx = 0
if 'show_jp' not in st.session_state:
    st.session_state.show_jp = True

col1, col2 = st.columns([3,1])
with col1:
    item = VOCAB[st.session_state.card_idx % len(VOCAB)]
    if st.session_state.show_jp:
        st.markdown(f"## {item['ja']}  `{item['yomi']}`")
        st.markdown("**의미?** ❓ (아래 버튼으로 확인)")
    else:
        st.markdown(f"### 뜻: {item['ko']}")
with col2:
    if st.button("뒤집기 🔁"):
        st.session_state.show_jp = not st.session_state.show_jp
    if st.button("다음 ▶️"):
        st.session_state.card_idx += 1
        st.session_state.show_jp = True

st.markdown("---")
st.subheader("선택형 퀴즈 🍥")
sample = random.sample(VOCAB, min(4, len(VOCAB)))
correct = random.choice(sample)
opts = [s['ko'] for s in sample]
choice = st.radio(f"다음 일본어 `{correct['ja']}` 의 뜻은?", opts, key="vocab_quiz")
if st.button("정답 제출", key="vocab_submit"):
    if choice == correct['ko']:
        st.success("정답! よくできました 🎉")
    else:
        st.error(f"틀렸습니다. 정답: {correct['ko']}")
