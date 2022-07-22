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

st.page("example_three.py", name="Custom name!", icon="🔥")

st.page("example_two.py", icon="random")

st.page(function_example, icon=":dog:")
