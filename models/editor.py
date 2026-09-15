# -*- coding: utf-8 -*-

from dataclasses import dataclass

@dataclass
class Editor:
    """Editeur du livre"""
    name: str

    def __str__(self) -> str:
        return f"{self.name}"
