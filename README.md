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


