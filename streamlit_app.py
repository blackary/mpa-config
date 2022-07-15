from itertools import chain
from pathlib import Path
from typing import List

import streamlit as st
import yaml

from page_config import Page, configure_pages, get_page_config, standard_page_widgets

#standard_page_widgets()

#st.balloons()

#config = get_page_config()

#st.json([p.as_dict() for p in config])

st.title("Dynamic Pages!")

"⬅ Try switching pages"

pages: List[Page] = [{
    "name": "Home",
    "path": "streamlit_app.py",
    "icon": "🏠",
}, {
    "name": "Example One",
    "icon": "⭐",
}]

configure_pages(pages)


"Or, try swithcing to a single page"

if st.button("Switch to a single page"):
    _pages: List[Page] = [{
        "name": "Home",
        "path": "streamlit_app.py",
        "icon": "🏠",
    }]
    configure_pages(_pages)

    if st.button("Switch back to multiple pages"):
        configure_pages(pages)



_ = """
config = [p.as_dict() for p in get_page_config()]

for idx, page in enumerate(config.copy()):
    if st.checkbox(f"Remove {page['page_name']}"):
        config.pop(idx)

st.json(config)

#if st.checkbox("Remove second page"):
#    config.pop(1)

"""



#to_exclude = []

#names = [p.page_name for p in config]
#to_show = st.multiselect("Pages to show", names, default=names)

_ = """
for page in config:
    if not st.checkbox("Show page: " + page.page_name, True):
        to_exclude.append(page.page_hash)
"""


#pages_to_use = [p.as_dict() for p in config if p.page_name in to_show]

#configure_pages(pages_to_use)

st.stop()

"""
# Customizing Multi-Page Apps

This is an example repo that shows how you can customize the display of a multi-page
app through accessing a private method which sets up the sidebar.

Note that this does NOT require you to rename the individual python scripts, and that
the naming, ordering, and icons are all controlled by the page_config.yaml file.
"""

col1, col2 = st.columns(2)


with col1:
    "## `page_config.yaml`"
    config = Path("page_config.yaml").read_text()
    st.code(config)


with col2:
    "## Streamlit app files in repository"
    paths = chain(Path(".").glob("streamlit_app.py"), Path("pages").glob("*.py"))
    st.code("\n".join(str(p) for p in paths))
