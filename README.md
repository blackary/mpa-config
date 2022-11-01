# Streamlit Multi-Page Configuration

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mpa-config.streamlitapp.com/)

<img width="600" src="https://user-images.githubusercontent.com/7164864/178483961-1f9abf49-eb44-455f-9362-37951daf055a.gif">

### Summary

Streamlit recently [released multi-page apps](https://blog.streamlit.io/introducing-multipage-apps/) 🎉 where page filenames are the source of truth for page settings.

In this repository, we show a prototype of a page_show module which controls which pages are visible.

This module contains the following functions:

In this repository, we show a prototype on how to use a [page_config.yaml](https://github.com/blackary/mpa-config/blob/main/page_config.yaml) to control the ordering, icons, and nesting of the pages in the sidebar of a multi-page Streamlit app.

Main features include:

- `show_pages(<list_of_pages>)`
- `clear_all_but_first_page()`
- `show_all_pages()`
- `show_page(<page_name>)` -- adds one page to list of visible pages
- `hide_page(<page_name>)` -- hides one page from the list of visible pages
