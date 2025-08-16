import streamlit as st
from PIL import Image

st.set_page_config(page_title = "User Profile", page_icon = "👤")

st.title("👤 Set Up Your Profile")

pfp_options = {
    "🐱 Cat": "images/cat.jpg",
    "🐶 Dog": "images/dog.jpg",
    "🤖 Robot": "images/robot.jpg",
    "👾 Alien": "images/alien.jpg"
}

choice = st.selectbox("Choose your avatar", list(pfp_options.keys()))
username = st.text_input("Enter your display name", value = st.session_state.get("username", "User"))

if st.button("✅ Save and Continue"):
    st.session_state["user_pfp"] = pfp_options[choice]
    st.session_state["username"] = username
    st.success("Profile saved! You can now go to the chat.")
