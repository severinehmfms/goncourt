#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion du prix Goncourt 2026
"""

from business.goncourt import Goncourt
from models.jury import Jury
from models.selection import Selection


def get_int_input(prompt, min_int, max_int):
    """Demande à l'utilisateur de saisir un entier compris entre min_int et max_int."""
    user_input = input(prompt).strip()

    while not user_input.isdigit() or not min_int <= int(user_input) <= max_int:
        user_input = input(
            "Saisie incorrecte. Merci de recommencer : "
        ).strip()

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

    # Menu de l'application => En test dans un premier temps (à modifier quand je gérerai la connection utilisateur)
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

        match choix:
            case 1:
                print("****************** Liste des membres du jury ******************")
                list_jurys: list[Jury] = goncourt_instance.get_jurys_list()
                for j in list_jurys:
                    print(j)
                input("Appuyez sur la touche 'Entrée' pour retourner au menu")
            case 2:
                print("****************** Sélections déjà passées ******************")
                num_selection = get_int_input("Entrez le numéro de la sélection demandée : 1,2,3 ou 4 pour voir le lauréat", 1, 4)
                selection: Selection = goncourt_instance.get_selection_by_id(num_selection)
                print(selection)
                input("Appuyez sur la touche 'Entrée' pour retourner au menu")
            case 3:
                print("****************** Choix des livres pour la 2ème puis la 3ème sélection ******************")
                # TODO Vérifier si la deuxième ET la troisième sélection ont pas déjà été faites
                num_selection = 2
                is_selection_2_already = False
                is_selection_3_already = False
                if (is_selection_2_already and is_selection_3_already):
                    print("ERREUR - Les deux sélections ont déjà été renseignées, ce n'est plus possible de le faire.")
                    input("Appuyez sur la touche 'Entrée' pour retourner au menu")
                    continue
                elif (is_selection_2_already):
                    num_selection = 3
                print(f"Sélection numéro {num_selection} : ")
                selection: Selection = goncourt_instance.get_selection_by_id(num_selection)
                print(selection)
                # Si ok, alors on affiche la liste des livres dans un joli tableau et on demande au président de noter les numéros un par un séparés par un espace
                # TODO Préparer une méthode d'input qui récupère le bon nombre de numéros en fonction de la sélection choisie (8 pour 2ème, 4 pour 3ème)

                # TODO Fonction à créer et faire en dao aussi --- On appelle la fonction métier qui renseigne cette sélection (et en base)

            case 4:
                print("cas 4")
            case 0:
                print("Merci, et à bientôt! ")


if __name__ == '__main__':
    main()
