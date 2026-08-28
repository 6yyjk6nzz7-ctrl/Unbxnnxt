# -*- coding: utf-8 -*-
"""Teil C: Anfangen — erste Sitzung, 4-Wochen-Plan, Prompten."""
from doc import (page, set_section, kicker, fact, callout, prompt, card,
                 resource, wk, toc_row, gloss, opener)


def build_c():
    set_section("Teil 3 — Anfangen")
    page(opener("3", "Anfangen",
        "Ab hier wird es konkret. Keine Theorie mehr, sondern: Was öffnest du, "
        "was tippst du, und was sollte dabei herauskommen.",
        [("Die erste Sitzung", "60 Minuten, wann es passt"),
         ("Kosten und Deutsch", "zwei praktische Fragen"),
         ("Der Wochenplan", "vierzehn Aufgaben aus deinem echten Alltag"),
         ("Gut fragen", "die ersten fünf Prinzipien von Anthropic selbst"),
         ("Vorher / Nachher", "derselbe Auftrag, zwei Ergebnisse")]),
        cls="opener", rh=False, anchor="teil3")

    # ── 3.1 Erste Sitzung, Teil 1 ──
    page("""
<div class="flow">
  <span class="kicker">3.1 — Die erste Sitzung</span>
  <h2>Die ersten 60 Minuten</h2>
  <hr class="hr-thick">

  <p class="lead">Kein Kurs, keine Installation, keine Kreditkarte. Ein Konto,
  ein Browser, eine Stunde — die nicht am Stück sein muss.</p>

  <div class="sp-4"></div>

  <div class="wk no-break">
    <div class="day">Vorab</div>
    <div class="body">
      <h4>Zwei Dinge, bevor du irgendetwas hineinkopierst</h4>
      <span class="mins">10 Min. · einmalig</span>
      <div class="sp-2"></div>
      <p><b>1.</b> In den Einstellungen nachsehen, ob deine Eingaben zur
      Verbesserung der Modelle verwendet werden — und es abschalten.</p>
      <p><b>2.</b> Die Prüfungsordnung deines Fachs öffnen und mit Strg+F
      (bzw. Cmd+F) nach „Hilfsmittel“, „Eigenständigkeit“ und „Künstliche
      Intelligenz“ suchen.</p>
      <p>Zehn Minuten, einmal. Ohne sie weißt du nicht, was in einer benoteten
      Arbeit überhaupt erlaubt ist — und ab dem nächsten Block kommen echte
      Texte ins Chatfenster. Die ausführliche Fassung steht in
      Teil&nbsp;4 ab Seite&nbsp;{{P:teil4}}.</p>
    </div>
  </div>

  <div class="wk no-break">
    <div class="day">0–5 Min.</div>
    <div class="body">
      <h4>Konto anlegen</h4>
      <span class="mins">claude.ai — kostenlose Stufe reicht</span>
      <div class="sp-2"></div>
      <p>Mit E-Mail-Adresse anmelden. Die kostenlose Stufe hat ein Limit — es
      läuft in einem rollierenden Fünf-Stunden-Fenster und zusätzlich in einem
      Wochenfenster. Wenn es dich mitten in der Arbeit stoppt, ist das normal
      und kein Fehler. Die 60&nbsp;Minuten müssen nicht am Stück sein.</p>
      <p>Wenn du lieber ChatGPT oder Gemini nimmst, funktioniert fast alles hier
      genauso — die Prinzipien sind dieselben.</p>
    </div>
  </div>

  <div class="sp-3"></div>
  <div class="callout co-tip no-break">
    <span class="clabel">Was du auf dem Bildschirm siehst</span>
    <p class="small">Unten das <b>Eingabefeld</b> — dort schreibst du hinein.
    Links die Liste deiner <b>Gespräche</b>. Neben dem Eingabefeld eine
    Büroklammer oder ein Plus: darüber lädst du <b>PDFs, Fotos und
    Screenshots</b> hoch — du musst Text also nicht abtippen oder kopieren.
    Unten links dein Konto-Menü, dort liegen die Einstellungen.</p>
    <p class="small">Ein Chat ist ein Gespräch. Neue Aufgabe = neues Gespräch.</p>
  </div>
</div>
""", anchor="ersten60")

    # ── 3.1 Erste Sitzung, Teil 2 ──
    page("""
<div class="flow">
  <div class="sp-2"></div>
  <div class="wk no-break">
    <div class="day">5–15 Min.</div>
    <div class="body">
      <h4>Der Halluzinations-Test</h4>
      <span class="mins">Seite {{P:halluzination}} — zuerst</span>
      <div class="sp-2"></div>
      <p>Erst misstrauisch werden, dann benutzen. Wenn du nur eine Übung aus
      diesem Dokument machst, dann diese.</p>
    </div>
  </div>

  <div class="wk no-break">
    <div class="day">15–35 Min.</div>
    <div class="body">
      <h4>Eine echte Aufgabe aus deinem Alltag</h4>
      <span class="mins">Nicht üben — arbeiten</span>
      <div class="sp-2"></div>
      <p>Nimm etwas, das ohnehin ansteht: eine E-Mail ans Prüfungsamt, ein
      Text, den du nicht verstehst, eine Gliederung, vor der du sitzt. Der
      entscheidende Punkt ist, dass es echt ist. Übungsaufgaben verraten dir
      nicht, ob dir das Werkzeug wirklich hilft.</p>
      <p class="small mut">Vorher kurz Seite&nbsp;{{P:datenschutz}} überfliegen:
      keine Klarnamen Dritter, keine Matrikelnummer, keine Gesundheitsangaben.
      Beschreib die Situation anonymisiert und setz die echten Angaben
      hinterher selbst ein.</p>
    </div>
  </div>

  <div class="wk no-break">
    <div class="day">35–50 Min.</div>
    <div class="body">
      <h4>Dieselbe Aufgabe, besserer Auftrag</h4>
      <span class="mins">Seite {{P:prompten}} — der Unterschied ist größer als erwartet</span>
      <div class="sp-2"></div>
      <p>Formuliere den Auftrag noch einmal nach den fünf Prinzipien. Vergleiche
      die beiden Antworten nebeneinander.</p>
    </div>
  </div>

  <div class="wk no-break">
    <div class="day">50–60 Min.</div>
    <div class="body">
      <h4>Ein Projekt anlegen und auf Deutsch stellen</h4>
      <span class="mins">Einmalig, spart dir danach jedes Mal einen Satz</span>
      <div class="sp-2"></div>
      <p>Lege ein <b>Projekt</b> an (in Claude: „Projects“). Trage als
      Anweisung ein: <i>„Antworte immer auf Deutsch. Wenn du etwas nicht sicher
      weißt, sag es ausdrücklich, statt zu raten.“</i> Anthropic empfiehlt
      ausdrücklich, die Zielsprache explizit zu nennen, statt sie erraten zu
      lassen.</p>
      <p class="small mut">Falls „Projects“ bei dir nicht auftaucht: Speichere
      die Zeilen in einer Notiz auf deinem Rechner und setz sie an den Anfang
      jedes neuen Chats. Wirkung identisch, Aufwand zehn Sekunden.</p>
    </div>
  </div>
</div>
""")

    # ── 3.2 Kosten & Sprache ──
    page("""
<div class="flow">
  <span class="kicker">3.2 — Zwei praktische Fragen</span>
  <h2>Was es kostet<br>und ob Deutsch funktioniert</h2>
  <hr class="hr-thick">
  <div class="sp-3"></div>

  <div class="cols-2">
    <div>
      <h3>Kostet das Geld?</h3>
      <p>Für die vier Wochen in diesem Dokument: <b>nein.</b> Die kostenlosen
      Stufen von Claude, ChatGPT und Gemini reichen für alles, was hier steht.</p>
      <p>Ein Bezahl-Plan wird erst nötig, wenn du <b>Claude Code</b> benutzen
      willst — also das Werkzeug, mit dem Konstantin OffCam baut. Anthropic
      schreibt dazu ausdrücklich: <i>„Claude Code requires a Pro, Max, Team, or
      Enterprise subscription.“</i> (Claude Code setzt ein kostenpflichtiges
      Abonnement voraus.)</p>
      <div class="sp-2"></div>
      <div class="callout co-warn">
        <span class="clabel">Keine Preise in diesem Dokument</span>
        <p class="small">Wir drucken bewusst keine Beträge. Preise ändern sich,
        und eine falsche Zahl, die jemanden zum Bezahlen bewegt, ist ein echter
        Schaden. Steht auf der Seite von Anthropic — dort nachsehen,
        nicht hier.</p>
      </div>
    </div>
    <div>
      <h3>Funktioniert das auf Deutsch?</h3>
      <p>Ja, und es gibt dazu eine veröffentlichte Zahl statt eines
      Werbeversprechens. Anthropic misst für Deutsch <b>97,0&nbsp;%</b> der
      englischen Leistung (Claude Sonnet 4.5 mit erweitertem Denken).</p>
      <div class="sp-3"></div>
      <p class="small"><b>Zwei ehrliche Einschränkungen:</b> Gemessen wurde
      Schlussfolgern in Prüfungsfragen, die professionelle Übersetzer übertragen
      haben — nicht Schreibqualität und nicht Code-Qualität. Und die Zahl stammt
      von einer älteren Modellgeneration; für die aktuellen Modelle ist kein
      deutscher Wert veröffentlicht.</p>
      <p class="small">Praktisch: Unterhaltung auf Deutsch führen. Bei
      technischen Aufträgen rund um Code lohnt sich manchmal Englisch — aber
      das ist Feinschliff, kein Einstiegsproblem.</p>
    </div>
  </div>

  <div class="sp-5"></div>
  <div class="callout co-tip no-break">
    <span class="clabel">Wenn dich das Limit ausbremst</span>
    <p class="small">Die kostenlose Stufe stoppt dich irgendwann mitten in der
    Arbeit. Nutzungsgrenzen laufen bei Claude in rollierenden Fenstern und
    werden zwischen Chat und den anderen Werkzeugen geteilt; bei den anderen
    Anbietern ist es vergleichbar begrenzt. Praktische Konsequenz: Lege die
    anspruchsvolle Aufgabe an den Anfang einer Sitzung, nicht ans Ende.</p>
  </div>
</div>
""", anchor="kosten")

    # ── 3.3 Woche 1 ──
    page("""
<div class="flow">
  <span class="kicker">3.3 — Woche 1</span>
  <h2>Fünfmal zwanzig Minuten</h2>
  <hr class="hr-thick">
  <p class="small mut">Jeden Tag eine Aufgabe aus deinem echten Leben. Nicht
  mehr. Wenn ein Tag ausfällt, fällt er aus — das ist kein Grund aufzuhören.
  Eine Aufgabe = ein Chat.</p>
  <div class="sp-4"></div>
""" +
    wk("Tag 1", "Erklär es mir wie jemandem aus einem anderen Fach", "20 Min.",
       """<p>Nimm das schwierigste Konzept aus deiner aktuellen Vorlesung und
       lass es dir dreimal erklären: einmal ausführlich, einmal in einem Satz,
       einmal mit einer Alltagsanalogie. Frag danach: „Was habe ich an dieser
       Erklärung wahrscheinlich <i>nicht</i> verstanden?“</p>""") +
    wk("Tag 2", "Prüf mich ab", "20 Min.",
       """<p>Nimm <b>deine eigenen Mitschriften</b> oder deine eigene
       Zusammenfassung — nicht das zugangsbeschränkte Skript deiner Dozentin.
       Das ist eine unveröffentlichte Arbeit einer anderen Person und fällt
       unter die Regel auf Seite&nbsp;{{P:datenschutz}}. Lade die Datei hoch
       (Büroklammer neben dem Eingabefeld; ein Foto einer handschriftlichen
       Seite geht auch) und lass dich abfragen: zehn Fragen, einzeln, und erst
       nach deiner Antwort die Auflösung.</p>""") +
    wk("Tag 3", "Der unangenehme Text", "20 Min.",
       """<p>Eine E-Mail, die du vor dir herschiebst. Lass drei Fassungen in
       verschiedenen Tonlagen schreiben (freundlich-knapp, förmlich, bestimmt)
       und nimm dir aus jeder einen Satz. Namen und Matrikelnummern erst
       hinterher selbst einsetzen.</p>""") +
    wk("Tag 4", "Gegenrede", "20 Min.",
       """<p>Der Auftrag, der langfristig am meisten bringt: <i>„Finde die drei
       schwächsten Stellen in dieser Argumentation und formuliere den stärksten
       Einwand dagegen.“</i> Nimm einen eigenen Text. Es ist unangenehm und
       außerordentlich nützlich.</p>""") +
    wk("Tag 5", "Ordnung aus Chaos", "20 Min.",
       """<p>Nimm etwas Unstrukturiertes — Notizen, eine lange Mail, eine
       Literaturliste — und lass eine Tabelle daraus bauen, mit Spalten, die du
       vorgibst. Danach: „Was fehlt in dieser Tabelle, das für meine
       Fragestellung wichtig wäre?“</p>""") +
"""
</div>
""", anchor="woche1")

    # ── 3.3b Bilanz Woche 1 ──
    page("""
<div class="flow">
  <span class="kicker">Am Ende von Woche 1</span>
  <h2>Zwei Zeilen aufschreiben</h2>
  <hr class="hr-thick">

  <p class="lead">Welche der fünf Aufgaben ging <i>tatsächlich</i> schneller
  oder besser als ohne? Und welche war ein Reinfall? Beides notieren — und zwar
  aus einem gut belegten Grund.</p>

  <div class="sp-5"></div>
  <div class="fact no-break">
    <div class="big">19&nbsp;%<small>langsamer mit KI —<br>und merkten es nicht</small></div>
    <div><p>In einer randomisierten Studie des Forschungsinstituts METR
    (Juli 2025) bearbeiteten 16 erfahrene Entwickler 246 echte Aufgaben. Mit
    KI-Werkzeugen brauchten sie <b>19&nbsp;% länger</b> — und glaubten
    hinterher, rund 20&nbsp;% schneller gewesen zu sein.</p>
    <span class="src">METR, randomisierte kontrollierte Studie, Juli 2025</span></div>
  </div>

  <div class="sp-4"></div>
  <p>Die Lehre daraus ist nicht „KI bringt nichts“ — die Teilnehmer arbeiteten
  in Code, den sie seit Jahren kannten, also im ungünstigsten Fall. Die Lehre
  ist: <b>Menschen können erstaunlich schlecht beurteilen, ob KI ihnen geholfen
  hat.</b> Der eigene Eindruck ist kein Messwert. Deshalb aufschreiben statt
  erinnern.</p>

  <div class="sp-5"></div>
  <div class="callout co-tip no-break">
    <span class="clabel">Die häufigste Anfänger-Verwirrung</span>
    <p>„Warum werden die Antworten schlechter, je länger ich schreibe?“ — Das
    liegt fast nie an dir. Ein langes Gespräch schleppt jede vorherige Korrektur
    mit. Anthropic beschreibt das als eigenes Fehlermuster und stellt fest, dass
    <b>eine frische Sitzung mit einem besseren Auftrag fast immer besser
    abschneidet als eine lange Sitzung voller Korrekturen.</b></p>
    <p><b>Praktisch:</b> Wenn es hakt — neues Gespräch aufmachen und den Auftrag
    einmal sauber neu formulieren. Nicht weiter nachbessern.</p>
  </div>
</div>
""")

    # ── 3.4 Wochen 2-4 ──
    page("""
<div class="flow">
  <span class="kicker">3.4 — Wochen 2 bis 4</span>
  <h2>Dreimal dreißig Minuten<br>pro Woche</h2>
  <hr class="hr-thick">
  <div class="sp-3"></div>
""" +
    wk("Woche 2", "Vom Benutzen zum Beurteilen", "3 × 30 Min.",
       """<p><b>Einheit 1:</b> Die fünf Prinzipien von Seite&nbsp;{{P:prompten}}
       auf eine echte Aufgabe anwenden, vorher/nachher vergleichen.<br>
       <b>Einheit 2:</b> Nimm ein Thema, zu dem du eine verlässliche Quelle
       danebenlegen kannst, und klopf eine KI-Antwort Behauptung für Behauptung
       ab. Findest du keine Ungenauigkeit, prüfe Zahlen und Quellenangaben
       einzeln — dort sitzen sie erfahrungsgemäß.<br>
       <b>Einheit 3:</b> Dein Projekt ausbauen: die vollständige Anweisung von
       Seite&nbsp;{{P:anhangB2}} eintragen und den Auftrag von
       Seite&nbsp;{{P:vorhernachher}} als Vorlage hineinlegen.</p>""") +
    wk("Woche 3", "Regeln und Grenzen", "3 × 30 Min.",
       """<p><b>Einheit 1:</b> Teil&nbsp;4 vollständig lesen und deiner Dozentin
       schriftlich die eine Frage stellen, die deine Prüfungsordnung
       offenlässt.<br>
       <b>Einheit 2:</b> Freie Wahl — irgendetwas, das dich wirklich
       interessiert. Ohne Nutzen macht man das nicht lange.<br>
       <b>Einheit 3:</b> Eine Aufgabe wiederholen, die in Woche&nbsp;1 ein
       Reinfall war. Diesmal mit allem, was du seitdem gelernt hast.</p>""") +
    wk("Woche 4", "Mitbauen", "3 × 30 Min.",
       """<p><b>Einheit 1:</b> Lass dich von der KI zu OffCam interviewen
       (Vorlage auf Seite&nbsp;{{P:interview}}). Du brauchst dafür keine Zeile
       Code.<br>
       <b>Einheit 2:</b> Such dir aus Teil&nbsp;5 den Bereich aus, der dich am
       wenigsten langweilt, und arbeite eine halbe Stunde daran. Länger ist ein
       gutes Zeichen, aber nicht Teil der Abmachung.<br>
       <b>Einheit 3:</b> Bilanz ziehen — die Abbruchbedingung von
       Seite&nbsp;{{P:deal}}. Ehrlich, nicht höflich.</p>""") +
"""
  <div class="sp-5"></div>
  <div class="card card-dark no-break">
    <span class="kicker">Was danach kommt</span>
    <p class="small" style="color:#CFC7CB">Erst <i>nach</i> diesen vier Wochen
    lohnt sich ein richtiger Kurs — dann weißt du, was du wissen willst. Die
    Empfehlungen stehen ab Seite&nbsp;{{P:anhangA}}: nimm ein Modul von ein bis
    vier Stunden, nicht den längsten Kurs im Katalog. Kurse, die man nicht
    beendet, hinterlassen ein schlechtes Gewissen und kein Können.</p>
  </div>
</div>
""")

    # ── 3.5 Prompten ──
    page("""
<div class="flow">
  <span class="kicker">3.5 — Die Technik</span>
  <h2>Gut fragen</h2>
  <hr class="hr-thick">

  <p class="lead">Es gibt keine Geheimformeln und keine „Prompt-Vorlagen, die
  Profis nicht teilen wollen“. Es gibt eine Handvoll Prinzipien, und Anthropic
  veröffentlicht sie selbst.</p>

  <div class="sp-5"></div>
  <div class="card card-dark no-break">
    <span class="kicker">Das Grundbild</span>
    <p class="lead" style="color:#F2ECE7;margin-top:1mm">„Stell dir Claude als
    brillante, aber neue Kollegin vor, der der Kontext für eure Abläufe und
    Gepflogenheiten fehlt. Je genauer du erklärst, was du willst, desto besser
    wird das Ergebnis.“</p>
    <p class="small" style="color:#9C949A;margin-top:4mm">Anthropic, Prompting
    best practices — sinngemäß übersetzt</p>
  </div>

  <div class="sp-5"></div>
  <h3>Die ersten fünf Prinzipien, in dieser Reihenfolge</h3>
  <div class="sp-3"></div>
  <ol class="steps">
    <li><b>Klar und direkt sein.</b> Schreib, was du willst, nicht, was du nicht
    willst. „Drei Absätze, sachlicher Ton, für Laien“ schlägt „nicht zu lang und
    nicht zu kompliziert“.</li>
    <li><b>Kontext mitgeben.</b> Wer liest das? Wofür? Was ist die Situation?
    Der häufigste Anfängerfehler ist nicht ein schlechter Auftrag, sondern ein
    Auftrag ohne Hintergrund.</li>
    <li><b>Beispiele zeigen.</b> Anthropic empfiehlt drei bis fünf. Ein Beispiel
    für den gewünschten Stil ersetzt drei Absätze Beschreibung.</li>
    <li><b>Struktur geben.</b> Trenne Anweisung und Material sichtbar
    voneinander — mit Überschriften, Bindestrichen oder Klammern. Bei langen
    Texten ist das der Unterschied zwischen brauchbar und Chaos.</li>
    <li><b>Eine Rolle zuweisen.</b> „Du bist Lektorin für wissenschaftliche
    Texte.“ Anthropic dazu: <i>„Even a single sentence makes a difference.“</i>
    (Schon ein einziger Satz macht einen Unterschied.)</li>
  </ol>

  <div class="sp-5"></div>
  <div class="callout co-tip no-break">
    <span class="clabel">Die goldene Regel</span>
    <p>Anthropics eigener Prüfstein: <b>„Zeig deinen Auftrag einer Kollegin, die
    kaum Kontext zur Aufgabe hat, und bitte sie, ihn zu befolgen. Wäre sie
    verwirrt, wäre Claude es auch.“</b> Das ist der beste Test, den es gibt, und
    man braucht dafür keine Technik.</p>
  </div>
</div>
""", anchor="prompten")

    # ── 3.6 Vorher / Nachher ──
    page("""
<div class="flow">
  <span class="kicker">3.6 — Derselbe Auftrag, zweimal</span>
  <h2>Vorher / Nachher</h2>
  <hr class="hr-thick">
  <p class="small mut">Aufgabe: eine Zusammenfassung für ein Seminar.</p>
  <div class="sp-4"></div>
""" +
    prompt("Vorher", "Fasse den Text bitte zusammen.") +
"""
  <div class="sp-2"></div>
  <p class="small mut">Ergebnis: irgendeine Länge, irgendein Ton, irgendeine
  Auswahl. In dem Auftrag steht nichts, woran sich die KI halten könnte.</p>

  <div class="sp-4"></div>
""" +
    prompt("Nachher — dieselbe Aufgabe, fünf Prinzipien angewendet",
           "<span class=\"c\">&lt;Rolle&gt;</span>\n"
           "Du bist Tutorin in einem sozialwissenschaftlichen Seminar.\n\n"
           "<span class=\"c\">&lt;Kontext&gt;</span>\n"
           "Ich halte nächste Woche ein Referat vor 25 Studierenden im\n"
           "zweiten Semester. Die meisten haben den Text nicht gelesen.\n\n"
           "<span class=\"c\">&lt;Aufgabe&gt;</span>\n"
           "Fasse den Text unten zusammen:\n"
           "- 200 Wörter, drei Absätze\n"
           "- Absatz 1: die These. Absatz 2: die Belege.\n"
           "  Absatz 3: die stärkste Gegenposition\n"
           "- keine Fachbegriffe ohne kurze Erklärung in Klammern\n"
           "- am Ende drei Fragen, die im Seminar Diskussion auslösen\n\n"
           "<span class=\"c\">&lt;Wichtig&gt;</span>\n"
           "Verwende ausschließlich Aussagen aus dem Text. Wenn etwas\n"
           "unklar bleibt, schreib das dazu, statt es zu ergänzen.\n\n"
           "<span class=\"c\">&lt;Text&gt;</span>\n"
           "[hier den Text einfügen]") +
"""
  <div class="sp-3"></div>
  <p class="small">Die spitzen Klammern sind kein Code und keine Zauberformel —
  sie sind sichtbare Überschriften, damit die KI Anweisung und Material nicht
  verwechselt. „Rolle:“ in einer eigenen Zeile tut genau dasselbe. Nimm, was
  sich für dich richtiger anfühlt.</p>

  <div class="sp-4"></div>
  <div class="cols-2u">
    <div class="card card-green">
      <h4>Was der zweite Auftrag anders macht</h4>
      <p class="small">Rolle, Publikum, Länge, Struktur, Sprachniveau,
      Zusatznutzen — und eine ausdrückliche Grenze gegen Erfindungen. Kein
      Trick, sondern schlicht ein vollständiger Auftrag.</p>
    </div>
    <div class="card card-gold">
      <h4>Der Aufwand relativiert sich</h4>
      <p class="small">Diesen Auftrag schreibst du einmal und legst ihn in dein
      Projekt. Ab dann tauschst du nur noch den Text aus. Deshalb lohnt sich die
      Sorgfalt beim ersten Mal.</p>
    </div>
  </div>
</div>
""", anchor="vorhernachher")
