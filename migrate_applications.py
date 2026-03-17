"""
Script de migration pour ajouter les colonnes version et environnement 
a la table applications dans la base de donnees PostgreSQL.
"""

import psycopg2
from psycopg2 import sql

DB_CONFIG = {
    "host": "localhost",
    "database": "gestion_de_motdepasse",
    "user": "postgres",
    "password": "123456"
}

def migrate_applications():
    """Ajoute les colonnes version et environnement a la table applications"""
    
    new_columns = [
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
            WHERE table_name = 'applications'
        """)
        existing_columns = [row[0] for row in cursor.fetchall()]
        
        print(f"Colonnes existantes dans 'applications': {existing_columns}")
        
        for column_name, column_type in new_columns:
            if column_name not in existing_columns:
                print(f"Ajout de la colonne '{column_name}'...")
                cursor.execute(
                    sql.SQL("ALTER TABLE applications ADD COLUMN {} {}").format(
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
            WHERE table_name = 'applications'
            ORDER BY ordinal_position
        """)
        print("\nNouvelle structure de la table 'applications':")
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
    print("Migration de la table applications")
    print("=" * 50)
    migrate_applications()
