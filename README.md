# IT Access Manager

Une application de gestion des accès et des mots de passe pour les systèmes internes, conçue pour les équipes IT et les testeurs.

## Fonctionnalités

- Gestion des applications (ajout, modification, suppression)
- Gestion des comptes utilisateurs associés aux applications
- Gestion des habilitations (permissions) pour chaque compte
- Suivi des tests fonctionnels avec statut (OK, BUG, etc.)
- Journalisation des actions (logs)
- Sécurisation des mots de passe (hashing avec bcrypt)
- Interface web simple (HTML/CSS/JavaScript)

## Structure du projet

```
IT-Access-Manager
│
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── security.py
│   │   └── routers
│   │       ├── applications.py
│   │       ├── comptes.py
│   │       ├── habilitations.py
│   │       └── tests.py
│
├── frontend
│   ├── login.html
│   └── dashboard.html (à créer)
│
├── docker
│   └── Dockerfile (à créer)
│
├── requirements.txt
│
└── README.md
```

## Installation

1. Cloner le dépôt (ou copier les fichiers)
2. Installer les dépendances Python :
   ```
   pip install -r requirements.txt
   ```
3. Configurer la base de données PostgreSQL :
   - Créer une base de données nommée `access_manager`
   - Mettre à jour la chaîne de connexion dans `backend/app/database.py` si nécessaire
4. Créer les tables dans la base de données (en utilisant les modèles SQLAlchemy) :
   ```
   from backend.app.database import engine
   from backend.app.models import Base
   Base.metadata.create_all(bind=engine)
   ```

## Utilisation

1. Démarrer le serveur backend :
   ```
   uvicorn backend.app.main:app --reload
   ```
2. Ouvrir `frontend/login.html` dans un navigateur pour accéder à l'interface.

## Sécurité

- Les mots de passe sont hashés avec bcrypt avant d'être stockés en base de données.
- Aucune information sensible n'est transmise en clair (en production, utilisez HTTPS).

## Développement futur

- Ajouter une interface de dashboard complète
- Implémenter l'authentification JWT
- Ajouter le chiffrement AES pour les données sensibles
- Créer des tests unitaires et d'intégration
- Containeriser l'application avec Docker
- Ajouter un système de journalisation avancé
- Exporter les données en Excel/CSV

## Auteur

Développé pour un projet de gestion informatique et de test logiciel.

## Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.