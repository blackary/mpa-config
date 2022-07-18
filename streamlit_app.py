from itertools import chain
from pathlib import Path
from typing import List

from streamlit import _get_script_run_ctx

import streamlit_patches as st

st.sidebar.write("Common sidebar element")

ctx = _get_script_run_ctx()

"## Common header!"


def function_example():
    st.title("Example")
    st.write("This is a function!")


st.page("example_one.py", name="Home!", icon="🍔")

st.page("example_two.py", icon="⭐")

st.page("example_three.py", name="Custom name!", icon="🔥")

st.page("example_four.py", icon="🦊")

st.page(function_example, icon="🌊")
