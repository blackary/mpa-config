# Streamlit Multi-Page Apps v2

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mpa-v2.streamlitapp.com/)

### Summary

Streamlit recently [released multi-page apps](https://blog.streamlit.io/introducing-multipage-apps/) 🎉 where page filenames are the source of truth for page settings.

In this repository, we show a prototype on how a new widget, `st.page`, could be used to populate the sidebar. This is very different from the current MPA, because
the main app script (in this case, streamlit_app.py) always runs, and then the page-specific code. This allows you to have easy control over which pages are loaded, and in what order, as well as have common functionality (e.g. a common sidebar) to be defined just once, and not repeated in each page.

In effect, the code that runs is always streamlit_app.py + one of the other app scripts (or functions).

More details available at this [page](https://www.notion.so/streamlit/Johannes-MPA-v2-idea-1869aafe213b45fabb090db9cae845c1)
