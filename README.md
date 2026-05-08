# virtualisierung_phisax_2026

## Mein erster Container

Ich habe meinen ersten Docker Container mit `sudo docker run hello-world` gestartet. Der Container hat kurz eine Nachricht angezeigt und sich danach wieder beendet.

Mit `docker ps` habe ich gesehen, dass kein Container läuft. Mit `docker ps -a` habe ich den gestoppten Container gefunden. Die Container ID war `1b5592e165fa`.

Danach habe ich mit `docker images` das Image `hello-world` gefunden.

Zum Schluss habe ich alles gelöscht: Zuerst den Container mit `docker rm 1b5592e165fa` und dann das Image mit `docker rmi hello-world`.


## Get rid of Sudo

Damit man bei Docker nicht mehr Sudo eingeben muss man eine Docker Gruppe erstellen `sudo groupadd docker`. Dannach den Benutzer zur Gruppe hinzufügen `sudo usermod -aG docker $USER`. Danach kann man das `docker run hello-world` ohne dem Sudo.


## Container Image auf Docker hochladen
[Docker-Repository](https://hub.docker.com/repository/docker/philippesaxer/pythonwebserver/general)
Zuerst muss man den Account und Repo erstellen danach muss man: 

`docker login`

`docker tag <dockername> <benutzernamedockerhub>/<repository>:latest`

`docker push <benutzernamedockerhub>/<repository>:latest`


## Container Performance
Man muss den Pythonwebserver wieder ausführen mit `docker run --rm -p 8000:8081 --name pythonwebserver pythonwebserver` um verschiedene Informationen zum Docker und Performance zu sehen muss man `docker stats` eingeben und bekommt das als Output:

```
CONTAINER ID   NAME              CPU %     MEM USAGE / LIMIT    MEM %     NET I/O         BLOCK I/O     PIDS
bdc58b90dcbd   pythonwebserver   0.02%     14.06MiB / 7.51GiB   0.18%     1.17kB / 126B   0B / 1.72MB   1
```


## Portainer installieren 
Um Portainer zu installieren habe ich zuerst `mkdir portainer` gemacht und dannach `cd portainer` (nicht unbedingt nötig).

Danach habe ich `nano docker-compose.yml` mit folgendem Inhalt:

```
version: "3.8"

services:
  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer_with_volume
    restart: always
    ports:
      - "9443:9443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - /srv/portainer_data:/data
```

Dann muss man den Datenordner erstellen `sudo mkdir -p /srv/portainer_data`.
Nachdem muss man den Container starten `docker compose up -d`
Portrainer kann man dann auf `https://localhost:9443`.


#### Warum braucht es dieses Persistent Volume ?

Das Persistent Volume braucht es damit die Daten nicht im Container selbst gespeichert werden sondern auf dem Host-System.

#### Was passiert mit den bereits erstellten Daten und Konfigurationen, wenn du den Container und das Image vollständig weglöscht und dann wieder installierst?

Alle Daten im Container wären weg und Portainer startet wie frisch installiert. Neues Login etc.


## Wichtige Docker Befehle
`docker build -t getting-started .`


##  Container-Monitoring mit cAdvisor, Prometheus und Grafana

Um mich in Grafana anzumelden bin ich mit `nano docker-compose.yml` einfach ins File gegangen. Dort habe ich bei `GF_SECURITY_ADMIN_USER` und `GF_SECURITY_ADMIN_PASSWORD` die Daten gefunden. Es waren admin und admin und schlussendlich konnte ich das Passwort auf Localhost:3000 ändern.


## Mail Relay Server mit postfix

Das habe ich in mein Docker-compose.yml geschrieben.

```
services:
  postfix:
    image: boky/postfix:latest
    container_name: mail-relay
    environment:
      - RELAYHOST=[smtp.gmail.com]:587
      - RELAYHOST_USERNAME=philippesaxer8@gmail.com
      - RELAYHOST_PASSWORD=vwyv tuxb sitk nflk
      - ALLOWED_SENDER_DOMAINS=gmail.com
    restart: always
```


## Container Netzwerk

Im Test Container bin ich mit `docker compose exec test sh` gekommen und habe folgende Tests gemacht:

```
~ $ nslookup backend
Server:         127.0.0.11
Address:        127.0.0.11:53

Non-authoritative answer:

Non-authoritative answer:
Name:   backend
Address: 172.28.0.2

~ $ curl http://backend:5000
{"hostname":"e75a0a24219d","remote_addr":"172.28.0.4","service":"backend"}

~ $ curl http://frontend
{"hostname":"e75a0a24219d","remote_addr":"172.28.0.3","service":"backend"}
~ $ nslookup frontend
Server:         127.0.0.11
Address:        127.0.0.11:53

Non-authoritative answer:

Non-authoritative answer:
Name:   frontend
Address: 172.28.0.3
```

Alle Test kamen korrekt heraus.
