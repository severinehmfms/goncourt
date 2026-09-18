# -*- coding: utf-8 -*-

"""
Classe Goncourt
"""

from dataclasses import dataclass
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
from models.president import President
from models.selection import Selection


@dataclass
class Goncourt:
    """Couche métier de l'application du prix Goncourt,
    reprenant les cas d'utilisation et les spécifications fonctionnelles """

    # Constantes pour l'application
    SAISIE_INCORRECTE = "Saisie incorrecte. Merci de recommencer : "
    PRESS_ENTER = "Appuyez sur la touche 'Entrée' pour retourner au menu"
    ERREUR_SELECTION = "ERREUR lors de la récupération de la sélection."

    @staticmethod
    def get_autor_by_id(id_autor: int) -> Optional[Autor]:
        """ Fonction qui retourne l'objet Autor via son id """
        autor_dao: AutorDao = AutorDao()
        return autor_dao.read(id_autor)

    @staticmethod
    def get_autors_list() -> list[Autor]:
        """ Fonction qui retourne la liste des objets Autor """
        autor_dao: AutorDao = AutorDao()
        return autor_dao.read_all()

    @staticmethod
    def get_editor_by_id(id_editor: int) -> Optional[Editor]:
        """ Fonction qui retourne l'objet Editor via son id """
        editor_dao: EditorDao = EditorDao()
        return editor_dao.read(id_editor)

    @staticmethod
    def get_editors_list() -> list[Editor]:
        """ Fonction qui retourne la liste des objets Editor """
        editor_dao: EditorDao = EditorDao()
        return editor_dao.read_all()

    @staticmethod
    def get_character_by_id(id_character: int) -> Optional[Character]:
        """ Fonction qui retourne l'objet Character via son id """
        character_dao: CharacterDao = CharacterDao()
        return character_dao.read(id_character)

    @staticmethod
    def get_characters_list() -> list[Character]:
        """ Fonction qui retourne la liste des objets Character """
        character_dao: CharacterDao = CharacterDao()
        return character_dao.read_all()

    @staticmethod
    def get_book_by_id(id_book: int) -> Optional[Book]:
        """ Fonction qui retourne l'objet Book via son id """
        book_dao: BookDao = BookDao()
        return book_dao.read(id_book)

    @staticmethod
    def get_books_list() -> list[Book]:
        """ Fonction qui retourne la liste des objets Book """
        book_dao: BookDao = BookDao()
        return book_dao.read_all()

    @staticmethod
    def get_jury_by_id(id_jury: int) -> Optional[Jury]:
        """ Fonction qui retourne l'objet Jury via son id """
        jury_dao: JuryDao = JuryDao()
        return jury_dao.read(id_jury)

    @staticmethod
    def get_president_by_id(id_jury: int) -> Optional[President]:
        """Retourne le président correspondant à son id."""
        jury = Goncourt.get_jury_by_id(id_jury)

        if isinstance(jury, President):
            return jury

        return None

    @staticmethod
    def get_jurys_list() -> list[Jury]:
        """ Fonction qui retourne la liste des objets Jury """
        jury_dao: JuryDao = JuryDao()
        return jury_dao.read_all()

    @staticmethod
    def get_selection_by_id(num_selection: int) -> Optional[Selection]:
        """ Fonction qui retourne l'objet Selection via son id """
        selection_dao: SelectionDao = SelectionDao()
        return selection_dao.read(num_selection)

    @staticmethod
    def get_selections_list() -> list[Selection]:
        """ Fonction qui retourne la liste des objets Selection """
        selection_dao: SelectionDao = SelectionDao()
        return selection_dao.read_all()

    @staticmethod
    def get_books_by_selection(num_selection: int) -> list[Book]:
        """ Fonction qui retourne la liste des livres correspondant à une sélection """
        book_dao: BookDao = BookDao()
        return book_dao.read_all(num_selection)

    @staticmethod
    def is_selection_already(num_selection: int) -> bool:
        """ Fonction qui retourne True si la selection comprend déjà le bon nombre de livres attendus, False sinon
        ==>Pour l'exercice, j'ai considéré qu'il faut obligatoirement 8 livres pour la 2ème sélection,
        et obligatoirement 4 livres pour la troisième, et un seul lauréat pour la quatrième
        On considère donc comme déjà faite toute sélection qui comporte le nombre de livres attendu
        """
        return BookDao.is_nb_books_completed(num_selection)

    @staticmethod
    def add_book_to_selection(jury: Jury, id_book: int, selection: Selection) -> bool:
        """ Fonction qui ajoute un livre à la sélection """
        return SelectionDao.add_book_to_selection(selection, id_book, jury)

    @staticmethod
    def update_nb_vote_by_book_selection(id_book: int, nb_votes_scrutin_final: int, nb_selection: int = 3) -> bool:
        """Fonction qui met à jour le nombre de votes des livres de la 3ème sélection pour le dernier scrutin
        Sauf demande contraire , on force à 3 le numéro de la sélection concerné par la mise à jour des votes
        """
        return SelectionDao.update_nb_vote_by_book_selection(id_book, nb_votes_scrutin_final, nb_selection)
