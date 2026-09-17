''' Insertion du premier livre, avec éditeur et auteur : suite sera faite dans autre fichier sql dont les lignes ont été générées par ChatGpt '''

INSERT INTO `editeur` (`id_editeur`, `nom_editeur`) VALUES
(1, 'Flammarion');

INSERT INTO `auteur` (`id_auteur`, `nom`, `prenom`, `biographie`) VALUES
(1, "Jaenada", "Philippe", "Philippe Jaenada est né à Saint-Germain-en-Laye où ses grands-parents maternels possédaient le restaurant Le Grand Cerf. Issu d’une famille de pieds-noirs récemment revenue d’Algérie, il grandit dans une banlieue pavillonnaire, à Morsang-sur-Orge en Essonne[1]. Après des études scientifiques, il s’installe à Paris en 1986 où il enchaîne les petits boulots pendant plusieurs années[2]. Sa première nouvelle est publiée en 1990 dans L'Autre Journal. Ses sept premiers romans sont d'inspiration autobiographique. Outre ses livres, il a écrit des articles pour le magazine Voici[3] pendant plusieurs années, avant d’arrêter en 2022 pour se concentrer pleinement à ses romans. Avec sa compagne Anne-Catherine Fath, ils ont un fils, Ernest, né en août 2000. Habitant le 10e arrondissement, il a ses habitudes au Bistrot Lafayette[4].");

INSERT INTO `livre` (`id_livre`, `titre`, `resume`, `date_parution`, `nb_pages`, `isbn`, `prix_editeur`, `id_editeur`, `id_auteur`) VALUES
(1, "L'inconnue du quai de Javel", "Le 6 septembre 1949, une jeune femme est retrouvée morte quai de Javel, à Paris, sans sac ni chaussures, manifestement rhabillée à la hâte puis déposée là par son assassin. Elle est identifiée le lendemain : c'est Louise Cansot, le modèle le plus demandé par les peintres de Montparnasse. Rapidement, quatre suspects se détachent, évidents, presque des archétypes. On dirait le début d'un roman de Simenon, mais l'inspecteur-chef Ferrière n'a pas le talent de Maigret, et doit se résoudre à classer l'affaire au bout de six mois, sans avoir arrêté personne.
Soixante-quinze ans plus tard, Philippe Jaenada reprend l'enquête à partir du dossier retrouvé puis, comme à son habitude, sollicite ses contacts aux archives, exhume tous les documents, arpente tous les lieux - remonte le temps.
Pour ce livre, il a lu les soixante-quinze enquêtes de Maigret, s'inspirant humblement et fidèlement des méthodes du commissaire fictif. Et il va résoudre ce meurtre bien réel, laissant le lecteur subjugué par la dextérité de son investigation et fasciné par cette jeune femme à laquelle il redonne un visage et une histoire.", "2026-08-12", "528", 9782080490896, 23.00, 1, 1 );


''' Après oubli des personnages principaux je mets ceux du premier livre et Chat Gpt va me préparer la suite'''
INSERT INTO `personnage` (`id_personnage`, `nom`, `prenom`, `id_livre`) VALUES
(1, 'Ferriere', '', 1);

''' Insertion des membres du jury et du président '''
INSERT INTO `jury` (`id_jury`, `nom`, `prenom`, `is_president`) VALUES
(1, 'Decoin', 'Didier', True),
(2, 'Chandernagor', 'Françoise', False),
(3, 'Ben Jelloun', 'Tahar', False),
(4, 'Constant', 'Paule', False),
(5, 'Claudel', 'Philippe', False),
(6, 'Assouline', 'Pierre', False),
(7, 'Schmitt', 'Eric-Emmanuel', False),
(8, 'Laurens', 'Camille', False),
(9, 'Bruckner', 'Pascal', False),
(10, 'Angot', 'Christine', False)
;

''' Insertion des sélections '''
INSERT INTO `selection` (`num_selection`, `date_selection`, `titre`, `nb_livres`) VALUES
(1, "2026-09-02", '1ère sélection', 16),
(2, "2026-10-06", '2ème sélection', 8),
(3, "2026-10-27", '3ème sélection', 4),
(4, "2026-11-03", 'Lauréat', 1)
 ;

''' Ajout des personnages principaux non reconnus par ChatGpt'''
INSERT INTO `personnage` (`id_personnage`, `nom`, `prenom`, `id_livre`) VALUES
(13, 'Le Minotaure', '', 2);

INSERT INTO `personnage` (`id_personnage`, `nom`, `prenom`, `id_livre`) VALUES
(14, 'Olivier', '', 7);

INSERT INTO `personnage` (`id_personnage`, `nom`, `prenom`, `id_livre`) VALUES
(15, 'Devillers', 'Sonia', 5);


''' Insertion des 16 livres dans la première sélection '''
INSERT INTO `choix` (id_livre, id_jury, num_selection) VALUES
(1, 1, 1),
(2, 1, 1),
(3, 1, 1),
(4, 1, 1),
(5, 1, 1),
(6, 1, 1),
(7, 1, 1),
(8, 1, 1),
(9, 1, 1),
(10, 1, 1),
(11, 1, 1),
(12, 1, 1),
(13, 1, 1),
(14, 1, 1),
(15, 1, 1),
(16, 1, 1);