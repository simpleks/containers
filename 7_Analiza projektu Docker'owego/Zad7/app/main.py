import psycopg2
import os

DB_NAME = os.getenv("POSTGRES_DB", "mydatabase")
DB_USER = os.getenv("POSTGRES_USER", "admin")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "db")

try:
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
    )
    cur = conn.cursor()

    # Tworzenie tabeli
    cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT);")
    cur.execute("INSERT INTO users (name) VALUES ('Tomasz'), ('Anna');")
    conn.commit()

    # Pobranie danych
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    print("👥 Lista użytkowników w bazie:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()
except Exception as e:
    print("❌ Błąd połączenia z bazą:", e)
