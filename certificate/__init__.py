from dataclasses import dataclass, field
from typing import Any, Dict, Tuple


@dataclass
class Certificate:
    template_image: str = "template.png"
    content: Dict[str, Dict[str, Any]] = field(default_factory=dict)

    def generate(self):
        """Generate certificate based on filler."""
        pass

    def save(self):
        """Save generated certificate."""
        pass
