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
from models.editor import Editor
from models.selection import Selection


@dataclass
class BookDao(Dao[Book]):

    @staticmethod
    def book_from_db(record) -> Book:
        """Construit un livre du modèle d'après son entité en BD"""
        # On récupère l'auteur correspondant à l'id_auteur
        autor: Optional[Autor] = None
        id_autor = record['id_auteur']
        if id_autor is not None:
            autor = AutorDao().read(id_autor)

        # On récupère l'éditeur correspondant à l'id_editeur
        editor: Optional[Editor] = None
        id_editor = record['id_editeur']
        if id_editor is not None:
            editor = EditorDao().read(id_editor)

        if (autor and editor) is not None:
            book: Book = Book(record['titre'], record['resume'], record['date_parution'], record['nb_pages'], record['ISBN'], record['prix_editeur'], autor, editor)

            # Si le nombre de votes a été retourné par la requête (quand on demande les livres pour une sélection donnée), on l'enregistre aussi dans le livre
            if ('nb_votes_scrutin_final' in record and record['nb_votes_scrutin_final'] is not None):
                book.set_nb_vote_final_round(record['nb_votes_scrutin_final'])

            book.id = record['id_livre']
            return book
        else:
            print("ERREUR l'auteur et l'éditeur ne peuvent pas être à null")
            return None

    def read(self, id_book: int) -> Optional[Book]:
        """Renvoie le livre correspondant à l'entité dont la clé primaire est id
           (ou None s'il n'a pu être trouvé)"""
        book: Optional[Book] = None

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

    def read_all(self, num_selection: Optional[int] = None) -> list[Book]:
        """Renvoie l'ensemble des personnages de la BD."""
        books_list: list[Book] = []

        try:
            with Dao.connection.cursor() as cursor:
                # Requête si on demande tous les livres
                if num_selection is None:
                    sql = ("""\
                                            SELECT * FROM livre L 
                                            LEFT JOIN auteur A 
                                            ON L.id_auteur = A.id_auteur 
                                            LEFT JOIN editeur E
                                            ON L.id_editeur = E.id_editeur 
                                            """
                           )
                    cursor.execute(sql)
                # Requête si on demande les livres d'une sélection
                else:
                    sql = ("""\
                                            SELECT C.nb_votes_scrutin_final, L.*
                                            FROM choix C
                                            LEFT JOIN livre L
                                            ON C.id_livre = L.id_livre
                                            JOIN auteur A
                                            ON L.id_auteur = A.id_auteur
                                            JOIN editeur E
                                            ON L.id_editeur = E.id_editeur
                                            WHERE C.num_selection =  %s"""
                           )
                    cursor.execute(sql, (num_selection,))

                # On récupère les enregistrements retournés par la requête
                records = cursor.fetchall()

            # Pour chaque enregistremnet on enregistre le livre correspondant dans la liste
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

    def is_selection_completed(self, num_selection:int) -> bool:
        """ Méthode qui compare le nombre de livres déjà sélectionnés avec le nombre de livres attendus pour la sélection
        Renvoie true si le nombre de livres sélectionnés est égal au nombre de livres attendus, false sinon
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = ("""\
                        SELECT COUNT(C.id_livre) AS nombre_livres, S.nb_livres AS nb_livres_attendus
                        FROM choix C
                        LEFT JOIN livre L
                        ON C.id_livre = L.id_livre
                        LEFT JOIN selection S
                        ON C.num_selection = S.num_selection
                        WHERE C.num_selection =  %s"""
                       )
                cursor.execute(sql, (num_selection,))

                record = cursor.fetchone()
                nombre_livres = record['nombre_livres']
                nb_livres_attendus = record['nb_livres_attendus']
                if (nombre_livres == nb_livres_attendus):
                    return True
        except Exception as e:
            print(f"Exception : {e}")
        return False
