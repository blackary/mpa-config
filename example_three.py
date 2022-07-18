from typing import List

import streamlit as st

from page_config import Page, configure_pages, standard_page_widgets

st.write("Example three")

st.stop()


pages: List[Page] = [
    {
        "name": "Home",
        "path": "streamlit_app.py",
        "icon": "🏠",
    },
    {
        "name": "Example One",
        "icon": "⭐",
    },
    {
        "name": "Example Two",
        "icon": "🦇",
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
