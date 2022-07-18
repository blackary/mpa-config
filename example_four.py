from tkinter import W
from typing import List

import streamlit as st
from streamlit import StreamlitAPIException, _get_script_run_ctx

from page_config import Page, configure_pages, standard_page_widgets

st.title("Four!")

st.write("Example four")

st.stop()

ctx = _get_script_run_ctx()
st.write(ctx)


# pages: List[Page] = [{
pages = [
    {
        "name": "Home",
        "path": "streamlit_app.py",
        "icon": "🏠",
    },
    {
        "name": "Example Three",
        "icon": "🦊",
    },
    {
        "name": "Example Four",
        "icon": "🦋",
    },
]

configure_pages(pages)
