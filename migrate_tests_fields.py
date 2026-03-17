"""
Script de migration pour ajouter les colonnes application_nom, version et environnement
a la table tests dans la base de donnees PostgreSQL.
"""

import psycopg2
from psycopg2 import sql

DB_CONFIG = {
    "host": "localhost",
    "database": "gestion_de_motdepasse",
    "user": "postgres",
    "password": "123456"
}

def migrate_tests():
    """Ajoute les nouvelles colonnes a la table tests"""
    
    new_columns = [
        ("application_nom", "VARCHAR(100)"),
        ("version", "VARCHAR(50)"),
        ("environnement", "VARCHAR(50)")
    ]
    
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = 'tests'
        """)
        existing_columns = [row[0] for row in cursor.fetchall()]
        
        print(f"Colonnes existantes dans 'tests': {existing_columns}")
        
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
        
        conn.commit()
        print("\n[OK] Migration terminee avec succes!")
        
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
    print("Migration de la table tests (nouveaux champs)")
    print("=" * 50)
    migrate_tests()
