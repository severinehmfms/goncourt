# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from datetime import date
from typing import List
from models.book import Book
from models.jury import Jury


@dataclass
class Selection:
    """Sélection"""
    nb_selection: int
    selection_date: date
    title: str
    nb_books: int
    jury: Jury
    # Liste des personnages principaux du livre
    selected_books: list[Book]

    def __init__(self, nb_selection: int, selection_date:date, title: str, nb_books:int, jury:Jury=None, selected_books:List=None) -> None:
        """ Constructeur """
        self.nb_selection = nb_selection
        self.selection_date = selection_date
        self.title = title
        self.nb_books = nb_books
        self.jury = jury
        self.selected_books = selected_books if selected_books is not None else []

    def get_jury(self):
        """ Renvoie le jury qui effectue la sélection"""
        return self.jury

    def set_jury(self, jury: Jury) -> None:
        """ Met à jour le jury qui effectue la sélection"""
        self.jury = jury

    def __str__(self) -> str:
        selection_str = f"{self.title} - {self.nb_books} livres - Date de la sélection : {self.selection_date} \n"
        if (self.selected_books is not None) and (len(self.selected_books) != 0):
            selection_str += f"Liste des livres : \n "
            selection_str += "------------------------------------------------------\n"
            for book in self.selected_books:
                selection_str += f"{book}"
        return selection_str