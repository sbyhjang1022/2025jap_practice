# pages/3_문장학습.py
import streamlit as st
from data import SENTENCES
import random

st.set_page_config(page_title="문장학습 📝", page_icon="🗒️")
st.title("③ 문장학습 — 읽기 · 쓰기 연습 ✍️")

st.write("예문을 보고 읽기(ふりがな)와 의미를 확인해 보세요. 빈칸 채우기 연습도 있어요!")

sent = random.choice(SENTENCES)
st.markdown("**문장 (일본어)**")
st.write(sent['ja'])
st.markdown("**읽는 방법 (よみ)**")
st.write(sent['yomi'])
st.markdown("**한국어 뜻**")
st.write(sent['ko'])

st.markdown("---")
st.subheader("빈칸 채우기 연습")
# 간단한 blank: 문장에서 한 단어를 지우기
words = sent['ja'].split()
if len(words) < 2:
    # fallback: remove a substring
    s = sent['ja']
    idx = len(s)//2
    blanked = s[:idx] + "＿＿＿" + s[idx+1:]
    answer = s[idx:idx+1]
else:
    i = random.randrange(len(words))
    answer = words[i]
    words[i] = "＿＿＿"
    blanked = " ".join(words)

st.write(blanked)
guess = st.text_input("빈칸에 들어갈 부분을 입력하세요 (정확히 같은 형태로)", key="sentence_guess")
if st.button("채점", key="sent_submit"):
    if guess.strip() == answer:
        st.success("정답! 문맥 파악이 훌륭해요 🎌")
    else:
        st.error(f"아쉽네요. 정답은 `{answer}` 입니다.")
