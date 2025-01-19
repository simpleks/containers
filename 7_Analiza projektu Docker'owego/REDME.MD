# zad 1.
docker build -t python-script-container .

docker run --rm python-script-container


# zad 2.

docker run -d --name moj_kontener python:3.9-slim tail -f /dev/null

docker cp kontener.txt moj_kontener:/app/kontener.txt

docker exec -it moj_kontener /bin/sh


docker stop moj_kontener && docker rm moj_kontener


# zad 3

docker cp moj_kontener:/app/kontener2 ./kontener2

docker cp moj_kontener:/app/kontener2 ~/Desktop/kontener2

# zad4

docker build -t entrypoint-demo .

docker run --rm entrypoint-demo


docker run --rm entrypoint-demo "Lato 2025"


# zad 5 

docker-compose up -d

docker ps


psql -h localhost -U admin -d mydatabase

lub

docker exec -it postgres_container psql -U admin -d mydatabase

# Zad 6

WORKDIR /app → Ustawia /app jako katalog roboczy.
COPY app /app → Kopiuje cały folder app do /app w kontenerze.
ADD archive.tar.gz /app/extracted → Automatycznie rozpakowuje archive.tar.gz do /app/extracted.
CMD ["python", "/app/script.py"] → Uruchamia script.py po starcie kontenera.


Komenda	Funkcja
COPY	Kopiuje pliki i foldery z hosta do kontenera bez zmian.


ADD	Kopiuje pliki i foldery, ale dodatkowo rozpakowuje archiwa .tar.gz i może pobierać pliki z URL.


# zad 7

docker-compose up --build

docker exec -it postgres_db psql -U admin -d mydatabase

SELECT * FROM users;



✅ docker-compose pozwala łatwo uruchamiać aplikacje z bazą danych.
✅ depends_on zapewnia kolejność uruchamiania usług.
✅ volumes pozwalają na trwałość danych bazy.

To gotowy projekt, który możesz od razu uruchomić! 🚀


# zad 8 


Komenda docker inspect zwraca szczegółowe informacje o kontenerze w formacie JSON, w tym:

- IP kontenera
- Mapowanie portów
- Ścieżki wolumenów
- Status uruchomienia
- Identyfikator kontenera


docker logs – Podgląd logów kontenera

Komenda docker logs pozwala zobaczyć:

- Output aplikacji w kontenerze
- Błędy i komunikaty debugowania
- Informacje o działaniu kontenera


# zad 9 

docker-compose up -d

docker network ls

docker network inspect my_network


Sieć Docker	Opis
bridge (domyślna)	Kontenery mogą się komunikować po nazwach hostów.

host	Kontener działa na tej samej sieci co host.

none	Brak sieci (pełna izolacja).



# zad 10

docker build -t my-python-app .

docker images

docker run --rm my-python-app

docker ps

docker ps -a


# zad 11

docker ps

docker exec -it <CONTAINER_ID> sh

lub

docker exec -it <CONTAINER_ID> bash

docker exec -it python_app sh

echo "To jest testowy plik w kontenerze" > /app/test.txt

cat /app/test.txt


docker run -it --rm -v $(pwd)/data:/app my-python-app sh

echo "Trwałe dane w kontenerze" > /app/test.txt

cat data/test.txt


# zad 12

docker build -t my-python-app .

docker images

docker.io/<nazwa_użytkownika>/<nazwa_obrazu>:<tag>

example:
docker tag my-python-app tomasz123/my-python-app:latest


docker login

docker push tomasz123/my-python-app:latest


// usuwanie

docker images

docker rmi tomasz123/my-python-app:latest

docker images


// pubieranie

docker pull tomasz123/my-python-app:latest

docker images


// uruchamianie pobranego obrazu


docker run --rm tomasz123/my-python-app





