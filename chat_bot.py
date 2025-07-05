import streamlit as st
from PIL import Image
from langchain.schema import HumanMessage
from agent_supervisor import supervisor  # LangGraph agent


st.set_page_config(page_title="Assistant Chatbot", page_icon="🤖") # doesnt work for some reason

if "user_pfp" not in st.session_state:
    st.session_state["user_pfp"] = "images/robot.jpg"  # Default avatar
if "username" not in st.session_state:
    st.session_state["username"] = "User"

with st.sidebar:
    st.markdown("## 👤 Your Profile")

    st.image(st.session_state["user_pfp"], width=100, caption="Your Avatar")

    st.markdown("---")
    st.write(f"**🧑 Username:** {st.session_state['username']}")

    if st.session_state["username"] == "User":
        st.info("💡 Go to the **Profile** page to personalize your avatar and name.")

st.title("🤖 Assistant Chatbot 🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    avatar = st.session_state["user_pfp"] if msg["role"] == "user" else "images/supervisor.jpeg"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

if prompt := st.chat_input("Say something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=st.session_state["user_pfp"]):
        st.markdown(prompt)

    try:
        response = supervisor.invoke(
            {'messages': [HumanMessage(content=prompt)]},
            {'configurable': {'thread_id': 'unique_session_id'}}
        )
        assistant_reply = response["messages"][-1].content
    except Exception as e:
        assistant_reply = f"Error: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    with st.chat_message("assistant", avatar="images/supervisor.jpeg"):
        st.markdown(assistant_reply)