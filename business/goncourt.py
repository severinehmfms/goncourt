# -*- coding: utf-8 -*-

"""
Classe Goncourt
"""

from dataclasses import dataclass, field
from datetime import date
from typing import Optional

from daos.autor_dao import AutorDao
from daos.book_dao import BookDao
from daos.character_dao import CharacterDao
from daos.editor_dao import EditorDao
from daos.jury_dao import JuryDao
from daos.selection_dao import SelectionDao
from models.autor import Autor
from models.book import Book
from models.character import Character
from models.editor import Editor
from models.jury import Jury
from models.selection import Selection


@dataclass
class Goncourt:
    """Couche métier de l'application du prix Goncourt,
    reprenant les cas d'utilisation et les spécifications fonctionnelles """

    # Constantes pour l'application
    SAISIE_INCORRECTE = "Saisie incorrecte. Merci de recommencer : "
    PRESS_ENTER = "Appuyez sur la touche 'Entrée' pour retourner au menu"

    def get_autor_by_id(self, id_autor: int) -> Autor:
        """ Fonction qui retourne l'objet Autor via son id """
        autor_dao: AutorDao = AutorDao()
        return autor_dao.read(id_autor)

    def get_autors_list(self) -> list[Autor]:
        """ Fonction qui retourne la liste des objets Autor """
        autor_dao: AutorDao = AutorDao()
        return autor_dao.read_all()

    def get_editor_by_id(self, id_editor: int) -> Editor:
        """ Fonction qui retourne l'objet Editor via son id """
        editor_dao: EditorDao = EditorDao()
        return editor_dao.read(id_editor)

    def get_editors_list(self) -> list[Editor]:
        """ Fonction qui retourne la liste des objets Editor """
        editor_dao: EditorDao = EditorDao()
        return editor_dao.read_all()

    def get_character_by_id(self, id_character: int) -> Character:
        """ Fonction qui retourne l'objet Character via son id """
        character_dao: CharacterDao = CharacterDao()
        return character_dao.read(id_character)

    def get_characters_list(self) -> list[Character]:
        """ Fonction qui retourne la liste des objets Character """
        character_dao: CharacterDao = CharacterDao()
        return character_dao.read_all()

    def get_book_by_id(self, id_book: int) -> Optional[Book]:
        """ Fonction qui retourne l'objet Book via son id """
        book_dao: BookDao = BookDao()
        return book_dao.read(id_book)

    def get_books_list(self) -> list[Book]:
        """ Fonction qui retourne la liste des objets Book """
        book_dao: BookDao = BookDao()
        return book_dao.read_all()

    def get_jury_by_id(self, id_jury: int) -> Optional[Jury]:
        """ Fonction qui retourne l'objet Jury via son id """
        jury_dao: JuryDao = JuryDao()
        return jury_dao.read(id_jury)

    def get_jurys_list(self) -> list[Jury]:
        """ Fonction qui retourne la liste des objets Jury """
        jury_dao: JuryDao = JuryDao()
        return jury_dao.read_all()

    def get_selection_by_id(self, num_selection: int) -> Selection:
        """ Fonction qui retourne l'objet Selection via son id """
        selection_dao: SelectionDao = SelectionDao()
        return selection_dao.read(num_selection)

    def get_selections_list(self) -> list[Selection]:
        """ Fonction qui retourne la liste des objets Selection """
        selection_dao: SelectionDao = SelectionDao()
        return selection_dao.read_all()

    def get_books_by_selection(self, num_selection: int) -> list[Book]:
        """ Fonction qui retourne la liste des livres correspondant à une sélection """
        book_dao: BookDao = BookDao()
        return book_dao.read_all(num_selection)

    def is_selection_already(self, num_selection: int) -> bool:
        """ Fonction qui retourne True si la selection comprend déjà le bon nombre de livres attendus, False sinon
        ==>Pour l'exercice, j'ai préféré considérer qu'il faut obligatoirement 8 livres pour la 2ème sélection,
        et obligatoirement 4 livres pour la troisième, et obligatoirement un lauréat pour la quatrième (=après le dernier scrutin)
        On considère donc comme déjà faite toute sélection qui comporte le nombre de livres attendu
        """
        #book_dao: BookDao = BookDao()
        return BookDao.is_nb_books_completed(num_selection)

    def add_book_to_selection(self,jury: Jury, id_book: int, selection: Selection) -> bool:
        """Fonction qui ajoute un livre à la sélection"""
        selection_dao: SelectionDao = SelectionDao()
        # print(f"On va ajouter le livre numéro {id_book} à la sélection {selection.nb_selection}")
        return selection_dao.add_book_to_selection(selection, id_book, jury)

    def update_nb_vote_by_book_selection(self, id_book: int, nb_votes_scrutin_final: int, nb_selection: Optional[int] = 3) -> bool:
        """Fonction qui met à jour le nombre de votes des livres de la 3ème sélection pour le dernier scrutin
        Sauf demande contraire , on force à 3 le numéro de la sélection concerné par la mise à jour des votes
        """
        selection_dao: SelectionDao = SelectionDao()
        # print(f"On va mettre le nombre de votes : {nb_votes_scrutin_final} pour la sélection {nb_selection} pour le livre {id_book}")
        return selection_dao.update_nb_vote_by_book_selection(id_book, nb_votes_scrutin_final, nb_selection)
