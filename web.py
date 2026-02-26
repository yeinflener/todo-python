import streamlit as st
import main_function

todos = main_function.get_todos()
#horizontal length of web page expands to the entire width of browser & responsive
st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    main_function.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("<h>This app is to increase your <b>productivity</b>.</h>.",
         unsafe_allow_html=True)

st.checkbox("Buy grocery")
st.checkbox("Get gas")
st.checkbox("Do strength training")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        main_function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter a todo:", placeholder="Add a new todo here...",
              on_change=add_todo, key='new_todo')

print("Hello")
print("second hello..........")

st.session_state