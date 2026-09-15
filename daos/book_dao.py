# -*- coding: utf-8 -*-

"""
Classe Dao[Book]
"""
from daos.autor_dao import AutorDao
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

from daos.editor_dao import EditorDao
from models.autor import Autor
from models.book import Book
from models.character import Character
from models.editor import Editor


@dataclass
class BookDao(Dao[Book]):

    @staticmethod
    def book_from_db(record) -> Book:
        """Construit un livre du modèle d'après son entité en BD"""

        # On récupère l'auteur correspondant à l'id_auteur
        autor: Autor = None
        id_autor = record['id_auteur']
        if id_autor is not None:
            autor = AutorDao().read(id_autor)

        # On récupère l'éditeur correspondant à l'id_editeur
        editor: Editor = None
        id_editor = record['id_editeur']
        if id_editor is not None:
            editor = EditorDao().read(id_editor)

        if (autor and editor) is not None:
            book: Book = Book(record['titre'], record['resume'], record['date_parution'], record['nb_pages'], record['ISBN'], record['prix_editeur'], autor, editor)
            book.id = record['id_livre']
            return book
        else:
            print("ERREUR l'auteur et l'éditeur ne peuvent pas être à null")
            return None

    def read(self, id_book: int) -> Optional[Character]:
        """Renvoie le livre correspondant à l'entité dont la clé primaire est id
           (ou None s'il n'a pu être trouvé)"""
        book: Optional[Book]

        try:
            with Dao.connection.cursor() as cursor:
                sql = "SELECT * FROM livre WHERE id_livre = %s"
                cursor.execute(sql, (id_book,))
                record = cursor.fetchone()
            if record is not None:
                book = self.book_from_db(record)
        except Exception as e:
            print(f"Exception : {e}")

        return book

    def read_all(self, id_selection: Optional[int] = None) -> list[Book]:
        """Renvoie l'ensemble des personnages de la BD."""
        books_list: list[Book] = []

        try:
            with Dao.connection.cursor() as cursor:

                sql = ("""\
                        SELECT * FROM livre L 
                        LEFT JOIN auteur A 
                        ON L.id_auteur = A.id_auteur 
                        LEFT JOIN editeur E
                        ON L.id_editeur = E.id_editeur 
                        """
                       )
                if id_selection is None:
                    cursor.execute(sql)
                else:
                    print("Recherche des livres via la sélection : Fonctionnalité à implémenter!")
                    #sql += "WHERE id_livre = %s"
                    #cursor.execute(sql, (id_book,))

                records = cursor.fetchall()

            for record in records:
                books_list.append(self.book_from_db(record))
        except Exception as e:
            print(f"Exception : {e}")

        return books_list

    def create(self, book: Book) -> None:
        print("Méthode non implémentée")

    def update(self, book: Book) -> None:
        print("Méthode non implémentée")

    def delete(self, book: Book) -> None:
        print("Méthode non implémentée")
