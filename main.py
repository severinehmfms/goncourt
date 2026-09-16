#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion du prix Goncourt 2026
"""

from business.goncourt import Goncourt
from daos import jury_dao
from models.book import Book
from models.jury import Jury
from models.president import President
from models.selection import Selection



def get_int_input(prompt, min_int, max_int):
    """Demande à l'utilisateur de saisir un entier compris entre min_int et max_int."""
    user_input = input(prompt).strip()

    while not user_input.isdigit() or not min_int <= int(user_input) <= max_int:
        user_input = input("Saisie incorrecte. Merci de recommencer : ").strip()

    return int(user_input)


def input_menu(items, multiline = False):
    """Demande à l'utilisateur de choisir un item dans un menu.
    Le choix 0 permet toujours de quitter.
    Les options fournies en paramètre commencent à 1.

    param items : liste des options du menu
    param multiline : affiche le menu sur une seule ligne si False.
    """
    separator = "\n" if multiline else " "
    menu = "Menu :\n"
    menu += "- 0 Quitter"
    menu += separator
    for numero, option in enumerate(items, start=1):
        menu += f"- {numero} {option} {separator}"
    menu += "\n"
    return get_int_input(menu, 0, len(items))


def main() -> None:
    """Programme principal."""
    print("""--------------------------    
Prix Goncourt 2026    
--------------------------""")

    goncourt_instance: Goncourt = Goncourt()

    # On récupère le President, pour l'instant id en dur
    president: President = goncourt_instance.get_jury_by_id(1)
    # print(president)

    # Menu de l'application
    menu = [
        "Visiteur : Afficher la liste des membres du jury",
        "Visiteur : Afficher les livres des sélections déjà passées",
        "Président : Choisir les livres pour la 2ème ou la 3ème sélection",
        "Président : Après le dernier scrutin, indiquer les votes pour les livres et le lauréat"
    ]
    choix = -1
    # On ne sort pas du programme tant que l'utilisateur ne l'a pas spécifié
    while (choix != 0):
        # On récupère le choix de l'utilisateur par rapport au menu
        choix = input_menu(menu, True)

        # On vérifie l'état des sélections
        is_selection_2_already = goncourt_instance.is_selection_already(2)
        is_selection_3_already = goncourt_instance.is_selection_already(3)
        is_selection_4_already = goncourt_instance.is_selection_already(4)

        match choix:
            case 1:
                print("****************** Liste des membres du jury ******************")
                list_jurys: list[Jury] = goncourt_instance.get_jurys_list()
                for j in list_jurys:
                    print(j)
                input("Appuyez sur la touche 'Entrée' pour retourner au menu")
            case 2:
                print("****************** Sélections déjà passées ******************")
                num_selection = get_int_input("Entrez le numéro de la sélection demandée : 1,2,3 ou 4 pour voir le lauréat\n", 1, 4)
                selection: Selection = goncourt_instance.get_selection_by_id(num_selection)
                print(selection)
                if (not goncourt_instance.is_selection_already(num_selection)):
                    print(f"Cette sélection n'a pas encore été effectuée, il faudra attendre le {selection.selection_date} pour voir les livres qui auront été choisis")
                input("Appuyez sur la touche 'Entrée' pour retourner au menu")
            case 3:
                print("****************** Choix des livres pour la 2ème puis la 3ème sélection ******************")
                num_selection = 2

                # On vérifie si la deuxième ET la troisième sélection ont pas déjà été faites
                if (is_selection_2_already and is_selection_3_already):
                    print("ERREUR - Les deux sélections ont déjà été renseignées, ce n'est plus possible de le faire.")
                    input("Appuyez sur la touche 'Entrée' pour retourner au menu")
                    continue

                # Si la 2ème sélection a déjà été faite, on va faire la troisième
                elif (is_selection_2_already):
                    num_selection = 3

                print(f"Vous allez choisir les livres pour la sélection numéro {num_selection} : ")
                selection: Selection = goncourt_instance.get_selection_by_id(num_selection)
                print(selection)

                #Pour la deuxième sélection, on va afficher les livres de la 1ère sélection, et pour la troisième sélection on va afficher les livres de la 2ème sélection !
                print("Voici les livres disponibles : ")
                list_books_availables: list[Book] = goncourt_instance.get_books_by_selection(num_selection-1)
                for b in list_books_availables:
                    print(b)

                print(f"Vous allez choisir {selection.nb_books} livres parmi les livres proposés ci-dessus.")
                list_id_books_selected: list[int] = []
                for i in range(0, selection.nb_books):
                    # On demande au président le numéro du livre qu'il souhaite ajouter à la sélection
                    # TODO Mis 16 en dur car c'est le numéro du dernier livre, mais idéalement il faudrait vérifier que le numéro de livre choisi
                    # Fait partie de la liste des livres de la sélection précédente (list_books_availables)
                    # Mais pour ça faut faire fonction spéciale input avec les tests qui vont bien et je manque de temps
                    id_book_choisi = get_int_input("Entrez le numéro d'un livre à ajouter à la sélection \n", 1, 16)
                    # TODO Mettre en place une vérification si un numéro a été choisi deux fois : peur de manquer de temps pour le faire !!!
                    #  (idem trois lignes plus haute dans fonction spécifique)
                    list_id_books_selected.append(id_book_choisi)

                # On appelle la fonction métier qui va ajouter le livre à cette sélection
                for id in list_id_books_selected:
                    # print(f"On va ajouter le livre numéro {id} à la base")
                    goncourt_instance.add_book_to_selection(president, id, selection)

            case 4:
                print("****************** Saisie des votes pour les livres de la dernière sélection, et attribution du lauréat ******************")
                # On vérifie si la deuxième ET la troisième sélection ont pas déjà été faites
                if (not is_selection_2_already and not is_selection_3_already):
                    print("ERREUR - Les sélections n'ont pas encore toutes été renseignées, il n'est pas encore possible de réaliser cette action.")
                    input("Appuyez sur la touche 'Entrée' pour retourner au menu")
                    continue
                # On vérifie que la sélection du lauréat n'a pas déjà été effectuée
                elif (is_selection_4_already):
                    print("ERREUR - Les votes de la dernière sélection et la désignation du lauréat ont déjà été effectués, il est impossible de réaliser cette action.")
                    input("Appuyez sur la touche 'Entrée' pour retourner au menu")
                    continue
                else:
                    num_selection = 4
                    selection: Selection = goncourt_instance.get_selection_by_id(num_selection)
                    print(selection)

                    # TODO Afficher chaque livre de la troisième sélection et demander le nombre de votes pour chaque livre

                    # TODO Afficher la liste des 4 livres, et demander au Président le numéro du lauréat

                    # TODO Enregistrer le lauréat dans la 4ème sélection

            case 0:
                print("Merci, et à bientôt! ")


if __name__ == '__main__':
    main()
