# Streamlit Multi-Page Configuration

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mpa-config.streamlitapp.com/)

<img width="600" src="https://user-images.githubusercontent.com/7164864/178483961-1f9abf49-eb44-455f-9362-37951daf055a.gif">

### Summary

Streamlit recently [released multi-page apps](https://blog.streamlit.io/introducing-multipage-apps/) 🎉 where page filenames are the source of truth for page settings.

In this repository, we show a prototype on how to use a [page_config.yaml](https://github.com/blackary/mpa-config/blob/main/page_config.yaml) to control the ordering, icons, and nesting of the pages in the sidebar of a multi-page Streamlit app.

Main features include:

- **Decoupling page settings from filenames.** No need to use indices or emojis in filenames to handle page titles, icons or ordering! You can name your Python scripts however you want.
- **Controling the order of the pages.** Adding pages in the config in the order you want them to appear in the app.
- **Nesting related pages within a "section".** Using `sections` in page_config.yaml will add un-clickable placeholders that group pages together.
- **Automatically adding the icon and title at the top of each page.** Bringing consistency to your pages!

⚠️ This project depends on an API that may change, and is not designed to be used this way,
so this will probably NOT work long-term.

### Get started

The easiest way to get started with this repo is to:

1. Clone the repo `git clone https://github.com/blackary/mpa-config.git`
2. Change your working directory to the repo `cd mpa-config`
3. Install requirements `pip install -r requirements.txt`
4. Run the Streamlit app `streamlit run streamlit_app.py`
5. Play around with the page_config.yaml!

Then, when you get the hang of how the page_config.yaml works and you want to implement the same functionality into your own Streamlit app, you can:

1. Copy the page_config.py file into your own Streamlit app
2. Make your own page_config.yaml file in the same directory with your apps' information
3. Import and add standard_page_widgets() to the top of your page scripts (in /pages)

### Documentation

#### In your page .py scripts:

All it takes for your app to support this is to add this little Python code on top of all your page scripts:

```python
import streamlit as st
from page_config import standard_page_widgets

# Add this on top of any page to make mpa-config work!
standard_page_widgets()
```

#### In the page_config.yaml

Supported parameters in page_config.yaml for `pages`:

- page_name: Page name.
- icon: Emoji you want to use as an icon
- created_date: App automatically adds a 🆕 flag to the page title if it is under 30 days old!
- script_path: Path to your Streamlit script for that page. Defaults to `snake_case(page_name).py`
- layout: Choose between 'wide' or 'centered'. Defaults to `'centered'`
- deprecated: If true, the page will not be displayed in the app. Defaults to `'false'`

Supported parameters in page_config.yaml for `sections`:

- name: Section name
- icon: Emoji you want to use as an icon
