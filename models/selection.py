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

    def __init__(self, nb_selection: int, selection_date:date, title: str, nb_books:int, jury:Jury, selected_books:List=None) -> None:
        self.nb_selection = nb_selection
        self.selection_date = selection_date
        self.title = title
        self.nb_books = nb_books
        self.jury = jury
        self.selected_books = selected_books if selected_books is not None else []

    def __str__(self) -> str:
        if (self.nb_selection == 1):
            selection_str = "Première sélection \n"
        elif (self.nb_selection == 2):
            selection_str = "Deuxième sélection \n"
        elif (self.nb_selection == 3):
            selection_str = "Troisième sélection \n"
        else:
            selection_str = "Lauréat \n"
        selection_str += f"{self.nb_books} livres - Date de la sélection : {self.selection_date} "
        if (len(self.selected_books) != 0):
            selection_str += f"\ Liste des livres : "
            for book in self.selected_books:
                selection_str += f"{book}"
        return selection_str