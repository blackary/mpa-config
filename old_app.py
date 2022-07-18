import streamlit as st
from page_config import standard_page_widgets

# Add this on top of any page to make mpa-config work!
standard_page_widgets()

# Because this page is set to "visible: false", this app will not be displayed!
st.write("Boo, nobody will see me!")
