# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import ClassVar, Optional


@dataclass
class Autor:
    """Auteur du livre"""
    last_name: str
    first_name: str
    biography: str
    id_autor: Optional[int] = 0

    def __init__(self, last_name: str, first_name: str, biography="") -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.biography = biography

    def __str__(self) -> str:
        #return f"{self.first_name} {self.last_name} : \n {self.biography}"
        autor_str = f"{self.last_name} {self.first_name} "
        if (self.biography != ""): autor_str += f"\nBiographie de l'auteur : {self.biography} "
        return autor_str

