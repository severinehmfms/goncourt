# -*- coding: utf-8 -*-

"""
Classe Dao[Selection]
"""
from daos.book_dao import BookDao
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

from models.jury import Jury
from models.selection import Selection


@dataclass
class SelectionDao(Dao[Selection]):

    @staticmethod
    def selection_from_db(record) -> Selection:
        """Construit une sélection du modèle d'après son entité en BD"""
        selection: Selection = Selection(record['num_selection'], record['date_selection'], record['titre'], record['nb_livres'])

        # On va récupérer les livres correspondant à cette sélection (en utilisant le DAO de Livre)
        book_dao: BookDao = BookDao()
        books_list = book_dao.read_all(record['num_selection'])
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

    # nb_votes_scrutin_final: Optional[int] = None
    def add_book_to_selection(self, selection: Selection, id_book:int, jury:Jury) -> bool:
        """ Méthode qui permet d'ajouter dans la base de données un livre à la sélection (= une ligne dans la table choix)"""
        try:
            with Dao.connection.cursor() as cursor:
                sql = """INSERT INTO choix(id_livre, id_jury, num_selection) 
                      VALUES (%s, %s, %s)"""
                cursor.execute(sql, (
                    id_book,
                    jury.id_jury,
                    selection.nb_selection
                ))

                # récupération de l'id généré (pas utile)
                # id_choice = cursor.lastrowid

                Dao.connection.commit()

                # cursor.rowcount permet de savoir si une ligne a été modifiée
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Exception : {e}")
            Dao.connection.rollback()
            return False

    def update_nb_vote_by_book_selection(self, id_book:int, nb_votes:int, nb_selection:int) -> bool:
        """ Méthode qui va permettre de mettre à jour le nombre de votes par livre de la 3ème sélection """
        try:
            with Dao.connection.cursor() as cursor:
                sql = "UPDATE choix set nb_votes_scrutin_final=%s WHERE num_selection=%s AND id_livre=%s"
                cursor.execute(sql, (
                    nb_votes,
                    nb_selection,
                    id_book
                ))

                Dao.connection.commit()

                # cursor.rowcount permet de savoir si une ligne a été modifiée
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Exception : {e}")
            Dao.connection.rollback()
            return False

    def create(self, selection: Selection) -> None:
        print("Méthode create non implémentée")

    def update(self, selection: Selection) -> None:
        print("Méthode update non implémentée")

    def delete(self, selection: Selection) -> None:
        print("Méthode delete non implémentée")
