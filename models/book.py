# -*- coding: utf-8 -*-

from dataclasses import dataclass
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
    autor: Autor
    editor: Editor
    id_book: Optional[int] = 0
    nb_vote_final_round: Optional[int] = 0
    # Liste des personnages principaux du livre
    main_characters: Optional[list[Character]] = None

    def __init__(self, title: str, resume: str, publication_date: date, nb_pages: int, isbn: int,
                 price: float, autor: Autor, editor: Editor) -> None:
        self.title = title
        self.resume = resume
        self.publication_date = publication_date
        self.nb_pages = nb_pages
        self.isbn = isbn
        self.price = price
        self.autor = autor
        self.editor = editor
        # On initialise la valeur de la liste des personnages
        self.main_characters = []

    def get_nb_votes_final_round(self) -> Optional[int]:
        return self.nb_vote_final_round

    def set_nb_vote_final_round(self, nb_vote_final_round: int) -> None:
        self.nb_vote_final_round = nb_vote_final_round

    def get_main_characters(self) -> Optional[List[Character]]:
        return self.main_characters

    def set_main_characters(self, main_characters: List[Character]) -> None:
        self.main_characters = main_characters

    def __str__(self) -> str:
        if self.id_book == 0:
            book_str = ""
        else:
            book_str = f"\n{self.id_book}\n"
        book_str += (f"""TITRE : {self.title} 
Ecrit par {self.autor} 
Edité par {self.editor}
Publié le {self.publication_date} - numéro ISBN {self.isbn} 
Prix : {self.price} - {self.nb_pages} pages \n""")
        book_str += f"Résumé : {self.resume}\n"
        if self.main_characters is not None and len(self.main_characters) > 0:
            book_str += "Personnages principaux : \n"
            for personnage in self.main_characters:
                book_str += str(personnage)
        book_str += "------------------------------------------------------"
        return book_str
