# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from datetime import date
from typing import Optional


@dataclass
class Autor:
    """Auteur du livre"""
    last_name: str
    first_name: str
    biography: str
    #biography: Optional[str] = field(default=None, init="")

    def __init__(self, last_name: str, first_name: str, biography="") -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.biography = biography
        #if (biography is not None): self.biography = biography

    def __str__(self) -> str:
        #return f"{self.first_name} {self.last_name} : \n {self.biography}"
        autor_str = f"{self.name} {self.last_name} "
        if (self.biography != ""): autor_str += f"\ Biographie de l'auteur : {self.biography} "
        return autor_str
