import os
from pathlib import Path


IMAGE_TEMPLATE_DIR = Path(os.getenv("IMAGE_TEMPLATE_DIR", "templates"))
FONT_DIR = Path(os.getenv("FONT_DIR", "fonts"))
CONFIG_FILE = Path(os.getenv("CONFIG_FILE", "config"))
OUT_DIR = Path(os.getenv("OUT_DIR", "outs"))


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
