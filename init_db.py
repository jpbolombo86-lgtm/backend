from backend.app.database import engine, SessionLocal
from backend.app import models
from backend.app.security import hash_password

# Create all tables
models.Base.metadata.create_all(bind=engine)

# Create test users if no users exist
db = SessionLocal()
try:
    # Check if we already have users
    if db.query(models.User).count() == 0:
        # Create a test regular user
        test_user = models.User(
            username="testuser",
            email="test@example.com",
            hashed_password=hash_password("123456"),
            role="user"
        )
        db.add(test_user)
        
        # Create an admin user
        admin_user = models.User(
            username="admin",
            email="admin@example.com",
            hashed_password=hash_password("admin123"),
            role="admin"
        )
        db.add(admin_user)
        
        db.commit()
        print("Test users created successfully!")
        print(" - Regular user: testuser / 123456")
        print(" - Admin user: admin / admin123")
    else:
        print("Users already exist, skipping test user creation.")
finally:
    db.close()

print("Database tables created successfully!")