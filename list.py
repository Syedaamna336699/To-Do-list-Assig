import streamlit as st

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

st.title("To-Do List App")
st.sidebar.header("Add New Task")

task = st.sidebar.text_input("Enter a task")
if st.sidebar.button("Add Task"):
    if task:
        st.session_state.tasks.append({"task": task, "completed": False})
        st.success("Task added successfully!")
    else:
        st.warning("Task cannot be empty!")

# Display tasks
st.subheader("Your To Do List")
if not st.session_state.tasks:
    st.info("No task added yet, start by adding a task from the sidebar!")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])

        # Mark as completed
        completed = col1.checkbox(f"{task['task']}", task["completed"], key=f"check_{index}")
        if completed != task["completed"]:
            st.session_state.tasks[index]["completed"] = completed

        # Update task
        if col2.button("Edit", key=f"edit_{index}"):
            new_task = st.text_input("Edit Task", task["task"], key=f"edit_input_{index}")
            if new_task and st.button("Save", key=f"save_{index}"):
                st.session_state.tasks[index]["task"] = new_task
                st.experimental_rerun()

        # Delete task
        if col3.button("Delete", key=f"delete_{index}"):
            del st.session_state.tasks[index]
            st.experimental_rerun()

# Clear all tasks
if st.button("Clear all tasks"):
    st.session_state["tasks"] = []
    st.success("All tasks deleted successfully!")

# Footer
st.markdown("---")
st.caption("Stay organized & productive with this simple To-Do list App.")
