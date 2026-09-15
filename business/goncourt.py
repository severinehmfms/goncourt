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
from models.character import Character
from models.editor import Editor
from models.selection import Selection


@dataclass
class Goncourt:
    """Couche métier de l'application du prix Goncourt,
    reprenant les cas d'utilisation et les spécifications fonctionnelles """

    def get_autor_by_id(self, id_autor: int) -> Optional[Autor]:
        autor_dao: AutorDao = AutorDao()
        return autor_dao.read(id_autor)

    def get_autors_list(self) -> list[Autor]:
        autor_dao: AutorDao = AutorDao()
        return autor_dao.read_all()

    def get_editor_by_id(self, id_editor: int) -> Optional[Editor]:
        editor_dao: EditorDao = EditorDao()
        return editor_dao.read(id_editor)

    def get_editors_list(self) -> list[Editor]:
        editor_dao: EditorDao = EditorDao()
        return editor_dao.read_all()

    def get_character_by_id(self, id_character: int) -> Optional[Character]:
        character_dao: CharacterDao = CharacterDao()
        return character_dao.read(id_character)

    def get_characters_list(self) -> list[Editor]:
        character_dao: CharacterDao = CharacterDao()
        return character_dao.read_all()

    def get_book_by_id(self, id_book: int) -> Optional[Character]:
        book_dao: BookDao = BookDao()
        return book_dao.read(id_book)

    def get_books_list(self) -> list[Editor]:
        book_dao: BookDao = BookDao()
        return book_dao.read_all()

    def get_jury_by_id(self, id_jury: int) -> Optional[Jury]:
        jury_dao: JuryDao = JuryDao()
        return jury_dao.read(id_jury)

    def get_jurys_list(self) -> list[Editor]:
        jury_dao: JuryDao = JuryDao()
        return jury_dao.read_all()

    def get_selection_by_id(self, num_selection: int) -> Optional[Selection]:
        selection_dao: SelectionDao = SelectionDao()
        return selection_dao.read(num_selection)

    def get_selections_list(self) -> list[Editor]:
        selection_dao: SelectionDao = SelectionDao()
        return selection_dao.read_all()