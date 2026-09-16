# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List

from models.autor import Autor
from models.character import Character
from models.editor import Editor


@dataclass
class Book:
    """Livre"""
    title: str
    resume: str
    publication_date: date
    nb_pages: int
    isbn: int
    price: float
    nb_vote_final_round: int
    autor: Autor
    editor: Editor
    # Liste des personnages principaux du livre
    main_characters: list[Character]

    def __init__(self, title: str, resume: str, publication_date:date, nb_pages:int, isbn:int, price:float, autor:Autor, editor:Editor ) -> None:
        self.title = title
        self.resume = resume
        self.publication_date = publication_date
        self.nb_pages = nb_pages
        self.isbn = isbn
        self.price = price
        self.autor = autor
        self.editor = editor
        # On initialise les valeurs des attributs facultatifs
        self.nb_vote_final_round = 0
        self.main_characters = []

    def get_nb_voteFinalRound(self) -> int:
        return self.nb_vote_final_round

    def set_nb_vote_final_round(self, nb_vote_final_round: int) -> None:
        self.nb_vote_final_round = nb_vote_final_round

    def __str__(self) -> str:
        return f"{self.title} écrit par {self.autor.first_name} {self.autor.last_name}, édité par {self.editor.name} publié le {self.publication_date}, {self.nb_pages} pages, numéro ISBN {self.isbn}, prix : {self.price} \n Résumé : {self.resume} "
