from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Tuple

import streamlit as st
from PIL import Image

import certificate.config as c


@dataclass
class Certificate:
    template_image: str = "template"
    file_format: List[str] = field(
        default_factory=lambda: [".png", ".jpg"]
    )

    def generate(self):
        """Generate certificate based on content."""
        pass

    def save(self):
        """Save generated certificate."""
        pass

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
                            image_filepath.name + f
                            for f in self.file_format
                        ])
                    )
                 )
            else:
                setattr(self, "_template", image)
                return getattr(self, "_template")

    def _find_image(self):
        for f in self.file_format:
            filepath = c.IMAGE_TEMPLATE_DIR / (self.template_image + f)
            if (filepath).exists():
                return filepath
        return
