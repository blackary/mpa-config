import streamlit as st

from page_show import clear_all_but_first_page, show_pages

default_pages = st.session_state.get("pages_to_show", None)

n_pages = len(default_pages) if default_pages is not None else 5

num_pages = st.slider("Number of pages", 1, 5, n_pages)

clear_all_but_first_page()

pages = ["streamlit_app", "example_one", "example_two", "example_three", "example_four"]

show_pages(pages[:num_pages])
