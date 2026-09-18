#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion du prix Goncourt 2026
"""

from business.goncourt import Goncourt
from models.book import Book
from models.jury import Jury


def get_int_input(prompt, min_int, max_int):
    """Demande à l'utilisateur de saisir un entier compris entre min_int et max_int."""
    user_input = input(prompt).strip()

    while not user_input.isdigit() or not min_int <= int(user_input) <= max_int:
        user_input = input(Goncourt.SAISIE_INCORRECTE).strip()

    return int(user_input)


def input_menu(items, multiline=False):
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


def show_jury():
    """ Affiche la liste des membres du jury"""
    print("****** Liste des membres du jury ******")
    list_jurys: list[Jury] = Goncourt.get_jurys_list()
    for j in list_jurys:
        print(j)


def show_selections():
    """ Affiche les sélections de livres """
    print("****** Affichage des sélections ******")
    num_selection = get_int_input("Entrez le numéro de la sélection : 1,2,3 ou 4 pour voir le lauréat\n", 1, 4)
    selection = Goncourt.get_selection_by_id(num_selection)
    if selection is None:
        print(Goncourt.ERREUR_SELECTION)
        return
    print(selection)
    if not Goncourt.is_selection_already(num_selection):
        print(f"Cette sélection n'a pas encore été effectuée, il faudra attendre le {selection.selection_date} pour voir les livres qui auront été choisis")


def is_entry_id_book_ok(id_book_choisi, list_books_availables: list[Book], list_id_books_selected: list[int]):
    """ Fonction qui vérifie si la saisie du numéro de livre par le président est correcte    """
    # On enlève les espaces autour
    cleaned_input = id_book_choisi.strip()

    if not cleaned_input.isdigit():
        print("ERREUR - La saisie doit obligatoirement être un chiffre.")
        return False

    cleaned_input = int(cleaned_input)

    if not any(book.id_book == cleaned_input for book in list_books_availables):
        print("ERREUR - Ce numéro de livre ne fait pas partie de la liste des livres disponibles.")
        return False

    if cleaned_input in list_id_books_selected:
        print("ERREUR - Ce livre a déjà été sélectionné.")
        return False

    return True


def get_input_books(prompt: str, nb_books: int, list_books_availables: list[Book]) -> list[int]:
    """ Fonction qui demande au Président d'effectuer la saisie des id pour le nombre de livres attendus
    prompt : Message qui s'affichera pour demander à l'utilisateur sa saisie
    nb_books: integer, nombre d'id de livres à renseigner
    list_books_availables: liste des livres disponibles
    Retourne une liste d'id choisis par le Président, ou un int seul si un seul livre est à renseigner (lauréat)
    """
    list_id_books_selected: list[int] = []

    for _ in range(0, nb_books):
        # On demande au président le numéro du livre qu'il souhaite ajouter à la sélection
        id_book_choisi = input(prompt).strip()

        # On effectue les contrôles sur la saisie
        while not is_entry_id_book_ok(id_book_choisi, list_books_availables, list_id_books_selected):
            id_book_choisi = input(Goncourt.SAISIE_INCORRECTE).strip()

        id_book_choisi = int(id_book_choisi)

        # On ajoute cet id à la liste des livres sélectionnés
        list_id_books_selected.append(id_book_choisi)

    return list_id_books_selected


def get_input_laureat(prompt: str, list_id_books_restants: list[int]):
    """ Fonction qui permet au président de choisir entre les livres ex-aequo en nombre de votes """
    id_book_choisi = input(prompt).strip()
    while not id_book_choisi.isdigit() or int(id_book_choisi) not in list_id_books_restants:
        id_book_choisi = input(Goncourt.SAISIE_INCORRECTE).strip()
    return id_book_choisi


def choice_for_selection(president:Jury):
    """ Fonction qui va permettre au Président de choisir les livres pour la deuxième et troisième sélection """
    # On vérifie l'état des sélections
    is_selection_2_already = Goncourt.is_selection_already(2)
    is_selection_3_already = Goncourt.is_selection_already(3)

    num_selection = 2
    # On vérifie si la deuxième ET la troisième sélection ont pas déjà été faites
    if is_selection_2_already and is_selection_3_already:
        print("ERREUR - Les deux sélections ont déjà été renseignées, ce n'est plus possible de le faire.")
        input(Goncourt.PRESS_ENTER)
        return

    # Si la 2ème sélection a déjà été faite, on va faire la troisième
    elif is_selection_2_already:
        num_selection = 3

    selection = Goncourt.get_selection_by_id(num_selection)
    if selection is None:
        print(Goncourt.ERREUR_SELECTION)
        return
    print(f"****** Choix des livres pour la {num_selection}ème sélection, en date du {selection.selection_date} ******")

    # Pour la deuxième sélection, on va afficher les livres de la 1ère sélection, et pour la troisième sélection on va afficher les livres de la 2ème sélection !
    print("Livres disponibles : ")
    list_books_availables: list[Book] = Goncourt.get_books_by_selection(num_selection - 1)
    for b in list_books_availables:
        print(b)

    print(f"Vous allez choisir {selection.nb_books} livres parmi les livres proposés ci-dessus.")

    # list_id_books_selected: list[int] = []
    list_id_books_selected = get_input_books("Entrez le numéro d'un livre à ajouter à la sélection \n", selection.nb_books, list_books_availables)

    # On appelle la fonction métier qui va ajouter le livre à cette sélection
    for id in list_id_books_selected:
        Goncourt.add_book_to_selection(president, id, selection)

    print("Sélection bien effectuée")
    input(Goncourt.PRESS_ENTER)


def choice_laureat(president:Jury):
    """ Fonction qui permet au Président d'enregistrer les votes pour les livres de la troisième sélection, et de choisir le lauréat """
    print("******* Saisie des votes pour les livres de la 3ème sélection, et choix du lauréat *******")

    # On vérifie l'état des sélections
    is_selection_2_already = Goncourt.is_selection_already(2)
    is_selection_3_already = Goncourt.is_selection_already(3)
    is_selection_4_already = Goncourt.is_selection_already(4)

    # On vérifie si la deuxième ET la troisième sélection ont pas déjà été faites
    if not is_selection_2_already or not is_selection_3_already:
        print("ERREUR - Les sélections n'ont pas encore toutes été renseignées, il n'est pas encore possible de réaliser cette action.")
        input(Goncourt.PRESS_ENTER)
        return

    # On vérifie que la sélection du lauréat n'a pas déjà été effectuée
    if is_selection_4_already:
        print(
            "ERREUR - Les votes de la dernière sélection et la désignation du lauréat ont déjà été effectués, il est impossible de réaliser cette action.")
        input(Goncourt.PRESS_ENTER)
        return


    num_selection = 4
    selection = Goncourt.get_selection_by_id(num_selection)
    if selection is None:
        print(Goncourt.ERREUR_SELECTION)
        return
    print(f"Choix du lauréat - Date : {selection.selection_date}")

    # On affiche les livres de la troisième sélection
    print("Voici les livres disponibles : ")
    list_books_availables: list[Book] = Goncourt.get_books_by_selection(num_selection - 1)

    # On crée un dictionnaire pour pouvoir mémoriser le nombre de votes par id de livre
    votes = {}

    # Pour chaque livre, on va demander au Président le nombre de votes obtenu
    for b in list_books_availables:
        print(f"Livre Numéro {b.id_book} Titre : {b.title} ")
        nb_votes = get_int_input("Combien de votes ce livre a t'il obtenu ? \n", 0, 10)

        votes[b.id_book] = nb_votes

        # On enregistre le nombre de votes dans la base (dans la sélection 3 en fait)
        if (not Goncourt.update_nb_vote_by_book_selection(b.id_book, nb_votes)):
            print("ERREUR lors de la mise à jour du nombre de votes pour ce livre")

    # On récupère le nombre de votes maximal
    max_votes = max(votes.values())

    # On récupère le ou les id correspondant à ce maximal
    ids_max = [id_book for id_book, nb_votes in votes.items() if nb_votes == max_votes]

    # S'il y a plus d'un seul livre qui a ce nombre de votes, alors on demande au Président de saisir l'id du livre lauréat
    if len(ids_max) > 1:
        print(f"Égalité ! Les livres {ids_max} ont chacun {max_votes} votes. C'est au président d'entrer le lauréat : ")
        # On demande au président de saisir le numéro du lauréat parmi les livres de la 3ème sélection
        laureat_id = get_input_laureat("Entrez le numéro de livre du lauréat 2026 parmi ces livres : ",ids_max)
    else:
        print(f"Le livre {ids_max[0]} a remporté {max_votes} votes, c'est donc le lauréat 2026")
        laureat_id = ids_max[0]

    # On ajoute le lauréat à la sélection numéro 4
    # print(f"On ajoute le lauréat : {laureat_id}")
    Goncourt.add_book_to_selection(president, laureat_id, selection)
    print("Action bien effectuée")
    input(Goncourt.PRESS_ENTER)


def main() -> None:
    """Programme principal."""
    print("""--------------------------    
Prix Goncourt 2026    
--------------------------""")

    # On récupère le President, pour l'instant id en dur
    president = Goncourt.get_president_by_id(1)

    if president is None:
        print("ERREUR - Le président n'existe pas.")
        return

    # Menu de l'application
    menu = [
        "Visiteur : Afficher la liste des membres du jury",
        "Visiteur : Afficher les livres des sélections déjà passées",
        "Président : Choisir les livres pour la 2ème ou la 3ème sélection",
        "Président : Après le dernier scrutin, indiquer les votes pour les livres et le lauréat"
    ]
    choix = -1
    # On ne sort pas du programme tant que l'utilisateur ne l'a pas spécifié
    while choix != 0:
        # On récupère le choix de l'utilisateur par rapport au menu
        choix = input_menu(menu, True)

        match choix:
            # Item : Visiteur : Afficher la liste des membres du jury
            case 1:
                show_jury()
                input(Goncourt.PRESS_ENTER)
            # Item : Visiteur : Afficher les livres des sélections déjà passées
            case 2:
                show_selections()
                input(Goncourt.PRESS_ENTER)
            # Item : Président : Choisir les livres pour la 2ème ou la 3ème sélection
            case 3:
                choice_for_selection(president)
            # Item : Président : Après le dernier scrutin, indiquer les votes pour les livres et le lauréat
            case 4:
                choice_laureat(president)
            case 0:
                print("Merci, et à bientôt! ")


if __name__ == '__main__':
    main()