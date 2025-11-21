# pages/1_문자학습.py
import streamlit as st
from data import HIRAGANA, KATAKANA
import random

st.set_page_config(page_title="문자학습 🍥", page_icon="🈶")
st.title("① 문자학습 — 히라가나 · 가타카나 📝🎏")

mode = st.radio("모드 선택", ("히라가나 연습", "가타카나 연습", "랜덤 퀴즈"))
st.write("발음(ローマ字)을 보고 맞는 문자를 고르거나, 문자를 보고 발음을 적어보세요. 🐣")

def show_table(table):
    cols = st.columns(5)
    for i,(ch,romaji) in enumerate(table):
        cols[i%5].markdown(f"### {ch}  \n`{romaji}`")

if mode == "히라가나 연습":
    st.subheader("기본 히라가나")
    show_table(HIRAGANA)
    st.markdown("**연습**: 아래 입력칸에 히라가나의 로마자를 입력해보세요.")
    ch,rom = random.choice(HIRAGANA)
    answer = st.text_input(f"문자: {ch}  → 발음(로마자)를 입력", key="hira_input")
    if st.button("제출", key="hira_btn"):
        if answer.strip().lower() == rom:
            st.success("정답! 잘했어요 🎉")
        else:
            st.error(f"아쉽네요. 정답은 `{rom}` 입니다.")

elif mode == "가타카나 연습":
    st.subheader("기본 가타카나")
    show_table(KATAKANA)
    ch,rom = random.choice(KATAKANA)
    answer = st.text_input(f"문자: {ch}  → 발음(로마자)를 입력", key="kata_input")
    if st.button("제출", key="kata_btn"):
        if answer.strip().lower() == rom:
            st.success("정답! 잘했어요 🎉")
        else:
            st.error(f"정답은 `{rom}` 입니다.")

else:
    st.subheader("랜덤 선택형 퀴즈")
    pool = HIRAGANA + KATAKANA
    ch,romaji = random.choice(pool)
    opts = [romaji]
    while len(opts) < 4:
        cand = random.choice(pool)[1]
        if cand not in opts:
            opts.append(cand)
    random.shuffle(opts)
    choice = st.radio(f"문자: {ch} → 발음은?", opts, key="quiz_choice")
    if st.button("제출", key="quiz_submit"):
        if choice == romaji:
            st.success("정답! 🍡")
        else:
            st.error(f"오답. 정답은 `{romaji}` 입니다.")
