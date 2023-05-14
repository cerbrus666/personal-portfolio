import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Halim's personal website", page_icon=":tada:", layout="wide"
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


############ Headers section ####################
with st.container():
    st.subheader("Hi, I am Halim :wave:")
    st.title("A Software Engineer From Malaysia")
    st.write("I am passionate in building software and machine learning model")
    st.write("Main programming language: Python, C/C++")

############# Load assets ###############
lottie_coding = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_iv4dsx3q.json"
)

####### What I do #############
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
        - 9-5 on the clock, 5 days per week: I build, maintain and optimise machine learning system for efficient deployment and functional machine learning model
        - On my spare times: I make stuff with 3D printer"""
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


# #### Projects ##############
# with st.container():
#     st.write("---")
#     st.header("My projects")
#     st.write("##")
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         # insert image
#     with text_column:
#         st.subheader("Animations here?")
#         st.write()
