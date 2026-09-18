# -*- coding: utf-8 -*-

"""
Classe Dao[Autor]
"""
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional
from models.autor import Autor


@dataclass
class AutorDao(Dao[Autor]):

    @staticmethod
    def autor_from_db(record) -> Autor:
        """Construit un auteur du modèle d'après son entité en BD"""
        autor: Autor = Autor(record['nom'], record['prenom'], record['biographie'])
        autor.id = record['id_auteur']
        return autor

    def read(self, id_autor: int) -> Optional[Autor]:
        """Renvoie l'auteur correspondant à l'entité dont la clé primaire est id
           (ou None s'il n'a pu être trouvé)"""
        autor: Optional[Autor] = None

        try:
            with Dao.connection.cursor() as cursor:
                sql = "SELECT * FROM auteur A WHERE A.id_auteur = %s"
                cursor.execute(sql, (id_autor,))
                record = cursor.fetchone()
            if record is not None:
                autor = self.autor_from_db(record)
        except Exception as e:
            print(f"Exception : {e}")

        return autor

    def read_all(self) -> list[Autor]:
        """Renvoie l'ensemble des auteurs de la BD."""
        autors_list: list[Autor] = []

        try:
            with Dao.connection.cursor() as cursor:
                sql = "SELECT * FROM auteur;"
                cursor.execute(sql)

                records = cursor.fetchall()

                for record in records:
                    autors_list.append(self.autor_from_db(record))

        except Exception as e:
            print(f"Exception : {e}")

        return autors_list

    def create(self, autor: Autor) -> None:
        print("Méthode non implémentée")

    def update(self, autor: Autor) -> None:
        print("Méthode non implémentée")

    def delete(self, autor: Autor) -> None:
        print("Méthode non implémentée")
