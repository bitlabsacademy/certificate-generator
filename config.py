import os
from pathlib import Path

CERT_FILENAME = os.getenv("CERT_FILENAME")
CERT_TARGET_DIR = Path(os.getenv("CERT_TARGET_DIR", "."))
CERT_COMPLETION_TEMPLATE = os.getenv("CERT_COMPLETION_TEMPLATE")
CERT_GRADUATION_TEMPLATE = os.getenv("CERT_GRADUATION_TEMPLATE")
CERT_OLD_TEMPLATE = os.getenv("CERT_OLD_TEMPLATE")
FONT_DIR = Path(os.getenv("FONT_DIR", "fonts"))
COMPETENCY_DIR = Path(os.getenv("COMPETENCY_DIR", "data"))

DICT_FONT_STYLE = {
    "graduation": {
        "class_title": {
            "font_type": "epilogue",
            "font_style": "semi-bold",
            "font_size": 14,
            "font-color": "192256",
            "coordinate": (50, 140),
        },
        "student_name": {
            "font_type": "epilogue",
            "font_style": "semi-bold",
            "font_size": 22,
            "font-color": "192256",
            "coordinate": (50, 220),
        },
        "competency_list": {
            "font_type": "epilogue",
            "font_style": "regular",
            "font_size": 12,
            "font-color": "192256",
            "coordinate": (50, 300),
        },
        "student_score": {
            "font_type": "epilogue",
            "font_style": "bold",
            "font_size": 18,
            "font-color": "6E40FB",
            "coordinate": (500, 266),
        },
        "certif_id": {
            "font_type": "space-mono",
            "font_style": "regular",
            "font_size": 10,
            "font-color": "FFFFFF",
            "coordinate": (705, 450),
        },
    },
    "completion": {
        "class_title": {
            "font_type": "epilogue",
            "font_style": "semi-bold",
            "font_size": 14,
            "font-color": "192256",
            "coordinate": (270, 500),
        },
        "student_name": {
            "font_type": "epilogue",
            "font_style": "semi-bold",
            "font_size": 28,
            "font-color": "192256",
            "coordinate": (270, 850),
        },
        "competency_list": {
            "font_type": "epilogue",
            "font_style": "regular",
            "font_size": 12,
            "font-color": "192256",
            "coordinate": (270, 1160),
        },
        "certif_id": {
            "font_type": "space-mono",
            "font_style": "regular",
            "font_size": 10,
            "font-color": "1A1C31",
            "coordinate": (2800, 1550),
        },
    },
    "old": {
        "class_title": {
            "font_type": "epilogue",
            "font_style": "semi-bold",
            "font_size": 16,
            "font-color": "192256",
            "coordinate": (50, 280),
        },
        "student_name": {
            "font_type": "epilogue",
            "font_style": "semi-bold",
            "font_size": 30,
            "font-color": "192256",
            "coordinate": (50, 160),
        },
        "certif_id": {
            "font_type": "space-mono",
            "font_style": "regular",
            "font_size": 10,
            "font-color": "1A1C31",
            "coordinate": (485, 514),
        },
    }
}
