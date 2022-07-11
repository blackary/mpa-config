from pathlib import Path

import streamlit as st
from page_config import standard_page_widgets

standard_page_widgets()

st.code(__file__)

st.code(Path(__file__).read_text())
