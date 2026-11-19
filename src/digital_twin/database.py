import psycopg
import os
from dotenv import load_dotenv

load_dotenv(override=True)

database_url = os.getenv("DATABASE_URL")

def initialize_database():
    """
    Initialize the database connection and create the necessary tables if they don't exist.
    """
    with psycopg.connect(database_url) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                name VARCHAR(255),
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

    print("Database initialized successfully!")

def add_user(email: str, name: str = "Name not provided", notes: str = "Notes not provided"):
    """
    Add a new user to the database.
    
    Args:
        email (str): The user's email address.
        name (str): The user's name. Defaults to "Name not provided".
        notes (str): Additional notes about the user. Defaults to "Notes not provided".

    """
    with psycopg.connect(database_url) as conn:
        conn.execute("""
            INSERT INTO users (email, name, notes)
            VALUES (%s, %s, %s)
            ON CONFLICT (email) DO NOTHING;
            """, (email, name, notes))

    print(f"User added successfully: {email}")

    
        
        