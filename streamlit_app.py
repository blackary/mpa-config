from itertools import chain
from pathlib import Path
from tkinter import W

import streamlit as st
import yaml

from page_config import get_config_file, standard_page_widgets

standard_page_widgets()

st.balloons()


"""
# Customizing Multi-Page Apps

This is an example repo that shows how you can customize the display of a multi-page
app through accessing a private method which sets up the sidebar.

Note that this does NOT require you to rename the individual python scripts, and that
the naming, ordering, and icons are all controlled by the page_config.yaml file.
"""

col1, col2 = st.columns(2)


with col1:
    "## `page_config.yaml`"
    config = Path("page_config.yaml").read_text()
    st.code(config)


with col2:
    "## python files in repository"
    paths = chain(Path(".").glob("streamlit_app.py"), Path("pages").glob("*.py"))
    for path in paths:
        st.code(path)
