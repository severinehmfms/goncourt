# -*- coding: utf-8 -*-

"""
Classe Dao[Jury]
"""
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional
from models.jury import Jury
from models.president import President


@dataclass
class JuryDao(Dao[Jury]):

    @staticmethod
    def jury_from_db(record) -> Jury:
        """Construit un membre du jury du modèle d'après son entité en BD"""
        if record['is_president']:
            # jury: President = President(record['nom'], record['prenom'])
            jury = President(record['nom'], record['prenom'])
        else:
            # jury: Jury = Jury(record['nom'], record['prenom'])
            jury = Jury(record['nom'], record['prenom'])

        jury.id_jury = record['id_jury']
        return jury

    def read(self, id_jury: int) -> Optional[Jury]:
        """Renvoie le jury correspondant à l'entité dont la clé primaire est id
           (ou None s'il n'a pu être trouvé)"""
        jury: Optional[Jury] = None

        try:
            with Dao.connection.cursor() as cursor:
                sql = "SELECT * FROM jury WHERE id_jury = %s"
                cursor.execute(sql, (id_jury,))
                record = cursor.fetchone()
            if record is not None:
                jury = self.jury_from_db(record)
        except Exception as e:
            print(f"Exception : {e}")

        return jury

    def read_all(self) -> list[Jury]:
        """Renvoie l'ensemble des membres du jury de la base de données."""
        jurys_list: list[Jury] = []

        try:
            with Dao.connection.cursor() as cursor:
                sql = "SELECT * FROM jury;"
                cursor.execute(sql)

                records = cursor.fetchall()

                for record in records:
                    jurys_list.append(self.jury_from_db(record))

        except Exception as e:
            print(f"Exception : {e}")

        return jurys_list

    def create(self, jury: Jury) -> None:
        print("Méthode create non implémentée")

    def update(self, jury: Jury) -> None:
        print("Méthode update non implémentée")

    def delete(self, jury: Jury) -> None:
        print("Méthode delete non implémentée")
