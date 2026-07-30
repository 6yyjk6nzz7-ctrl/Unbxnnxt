# OffCam 🔴

**Dating & Collabs für verifizierte Creator — off camera, auf Augenhöhe.**

OffCam ist ein klickbarer Prototyp für eine Members-only-Plattform, auf der
Adult-Content-Creator (OnlyFans, Fansly & Co.) einander daten und collaben können.
Die Idee: Wer täglich tausende DMs von Fans bekommt, braucht keinen größeren
Posteingang — sondern einen Raum, in dem alle auf Augenhöhe sind: verifiziert,
diskret, ohne Fans im Feed.

## Was der Prototyp kann

- **Age Gate (18+)** — Altersbestätigung vor dem Einstieg, lokal gespeichert
- **Landing Page** — Positionierung, Features, „In drei Takes drin", Legal-Platzhalter
- **Swipe-Deck** — Karten ziehen oder per Button/Pfeiltasten liken, passen, Collab anfragen
- **Filter** — Alle / Dates / Collabs
- **Match-Flow** — „Match!"-Modal, wenn beide sich liken
- **Chats** — Chatliste mit Unread-Badges, Konversation mit Auto-Replies (Demo)
- **Profil** — Verifizierungs-Status, Sichtbarkeits-Schalter (Dates/Collabs/Alias), Wochen-Stats

Alles läuft komplett im Browser: **kein Backend, keine Dependencies, keine Daten
verlassen das Gerät.** Alle Profile sind fiktiv, Zahlen sind Mock-Daten.

## Starten

Einfach `index.html` im Browser öffnen — oder mit einem statischen Server:

```bash
npx serve .
```

## Struktur

```
index.html      Landing, Age Gate, App-Demo, Match-Modal
css/style.css   Design-System (Token-basiert, dark-only by design)
js/data.js      Fiktive Creator-Profile & Auto-Replies
js/app.js       Gate, Views, Swipe-Deck, Matching, Chats, Profil
```

## Design

- **Konzept:** Der Moment, in dem das Ringlicht ausgeht. Hero ist ein
  „OFF CAM"-Leuchtschild — ein „ON AIR"-Schild, nur umgedreht.
- **Farben:** Warmes Fast-Schwarz `#100D0F`, Tally-Light-Rot `#FF5747`
  (das Aufnahme-Lämpchen), Amber `#FFB86B`, Gold `#F0C37E` für Verified-Badges.
- **Typo:** System-Grotesk (Black-Weight fürs Display), Mono als
  Kamera-OSD-Ebene für Labels, Zahlen und Timestamps.

## Roadmap Richtung v1

1. **Backend & Auth** — Accounts, Sessions, echte Match-Logik
2. **Creator-Verifizierung** — OAuth-Verknüpfung mit der Creator-Plattform + Altersprüfung (KYC)
3. **Sicherheit** — Screenshot-Erkennung, Blur-by-default, Block/Report-Flows
4. **Payments** — Membership-Modell (Creator zahlen keine Reichweite, sondern Zugang)
5. **Apps** — PWA zuerst, dann nativ

## Rechtliches

Nur für Erwachsene (18+). Dieses Projekt ist ein unabhängiger Prototyp und steht
in keiner Verbindung zu OnlyFans (Marke von Fenix International Ltd.) oder Fansly.
Impressum, Datenschutzerklärung und AGB sind im Prototyp als Platzhalter angelegt.
