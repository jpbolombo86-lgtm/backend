"""
Script de migration pour ajouter les nouvelles colonnes a la table tests
dans la base de donnees PostgreSQL.

Executer ce script pour mettre a jour la structure de la table.
"""

import psycopg2
from psycopg2 import sql
import sys

# Set UTF-8 encoding
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Configuration de la connexion PostgreSQL
DB_CONFIG = {
    "host": "localhost",
    "database": "gestion_de_motdepasse",
    "user": "postgres",
    "password": "123456"
}

def migrate_tests_table():
    """Ajoute les nouvelles colonnes a la table tests"""
    
    # Colonnes a ajouter
    new_columns = [
        ("fonction", "VARCHAR(200)"),
        ("precondition", "TEXT"),
        ("etapes", "TEXT"),
        ("resultat_attendu", "TEXT"),
        ("resultat_obtenu", "TEXT"),
        ("commentaires", "TEXT")
    ]
    
    conn = None
    try:
        # Connexion a la base de donnees
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Verifier quelles colonnes existent deja
        cursor.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = 'tests'
        """)
        existing_columns = [row[0] for row in cursor.fetchall()]
        
        print(f"Colonnes existantes dans 'tests': {existing_columns}")
        
        # Ajouter les colonnes manquantes
        for column_name, column_type in new_columns:
            if column_name not in existing_columns:
                print(f"Ajout de la colonne '{column_name}'...")
                cursor.execute(
                    sql.SQL("ALTER TABLE tests ADD COLUMN {} {}").format(
                        sql.Identifier(column_name),
                        sql.SQL(column_type)
                    )
                )
                print(f"[OK] Colonne '{column_name}' ajoutee avec succes")
            else:
                print(f"[-] Colonne '{column_name}' existe deja, ignoree")
        
        # Valider les modifications
        conn.commit()
        print("\n[OK] Migration terminee avec succes!")
        
        # Afficher la nouvelle structure
        cursor.execute("""
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = 'tests'
            ORDER BY ordinal_position
        """)
        print("\nNouvelle structure de la table 'tests':")
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
    print("Migration de la table tests")
    print("=" * 50)
    migrate_tests_table()
