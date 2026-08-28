# -*- coding: utf-8 -*-
"""Teil D: Regeln (Studium, Datenschutz) + Zusammen bauen (Claude Code, OffCam)."""
from doc import (page, set_section, kicker, fact, callout, prompt, card,
                 resource, wk, toc_row, gloss, opener)


def build_d():
    # ══════════════════ OPENER TEIL 4 ══════════════════
    set_section("Teil 4 — Regeln")
    page(opener("4", "Regeln",
        "Zwei Kapitel, die man überspringt, bis es zu spät ist. "
        "Bitte lies sie vorher.",
        [("KI im Studium", "was erlaubt ist und was ein Täuschungsversuch"),
         ("Datenschutz", "was nie in ein Chatfenster gehört")]),
        cls="opener", rh=False, anchor="teil4")

    # ── 4.1 KI im Studium ──
    page("""
<div class="flow">
  <span class="kicker">4.1 — Das wichtigste Kapitel für eine Studentin</span>
  <h2>KI im Studium:<br>Was erlaubt ist</h2>
  <hr class="hr-thick">

  <div class="callout co-warn no-break">
    <span class="clabel">Vorweg, weil es ernst ist</span>
    <p>Ein Täuschungsversuch kann eine Prüfung ungültig machen, im
    Wiederholungsfall den Prüfungsanspruch kosten und in schweren Fällen zur
    Exmatrikulation führen. Wenn dieses Dokument dich ermutigt, KI im Studium zu
    nutzen, und du fliegst deshalb aus einer Prüfung, wäre das unser Fehler.
    Deshalb steht die Kurzfassung schon auf Seite&nbsp;{{P:ersten60}}, bevor du
    zum ersten Mal etwas hineinkopierst — und hier die vollständige.</p>
  </div>

  <div class="sp-5"></div>
  <div class="cols-2u">
    <div class="card card-green">
      <h4>In aller Regel unbedenklich</h4>
      <ul class="clean" style="margin-top:2mm">
        <li class="small">Dir Konzepte erklären lassen</li>
        <li class="small">Dich abfragen lassen</li>
        <li class="small">Eine Gliederung diskutieren</li>
        <li class="small">Gegenargumente zu deiner These suchen</li>
        <li class="small">Verständnisfragen zu einem Text stellen</li>
        <li class="small">Deine eigenen Formulierungen überarbeiten lassen</li>
        <li class="small">Literaturhinweise als <i>Startpunkt</i>, jeder einzeln
        nachgeprüft</li>
      </ul>
    </div>
    <div class="card card-red">
      <h4>Gefährlich bis verboten</h4>
      <ul class="clean" style="margin-top:2mm">
        <li class="small">Generierten Text als eigenen abgeben</li>
        <li class="small">Quellenangaben übernehmen, ohne sie zu öffnen</li>
        <li class="small">KI-Nutzung verschweigen, wo sie zu deklarieren ist</li>
        <li class="small">In Klausuren und geschlossenen Prüfungen</li>
        <li class="small">Wenn deine Prüfungsordnung es untersagt — unabhängig
        davon, wie sinnvoll du das findest</li>
      </ul>
    </div>
  </div>

  <div class="sp-3"></div>
  <p class="small"><b>Achtung:</b> „Unbedenklich“ heißt nur, dass es in der
  Regel keine Täuschung ist — nicht, dass du es verschweigen darfst. Viele
  Eigenständigkeitserklärungen verlangen, jede KI-Nutzung anzugeben, auch die
  aus der linken Spalte. Was zu deklarieren ist, steht in deiner
  Prüfungsordnung.</p>

</div>
""", anchor="studiumregeln")

    page("""
<div class="flow">
  <div class="sp-2"></div>
  <h3>Was du diese Woche tun solltest</h3>
  <ol class="steps">
    <li><b>Prüfungsordnung durchsuchen</b> nach „Hilfsmittel“,
    „Eigenständigkeit“ und „Künstliche Intelligenz“. Die Regelungen
    unterscheiden sich zwischen Hochschulen und Fakultäten erheblich.</li>
    <li><b>Die Handreichung deines Instituts suchen.</b> Fast alle Hochschulen
    haben inzwischen eine; sie ist konkreter als die Prüfungsordnung.</li>
    <li><b>Im Zweifel die Dozentin fragen — vorher und schriftlich.</b> Eine
    Nachfrage vorher ist nie ein Problem; eine Erklärung hinterher schon.</li>
  </ol>

  <div class="sp-4"></div>
  <div class="callout co-honest no-break">
    <span class="clabel">Der Lernvorbehalt</span>
    <p class="small">Unabhängig von jeder Regel: Wer sich Texte schreiben
    lässt, die er selbst nicht schreiben könnte, merkt es in der Klausur. Das
    ist dieselbe Regel wie auf Seite&nbsp;{{P:koennennicht}}: Beurteilen kann
    nur, wer das Thema kennt. KI ersetzt kein Verstehen; sie beschleunigt
    vorhandenes.</p>
  </div>

  <div class="sp-5"></div>
  <div class="callout co-tip no-break">
    <span class="clabel">Wie man eine KI-Nutzung angibt</span>
    <p>Falls deine Prüfungsordnung eine Angabe verlangt und kein Muster
    vorgibt, reicht in der Regel ein kurzer, konkreter Absatz: <b>welches
    Werkzeug, wofür, in welchem Umfang.</b> Zum Beispiel: „Für die Gliederung
    und zur sprachlichen Überarbeitung einzelner Absätze wurde [Werkzeug]
    genutzt. Alle Inhalte, Quellen und Argumente stammen von mir und wurden
    eigenständig geprüft.“</p>
    <p class="small">Vage Formulierungen sind schlechter als gar keine — sie
    wirken, als solle etwas verborgen werden. Konkret ist immer besser.</p>
  </div>

  <div class="sp-5"></div>
  <div class="card card-dark no-break">
    <span class="kicker">Die kürzeste Fassung</span>
    <p class="small" style="color:#CFC7CB">Erklären lassen, abfragen lassen,
    gliedern, kritisieren lassen: fast immer in Ordnung. Generierten Text
    abgeben oder Quellenangaben übernehmen, ohne sie geöffnet zu haben: fast
    immer ein Problem. Und dazwischen entscheidet nicht dein Gefühl, sondern
    deine Prüfungsordnung.</p>
  </div>
</div>
""")

    # ── 4.2 Datenschutz ──
    page("""
<div class="flow">
  <span class="kicker">4.2 — Datenschutz</span>
  <h2>Was nie in ein Chatfenster gehört</h2>
  <hr class="hr-thick">

  <p class="lead">Alles, was du eintippst, verlässt deinen Rechner. Das ist
  keine Panikmache, sondern schlicht die Funktionsweise — und daraus folgen ein
  paar Regeln, die man einmal lernt und dann nie wieder überdenken muss.</p>

  <div class="sp-5"></div>
  <div class="cols-2u">
    <div class="card card-red">
      <h4>Nicht hineinkopieren</h4>
      <ul class="clean" style="margin-top:2mm">
        <li class="small">Klarnamen und Kontaktdaten Dritter</li>
        <li class="small">Gesundheitsdaten, auch eigene</li>
        <li class="small">Alles, was unter eine Schweigepflicht fällt —
        Praktikum, Nebenjob, Pflege, Beratung</li>
        <li class="small">Unveröffentlichte Arbeiten anderer</li>
        <li class="small">Zugangsdaten und Schlüssel, unter keinen Umständen</li>
        <li class="small">Interne Unterlagen eines Arbeitgebers ohne
        ausdrückliche Erlaubnis</li>
      </ul>
    </div>
    <div class="card card-green">
      <h4>Was hilft</h4>
      <ul class="clean" style="margin-top:2mm">
        <li class="small"><b>Anonymisieren.</b> „Frau M., 34, aus einer
        mittelgroßen Stadt“ statt echter Angaben. Für die Aufgabe reicht das
        fast immer.</li>
        <li class="small"><b>Training abschalten.</b> In den Einstellungen
        nachsehen, ob deine Eingaben zur Verbesserung der Modelle verwendet
        werden — und es abwählen.</li>
        <li class="small"><b>Bei beruflicher Nutzung zuerst fragen,</b> ob es
        eine Regelung gibt. Es gibt fast immer eine.</li>
      </ul>
    </div>
  </div>

  <div class="sp-6"></div>
  <div class="card card-dark no-break">
    <span class="kicker">Die Faustregel</span>
    <p class="lead" style="color:#F2ECE7;margin-top:2mm">Wenn du es nicht auf
    eine Postkarte schreiben würdest, schreib es nicht in ein Chatfenster.</p>
  </div>

  <div class="sp-5"></div>
  <div class="callout co-honest no-break">
    <span class="clabel">Warum das gerade jetzt jemand können muss</span>
    <p>Nach der TÜV-Weiterbildungsstudie 2026 (repräsentative Forsa-Befragung
    von 500 Unternehmen ab 20 Beschäftigten) nutzen 56&nbsp;% der Unternehmen
    generative KI im Arbeitsalltag — aber nur 27&nbsp;% haben ihre Beschäftigten
    dafür geschult. Bei kleinen Unternehmen sind es 21&nbsp;%. Die Lücke
    zwischen „wird eingesetzt“ und „jemand weiß, was er tut“ ist derzeit die
    ehrlichste Antwort auf die Frage, warum sich das lohnt.</p>
    <p class="small mut">Einordnung: Der TÜV-Verband betreibt selbst
    Weiterbildungsakademien und hat ein Interesse an der Botschaft „zu wenig
    Schulung“.</p>
  </div>
</div>
""", anchor="datenschutz")

    # ══════════════════ OPENER TEIL 5 ══════════════════
    set_section("Teil 5 — Zusammen bauen")
    page(opener("5", "Zusammen bauen",
        "Der Teil, für den Konstantin dieses Dokument bestellt hat. "
        "Hier steht, was du wirklich beitragen könntest — und was ihr "
        "vorher miteinander klären solltet.",
        [("Claude Code", "ohne Terminal, mit Rückgängig-Knopf"),
         ("Das Interview", "die Vorlage, die alles verändert"),
         ("Fünf Beiträge zu OffCam", "ohne eine Zeile Code"),
         ("Jugendschutz und Zahlungen", "der Bereich, der wirklich brennt"),
         ("KI-Code prüfen", "Artikel 9 und das Grindr-Bußgeld"),
         ("Euer Arbeitsprotokoll", "damit es nicht im Streit endet")]),
        cls="opener", rh=False, anchor="teil5")

    # ── 5.1 Claude Code ──
    page("""
<div class="flow">
  <span class="kicker">5.1 — Das Werkzeug, mit dem Konstantin baut</span>
  <h2>Claude Code, ohne Terminal</h2>
  <hr class="hr-thick">

  <p class="lead">Die gute Nachricht zuerst: Es gibt eine Desktop-App mit
  normalen Fenstern und Knöpfen. Anthropics eigene Formulierung lautet
  <i>„No terminal required.“</i> (kein Terminal nötig)</p>

  <div class="sp-4"></div>
  <p>Die App hat drei Reiter — Chat, Cowork und Code — und Installationsprogramme
  für macOS, Windows und Ubuntu/Debian. Node.js oder eine Kommandozeile brauchst
  du ausdrücklich nicht.</p>

  <div class="sp-4"></div>
  <div class="stack">
    <div class="callout co-warn no-break">
      <span class="clabel">Drei Dinge, die in der Werbung nicht stehen</span>
      <p><b>1. Es kostet.</b> Claude Code gibt es nicht in der kostenlosen Stufe.
      Anthropic: <i>„Claude Code requires a Pro, Max, Team, or Enterprise
      subscription.“</i></p>
      <p><b>2. Auf Windows muss Git separat installiert sein,</b> sonst startet
      der Code-Reiter nicht. Das steht in keinem Werbetext und kostet sonst
      einen frustrierenden Abend.</p>
      <p><b>3. Der Sicherheitsmodus ist nicht voreingestellt.</b> Siehe unten —
      das ist der wichtigste Absatz auf dieser Seite.</p>
    </div>
    <div class="callout co-tip no-break">
      <span class="clabel">Stell als Erstes „Manual“ ein</span>
      <p>Im manuellen Modus schlägt Claude jede Änderung vor und wartet auf deine
      Freigabe. Anthropic: <i>„Your files aren't modified until you accept.“</i> — deine Dateien werden erst geändert, wenn du zustimmst.</p>
      <p><b>Aber:</b> In den Pro-, Max- und Team-Plänen ist der Startmodus
      <i>Auto</i>, in dem ein Klassifikator an deiner Stelle zustimmt. Du musst
      „Manual“ aktiv auswählen — im Modus-Auswahlfeld neben dem Senden-Knopf
      (Cmd/Strg+Shift+M). Mach das in der ersten Sitzung, bevor du irgendetwas
      anderes tust.</p>
    </div>
  </div>

  <div class="sp-4"></div>
  <div class="callout co-honest no-break">
    <span class="clabel">Kann ich etwas kaputt machen?</span>
    <p class="small">Fast alles lässt sich rückgängig machen: Esc, der Befehl
    <b>/rewind</b>, oder schlicht „Mach das rückgängig“. Anthropic warnt aber
    ausdrücklich, dass diese Wiederherstellungspunkte nur Änderungen erfassen,
    die Claude über seine Datei-Werkzeuge vorgenommen hat — nicht solche über
    Kommandozeilenbefehle oder externe Programme — und <i>„This isn't a
    replacement for git.“</i> (das ersetzt kein Git) Praktisch: Von allem, was ihr nicht verlieren
    dürft, gehört eine Kopie woanders hin. Das gilt für OffCam ohnehin.</p>
  </div>
</div>
""", anchor="claudecode")

    # ── 5.2 Das Interview ──
    page("""
<div class="flow">
  <span class="kicker">5.2 — Der größte Hebel für dich</span>
  <h2>Lass dich interviewen</h2>
  <hr class="hr-thick">

  <p class="lead">Der wertvollste Beitrag einer Nicht-Programmiererin zu einem
  Softwareprojekt ist fast nie Code. Er ist eine präzise Antwort auf die Frage,
  was das Ding eigentlich können soll — und genau dafür gibt es eine Vorlage von
  Anthropic.</p>

  <div class="sp-5"></div>
""" +
    prompt("Anthropics eigene Vorlage — für größere Funktionen",
           "Ich möchte [Funktion] bauen.\n\n"
           "Bevor du mit der Umsetzung beginnst, stelle mir Fragen zu allem,\n"
           "was unklar ist: Anforderungen, Grenzfälle, gewünschtes Verhalten.\n"
           "Stelle die Fragen einzeln nacheinander.\n\n"
           "Schreibe danach eine Spezifikation, die ich prüfen kann,\n"
           "bevor du irgendetwas umsetzt.") +
"""
  <div class="sp-5"></div>
  <h3>Warum das ausgerechnet deine Stärke ist</h3>
  <p>Konstantin kennt den Code. Deshalb beantwortet er diese Fragen schnell,
  aus der Perspektive dessen, der weiß, wie es gebaut ist. Du kennst ihn nicht —
  und beantwortest sie deshalb aus der Perspektive dessen, der die App später
  benutzt. Das ist bei einem Produkt wie OffCam nicht die schwächere, sondern
  die wertvollere Perspektive.</p>

  <p>Die Fragen, an denen ein Interview meistens hängen bleibt, sind ohnehin
  keine technischen: Was passiert, wenn jemand gemeldet wird? Was sieht die
  gemeldete Person? Wer entscheidet, und in welcher Frist? Was, wenn beide sich
  gegenseitig melden? Für keine dieser Fragen braucht man Programmierkenntnisse.
  Man braucht Urteilsvermögen — und die Bereitschaft, unbequeme Fälle zu Ende zu
  denken.</p>

  <div class="sp-5"></div>
  <div class="card card-dark no-break">
    <span class="kicker">Der Arbeitsablauf, den Anthropic empfiehlt</span>
    <p class="lead" style="color:#F2ECE7;margin-top:1mm;font-size:13pt">
    Erkunden&nbsp;→ Planen&nbsp;→ Umsetzen&nbsp;→ Festschreiben</p>
    <p class="small" style="color:#B5ACB1;margin-top:3mm">Die meisten Anfänger
    springen direkt zu „Umsetzen“ und wundern sich. Anthropic nennt in seinen
    Best Practices fünf typische Fehlermuster; das lehrreichste heißt
    <i>„Correcting over and over“</i> — mit der Erkenntnis, dass eine <b>frische
    Sitzung mit einem besseren Prompt fast immer besser abschneidet als eine
    lange Sitzung voller Korrekturen.</b> Wenn es hakt: neu anfangen, nicht
    weiter nachbessern.</p>
  </div>
</div>
""", anchor="interview")
