import streamlit as st
# Hello World

st.set_page_config(page_title="Asadbek Akramov", page_icon=":a:", layout="wide")

# Assets
def local_css(file_name): 
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("styles/style.css")

# Hero (Index)
with st.container():
    st.subheader("Hi, I am Asadbek :wave:")
    st.title("Web Programmer from Uzbekistan")
    st.write("[Go To Telegram Channel &rarr;](https://t.me/asad_projects)")

# What I Do?

with st.container():
    st.write("---")
    wid_left, wid_right = st.columns(2)
    with wid_left:
        st.header("What I Do?")
        st.write("##")
        st.write(
            """                 
            I do projects using:
            - HTML
            - CSS 
            - JavaScript
            - Bootstrap
            - Node Js & MongoDB
            - Python
        """)
            
        st.write("[Learn more about me &rarr;](https://asad2010.github.io/porfolio-new/)")
    with wid_right:
        st.image("https://www.freecodecamp.org/news/content/images/2022/12/main-image.png")

# Projects

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    img_col, text_col = st.columns((1,2))

    with img_col:
        st.image("https://asad2010.github.io/porfolio-new/src/img/Screenshot_1.png",use_column_width=True)
    with text_col:
        st.subheader("Help To Africa")
        st.write (
            """      
            The languages ​​that I used:
            - HTML 
            - CSS
            - JavaScript
            - Bootstrap
            """
        )

with st.container():
    st.write("##")
    img_col, text_col = st.columns((1,2))

    with img_col:
        st.image("https://asad2010.github.io/porfolio-new/src/img/Screenshot_2.png",use_column_width=True)
    with text_col:
        st.subheader("Design")
        st.write (
            """      
            The languages ​​that I used:
            - HTML 
            - CSS
            """
        )


with st.container():
    st.write("##")
    img_col, text_col = st.columns((1,2))

    with img_col:
        st.image("https://asad2010.github.io/porfolio-new/src/img/Screenshot_3.png",use_column_width=True)
    with text_col:
        st.subheader("Rings")
        st.write (
            """      
            The languages ​​that I used:
            - HTML 
            - CSS
            """
        )

with st.container():
    st.write("##")
    img_col, text_col = st.columns((1,2))

    with img_col:
        st.image("https://asad2010.github.io/porfolio-new/src/img/Screenshot_4.png",use_column_width=True)
    with text_col:
        st.subheader("Furniture")
        st.write (
            """      
            The languages ​​that I used:
            - HTML 
            - CSS
            - Bootstrap
            """
        )
with st.container():
    st.header("More Projects You Can Find On My Telegram Channel")
    st.write("[Go To Telegram Channel &rarr;](https://t.me/asad_projects)")


with st.container(): 
    st.write("---")
    st.write("##")
    st.header("Send Text To Me")
    st.markdown(
        """
        <form action="https://formsubmit.co/asadbek.akramov.web@gmail.com" method="POST">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
    , unsafe_allow_html=True)