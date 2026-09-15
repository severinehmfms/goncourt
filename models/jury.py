# -*- coding: utf-8 -*-

from dataclasses import dataclass

@dataclass
class Jury:
    """Membre du jury"""
    last_name: str
    first_name: str

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
