# -*- coding: utf-8 -*-

"""
Classe Dao[Character]
"""
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional
from models.character import Character


@dataclass
class CharacterDao(Dao[Character]):

    @staticmethod
    def character_from_db(record) -> Character:
        """Construit un personnage du modèle d'après son entité en BD"""
        character: Character = Character(record['nom'], record['prenom'])
        character.id = record['id_personnage']
        # TODO Récupérer le livre correspondant à l'id
        # record['id_livre']
        return character

    def read(self, id_character: int) -> Optional[Character]:
        """Renvoie le personnage correspondant à l'entité dont la clé primaire est id
           (ou None s'il n'a pu être trouvé)"""
        character: Optional[Character]

        try:
            with Dao.connection.cursor() as cursor:
                sql = "SELECT * FROM personnage WHERE id_personnage = %s"
                cursor.execute(sql, (id_character,))
                record = cursor.fetchone()
            if record is not None:
                character = self.character_from_db(record)
        except Exception as e:
            print(f"Exception : {e}")

        return character

    def read_all(self, id_book: Optional[int] = None) -> list[Character]:
        """Renvoie l'ensemble des personnages de la BD."""
        characters_list: list[Character] = []

        try:
            with Dao.connection.cursor() as cursor:

                sql = ("SELECT * FROM personnage P "
                       "LEFT JOIN livre L "
                       "ON P.id_livre = L.id_livre")
                if id_book is None:
                    cursor.execute(sql)
                else:
                    sql += "WHERE id_livre = %s"
                    cursor.execute(sql, (id_book,))

                records = cursor.fetchall()

            for record in records:
                characters_list.append(self.character_from_db(record))
        except Exception as e:
            print(f"Exception : {e}")

        return characters_list

    def create(self, character: Character) -> None:
        print("Méthode non implémentée")

    def update(self, character: Character) -> None:
        print("Méthode non implémentée")

    def delete(self, character: Character) -> None:
        print("Méthode non implémentée")
