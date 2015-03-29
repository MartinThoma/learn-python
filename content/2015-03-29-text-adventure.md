Title: Text adventure
Date: 2015-03-29 10:41
Modified: 2015-03-29 10:41
Category: Python
Tags: if/else,Variablen,input,Datentypen
Slug: text-adventure
Authors: Martin Thoma
Summary: Programmieren eines Text-Adventure-Spiels

Heute wollen wir ein Text-Adventure-Spiel programmieren. Das sind Spiele,
die im Termal ablaufen und rein Text-basiert sind. Man gibt dem Spieler
immer wieder Text (z.B. was er gerade sieht oder was gerade passiert) und
Auswahlmöglichkeiten, was er als nächstes tun kann.

Wir benötigen also:

* Eine Möglichkeit vom Spieler Eingaben zu bekommen
* Eine Möglichkeit diese Eingaben mit etwas zu vergleichen
* Eine Geschichte

## Benutzereingaben

Mit [`input`](https://docs.python.org/3/library/functions.html#input) kann man
vom Benutzer Eingaben bekommen. Das sieht dann so aus:

```python
input("Wie heist du? ")
```

Speichere das in einer Datei names `tag2.py` und führe es mit `python3 tag2.py`
aus.

Das ist aber so noch nicht hilfreich. Nun kann der Benutzer zwar etwas
eingeben, aber wir machen nichts dafür. Um etwas mit der Eingabe machen zu
können, müssen wir die Eingabe speichern. Dazu brauchen wir eine Variable.
Variablen sind wie Ettiketten. Du hast Werte, aber um sie zu finden benötigst
du die Ettiketten. Und man ettikettiert so:

```python
variable = "Wert"
```

Die Anführungszeichen `"` um `"Wert"` sagen, dass es sich um eine Zeichenkette
handelt. Da Variablen immer mit einem Buchstaben (egal ob groß oder klein)
anfangen und beliebig (ohne Leerzeichen) weiter gehen, kann `Wert` ja auch eine
Variable sein. Der Code

```python
variable = Wert
```

würde also bedeuten, dass die Variable `variable` den selben Wert ettikettiert
wie die Variable `Wert`. Daher benötigen wir bei Zeichenketten die
Anführungszeichen um klar zu machen, dass es sich nicht um eine Variable,
sondern um eine Zeichenkette handelt.

Bei Zahlen ist das anders. Da Variablen immer mit Buchstaben beginnen, kann
man direkt erkennen wenn es sich um eine Zahl handelt:

```python
mein_alter = 24
```

Nun könnte man aber auch

```python
mein_alter = "24"
```

schreiben. Der Unterschied ist, dass der Computer im ersten Fall (ohne die
Anführungszeichen) davon ausgeht, dass es sich um eine Zahl handelt.
Im zweiten Fall geht er davon aus, dass es sich um eine Zeichenkette handelt.
Das macht einen Unterschied, wenn wir damit arbeiten wollen. Zum Beispiel
wollen wir ausdrücken, dass ein Jahr vergangen ist. Dann bin ich natürlich
ein Jahr älter geworden. Also erhöhen wir mein alter um 1:

```python
mein_alter = mein_alter + 1
```

Hier sieht man, dass die Schreibweise nicht gleich der Schreibweise in der
Mathematik ist. In der Mathematik vergleicht man mit `=` die linke und die
rechte Seite. In der Informatik weist man den Wert der rechten Seite der
Variablen auf der linken Seite zu.

Nun probiere mal beide Varianten aus. Erstelle dazu eine Datei `meinAlter.py`
und führe diese mit `python3 meinAlter.py` aus.

**Variante 1**: Zahlen-Schreibweise

```python
mein_alter = 24
mein_alter = mein_alter + 1
print(mein_alter)
```

**Variante 2**: Zeichenkette-Schreibweise

```python
mein_alter = "24"
mein_alter = mein_alter + 1
print(mein_alter)
```

Die zweite Ausgabe hat zu dem Fehler

```bash
$ python3 meinAlter.py
Traceback (most recent call last):
  File "meinAlter.py", line 2, in <module>
    mein_alter = mein_alter + 1
TypeError: Can't convert 'int' object to str implicitly
```

geführt. Wichtig ist, dass der Computer dir sagt, dass der Fehler in `line 2`,
also Zeile 2 passiert ist. Außerdem sagt er dir, dass der Fehler
`TypeError: Can't convert 'int' object to str implicitly` war. Das bedeutet,
der Datentyp `int` (englisch für *integer*, also eine ganze Zahl) kann nicht
zu `str` (englisch für *string*, also Zeichenkette) konvertiert werden.
Die Operation `+` ist also nicht definiert, wenn links eine Zeichenkette und
rechts eine Zahl steht. Nun ändere `1` in `"1"` und schau dir an was passiert.
Macht das Sinn?

Nun wieder zurück zu der `input` Funktion. Wir speichern uns den Rückgabewert
der Funktion in einer Variablen und geben `Hallo [Name]` aus. Speichere
den folgenden Text in einer Datei `begruessung.py` (bitte benutze vorerst noch
keine Umlaute) und führe es mit `python3 begruessing.py` aus:

```python
name = input("Wie heist du? ")
print("Hallo " + name + ". Wie geht es dir?")
```

Ok. Du weißst nun also wie man Benutzereingaben bekommt. `input` gibt immer
eine Zeichenkette zurück. Was macht man aber, wenn man eine Zahl will? Wenn wir
also ein Programm zum multiplizieren von ganzen Zahlen schreiben wollen?

Dann müssen wir die Eingabe in den Ganzzahl-Typ `int` konvertieren. Das macht
man mit der gleichnamigen Funktion
[`int`](https://docs.python.org/3/library/functions.html#int). Speichere das
folgende Programm als `taschenrechner.py` und führe es mit `python3
taschenrechner.py` aus:

```python
erste_zahl = input("Wie lautet die erste Zahl? ")
erste_zahl = int(erste_zahl)
zweite_zahl = input("Wie lautet die zweite Zahl? ")
zweite_zahl = int(zweite_zahl)
print(erste_zahl * zweite_zahl)
```

Komma-Zahlen heißen im Computer `float` und entsprechend kann man die Funktion
`int` einfach durch die Funktion
[`float`](https://docs.python.org/3/library/functions.html#float) ersetzen:

```python
erste_zahl = input("Wie lautet die erste Zahl? ")
erste_zahl = float(erste_zahl)
zweite_zahl = input("Wie lautet die zweite Zahl? ")
zweite_zahl = float(zweite_zahl)
print(erste_zahl * zweite_zahl)
```


## Die Geschichte

Es gibt unendlich viele Geschichten, die man den Spieler erleben lassen kann.
Ich will mich hier auf eine ganz einfache beschränken, aber du solltest dir
überlegen, wie du eine eingene Geschichte schreiben kannst bzw. wie du
meine Geschichte erweitern kannst.

> Das erste, was du wahrnimmst ist Salzwasser in deinem Mund. Du liegst an
> einem Strand und fühlst wie die Wellen. Dein Magen knurrt und dir ist ein
> wenig schlecht. Eventuell hast du Salzwasser verschluckt.
>
> Du hast nur ein T-Shirt, eine lange Hose und einen Schuh an. In deinen
> Hosentaschen ist nichts.
>
> Verwirrt stehst du auf und siehst dich um. Du bist auf einer wunderschönen
> Insel. Das Wasser brandet klar den flachen Sandstrand entlang. Die Sonne
> brennt vom Himmel herab. Ein paar
> hundert Meter vor dir geht der Strand in einen Wald über. Links von dir
> siehst du einen Berg. Dort scheint Rauch zu sein. Eventuell ein Lagerfeuer?
>
> Was willst du tun?
>
> (1) In den Wald gehen (2) Nach rechts, am Strand entlang gehen (3) Nach links
> am Strand entlang auf den Berg zu gehen.

Nun kann der Spieler eine Wahl treffen. Damit wir uns die verschiedenen Pfade,
die der Spieler in dem Handlungsstrang nehmen kann merken können, notieren
wir diese in der Form 1.2.1.4. Das Bedeutet, der Spieler hat die erste Frage
mit 1 beantwortet, die zweite Frage mit 2, die dritte Frage mit 1 und die
vierte Frage mit 4.

### 1

> Du gehst in den Wald. Dort ist es deutlich kühler. Allerdings haben das auch
> einige Insekten erkannt. Dich umschwirren viele Mücken. Du wartest ein paar
> Sekunden, bis sich deine Augen an die neuen Lichtverhältnisse gewöhnt haben.
> Nun siehst du, dass der Wald nur leichten Unterwuchs hat; du kannst also
> gut durch den Wald laufen. Die Pflanzen fühlen sich angenehm an, aber du
> siehst nicht worauf du trittst.
>
> Der Wald scheint sich sehr weit auszubreiten. Was wohl dahinter kommt?
>
> Was willst du tun?
>
> (1) Zurück zum Strand (2) Im Wald, aber in Sichtweite des Strandes nach
> rechts laufen (3) Im Wald, aber in Sichtweite des Strandes, in richtung Berg
> laufen (4) Den Wald durchqueren.

### 1.1

> Am Strand hat sich nichts geändert es ist immer noch heiß.
>
> Was willst du tun?
>
> (1) Zurück in den Wald (2) Am Strand entlang, weg vom Berg gehen (3) Nach
> links am Strand entlang auf den Berg zu gehen.

### 1.2

> Du läufst ca. 2 Stunden, dann siehst du eine Hütte am Strand, nur ein paar
> Meter von den ersten Bäumen entfernt. Was willst du tun?

## Das Programm

Wie wir den ersten Text ausgeben, haben wir ja schon gelernt. Speichere
das folgende in `adventure.py`:

```python
print("Das erste, was du wahrnimmst ist Salzwasser in deinem Mund. Du liegst ")
print("an einem Strand und fühlst wie die Wellen. Dein Magen knurrt und dir ")
print("ist ein wenig schlecht. Eventuell hast du Salzwasser verschluckt. ")
print("Du hast nur ein T-Shirt, eine lange Hose und einen Schuh an. In deinen")
print("Hosentaschen ist nichts.")
print("Verwirrt stehst du auf und siehst dich um. Du bist auf einer")
print("wunderschönen Insel. Das Wasser brandet klar den flachen Sandstrand ")
print("entlang. Die Sonne brennt vom Himmel herab. Ein paar")
print("hundert Meter vor dir geht der Strand in einen Wald über. Links von")
print("dir siehst du einen Berg. Dort scheint Rauch zu sein. Eventuell ein ")
print("Lagerfeuer?")
print("")
print("Was willst du tun?")
print("")
print("(1) In den Wald gehen ")
print("(2) Nach rechts, am Strand entlang gehen ")
print("(3) Nach links am Strand entlang auf den Berg zu gehen.")
wahl = input("Gebe deine Wahl ein [1,2,3]:")
```

Die Zeilen sollten nicht zu lang werden. Maximal 80 Zeichen pro Zeile, damit
der Code gut lesbar bleibt.

Ok, nun haben wir was der Spieler machen will in der Variable `wahl`. Mit
if/elif/else müssen wir unser Programm nun darauf anpassen. Füge die folgenden
Zeilen nach der letzten Zeile in `adventure.py` hinzu:

```python
if wahl == "1":
    print("Du gehst in den Wald.")
    print("Eine interessante Wahl!")
elif wahl == "2":
    print("Du bist nach rechts gegangen.")
elif wahl == "3":
    print("Du bist nach links gegangen.")
else:
    print("Keine korrekte Auswahl.")

print("Das hier wird immer ausgeführt, egal wie die Wahl war.")
```

`elif` steht dabei für `else if`. Man geht also alle Möglichkeiten durch.
Wichtig ist hierbei, dass was auch immer nun kommt mit 4 Leerzeichen eingerückt
wird. Also für `print("...")` müssem 4 Leerzeichen stehen. Das macht man, indem
man die Taste `Tab` (ganz links auf der Tastatur, sie zeigt einen Pfeil der
nach links geht und einen Pfeil der nach rechts geht übereinander) drückt.

Wir haben mit `==` verglichen, ob die Variable `wahl` gleich `"1"` ist.
Wenn das der Fall ist, wir der eingerückte Block dannach ausgeführt. Falls
nicht, wird der nächste Vergleich gemacht (`elif wahl == "2"`). Das, was dann
Eingerückt kommt wird also "Block" genannt. Den Teil nach `if` bzw `elif` nennt
man die Bedingung für den Block. `else` hat keine Bedinung. Der else-Block
steht am Ende und wird ausgeführt, wenn alle vorherigen Bedingungen falsch
waren.

Man kann das auch schachteln:

```python
eingabe = input("Gebe eine ganze Zahl ein: ")
eingabe = int(eingabe)

if eingabe > 10:
    print("Deine Eingabe war größer als 10")
    if eingabe < 100:
        print("Deine Eingabe war kleiner als 100.")
    else:
        print("Deine Eingabe war sogar größer als 100.")
else:
    print("Deine Eingabe war kleiner oder gleich 10.")
```