import streamlit as st
import time
from datetime import datetime

# https://darrellajenkins-webst-todo-app-home-xl3vgk.streamlit.app/

def get():
    with open('webtodos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write(todos_arg):
    with open('webtodos.txt', 'w') as file:
        file.writelines(todos_arg)
    return todos_arg


# """This is the entry point to test your app. In terminal type streamlit run Home.py. Now it will show both the Home and About pages.
# All files are: Home.py, About.py, webtodos.txt, pages directory."""


def add_todo():
    task = st.session_state["add_todo"] + "\n"
    todos.append(task)
    write(todos)
    st.session_state["add_todo"] = ""


todos = get()
st.title("My TODO App")
st.subheader("A fun, easy way to track your tasks!")
st.write("Web-deployed applications are easier for users to access and <b>allow much faster updating and maintaining by software engineers.<b/>",
         unsafe_allow_html=True)

st.write("<h4>Are you ready?<h4/>", unsafe_allow_html=True)  # h3 == subheader setting, so I chose h4 instead, which is a little smaller.
st.text_input(label="Enter a task:", placeholder="Which task do you need to focus on today?",
              on_change=add_todo, key="add_todo")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write(todos)
        del st.session_state[todo]
        st.rerun()
