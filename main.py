# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st

from langchain_openai import ChatOpenAI

# Initialize the ChatOpenAI class
chat_model = ChatOpenAI()

st.title("경영 그룹 피터드러커")

content = st.text_input("배우고 싶어 주제를 입력해주세요.")

if st.button("경영 및 사고 방식에 대한 설명을 기술하기"):
    with st.spinner('생각 중...'):
        result =chat_model.predict(content + "에 대한 이론을 설명해주세요.")
        st.write(result)

