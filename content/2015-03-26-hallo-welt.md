Title: Hallo Welt!
Date: 2015-03-26 20:13
Modified: 2015-03-26 20:13
Category: Python
Tags: Terminal,print
Slug: hallo-welt
Authors: Martin Thoma
Summary: Installation, Editor, Ausgabe von Text

Das folgende Tutorial bereitet alles vor, damit wir mit dem Programmieren
anfangen können. Du wirst damit lernen, wie du ein Programm schreibst, wie du
dir Werte speicherst, wie du einen Editor benutzt und Text im Terminal
ausgibst.


## Installation

Starte ein Terminal. Das kannst du eventuell mit dem Tastenkürzel
<kbd>Strg</kbd>+<kbd>Shift</kbd>+<kbd>T</kbd> machen. <kbd>Shift</kbd> ist die
"Pfeil-nach-oben-Taste". Du musst alle drei Tasten gleichzeitig drücken.
Ich drücke dazu zuerst <kbd>Strg</kbd>, halte die Taste gedrückt, drücke dann
<kbd>Shift</kbd>, halte auch diese Taste gedrückt (nun sind es schon zwei!)
und drücke schließlich <kbd>T</kbd> für Terminal.

Wenn das nicht geklappt hat, kannst du das Terminal auch über die Startleiste
öffnen. Bei mir sieht das so aus:

![Screenshot der geöffnenten Startleiste]({attach}/images/open-terminal.png)

Eine weitere Möglichkeit das Terminal zu öffnen ist über den Datei-Explorer.
Dazu öffnet man ihn, macht in den Ordner in dem man arbeiten will einen
Rechtsklick, und klickt auf das Terminal:

![Screenshot des Kontext-Menüs zum öffnen des Terminals]({attach}/images/open-terminal-via-context-menu.png)


Wenn es wie folgt aussieht, hast du alles richtig gemacht:

![Screenshot der geöffnenten Startleiste]({attach}/images/terminal-screenshot.png)


## Tools

Jeder hat so seine Lieblingswerkzeuge und der Werkzeugkasten eines Hackers ist
sehr groß. Einen Überblick über die wichtigsten gibt es nun.


### Terminal-Befehle

Gute Hacker müssen mit dem Terminal umgehen können. Das Terminal kann
man immer auf die gleiche Art bedienen. Es ändert sich nichts. Das ist ein
riesiger Vorteil im Vergleich zu grafischen Benutzeroberflächen.

Das blinkende kleine Kästchen in Terminal heißt *Cursor*. Um es vom Mauscursor
abzugrenzen sagt man manchmal auch *Textcursor*. Links vom Cursor steht bei mir
`moose@pc08`, weil mein Benutzername `moose` ist und ich meinen PC `pc08`
genannt habe. Bei dir steht steht eventuell `nicolai@meinerster`. Da das bei
jedem anders ist, gibt man Befehle häufig mit einem führendem Dollar-Zeichen
(`$`) an. Das Dollar-Zeichen soll **nicht** getippt werden. Es dient nur zur
verdeutlichung, dass man nun einen Befehl in das Terminal eingeben soll.

Manchmal sieht das Terminal so aus:

![Screenshot vom Terminal, das im Desktop geöffnet wurde]({attach}/images/terminal-in-desktop.png)

Die wichtigsten Befehle sind:

| Befehl             | Name             | Was der Befehl macht                                                             |
| ------------------ | ---------------- | -------------------------------------------------------------------------------- |
| `ls`               | list segments    | Liste dir alle Dateien und Ordner auf, die in dem aktuellen Ordner sind          |
| `cd ORDNER`        | change direktory | Wechsel in den Ordner ORDNER                                                     |
| `cd ..`            |                  | In eine Ordnerebene höher wechseln                                               |
| `cd ~`             |                  | In den einen Home-Ordner wechseln                                                |
| `mkdir ORDNERNAME` | make directory   | Erstelle im aktuellen Ordner einen neuen Ordner mit dem Namen ORDNERNAME         |
| `sublime`          |                  | Startet das Programm 'sublime', falls es installiert ist.                        |
| `history`          |                  | Die letzten Befehle anzeigen                                                     |
| `clear`            |                  | Den Inhalt des Terminals entfernen - es wird nichts gelöscht. Nur saubergemacht. |

Spiel doch mal ein bisschen damit herum. Öffne einen Order im Datei-Explorer
und gleichzeitig im Terminal. Erzeuge neue Ordner mit `mkdir` und lasse dir das
Ergebnis mit `ls` anzeigen. Schau auch mal mit dem Datei-Explorer nach, ob es
wirklich dort ist.

### Editor

Ich verwende [Sublime Text 3](http://www.sublimetext.com/). Das ist ein toller
Editor der für alle Betriebssysteme verfügbar ist. Allerdings tut es für dieses
Tutorial auch `gedit`. Dieser ist auf Ubuntu mit GNOME bereits vorinstalliert.

Öffne deinen Editor.

**WICHTIG: Microsoft Word, Libre Office und OpenOffice sind keine Text-Editoren!**

## Erstes Programm

1. Erstelle einen neuen Ordner für diese Tutorials. Mache dazu in deinem
   Home-Ordner (z.B. `/home/nicolai/`, also inclusive Benutzername) einen neuen
   Ordner `python-lernen`.
2. Erstelle in diesem Ordner (z.B. `/home/nicolai/python-lernen`) eine Datei
   mit dem Namen `hello.py`. Die Dateiendung `.py` signalisiert, dass dort
   Python Code stehen wird.

Nun schreibe folgenden Inhalt in die Datei:

```python
print("Hallo Welt")
```

Öffne die Konsole in dem Ordner mit der Python-Datei. Überprüfe mit `ls`, ob
die Python-Datei auch wirklich da ist. Falls sie nicht angezeigt wird, bist
die mit der Konsole im falschen Ordner. Wechsle mit `cd` in den richtigen
Ordner.

Nun gibt im Terminal

```bash
$ python3 hello.py
```

ein. Nicht vergessen, dass `$`-Zeichen soll *nicht* mit eingegeben werden. Es
signalisiert nur, dass etwas folgt was im Terminal eingegeben werden soll.

Es sollte nun etwa so aussehen:

![Screenshot des Terminals]({attach}/images/python-hallo-welt.png)

Gratulation, du hast gerade dein erstes Programm geschrieben!