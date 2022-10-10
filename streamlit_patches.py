import inspect
import re
from pathlib import Path
from time import sleep
from typing import Dict, Optional, Tuple

import requests
from streamlit import *
from streamlit import __version__, set_page_config
from streamlit import title as old_title
from streamlit import write
from streamlit.commands.page_config import get_random_emoji
from streamlit.delta_generator import DeltaGenerator
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit.util import calc_md5

set_page_config


@experimental_singleton
def get_icons() -> Dict[str, str]:
    url = "https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json"
    return requests.get(url).json()


def translate_icon(icon: str) -> str:
    """
    If you pass a name of an icon, like :dog:, translate it into the
    corresponding unicode character
    """
    icons = get_icons()
    if icon == "random":
        icon = get_random_emoji()
    elif icon[0] == icon[-1] == ":":
        icon = icon[1:-1]
        if icon in icons:
            return icons[icon]
    return icon


def scrape_page(path: Path) -> Tuple[Optional[str], Optional[str]]:
    text = path.read_text()

    try:
        title = re.findall(r"st\.title\((.*?)\)", text)[0].strip('"').strip("'")
    except IndexError:
        title = None
    try:
        icon = translate_icon(
            re.findall(r"st\.icon\((.*?)\)", text)[0].strip("'").strip('"')
        )
    except IndexError:
        icon = None

    return title, icon


def initial_sync(page_config: Dict[str, Dict[str, str]]):
    for page in page_config.values():
        title, icon = scrape_page(Path(page["script_path"]))
        if title:
            page["page_name"] = title
        if icon:
            page["icon"] = icon
        page["synced"] = "True"


def _title(body: str, anchor: Optional[str] = None) -> DeltaGenerator:
    path = inspect.stack()[1][1]
    page_script_hash = calc_md5(str(path))

    main_script_path = "streamlit_app.py"

    page_config = get_pages(main_script_path)

    if page_script_hash in page_config:
        this_page = page_config[page_script_hash]
        if body != this_page["page_name"]:
            this_page["page_name"] = body
            _on_pages_changed.send()
            sleep(0.1)
        if this_page.get("synced", "") != "True":
            initial_sync(page_config)
            _on_pages_changed.send()
            sleep(0.1)

    return old_title(body, anchor)


title = _title


def icon(page_icon: str):
    """
    Add an icon to the sidebar
    icon: The icon to be used for the page. Can either be the actual icon
        (e.g. 🔥) or with colons around the name (e.g. :fire:), or "random" for a random
        emoji
    """

    page_icon = translate_icon(page_icon)

    page_config = get_pages("streamlit_app.py")

    path = inspect.stack()[1][1]
    page_script_hash = calc_md5(str(path))

    if page_script_hash in page_config:
        if page_icon != page_config[page_script_hash]["icon"]:
            page_config[page_script_hash]["icon"] = page_icon
            _on_pages_changed.send()
            sleep(0.1)

    write("# " + page_icon)
