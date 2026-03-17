# Guide de Déploiement Gratuit

## Architecture
- **Frontend**: React (Vercel)
- **Backend**: FastAPI (Render)
- **Base de données**: Supabase (PostgreSQL)

---

## Étape 1: Base de données (Supabase)

1. Créez un compte sur [supabase.com](https://supabase.com)
2. Créez un nouveau projet
3. Attendez que le projet soit prêt
4. Allez dans **Settings > Database**
5. Copiez la **Connection String** (elle ressemble à `postgresql://postgres:[password]@db.[project].supabase.co:5432/postgres`)

---

## Étape 2: Backend (Render)

1. Créez un compte sur [render.com](https://render.com)
2. Connectez votre repository GitHub
3. Créez un nouveau **Web Service**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`
4. Ajoutez les variables d'environnement:
   - `DATABASE_URL`: Votre URL Supabase

---

## Étape 3: Frontend (Vercel)

1. Créez un compte sur [vercel.com](https://vercel.com)
2. Importez votre repository
3. Configurez:
   - Framework Preset: **Create React App**
   - Build Command: `npm run build`
   - Output Directory: `build`
4. Ajoutez les variables d'environnement:
   - `REACT_APP_API_URL`: L'URL de votre backend Render

---

## Variables d'environnement nécessaires

### Backend
```
DATABASE_URL=postgresql://postgres:votre-mot-de-passe@db.xxxx.supabase.co:5432/postgres
```

### Frontend
```
REACT_APP_API_URL=https://votre-backend.onrender.com
```

---

## Notes importantes

1. **CORS**: Le backend est configuré pour autoriser toutes les origines
2. **Pool de connexion**: Supabase gratuite a une limite de connexions
3. **Migrations**: Exécutez les migrations SQL manuellement sur Supabase
