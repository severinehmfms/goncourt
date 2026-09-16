# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional


@dataclass
class Editor:
    """Editeur du livre"""
    name: str
    id_editor: Optional[int] = 0

    def __str__(self) -> str:
        return f"{self.name}"
