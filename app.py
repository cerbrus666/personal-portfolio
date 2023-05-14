import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from pathlib import Path

st.set_page_config(
    page_title="Halim's personal website", page_icon=":tada:", layout="wide"
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css(Path("style/style.css"))

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
img_contact_form = Image.open(Path("images/binary.jpg"))
img_lottie_animation = Image.open(Path("images/screen.jpg"))
img_robotic_arm = load_lottieurl(
    "https://assets1.lottiefiles.com/packages/lf20_bPtkGeNd9y.json"
)
threed_printer = load_lottieurl(
    "https://assets1.lottiefiles.com/packages/lf20_vu2p4il8.json"
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


#### Projects ##############
with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # insert image
        # st.image(img_lottie_animation)
        st_lottie(img_robotic_arm, height=300, key="robotic")
    with text_column:
        st.subheader("VEX Robotics")
        st.write("I created a line following robot")
        # st.markdown("Watch video")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            # st.image(img_contact_form)
            st_lottie(threed_printer, height=300, key="3dprinter")
        with text_column:
            st.subheader("Make stuff with 3D printer")
            st.write("I make stuff that ease my daily life")
            # st.markdown("Watch video")


#### Contact form ############
with st.container():
    st.write("---")
    st.header("Get in touch with me")
    st.write("###")

    contact_form = """
    <form action="https://formsubmit.co/your@email.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="Your name" required>
     <input type="email" name="Your email" required>
     <textarea name="message" placeholder ="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>"""

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
