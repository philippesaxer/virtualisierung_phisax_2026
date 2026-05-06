# virtualisierung_phisax_2026

## Mein erster Container

Ich habe meinen ersten Docker Container mit `sudo docker run hello-world` gestartet. Der Container hat kurz eine Nachricht angezeigt und sich danach wieder beendet.

Mit `docker ps` habe ich gesehen, dass kein Container läuft. Mit `docker ps -a` habe ich den gestoppten Container gefunden. Die Container ID war `1b5592e165fa`.

Danach habe ich mit `docker images` das Image `hello-world` gefunden.

Zum Schluss habe ich alles gelöscht: Zuerst den Container mit `docker rm 1b5592e165fa` und dann das Image mit `docker rmi hello-world`.


## Get rid of Sudo

Damit man bei Docker nicht mehr Sudo eingeben muss man eine Docker Gruppe erstellen `sudo groupadd docker`. Dannach den Benutzer zur Gruppe hinzufügen `sudo usermod -aG docker $USER`. Danach kann man das `docker run hello-world` ohne dem Sudo.
