# Fragen

## Zugriff per Index/Key auf Listen/Maps:

- Listen in SetlX fangen bei Index 1 an, in Python bei 0
- Zugriff auf Map-Werte über Key wird mit selbem Syntax wie Index Zugriff auf Listen  umgesetzt
- Abziehen von "1" bei jedem Index Zugriff geht nicht, da nicht bekannt ob Liste oder Map
- Lösungen:
    - Implementierung einer eigenen Liste Klasse, welche mit Index 1 beginnt
    - Index Zugriff mit Funktion, welche zur Laufzeit zwischen Liste und Map unterscheiden kann
        - z.B. `liste[2]` wird übersetzt zu `get(liste,2)`

## Boolesche Operatoren

- In SetlX können boolesche Operatoren nur auf boolesche Werte (true/false) ausgeführt werden
- Python erlaubt das Ausführen dieser Operatoren auf alle Werte 
- z.B. der Ausdruck `True and 2` in Python liefert das Ergebis `2`. Der vergleichbare Ausdruck `true && 2` in SetlX wirft einen Fehler, da `2` kein boolescher Ausdruck ist.
- Lösungen:
    - Keine "Sonderbehandlung" korrekte SelX Programme funktionieren trotzdem
    - Verpacken der Argumente in eine Funktion: `x && y ` wird übersetzt zu `bool(x) and bool(y)`. Funktion `bool` wirft einen Fehler, falls der übergebene Wert kein boolescher Wert ist


## Values and References
- SetlX-Mengen enthalten Values, Python References
- Müssen alle Werte _deepcopied_ werden?