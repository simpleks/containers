FROM python:3.9-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie folderu 'app' do kontenera
COPY app /app

# Dodanie pliku tar.gz (automatycznie go rozpakowuje)
ADD archive.tar.gz /app/extracted

# Uruchomienie skryptu
CMD ["python", "/app/script.py"]
