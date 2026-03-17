"""
Script de migration pour ajouter les colonnes environnement, version et nom_document
à la table test_sessions
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Configuration de la base de données
DB_HOST = "localhost"
DB_NAME = "gestion_de_motdepasse"
DB_USER = "postgres"
DB_PASSWORD = "123456"

def migrate():
    try:
        # Connexion à la base de données
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Vérifier si les colonnes existent déjà
        cursor.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = 'test_sessions'
        """)
        existing_columns = [row[0] for row in cursor.fetchall()]
        
        # Ajouter la colonne environnement si elle n'existe pas
        if 'environnement' not in existing_columns:
            cursor.execute("""
                ALTER TABLE test_sessions 
                ADD COLUMN environnement VARCHAR(50)
            """)
            print("Colonne 'environnement' ajoutée avec succès")
        else:
            print("La colonne 'environnement' existe déjà")
        
        # Ajouter la colonne version si elle n'existe pas
        if 'version' not in existing_columns:
            cursor.execute("""
                ALTER TABLE test_sessions 
                ADD COLUMN version VARCHAR(50)
            """)
            print("Colonne 'version' ajoutée avec succès")
        else:
            print("La colonne 'version' existe déjà")
        
        # Ajouter la colonne nom_document si elle n'existe pas
        if 'nom_document' not in existing_columns:
            cursor.execute("""
                ALTER TABLE test_sessions 
                ADD COLUMN nom_document VARCHAR(200)
            """)
            print("Colonne 'nom_document' ajoutée avec succès")
        else:
            print("La colonne 'nom_document' existe déjà")
        
        cursor.close()
        conn.close()
        print("\nMigration terminée avec succès!")
        
    except psycopg2.Error as e:
        print(f"Erreur lors de la migration: {e}")

if __name__ == "__main__":
    migrate()
