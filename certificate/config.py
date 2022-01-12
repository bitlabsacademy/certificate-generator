import os
from pathlib import Path

import streamlit as st


# IMAGE_TEMPLATE_DIR = Path(os.getenv("IMAGE_TEMPLATE_DIR", "templates"))
# FONT_DIR = Path(os.getenv("FONT_DIR", "fonts"))
# CONFIG_FILE = Path(os.getenv("CONFIG_FILE", "config"))
# OUT_DIR = Path(os.getenv("OUT_DIR", "outs"))

IMAGE_TEMPLATE_DIR = Path(
    os.getenv("IMAGE_TEMPLATE_DIR", st.secrets["IMAGE_TEMPLATE_DIR"])
)
FONT_DIR = Path(
    os.getenv("FONT_DIR", st.secrets["FONT_DIR"])
)
CONFIG_FILE = Path(
    os.getenv("CONFIG_FILE", st.secrets["CONFIG_FILE"])
)
OUT_DIR = Path(
    os.getenv("OUT_DIR", st.secrets["OUT_DIR"])
)


DICT_CONTENT = {
    "webinar": {
        "id": {"text": "", "pos": ()},
        "title": {"text": "", "pos": ()},
        "date": {"text": "", "pos": ()},
        "name": {"text": "", "pos": ()},
    },
    "workshop": {
        "id": {"text": "", "pos": ()},
        "title": {"text": "", "pos": ()},
        "date": {"text": "", "pos": ()},
        "name": {"text": "", "pos": ()},
    },
    "custom": {
        "id": {"text": "", "pos": ()},
        "title": {"text": "", "pos": ()},
        "date": {"text": "", "pos": ()},
        "name": {"text": "", "pos": ()},
    },
}
