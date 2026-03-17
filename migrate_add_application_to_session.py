"""
Script de migration pour ajouter la colonne application_id
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
        
        # Vérifier si la colonne existe déjà
        cursor.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = 'test_sessions' AND column_name = 'application_id'
        """)
        existing = cursor.fetchone()
        
        if not existing:
            cursor.execute("""
                ALTER TABLE test_sessions 
                ADD COLUMN application_id INTEGER REFERENCES applications(id)
            """)
            print("Colonne 'application_id' ajoutée avec succès")
        else:
            print("La colonne 'application_id' existe déjà")
        
        cursor.close()
        conn.close()
        print("\nMigration terminée avec succès!")
        
    except psycopg2.Error as e:
        print(f"Erreur lors de la migration: {e}")

if __name__ == "__main__":
    migrate()
