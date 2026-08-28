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

---

## Interaktive englische Fassung

**[Off Cam, On Build](https://claude.ai/code/artifact/d51cc57a-617e-44a3-8fac-7ff06104691d)** —
Quelle: `interactive/off-cam-on-build.html`

Dieselbe Recherche, aber als interaktive Seite auf Englisch, mit der Chance
zuerst und den Einschränkungen danach:

- **Bearbeitbare persönliche Notiz** — Klick in den Text, wird lokal gespeichert
- **Drei Sichten auf die Belege** — Chancen / Kleingedrucktes / Deutschland
- **Verdienstrechner** — eigene Werte eingeben; zeigt Median, realistischen und
  guten Fall gegen die Zahl, die Kurse versprechen
- **Vier-Wochen-Plan** — 18 Aufgaben zum Abhaken, Fortschritt bleibt erhalten
- **Prompts** mit Kopier-Knopf, Ressourcen, und eine Tabelle mit jeder
  Behauptung der Seite und ihrem Prüfergebnis

Hell und dunkel, ohne externe Bibliotheken; Fortschritt liegt in `localStorage`
und verlässt das Gerät nicht.

---

## The Second Company

**[Live](https://claude.ai/code/artifact/e66359e5-e55c-41d7-95ae-adee2484868a)** —
Quelle: `interactive/the-second-company.html`

Nach dem ersten Jahr neu aufgesetzt: nicht mehr „lohnt sich KI?“, sondern das
Angebot an Marion, als Mitgründerin einzusteigen.

- **Hero** — die Jahreszahl als animierter Zähler in Messing-Verlauf
- **19 editierbare Felder** — Zahlen, Firmennamen, Rollen, der Brief; alles
  anklickbar und lokal gespeichert
- **Drei Ventures** mit der vorgeschlagenen Aufteilung
- **Vier-Wochen-Ramp** — auf Mitgründerin ausgelegt, nicht auf Anfängerin
- **Zwei-Operator-Modell** — Basisjahr, Stunden, Horizont, Anzahl Firmen als
  Eingaben; Zuwachs bewusst sublinear (+55 %, nicht +100 %) plus
  Einarbeitungskurve und eine ehrliche Erfolgswahrscheinlichkeit
- **The floor** — wie außergewöhnlich das Ergebnis im Verteilungsvergleich ist

Instrument Serif / Onest / JetBrains Mono, Canvas-Aurora mit Korn-Overlay,
scroll-getriggerte Reveals, keine externen Bibliotheken.

`build/shot.js` macht Ganzseiten-Screenshots über CDP — scrollt vorher durch die
Seite, damit IntersectionObserver-Reveals ausgelöst werden, bevor aufgenommen wird.

---

## Two Operators (aktuelle Fassung)

**[Live](https://claude.ai/code/artifact/18d32657-f282-4f46-aefe-b8b68c9ade3b)** —
Quelle: `interactive/two-operators.html`

Neu gestaltet: monochrom, hoher Kontrast, ein einziger Akzent (`#5D7FFF`),
Haarlinien statt Karten. Kein Verlauf, kein Glow, kein Korn — Archivo (variable
Breitenachse) plus JetBrains Mono.

- **Rail-Navigation** links mit aktivem Abschnitt, Scroll-Fortschritt oben
- **22 editierbare Felder**, lokal gespeichert
- **Maschinen** — M5 Ultra / MacBook Pro M4 Max 36 GB
- **Modell** — zeigt jetzt auch, auf wie viele Wochenstunden Konstantin fällt
  (aus 50+), nicht nur den Umsatz
- **50+ h/Woche** steht offen im Hero: der Preis des ersten Jahres

### Zwei Werkzeuge

`build/shot.js` — Ganzseiten-Screenshots über CDP. Scrollt vorher durch die Seite,
weil IntersectionObserver-Reveals sonst nicht auslösen; `--reveal` erzwingt sie
zusätzlich, `dark`/`light` emuliert das Farbschema.

`build/probe.js` — wertet einen JS-Ausdruck gegen eine lokale HTML-Datei aus und
gibt das Ergebnis als JSON zurück. Damit ließ sich eine Klassenkollision finden,
die visuell nicht eindeutig war: `.chip.v` traf auch die Venture-Regel `.v`
(`display:grid`), und dieselbe Regel vererbte `border-bottom` an `.kpi .v`.
Klassen heißen jetzt `.vrow` und `.chip-alt`.
