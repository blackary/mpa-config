import json
from pathlib import Path
from typing import Iterable

import streamlit as st
from streamlit.server.server import Server
from streamlit.source_util import _on_pages_changed, get_pages

server = Server.get_current()

DEFAULT_PAGE = server._main_script_path

PAGES_PATH = ".pages.json"

if "pages_to_show" not in st.session_state:
    pages = get_pages(DEFAULT_PAGE)
    st.session_state.pages_to_show = [val["page_name"] for val in pages.values()]


def _get_all_pages():
    default_pages = get_pages(DEFAULT_PAGE)

    if PAGES_PATH.exists():
        saved_default_pages = json.loads(PAGES_PATH.read_text())
    else:
        saved_default_pages = default_pages.copy()
        PAGES_PATH.write_text(json.dumps(default_pages, indent=4))

    return saved_default_pages


def _update_pages():
    current_pages = get_pages(DEFAULT_PAGE)

    saved_pages = _get_all_pages()

    current_pages.clear()

    for key, val in saved_pages.items():
        if val["page_name"] in st.session_state.pages_to_show:
            current_pages[key] = val

    _on_pages_changed.send()


def show_pages(names: Iterable[str]):
    st.session_state.pages_to_show = names
    _update_pages()


def clear_all_but_first_page():
    saved_pages = _get_all_pages()
    first_page_name = list(saved_pages.values())[0]["page_name"]
    st.session_state["pages_to_show"] = [first_page_name]
    _update_pages()


def show_all_pages():
    saved_pages = _get_all_pages()
    names = [val["page_name"] for val in saved_pages.values()]
    st.session_state["pages_to_show"] = names

    _update_pages()


def show_page(name: str):
    current_pages = st.session_state.pages_to_show
    # Make sure the page to show ends up in the same order as before

    saved_pages = _get_all_pages()

    new_pages = []

    for key, val in saved_pages.items():
        if val["page_name"] in [name] + current_pages:
            new_pages.append(val["page_name"])

    st.session_state.pages_to_show = new_pages
    _update_pages()


def hide_page(name: str):
    st.session_state.pages_to_show.remove(name)
    _update_pages()
