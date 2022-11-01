import streamlit as st

from page_show import show_pages

"""# Dynamically Show and Hide Pages in MPA"""

with st.echo("above"):
    st.checkbox("Simulate logged-in user", key="logged_in")

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
Note that this checkbox doesn't just hide the sidebar, it actually removes the
pages from the page list. To see this, uncheck the checkbox and then
click on this link to try to visit [/example_one](/example_one). You'll get a
`Page Not Found` error
"""
