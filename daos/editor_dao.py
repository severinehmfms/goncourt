# -*- coding: utf-8 -*-

"""
Classe Dao[Editor]
"""
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional
from models.editor import Editor


@dataclass
class EditorDao(Dao[Editor]):

    @staticmethod
    def editor_from_db(record) -> Editor:
        """Construit un éditeur du modèle d'après son entité en BD"""
        editor: Editor = Editor(record['nom_editeur'])
        editor.id = record['id_editeur']
        return editor

    def read(self, id_editor: int) -> Optional[Editor]:
        """Renvoie l'éditeur correspondant à l'entité dont la clé primaire est id
           (ou None s'il n'a pu être trouvé)"""
        editor: Optional[Editor]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM editeur WHERE id_editeur = %s"
            cursor.execute(sql, (id_editor,))
            record = cursor.fetchone()
        if record is not None:
            autor = self.editor_from_db(record)
        else:
            autor = None

        return autor

    def read_all(self) -> list[Editor]:
        """Renvoie l'ensemble des éditeurs de la BD."""
        editors_list: list[Editor] = []

        with Dao.connection.cursor() as cursor:
           sql = "SELECT * FROM editeur;"
           cursor.execute(sql)

           records = cursor.fetchall()

        for record in records:
            editors_list.append(self.editor_from_db(record))

        return editors_list


    def create(self, editor: Editor) -> int:
        print("Méthode non implémentée")


    def update(self, editor: Editor) -> bool:
        print("Méthode non implémentée")


    def delete(self, editor: Editor) -> bool:
        print("Méthode non implémentée")

