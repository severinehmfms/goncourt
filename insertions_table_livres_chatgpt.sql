INSERT INTO `editeur` (`id_editeur`, `nom_editeur`) VALUES
(2, 'Albin Michel'),
(3, 'P.O.L'),
(4, 'Grasset'),
(5, 'Robert Laffont'),
(6, 'Actes Sud'),
(7, 'L''Iconoclaste'),
(8, 'Gallimard'),
(9, 'Verdier'),
(10, 'Minuit'),
(11, 'Maurice Nadeau');

INSERT INTO `auteur` (`id_auteur`, `nom`, `prenom`, `biographie`) VALUES
(2, "Bergmann", "Boris", "Boris Bergmann est un écrivain français né à Paris en 1992. Il est l'auteur de plusieurs romans, dont Nage Libre, qui reçoit le prix de la Vocation en 2018, et Les Corps insurgés, récompensé par le prix Fénéon en 2020. Il a été pensionnaire de la Villa Médicis et de la Villa Kujoyama et collabore à la revue d'art et de littérature Magma."),
(3, "Chennevière", "Louise", "Louise Chennevière est une autrice, chanteuse et musicienne française née en 1993. Elle grandit à Paris, suit des classes préparatoires littéraires et obtient un master de philosophie. Elle publie son premier roman, Comme la chienne, en 2019, puis Mausolée en 2021 et Pour Britney en 2024. Elle intègre la Villa Médicis comme pensionnaire."),
(4, "Devi", "Ananda", "Ananda Devi, née en 1957 à Trois Boutiques à l'île Maurice, est une femme de lettres mauricienne. Issue d'une famille d'origine indienne, elle maîtrise notamment le français, le créole, l'anglais et le télougou. Elle obtient un doctorat d'anthropologie sociale à l'École des études orientales et africaines de l'université de Londres. Son œuvre littéraire explore notamment les violences faites aux femmes et les rapports entre classes et sexes."),
(5, "Devillers", "Sonia", "Sonia Devillers est une journaliste française. Elle grandit à Vincennes et étudie les lettres et la philosophie avant de se tourner vers le journalisme. Elle travaille notamment pour Le Figaro et la radio. Son histoire familiale, marquée par l'exil de sa famille maternelle depuis la Roumanie communiste, est au cœur de son livre Les Exportés."),
(6, "Godard", "Anne", "Anne Godard est une universitaire et écrivaine française. Après des études de lettres modernes, elle soutient une thèse consacrée aux dialogues de la Renaissance et devient maîtresse de conférences à l'université Sorbonne-Nouvelle. Son premier roman, L'Inconsolable, paraît en 2006 et reçoit le grand prix RTL-Lire. Elle publie ensuite Une chance folle."),
(7, "Grondeau", "Olivier", ""),
(8, "Haenel", "Yannick", "Yannick Haenel est un écrivain français et agrégé de lettres modernes. Il a étudié au Prytanée national militaire de La Flèche puis au lycée Chateaubriand de Rennes. Il fonde en 1997 la revue Ligne de risque et enseigne le français jusqu'en 2005. Pensionnaire de la Villa Médicis en 2008-2009, il reçoit notamment le prix Décembre et le prix Roger-Nimier pour Cercle, puis le prix Interallié pour Jan Karski et le prix Médicis pour Tiens ferme ta couronne."),
(9, "Hassaine", "Lilia", "Lilia Hassaine, née en 1991, est une romancière, journaliste française et chroniqueuse de télévision. Après des études littéraires, elle intègre l'Institut français de presse dont elle sort diplômée en 2015. Elle travaille notamment pour Arte, Le Parisien et Le Monde, puis devient chroniqueuse dans l'émission Quotidien. Elle publie plusieurs romans chez Gallimard, dont L'Œil du paon, Soleil amer, Panorama et Je."),
(10, "Jouannais", "Jean-Yves", "Jean-Yves Jouannais, né en 1964 à Montluçon, est un critique d'art et écrivain français. Il devient rédacteur en chef de la revue Art Press et travaille également pour l'émission Exhibition sur Arte. Depuis 2009, il anime L'Encyclopédie des guerres, un spectacle-conférence consacré à l'histoire des conflits."),
(11, "Marsantes", "Emma", ""),
(12, "Mélois", "Clémentine", "Clémentine Mélois est une artiste et écrivaine française. Elle étudie aux Beaux-Arts de Paris de 2000 à 2005, où elle se spécialise dans les techniques d'impression et le livre d'artiste. Son travail repose notamment sur le détournement d'images et de textes. Elle publie son premier livre, Cent Titres, en 2014 et est membre de l'Oulipo de 2017 à 2026."),
(13, "Orélien", "Thélyson", "Thélyson Orélien est un écrivain québécois d'origine haïtienne. Né aux Gonaïves, il s'installe au Québec après le séisme de 2010. Poète, romancier et chroniqueur, il écrit sur l'exil, la mémoire, la transmission et l'identité. Il publie son premier roman, C'était ça ou mourir, en 2026."),
(14, "Prudhomme", "Sylvain", "Sylvain Prudhomme, né en 1979 à La Seyne-sur-Mer, est un écrivain français. Il passe son enfance dans différents pays d'Afrique avant d'étudier les lettres à Paris. Agrégé de lettres modernes, il dirige notamment l'Alliance franco-sénégalaise de Ziguinchor. Il est l'auteur de nombreux romans et reportages et reçoit notamment le prix Femina en 2019 pour Par les routes."),
(15, "Rolin", "Olivier", "Olivier Rolin est un écrivain français, né à Boulogne-Billancourt. Il passe son enfance au Sénégal, étudie au lycée Louis-le-Grand puis à l'École normale supérieure, où il se forme à la philosophie et aux lettres. Il est notamment l'auteur de Port-Soudan, pour lequel il reçoit le prix Femina en 1994, de Tigre en papier et du Météorologue."),
(16, "Trigano", "Patrice", "Patrice Trigano, né en 1947 à Paris, est un expert en tableaux, collectionneur, galeriste et écrivain français. Fils de l'industriel et homme politique André Trigano, il étudie le droit, l'histoire de l'art et la philosophie. Il consacre ensuite sa vie à l'art et publie des ouvrages consacrés notamment à des figures de la littérature et de l'art.");

INSERT INTO `livre`
(`id_livre`, `titre`, `resume`, `date_parution`, `nb_pages`, `isbn`, `prix_editeur`, `id_editeur`, `id_auteur`)
VALUES

(2, "Minotaure",
"A 23 ans, Boris Bergmann entreprend de retrouver son père, qu'il n'a jamais rencontré. Cette quête personnelle devient un récit autobiographique consacré à l'absence du père, à la relation à la mère et au besoin de construire son identité. Le livre mêle souvenirs, histoires vécues et réflexion sur l'amour et la filiation.",
"2026-08-19", 256, 9782226511874, 20.90, 2, 2),

(3, "Faire la peau",
"Une femme interroge le lien entre les mères et leurs filles, ainsi que la violence qui peut circuler dans cette relation. Le roman explore la transmission, la haine, l'amour et les blessures familiales à travers une écriture qui cherche à regarder les rapports mère-fille sans détour.",
"2026-08-20", 288, 9782818063583, 21.00, 3, 3),

(4, "Chronique d'un royaume perdu",
"Sur l'île Maurice, dans le village isolé du Bouchon, quatre générations d'une même famille vivent depuis l'époque de l'esclavage. Les destins familiaux, les passions, les croyances et les rapports entre les êtres se mêlent dans une fresque où le réel côtoie le surnaturel.",
"2026-08-19", 464, 9782246846949, 24.00, 4, 4),

(5, "Le fabuleux piano",
"Sonia Devillers part à la recherche d'un piano à queue volé par les nazis en 1943 à une famille juive. Cette enquête la conduit sur les traces des instruments de musique spoliés pendant l'Occupation et de la famille d'éditeurs de musique Enoch. La disparition de ce piano fait également écho à l'histoire familiale de l'autrice et à l'exil de sa grand-mère.",
"2026-08-27", 288, 9782221286807, 21.00, 5, 5),

(6, "Nous aussi",
"Une famille bourgeoise du Quartier latin semble vivre dans une parfaite harmonie. Ses membres forment un groupe très soudé, presque indissociable. Mais lorsque la façade familiale se fissure, les certitudes et les règles tacites qui régissaient leur existence sont bouleversées.",
"2026-08-19", 240, 9782330225575, 20.00, 6, 6),

(7, "Joseph dans la nuit",
"Olivier Grondeau raconte le voyage d'un homme arrêté en Iran alors qu'il se rendait en Asie. Accusé d'espionnage, il passe deux ans et demi en prison. Dans cet univers clos, la poésie, les souvenirs, les rêves et l'imagination deviennent des moyens de résister et de préserver une forme de liberté intérieure.",
"2026-08-20", 256, 9782378805975, 19.90, 7, 7),

(8, "La solitude des professeurs est infinie",
"Jean Deichel, jeune professeur de français, effectue son stage dans un collège de la banlieue parisienne. Il découvre les difficultés et les violences du métier mais aussi la beauté de la transmission. Poète et rêveur, il cherche dans ses cours et dans son quotidien une forme de lumière et de vérité.",
"2026-08-20", 320, 9782073161925, 21.50, 8, 8),

(9, "Je",
"En Jamaïque en 1831, Antoinette Cosway, jeune créole, rencontre Edward Rochester. Leur relation se transforme progressivement en une histoire de domination et de violence. Inspiré de la première épouse de Rochester dans Jane Eyre, le roman donne à Antoinette une voix et revisite son histoire à travers une forme mêlant roman victorien et thriller contemporain.",
"2026-08-20", 256, 9782073099945, 21.00, 8, 9),

(10, "Une forêt",
"Dans une forêt allemande, le capitaine Lenz s'intéresse à une mystérieuse affaire liée à des oiseaux. Derrière cette enquête se dessine un récit étrange et mélancolique où se mêlent mémoire, guerre, culpabilité et rapport au vivant.",
"2026-01-02", 112, 9782226499523, 16.90, 2, 10),

(11, "N'efface pas mes cercles",
"En 1980, une femme se suicide dans un appartement cossu. Des décennies plus tôt, elle avait épousé un homme auquel tout l'opposait. En enquêtant sur son histoire familiale, la narratrice remonte le fil des destins brisés et d'une société marquée par le patriarcat, la guerre, la colonisation et les injonctions à la réussite.",
"2026-08-20", 160, 9782378562953, 19.50, 9, 11),

(12, "Choses que je croyais perdues",
"Une jeune femme prépare son déménagement après une rupture. En emballant ses affaires, elle se remémore sa relation et les épisodes de sa vie associés aux objets qui l'entourent. Les souvenirs attachés aux choses ordinaires deviennent ainsi une manière d'interroger l'amour, la séparation, la mémoire et les histoires que nous construisons autour de nos vies.",
"2026-08-20", 176, 9782073162854, 19.00, 8, 12),

(13, "C'était ça ou mourir",
"Jonas Dorléon quitte Haïti après l'embrasement de son quartier de Port-au-Prince. Avec quelques affaires dans un sac plastique, il traverse la République dominicaine puis l'Amérique, affrontant les frontières, la violence, la faim et les dangers de la jungle du Darién. Son périple est celui d'un homme qui cherche à atteindre le Canada tout en conservant l'espoir d'une vie meilleure.",
"2026-08-19", 272, 9782246847069, 21.50, 4, 13),

(14, "De l'autre côté du lac",
"Aux abords d'un lac de haute montagne, un groupe de chercheurs travaille à la limite d'une réserve interdite aux humains. Une photographe aperçoit un phénomène que les autres ne remarquent pas. Après plusieurs événements étranges et la découverte d'un corps, elle décide de rester seule sur place avant de disparaître à son tour. Un roman consacré au désir d'intensité, à l'appel du sauvage et à la recherche d'une vie plus authentique.",
"2026-08-27", 288, 9782707358233, 22.00, 10, 14),

(15, "La guerre éternelle",
"Olivier Rolin se rend en Troade pour contempler les paysages associés à la guerre de Troie. À partir de l'Iliade et de la mémoire des lieux, il réfléchit à la permanence des guerres et à la destruction des villes. La tragédie de Troie devient ainsi une méditation sur les conflits qui traversent encore le monde contemporain.",
"2026-08-20", 224, 9782073121349, 20.00, 8, 15),

(16, "Bataille au procès",
"En 1956, Georges Bataille témoigne au procès de Jean-Jacques Pauvert, poursuivi pour avoir publié les œuvres de Sade. Cet épisode conduit Bataille à réfléchir à la menace que la morale fait peser sur la littérature. À travers ses souvenirs, ses expériences et ses réflexions sur l'art, Patrice Trigano explore le rapport entre la vie de l'écrivain et une œuvre qui finit par échapper à son créateur.",
"2026-08-21", 136, 9782862316857, 19.00, 11, 16);


INSERT INTO `personnage` (`id_personnage`, `nom`, `prenom`, `id_livre`) VALUES
(2, 'Dumontais', '', 4),
(3, 'Vieux Bouc', '', 4),
(4, 'Deichel', 'Jean', 8),
(5, 'Cosway', 'Antoinette', 9),
(6, 'Rochester', 'Edward', 9),
(7, 'Lenz', 'Jacob', 10),
(8, 'Niege', 'Georg', 10),
(9, 'Dorléon', 'Jonas', 13),
(10, 'Paola', '', 14),
(11, 'Bataille', 'Georges', 16),
(12, 'Pauvert', 'Jean-Jacques', 16);
