import streamlit_patches as st

st.sidebar.write("Common sidebar element")

"## Common header!"


def function_example():
    st.title("Example")
    st.write("This is a function!")


st.page("example_one.py", name="Home!", icon="🍔")

st.page("example_two.py", icon="⭐")

st.page("example_three.py", name="Custom name!", icon="🔥")

st.page("example_four.py", icon="🦊")

st.page(function_example, icon="🌊")
