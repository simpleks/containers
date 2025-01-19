FROM python:3.9-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie plików do kontenera
COPY script.py /app/
COPY entrypoint.sh /app/

# Nadanie uprawnień do wykonywania
RUN chmod +x /app/entrypoint.sh

# Definicja ENTRYPOINT i CMD
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["Brak argumentów domyślnych"]


