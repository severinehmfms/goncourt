# -*- coding: utf-8 -*-

from dataclasses import dataclass

@dataclass
class Jury:
    """Membre du jury"""
    last_name: str
    first_name: str
    id_jury: int

    def __init__(self, last_name: str, first_name: str) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.id_jury = 0

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
