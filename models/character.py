# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass
class Character:
    """Personnage du livre"""
    name: str
    first_name: str

    def __init__(self, name: str, first_name="") -> None:
        self.name = name
        self.first_name = first_name

    def __str__(self) -> str:
        return f"{self.name} {self.first_name}"

