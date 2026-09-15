# -*- coding: utf-8 -*-

from dataclasses import dataclass
from models.jury import Jury

@dataclass
class President(Jury):
    """Président du jury"""

    def __str__(self) -> str:
        return f"Président : {self.first_name} {self.last_name}"
