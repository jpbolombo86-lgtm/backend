-- Script SQL pour initialiser la base de données
-- Ce script crée les tables et les utilisateurs de test

-- Créer la table users
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'user',
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Créer la table applications
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom VARCHAR(100) NOT NULL,
    description TEXT,
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Créer la table comptes
CREATE TABLE IF NOT EXISTS comptes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    application_id INTEGER,
    username VARCHAR(100) NOT NULL,
    password TEXT NOT NULL,
    role VARCHAR(50),
    commentaire TEXT,
    FOREIGN KEY (application_id) REFERENCES applications(id)
);

-- Créer la table habilitations
CREATE TABLE IF NOT EXISTS habilitations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    compte_id INTEGER,
    permission VARCHAR(100) NOT NULL,
    FOREIGN KEY (compte_id) REFERENCES comptes(id)
);

-- Créer la table tests
CREATE TABLE IF NOT EXISTS tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    application_id INTEGER,
    fonctionnalite VARCHAR(200) NOT NULL,
    statut VARCHAR(50),
    commentaire TEXT,
    FOREIGN KEY (application_id) REFERENCES applications(id)
);

-- Créer la table logs
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action TEXT NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insérer les utilisateurs de test
-- Mot de passe : 123456 (hashé en bcrypt)
INSERT INTO users (username, email, hashed_password, role) 
VALUES ('testuser', 'test@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5ePLF3Sp.c6DO', 'user');

-- Mot de passe : admin123 (hashé en bcrypt)
INSERT INTO users (username, email, hashed_password, role) 
VALUES ('admin', 'admin@example.com', '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW', 'admin');
