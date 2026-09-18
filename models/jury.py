# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional


@dataclass
class Jury:
    """Membre du jury"""
    last_name: str
    first_name: str
    id_editor: Optional[int] = 0
    id_jury: Optional[int] = 0

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
