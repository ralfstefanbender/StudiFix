# Wie Sie das Bank-Beispiel starten
In diesem Dokument skizzieren wir kurz, was Sie tun müssen, um das Bank-Beispiel 
erfolgreich **auf Ihrem Entwickluzngsrechner** zu starten. 

**ACHTUNG:** Für den Start nach einem Deployment in die Cloud gelten andere Regeln
(vgl. Vorlesung)!

## Schritt 1: Starten des DBMS
1. Installieren Sie mySQL
2. Starten Sie den Dienst mySQL (Vorgehensweise plattformabhängig, siehe 
Hersteller-Dokumentation zu mySQL).
3. Erstellen Sie mit der Datei ```/mysql/MySQL-Dump.sql``` eine Datenbank mit 
Beispieldaten.

## Schritt 2: Starten des Backend
1. Erstellen Sie für das Projekt ein Virtual Environment, das die in dem [Dokument 
INSTALLATION.md](INSTALLATION.md) formulierten Anforderungen erfüllt.
2. Starten Sie die Datei ```/src/main.py```. Achten Sie dabei auf die Console. Dort
erscheinen entsprechende Meldungen, wenn der Start erfolgt ist.

**Anmerkungen:** Wenn Sie in PyCharm sind, einfach im Project Explorer mit der Maus 
auf die Datei gehen, Rechtsklick bzw. Sekundärklick und starten. Es entsteht dann eine
Konfiguration, die Sie später wiederverwenden und auch editieren können. Sie finden
diese Konfirguration in der IDE oben rechts in einer Klappliste neben den Buttons
für Starten, Debuggen und Stoppen. 
 
## Schritt 2: Starten des Frontend
1. Stellen Sie sicher, dass sich im Verzeichnis ```/src/static/``` ein Unterordner 
mit dem kompilierten React Client befindet. Wie Sie die React-spezifischen Vorbereitungen
treffen, wird Ihnen ebenfalls in dem [Dokument INSTALLATION.md](INSTALLATION.md) beschrieben.
2. Rufen Sie in Ihrem Browser die URL auf, die die Datei ```index.html``` innerhalb
des React Client-Ordners korrekt adressiert. Dies wird wahrscheinlich diese URL sein:
http://127.0.0.1:5000/static/reactcliengt/index.html