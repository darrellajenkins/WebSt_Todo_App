import streamlit as st
import time


def get():
    with open('webtodos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write(todos_arg):
    with open('webtodos.txt', 'w') as file:
        file.writelines(todos_arg)
    return todos_arg


def my_datetime():
    import time

    my_date = time.strftime('%A %B %d, %Y')
    my_time = time.strftime('%I:%M:%S %p')
    return my_date, my_time


def add_todo():
    task = st.session_state["add_todo"] + "\n"
    todos.append(task)
    write(todos)
    st.session_state["add_todo"] = ""  # Clear the input field - added by Claude.


def edit_todo(index):
    st.session_state["editing"] = index
    st.session_state["edit_todo"] = todos[index].strip()


def save_edit():
    index = st.session_state["editing"]
    todos[index] = st.session_state["edit_todo"] + "\n"
    write(todos)
    st.session_state["editing"] = -1


todos = get()
t = my_datetime()
st.title("My TODO App")
st.subheader("A fun, easy way to track your tasks!")

st.write(f"{t[0]} {t[1]}", end='\r\n')

for index, todo in enumerate(todos):
    col1, col2, col3 = st.columns([0.05, 0.8, 0.15])

    with col1:
        checkbox = st.checkbox("", key=f"checkbox_{index}")

    with col2:
        if st.session_state.get("editing") == index:
            st.text_input("Edit task:", value=todo.strip(), key="edit_todo", on_change=save_edit)
        else:
            st.write(todo.strip())

    with col3:
        if st.session_state.get("editing") == index:
            st.button("Save", key=f"save_{index}", on_click=save_edit)
        else:
            st.button("Edit", key=f"edit_{index}", on_click=edit_todo, args=(index,))

    if checkbox:
        todos.pop(index)
        write(todos)
        st.rerun()

st.text_input(label="Enter a task:", placeholder="Which task do you need to focus on today?", on_change=add_todo, key="add_todo")

if "editing" not in st.session_state:
    st.session_state["editing"] = -1
