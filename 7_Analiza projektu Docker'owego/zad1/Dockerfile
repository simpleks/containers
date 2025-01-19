FROM python:3.9-slim

# Ustawienie katalogu roboczego w kontenerze
WORKDIR /app

# Kopiowanie folderu 'code' z hosta do kontenera
COPY code /app

# Ustawienie uprawnień do skryptu (opcjonalnie)
RUN chmod +x /app/script.py

# Uruchomienie skryptu
CMD ["python", "/app/script.py"]
