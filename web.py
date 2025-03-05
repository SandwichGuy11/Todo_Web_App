import streamlit as st
import functions

todo_list = functions.get_todo_list()


def add_todo():
    local_todo = st.session_state["new_todo"]
    todo_list.append(local_todo)
    functions.save_txt_file(todo_list)  # important to save
    st.session_state["new_todo"] = ""  # clear the input box


# -------------------- WEB LAYOUT --------------------

st.title("Todo List App")
st.subheader("This is my todo app.")
st.write("Useful text here.")

# Checkboxes for todos
for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(label=todo,
                           key=todo
                           )
    # Remove TO-DO | Complete TO-DO
    if checkbox:    # checkbox returns bool if checked
        todo_list.pop(index)
        functions.save_txt_file(todo_list)
        del st.session_state[todo]  # remove from session state dict
        st.experimental_rerun()  # required for checkboxes

# Input box for adding todos
input_todo = st.text_input(label="",
                           placeholder="Add new todo..",
                           on_change=add_todo,
                           key="new_todo"
                           )

st.write("input: ", input_todo)
# st.session_state
