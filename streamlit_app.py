import platform
import time

import streamlit_patches as st

url = "https://www.notion.so/streamlit/Johannes-MPA-v2-idea-1869aafe213b45fabb090db9cae845c1"

## Common elements

st.sidebar.write("Common sidebar element")

st.sidebar.write("Streamlit version:", st.__version__)
st.sidebar.write("Python version:", platform.python_version())

if st.sidebar.checkbox("Run long function before st.page commands"):
    time.sleep(3)

"# Common header!"

f"### [Give feedback here]({url})"

## Pages


def function_example():
    st.write(
        """
        ## Example
        This is a function!
        """
    )


st.page("example_one.py", name="Home!", icon="🍔")

st.page("example_four.py", icon="🦊")

section = st.section("Section", icon="🧯")

st.page("example_three.py", name="Custom name!", icon="🔥")

section.page("example_three.py", name="Custom name!", icon="🔥")

section.page("example_two.py", icon="⭐")

section.page(function_example, icon="🌊")


def test():
    st.write("This is a test")


st.page(test, name="Unindented?", icon="🔥")


def test2():
    st.write("This is a test")


section.page(test2, icon="🌊")


def test3():
    st.write("This is a test")


def test4():
    st.write("This is a test")


def test5():
    st.write("This is a test")


section = st.section("Section2", icon="🧯")

section.page(test3, "Test3", icon="🔥")

section.page(test4, "Test4", icon="🔥")

st.page(test5, "Test5", icon="🔥")

# st.page("example_three.py", name="Custom name!", icon="🔥")
section.page("example_three.py", name="Custom name!", icon="🔥")

section.page("example_two.py", icon="⭐")

section.page(function_example, icon="🌊")
