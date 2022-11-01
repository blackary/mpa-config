import streamlit as st

from page_show import show_pages

"""# Dynamically Show and Hide Pages in MPA"""


with st.echo("above"):
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        if st.button("Log out"):
            st.session_state.logged_in = False
            st.experimental_rerun()
    else:
        if st.button("Log in"):
            st.session_state.logged_in = True
            st.experimental_rerun()

    if st.session_state["logged_in"]:
        show_pages(
            [
                "streamlit_app",
                "example_one",
                "example_two",
                "example_three",
                "example_four",
            ]
        )
    else:
        show_pages(["streamlit_app"])

"""
Note that these log out / log in buttons don't just hide the sidebar, it actually
removes the pages from the page list. To see this, log out and then
click on this link to try to visit [/example_one](/example_one). You'll get a
`Page Not Found` error

See code here: https://github.com/blackary/mpa-config/tree/dynamic-hide
"""
