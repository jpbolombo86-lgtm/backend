"""
Script de migration pour créer la table test_sessions et ajouter session_id à tests
"""

import psycopg2
from psycopg2 import sql

DB_CONFIG = {
    "host": "localhost",
    "database": "gestion_de_motdepasse",
    "user": "postgres",
    "password": "123456"
}

def migrate():
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Create test_sessions table if it doesn't exist
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_name = 'test_sessions'
        """)
        if not cursor.fetchone():
            print("Création de la table 'test_sessions'...")
            cursor.execute("""
                CREATE TABLE test_sessions (
                    id SERIAL PRIMARY KEY,
                    nom VARCHAR(200) NOT NULL,
                    description TEXT,
                    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    statut VARCHAR(50) DEFAULT 'En cours'
                )
            """)
            print("[OK] Table 'test_sessions' créée")
        else:
            print("[-] Table 'test_sessions' existe déjà")
        
        # Check if session_id column exists in tests
        cursor.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = 'tests' AND column_name = 'session_id'
        """)
        if not cursor.fetchone():
            print("Ajout de la colonne 'session_id' à la table 'tests'...")
            cursor.execute("""
                ALTER TABLE tests 
                ADD COLUMN session_id INTEGER REFERENCES test_sessions(id)
            """)
            print("[OK] Colonne 'session_id' ajoutée")
        else:
            print("[-] Colonne 'session_id' existe déjà")
        
        conn.commit()
        print("\n[OK] Migration terminée avec succès!")
        
        # Show test_sessions structure
        cursor.execute("""
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = 'test_sessions'
            ORDER BY ordinal_position
        """)
        print("\nStructure de la table 'test_sessions':")
        for row in cursor.fetchall():
            print(f"  - {row[0]}: {row[1]}")
            
    except psycopg2.Error as e:
        print(f"Erreur PostgreSQL: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    print("=" * 50)
    print("Migration: test_sessions")
    print("=" * 50)
    migrate()
