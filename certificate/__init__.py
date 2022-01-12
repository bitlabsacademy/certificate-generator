from dataclasses import dataclass, field
from pathlib import Path, PosixPath
from textwrap import wrap
from time import time
from typing import Any, Dict, List, Tuple

import pandas as pd
import streamlit as st
from PIL import Image, ImageFont, ImageColor, ImageDraw

import certificate.config as c


@dataclass
class Certificate:
    name: str = field(default_factory=str)
    template_image: str = "template"
    file_format: List[str] = field(
        default_factory=lambda: [".png", ".jpg"]
    )

    def _find_image(self):
        for f in self.file_format:
            filepath = c.IMAGE_TEMPLATE_DIR / (self.template_image + f)
            if (filepath).exists():
                return filepath
        return

    def _get_text(self, recipient, component: str, prefix: str = "") -> str:
        if component == "id":
            text = prefix + f"{recipient.Index+1:03}"
            return text

        attr = str(getattr(recipient, component))
        return "\n".join(wrap(attr))

    def _get_fonts(self, config: Dict, component: str) -> Dict:
        font_type = ImageFont.truetype(
            (
                c.FONT_DIR
                / (
                    config[component + "_font_type"]
                    + ".ttf"
                )
            ).as_posix(),
            size=int(config[component + "_font_size"]),
        )
        font_color = ImageColor.getrgb(
            config[component + "_font_color"]
        )
        return {"font_type": font_type, "font_color": font_color}

    def generate(self, recipient, template, config: Dict,
                 prefix: str = "WBL0101"):
        """Generate certificate based on content.

        Args:
            recipient: file contains list of recipients as CSV file
            config (Dict): configuration for writing the components
            out_dir (str): directory the generated certificates are stored
            prefix (str): prefix used when saving the certificates
        """
        template_config = config[self.template_image]
        components = [
            component.split("_", 1) for component in template_config.keys()
        ]
        drawer = ImageDraw.Draw(template)

        for component in components:
            text = self._get_text(recipient, component[0], prefix)
            fonts = self._get_fonts(template_config, component[0])

            drawer.textsize(text, font=fonts["font_type"])
            drawer.text(
                template_config[component[0] + "_loc"],
                text=text,
                anchor="la",
                font=fonts["font_type"],
                fill=fonts["font_color"]
            )

        setattr(self, "certificate_", template)
        return template

    def save(self, recipient, prefix: str = "WBL0101",
             out_dir: PosixPath = Path()):
        """Save generated certificate."""
        out_dir.mkdir(exist_ok=True)
        prefix_text = self._get_text(recipient, "id", prefix)
        filename = (out_dir / (prefix_text + "_" + self.name)).as_posix()
        self.certificate_.save(filename + ".png")
        return

    @property
    def template(self):
        img = self._find_image()
        if not hasattr(self, "_template"):
            try:
                image = Image.open(img)
            except AttributeError:
                st.error(
                    "Cannot find any of these files: {}".format(
                        ", ".join([
                            img.name + f
                            for f in self.file_format
                        ])
                    )
                 )
            else:
                setattr(self, "_template", image)
                return getattr(self, "_template")

