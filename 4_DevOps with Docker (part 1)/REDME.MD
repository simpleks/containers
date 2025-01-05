
# Section -1

1. Tworzenie konterera

![](images/img.png)

2. Lista kontenerów

![](images/img_1.png)

3. Zarządzanie kontenerami

![](images/img_2.png)

4. Tworzenie ngix

![](images/img_3.png)

![](images/img_5.png)

![](images/img_6.png)

![](images/img_7.png)


# Section-2

![](images/img_8.png)

![](images/img_9.png)

![](images/img_10.png)

![](images/img_11.png)\

![](images/img_12.png)

![](images/img_13.png)


5. CURL

![](images/img_15.png)

![](images/img_16.png)

![](images/img_17.png)

niestety po zainstalowaniu curdla mam tylko to nie po potrafię sobie z tym poradzić.



# Section-3

![](images/img_18.png)

![](images/img_19.png)

![](images/img_20.png)

żróduło : 
```https://hub.docker.com/r/devopsdockeruh/pull_exercise ```  

![](images/img_21.png)

6. Zadanie 1.7
script.sh
```
#!/bin/bash
while true
do
  echo "Input website:"
  read website; echo "Searching.."
  sleep 1; curl http://$website
done
```

Dockerfile
```
# Use Ubuntu 22.04 as base image
FROM ubuntu:22.04

# Update and install curl
RUN apt-get update && apt-get install -y curl

# Copy the script into the container
COPY script.sh /script.sh

# Grant execute permissions to the script
RUN chmod +x /script.sh

# Set the script as the command to run when the container starts
CMD ["/script.sh"]
```


![](images/img_23.png)

![](images/img_24.png)


# Section-4

![](images/img_25.png)

![](images/img_26.png)

![](images/img_27.png)

![](images/img_28.png)

![](images/img_29.png)


# Sekcja 5 

![](images/img_30.png)

![](images/img_31.png)

![](images/img_32.png)

![](images/img_33.png)

zadanie 1.10
![](images/img_36.png)

![img.png](img.png)


# sekcja 6

Dockerfile :
```
# Użyj Ruby 3.1.0 jako bazowego obrazu
FROM ruby:3.1.0

# Otwórz port 3000
EXPOSE 3000

# Ustaw katalog roboczy
WORKDIR /usr/src/app

# Zainstaluj odpowiednią wersję Bundlera
RUN gem install bundler:2.3.3

# Skopiuj pliki potrzebne do instalacji zależności
COPY Gemfile* ./

# Zainstaluj zależności
RUN bundle install

# Skopiuj całą resztę kodu źródłowego
COPY . .

# Uruchom migracje bazy danych
RUN rails db:migrate RAILS_ENV=production

# Prekompiluj zasoby (assets)
RUN rake assets:precompile

# Uruchom aplikację w trybie produkcyjnym
CMD ["rails", "s", "-e", "production"]
```

Uruchomiona gra:
![](images/img_34.png)

![](images/img_35.png)

zadanie 1.11 SPRING

![](images/img_37.png)

błąd z plikiem ./mvnw


zadanie 1.12 frontend:

Dockerfile się buduje niestety pod adresem nic się nie dzeje

zadanie 1.13 backend:

problem z npm



