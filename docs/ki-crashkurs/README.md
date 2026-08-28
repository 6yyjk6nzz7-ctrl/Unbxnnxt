# KI-Crashkurs für Marion

**[KI-Crashkurs-fuer-Marion.pdf](KI-Crashkurs-fuer-Marion.pdf)** — 57 Seiten, A4, deutsch.

Ein Einsteigerdokument über KI: was an den Zahlen dran ist, was nicht, ein
Vier-Wochen-Plan zum Selbstlernen, und was man ohne Programmierkenntnisse zu
OffCam beitragen kann.

## Was drin ist

| Teil | Inhalt |
|---|---|
| 1 · Die Lage | Arbeitsmarktzahlen mit ihren Einschränkungen; die Studiumsfrage, mit Belegen für beide Seiten |
| 2 · Verstehen | Wie ein Sprachmodell funktioniert, warum es halluziniert, was es nicht kann, Glossar, Kritikpunkte |
| 3 · Anfangen | Die ersten 60 Minuten, ein Vier-Wochen-Plan mit 14 Aufgaben, Prompting-Grundlagen |
| 4 · Regeln | KI in Prüfungsordnungen; Datenschutz |
| 5 · Zusammen bauen | Claude Code, fünf nicht-technische OffCam-Beiträge, Jugendschutz/Zahlungen/App Store, Lern-Absprache |
| 6 · Geld, ehrlich | Einkommensverteilungen, FTC-Verfahren gegen „KI-Nebeneinkommen“, ein realistischer Weg |
| Anhänge | Kurse und Quellen mit QR-Codes, Prompt-Sammlung, Kleinunternehmerregelung/KV/BAföG |

## Zur Sorgfalt

Die Recherche lief über mehrere Dutzend Websuchen, gefolgt von einem
Prüfdurchgang, der jede Aussage gegen die Originalquelle stellen und, wo
möglich, widerlegen sollte.

| Ergebnis | Anzahl |
|---|---|
| sauber belegt | 53 |
| übertrieben (entschärft übernommen) | 46 |
| nicht überprüfbar (gestrichen) | 43 |
| falsch (gestrichen) | 11 |

Gedruckt wurden nur die ersten beiden Gruppen. `build/quellen-geprueft.txt`
enthält die druckfähigen Formulierungen mit Quell-URLs.

Danach zwei Review-Runden mit je sechs bis zehn unabhängigen Prüfungen
(Layout, Faktenlage, Deutsch, Zielgruppe, Didaktik, Schadenspotenzial,
Konsistenz): 192 Befunde in Runde eins, davon alle behoben; Runde zwei
bestätigte die Korrekturen und fand 16 weitere.

Bewusste Entscheidungen: keine Preisangaben (veralten und kosten im
Zweifel echtes Geld), keine unbelegten Rechtsaussagen, und Angaben, die sich
nicht bestätigen ließen, stehen als solche gekennzeichnet im Dokument.

## Neu bauen

```bash
python3 -m venv venv && venv/bin/pip install pypdf pypdfium2 pillow qrcode
cd build
python make.py                              # Inhalt -> marion.html
python render_chunked.py marion.html out.pdf 8   # HTML -> PDF (Chromium, stückweise)
python check_overflow.py out.pdf            # Seiten prüfen, die über den Satzspiegel laufen
python preview.py out.pdf preview 1.0       # Seiten als PNG zum Durchsehen
```

Schriften (Inter, Source Serif 4, JetBrains Mono) werden unter `/home/user/fonts`
erwartet; der Pfad steht in `doc.py` als `FONTDIR`.

**Zwei Fallstricke**, die im Bau aufgetreten sind und im Code kommentiert sind:

- Chromiums `printToPDF` bleibt bei sehr langen Dokumenten hängen. `render_chunked.py`
  rendert deshalb in Blöcken und fügt zusammen.
- Seiten haben feste Höhe mit `overflow:hidden` — zu viel Inhalt wird stillschweigend
  am Seitenrand abgeschnitten. `check_overflow.py` findet das; einmal hat genau dieser
  Fehler einen ganzen Absatz gekostet.

Seitenverweise im Text werden über `{{P:anker}}` gesetzt und erst nach dem Umbruch
aufgelöst, damit sie beim Umstellen nicht veralten.
