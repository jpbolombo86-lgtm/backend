-- Migration pour ajouter les nouvelles colonnes à la table tests
-- Ce script doit être exécuté manuellement sur la base de données SQLite

-- Vérifier si les colonnes existent déjà et les ajouter si nécessaire
-- Les nouvelles colonnes: fonction, precondition, etapes, resultat_attendu, resultat_obtenu, commentaires

-- Note: SQLite ne supporte pas ALTER TABLE ADD COLUMN avec des contraintes NOT NULL
-- Si vous avez des données existantes, vous devrez les mettre à jour manuellement

-- Ajouter les colonnes une par une
ALTER TABLE tests ADD COLUMN fonction VARCHAR(200);
ALTER TABLE tests ADD COLUMN precondition TEXT;
ALTER TABLE tests ADD COLUMN etapes TEXT;
ALTER TABLE tests ADD COLUMN resultat_attendu TEXT;
ALTER TABLE tests ADD COLUMN resultat_obtenu TEXT;
ALTER TABLE tests ADD COLUMN commentaires TEXT;
