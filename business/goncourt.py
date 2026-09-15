# -*- coding: utf-8 -*-

"""
Classe Goncourt
"""

from dataclasses import dataclass, field
from datetime import date
from typing import Optional

from daos.autor_dao import AutorDao
from daos.editor_dao import EditorDao
from models.autor import Autor
from models.editor import Editor


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
