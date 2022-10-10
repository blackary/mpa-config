# Streamlit Multi-Page Apps v3

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blackary-mpa-config-streamlit-app-mpa-title-icon-i42dg6.streamlitapp.com/)

[Notion Doc](https://www.notion.so/streamlit/Draft-spec-to-fix-filename-issues-1c8ceb4d91b64280a28cb20531a121b0) (This is proposed solution #1)

### Summary

Another iteration of how MPA could work

`st.title` now _both_ inserts a page title and adds a custom title to the sidebar
`st.icon` is a new command which inserts a large icon and adds a custom icon to the sidebar

If you change either of these while on a page, auto-reload should also change the sidebar

On the initial page load, we simply use regex to find the first instances of st.title and st.icon, and use those if
they exist to pre-populate the icon and title in sidebar.
