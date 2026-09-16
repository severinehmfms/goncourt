# -*- coding: utf-8 -*-

"""
Classe Dao[Selection]
"""
from daos.book_dao import BookDao
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

from models.book import Book
from models.selection import Selection


@dataclass
class SelectionDao(Dao[Selection]):

    @staticmethod
    def selection_from_db(record) -> Selection:
        """Construit une sélection du modèle d'après son entité en BD"""
        selection: Selection = Selection(record['num_selection'], record['date_selection'], record['titre'], record['nb_livres'])

        # On va récupérer les livres correspondant à cette sélection (en utilisant le DAO de Livre)
        book_dao: BookDao = BookDao()
        books_list = book_dao.read_all(record['num_selection']);
        selection.selected_books = books_list

        return selection

    def read(self, num_selection: int) -> Optional[Selection]:
        """Renvoie la sélection correspondant à l'entité dont la clé primaire est id
           (ou None s'il n'a pu être trouvé)"""
        selection: Optional[Selection] = None

        try:
            with Dao.connection.cursor() as cursor:
                sql = "SELECT * FROM selection WHERE num_selection = %s"
                cursor.execute(sql, (num_selection,))
                record = cursor.fetchone()
            if record is not None:
                selection = self.selection_from_db(record)
        except Exception as e:
            print(f"Exception : {e}")

        return selection

    def read_all(self) -> list[Selection]:
        """Renvoie l'ensemble des sélections de la base de données."""
        selections_list: list[Selection] = []

        try:
            with Dao.connection.cursor() as cursor:
                sql = "SELECT * FROM selection;"
                cursor.execute(sql)

                records = cursor.fetchall()

                for record in records:
                    selections_list.append(self.selection_from_db(record))

        except Exception as e:
            print(f"Exception : {e}")

        return selections_list

    def create(self, selection: Selection) -> None:
        print("Méthode non implémentée")

    def update(self, selection: Selection) -> None:
        print("Méthode non implémentée")

    def delete(self, selection: Selection) -> None:
        print("Méthode non implémentée")
