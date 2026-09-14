USE goncourt;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

DROP TABLE IF EXISTS `auteur`;
CREATE TABLE `auteur`(
   id_auteur INT NOT NULL AUTO_INCREMENT,
   nom VARCHAR(50) NOT NULL,
   prenom VARCHAR(50) NOT NULL,
   biographie TEXT,
   PRIMARY KEY(id_auteur)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `editeur`;
CREATE TABLE `editeur`(
   id_editeur INT NOT NULL AUTO_INCREMENT,
   nom_editeur VARCHAR(50) NOT NULL,
   PRIMARY KEY(id_editeur)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `jury`;
CREATE TABLE `jury`(
   id_jury SMALLINT NOT NULL AUTO_INCREMENT,
   nom VARCHAR(50) NOT NULL,
   prenom VARCHAR(50) NOT NULL,
   is_president BOOLEAN NOT NULL,
   PRIMARY KEY(id_jury)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `selection`;
CREATE TABLE `selection`(
   num_selection SMALLINT NOT NULL AUTO_INCREMENT,
   date_selection DATE NOT NULL,
   titre VARCHAR(50) NOT NULL,
   nb_livres SMALLINT NOT NULL,
   PRIMARY KEY(num_selection)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `livre`;
CREATE TABLE `livre`(
   id_livre INT NOT NULL AUTO_INCREMENT,
   titre VARCHAR(100) NOT NULL,
   resume TEXT,
   date_parution DATE,
   nb_pages SMALLINT,
   isbn BIGINT,
   prix_editeur DECIMAL(10,2),
   id_editeur INT NOT NULL,
   id_auteur INT NOT NULL,
   PRIMARY KEY(id_livre),
   KEY `id_editeur` (`id_editeur`),
   KEY `id_auteur` (`id_auteur`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `personnage`;
CREATE TABLE `personnage`(
   id_personnage INT NOT NULL AUTO_INCREMENT,
   nom VARCHAR(50) NOT NULL,
   prenom VARCHAR(50),
   id_livre INT NOT NULL,
   PRIMARY KEY(id_personnage),
   KEY `id_livre` (`id_livre`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `choix`;
CREATE TABLE `choix`(
   id_livre INT NOT NULL,
   id_jury SMALLINT NOT NULL,
   num_selection SMALLINT NOT NULL,
   nb_votes_scrutin_final SMALLINT,
   PRIMARY KEY(id_livre, id_jury, num_selection),
   KEY `id_livre` (`id_livre`),
   KEY `id_jury` (`id_jury`),
   KEY `num_selection` (`num_selection`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

ALTER TABLE `livre`
  ADD CONSTRAINT `livre_ibfk_1` FOREIGN KEY (`id_auteur`) REFERENCES `auteur` (`id_auteur`),
  ADD CONSTRAINT `livre_ibfk_2` FOREIGN KEY (`id_editeur`) REFERENCES `editeur` (`id_editeur`);

ALTER TABLE `personnage`
  ADD CONSTRAINT `personnage_ibfk_1` FOREIGN KEY (`id_livre`) REFERENCES `livre` (`id_livre`);

ALTER TABLE `choix`
  ADD CONSTRAINT `choix_ibfk_1` FOREIGN KEY (`id_livre`) REFERENCES `livre` (`id_livre`),
  ADD CONSTRAINT `choix_ibfk_2` FOREIGN KEY (`id_jury`) REFERENCES `jury` (`id_jury`),
  ADD CONSTRAINT `choix_ibfk_3` FOREIGN KEY (`num_selection`) REFERENCES `selection` (`num_selection`);

  