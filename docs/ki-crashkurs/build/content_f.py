# -*- coding: utf-8 -*-
"""Teil F: Geld, Prüf mich nach, Ressourcen, Anhänge."""
from doc import (page, set_section, kicker, fact, callout, prompt, card,
                 resource, wk, toc_row, gloss, opener)


def build_f():
    # ══════════════════ OPENER TEIL 6 ══════════════════
    set_section("Teil 6 — Geld, ehrlich")
    page(opener("6", "Geld, ehrlich",
        "Der Teil des ursprünglichen Auftrags, der am wenigsten standhält. "
        "Hier sind die Zahlen, die in keinem Werbevideo vorkommen.",
        [("Die Verteilung", "warum der Durchschnitt lügt"),
         ("Grundausstattung", "warum „ich kann KI“ nicht reicht"),
         ("Die Betrugsmasche", "was die US-Handelsaufsicht gefunden hat"),
         ("Der realistische Weg", "eine Leiter, kein Sprung")]),
        cls="opener", rh=False, anchor="teil6")

    # ── 6.1 Die Zahlen ──
    page("""
<div class="flow">
  <span class="kicker">6.1 — Die unbequemen Zahlen</span>
  <h2>Was Menschen mit digitalen<br>Produkten wirklich verdienen</h2>
  <hr class="hr-thick">

  <div class="fact no-break">
    <div class="big">72&nbsp;$<small>Median pro Monat<br>auf Gumroad</small></div>
    <div><p>Auswertung von 146.271 Produkten auf der Verkaufsplattform Gumroad
    (Januar bis April 2026): Der mittlere Verkäufer verdient 72&nbsp;Dollar im
    Monat. <b>44&nbsp;% aller Produkte machen exakt null.</b> Rund 5&nbsp;%
    kommen über 1.000&nbsp;Dollar monatlich, und das oberste Prozent
    vereinnahmt 99,5&nbsp;% des gesamten Plattformumsatzes.</p>
    <span class="src">InsightRaider, State of Gumroad 2026</span></div>
  </div>

  <div class="sp-4"></div>
  <div class="fact no-break">
    <div class="big">38,1&nbsp;%<small>der Gründungen leben<br>nach fünf Jahren noch</small></div>
    <div><p>Amtliche Zahlen des IfM Bonn auf Basis des Statistischen
    Bundesamts, Gründungsjahrgang 2017: Nach einem Jahr waren noch 74,0&nbsp;%
    am Markt, nach fünf Jahren 38,1&nbsp;%. Entscheidend ist die Größe beim
    Start: von den Gründungen <b>ohne</b> Beschäftigte existierte nach fünf
    Jahren nur noch rund ein Drittel (33,7&nbsp;%), von denen <b>mit</b>
    Beschäftigten knapp die Hälfte (49,5&nbsp;%).</p>
    <span class="src">IfM Bonn · Das IfM merkt selbst an, dass sehr kleine
    Unternehmen aus dem Register fallen und dann als „geschlossen“ zählen,
    obwohl sie noch laufen</span></div>
  </div>

  <div class="sp-4"></div>
  <div class="callout co-honest no-break">
    <span class="clabel">Und eine Zahl, die zeigt, wie man Zahlen prüft</span>
    <p>Überall im Netz steht: „Über 54&nbsp;% der Produkte auf Indie Hackers
    machen keinen Umsatz, nur 5&nbsp;% kommen über 100.000&nbsp;$ im Jahr.“ Die
    Zahl stimmt — sie stammt aus einer Auswertung von 937&nbsp;Produkten vom
    <b>16.&nbsp;Juli 2022</b> und wird seither jedes Jahr als aktuell zitiert.</p>
    <p>Genau so entstehen Fakten im KI-Geld-Umfeld. <b>Immer das Datum prüfen.</b>
    Auch bei diesem Dokument.</p>
  </div>

  <div class="sp-4"></div>
  <p>Für den deutschen Freelancer-Markt sieht es ähnlich uneindeutig aus: Der
  durchschnittliche monatliche Projektumsatz fiel 2026 um 17,1&nbsp;% von
  8.022&nbsp;€ auf 6.653&nbsp;€ — der stärkste Rückgang seit Beginn der
  Erhebung. Der Stundensatz blieb fast unverändert bei 103&nbsp;€. Es fehlten
  also nicht die Preise, sondern die abrechenbaren Projektstunden.</p>
  <p class="small mut"><b>Wichtig:</b> Das ist der ungewichtete Mittelwert
  aller Befragten, und es ist Umsatz <b>vor</b> Steuern und Sozialabgaben —
  nicht das, was übrig bleibt. Dazu kommen im Schnitt 783&nbsp;€
  Betriebsausgaben im Monat.</p>
</div>
""", anchor="geldzahlen")

    # ── 6.2 KI als Verkaufsargument ──
    page("""
<div class="flow">
  <span class="kicker">6.2 — Warum „Ich kann KI“ nicht reicht</span>
  <h2>Das Werkzeug ist<br>Grundausstattung</h2>
  <hr class="hr-thick">

  <div class="cols-2u">
    <div class="card card-tint">
      <h4>85 %</h4>
      <p class="small">der deutschen Freelancer nutzen laut
      Freelancer-Kompass 2026 (freelancermap) bereits KI-Werkzeuge im
      Arbeitsalltag. Nach der Freelancer-Studie 2026 von freelance.de setzen
      53&nbsp;% sie täglich ein, weitere 23&nbsp;% wöchentlich.</p>
    </div>
    <div class="card card-tint">
      <h4>&minus;13 %</h4>
      <p class="small">Verdienst pro Auftrag bei generativer KI und kreativer
      Produktion auf Upwork — bei gleichzeitig <b>90&nbsp;% mehr</b>
      Aufträgen. Mehr Arbeit, weniger Geld pro Stück.</p>
    </div>
  </div>

  <div class="sp-5"></div>
  <p>„Ich benutze KI“ ist also kein Verkaufsargument mehr, sondern die
  Erwartung. Interessanter ist, was in denselben Daten <b>gestiegen</b> ist:
  Upwork berichtet für komplexere KI-Arbeit ein Plus von 45&nbsp;%, und für
  „KI-gestützte Fachdienstleistungen“ — also Fachleute, die KI in ihr
  bestehendes Fachgebiet integrieren — ein Volumenwachstum von 72&nbsp;% bei
  22&nbsp;% höheren Einkünften.</p>

  <div class="sp-4"></div>
  <div class="card card-dark no-break">
    <span class="kicker">Der Satz, der aus allen Geld-Daten übrig bleibt</span>
    <p class="lead" style="color:#F2ECE7;margin-top:2mm">Einfache KI-Ausführung
    wird zur Massenware. <span class="red">KI plus Urteilsvermögen</span>
    nicht.</p>
    <p class="small" style="color:#B5ACB1;margin-top:4mm">Und Urteilsvermögen
    in einem Fachgebiet erwirbt man — das ist der unbequeme Teil — durch das
    Studium dieses Fachgebiets. Womit wir wieder bei Seite&nbsp;{{P:studium}} wären.</p>
  </div>

  <div class="sp-5"></div>
  <div class="callout co-warn no-break">
    <span class="clabel">Und die Branche, auf die es OffCam abgesehen hat</span>
    <p class="small">Auf Erwachsenen-Creator-Plattformen folgen die Einnahmen
    einer extremen Potenzverteilung: Eine kleine Minderheit der Konten
    vereinnahmt den größten Teil des Geldes, während der typische Creator sehr
    wenig verdient. Die konkreten Prozentzahlen, die dazu kursieren, ließen sich
    <b>nicht</b> auf eine belastbare Primärquelle zurückführen — wir drucken sie
    deshalb nicht. Für OffCams Geschäftsmodell ist die Form der Verteilung
    ohnehin wichtiger als die genaue Zahl: Wenn Mitglieder für Zugang zahlen
    sollen, können die meisten von ihnen wenig zahlen.</p>
  </div>
</div>
""")

    # ── 6.3 Die Betrugsmasche ──
    page("""
<div class="flow">
  <span class="kicker">6.3 — Was passiert, wenn du „KI Nebeneinkommen“ suchst</span>
  <h2>Operation AI Comply</h2>
  <hr class="hr-thick">

  <p class="lead">In dem Moment, in dem du anfängst, nach Geldverdienen mit KI
  zu suchen, findet dich eine ganze Industrie. Es hilft, vorher zu wissen, wie
  sie arbeitet.</p>

  <div class="sp-4"></div>
  <p>Am 25.&nbsp;September 2024 ging die US-Handelsaufsicht FTC unter dem Namen
  „Operation AI Comply“ gleichzeitig gegen fünf Anbieter vor. Vier davon, aus
  den Klageschriften:</p>

  <div class="sp-3"></div>
  <table>
    <tr><th>Anbieter</th><th>Vorwurf laut FTC</th></tr>
    <tr><td><b>Ascend Ecom</b></td><td>soll Verbraucher um mindestens
        25&nbsp;Mio.&nbsp;$ gebracht haben</td></tr>
    <tr><td><b>Passive Scaling / FBA Machine</b></td><td>soll Verbraucher mehr
        als 15,9&nbsp;Mio.&nbsp;$ gekostet haben</td></tr>
    <tr><td><b>Ecommerce Empire Builders</b></td><td>verlangte bis zu
        35.000&nbsp;$ für einen „fertigen“ Shop und warb mit
        10.000&nbsp;$ Monatsverdienst — laut FTC ohne jeden Beleg</td></tr>
    <tr><td><b>DoNotPay</b></td><td>beworben als „erster Roboter-Anwalt der
        Welt“; zahlte zur Beilegung 193.000&nbsp;$</td></tr>
  </table>

  <div class="sp-5"></div>
  <div class="card card-dark no-break">
    <span class="kicker">Der Satz, den man sich merken sollte</span>
    <p class="lead" style="color:#F2ECE7;margin-top:2mm;font-style:italic;font-size:12.5pt">
    „Für fast alle Verbraucher treten die versprochenen Gewinne nie ein, und die
    Verbraucher bleiben mit geleerten Bankkonten und hohen Kreditkartenschulden
    zurück.“</p>
    <p class="small" style="color:#9C949A;margin-top:4mm">FTC über Ascend Ecom,
    September 2024 — sinngemäß übersetzt</p>
  </div>

  <div class="sp-5"></div>
  <div class="callout co-tip no-break">
    <span class="clabel">Der Filter, der fast immer funktioniert</span>
    <p>Wer dir <b>ein Einkommen</b> verkauft, verkauft dir etwas. Wer dir eine
    <b>Fähigkeit</b> beibringt, sagt dir dazu, wie lange es dauert und wie
    unsicher der Ertrag ist. Der Unterschied ist auf der Verkaufsseite meistens
    in zehn Sekunden erkennbar: Kommen zuerst Zahlen und Autos, oder kommt
    zuerst ein Lehrplan?</p>
  </div>
</div>
""")

    # ── 6.4 Die Leiter ──
    page("""
<div class="flow">
  <span class="kicker">6.4 — Der realistische Weg</span>
  <h2>Eine Leiter, kein Sprung</h2>
  <hr class="hr-thick">

  <p class="lead">Falls überhaupt jemals Geld dabei herauskommen soll, dann so —
  und nicht durch ein Produkt, das sich nachts von allein verkauft.</p>

  <div class="sp-5"></div>
  <ol class="steps">
    <li><b>Unbezahlt, für dich selbst.</b> Vier Wochen. Ziel ist nicht Umsatz,
    sondern dass du beurteilen kannst, was gut ist. Ohne diese Stufe verkaufst
    du etwas, dessen Qualität du nicht einschätzen kannst.</li>

    <li><b>Einmal für jemanden, den du kennst.</b> Eine Kommilitonin, ein
    kleiner Betrieb, der Verein deiner Eltern. Auch unbezahlt oder gegen
    Kuchen. Hier lernst du das eigentlich Schwierige: dass niemand weiß, was er
    will, bis er etwas Falsches gesehen hat.</li>

    <li><b>HiWi, Tutorium oder Werkstudentenstelle.</b> <b>Der am meisten
    unterschätzte Weg für eine Studentin.</b> An deiner eigenen Hochschule
    oder in einem lokalen Betrieb. Bezahlt, sozialversichert, ohne
    Gewerbeanmeldung, ohne Steuerberater, ohne Risiko — und es zählt als
    Berufserfahrung, also genau als das „implizite Wissen“, das nach der
    Stanford-Auswertung gerade wertvoller wird.</li>

    <li><b>Erst danach: freiberuflich.</b> Und auch dann über das eigene Netz.</li>
  </ol>

  <div class="sp-5"></div>
  <div class="fact no-break">
    <div class="big">55&nbsp;%<small>der Aufträge kommen<br>übers eigene Netzwerk</small></div>
    <div><p>Der belastbarste Praxisbefund im gesamten Datensatz. Der erste
    bezahlte Auftrag kommt fast sicher von jemandem, der dich bereits kennt —
    und praktisch nie von einem Marktplatz, auf dem du mit tausenden anonymen
    Anbietern über den Preis konkurrierst. freelancermaps eigene Empfehlung für
    einen schwachen Markt lautet folgerichtig nicht „mehr Kanäle“, sondern die
    vorhandenen konsequenter nutzen.</p>
    <span class="src">Freelancer-Kompass 2026, freelancermap</span></div>
  </div>

  <div class="sp-4"></div>
  <p class="small mut">Was rechtlich zu beachten ist, wenn es je so weit
  kommt — Kleinunternehmerregelung, Krankenversicherung, BAföG — steht bewusst
  im Anhang ab Seite&nbsp;{{P:anhangC}}. Nicht weil es unwichtig wäre, sondern weil es an
  dieser Stelle wie eine Erwartung wirken würde.</p>
</div>
""", anchor="leiter")

    # ── PRÜF MICH NACH ──
    set_section("Prüf mich nach")
    page("""
<div class="flow">
  <span class="kicker">Die letzte Übung</span>
  <h2>Prüf mich nach</h2>
  <hr class="hr-thick">

  <p class="lead">Du hast dieses Dokument vermutlich mit einer gewissen Skepsis
  aufgeschlagen. Das war angemessen. Hier ist die Gelegenheit, diese Skepsis
  produktiv zu machen — und nebenbei genau die Fähigkeit zu üben, um die es in diesem
  Dokument ging.</p>

  <div class="sp-5"></div>
  <p><b>Drei Behauptungen aus diesem Dokument. Prüf sie selbst nach.</b>
  Die QR-Codes auf den nächsten Seiten führen zu den Quellen.</p>

  <div class="sp-4"></div>
  <div class="stack">
    <div class="card">
      <h4>1 &nbsp;„Die Arbeitslosenquote lag 2025 bei 3,3 % für Akademiker und 21,3 % ohne Berufsabschluss.“</h4>
      <p class="small">Steht auf Seite&nbsp;{{P:studium}}. Quelle: Statistisches Landesamt
      Baden-Württemberg auf Basis der Bundesagentur für Arbeit. <b>Frage an dich:</b>
      Beziehen sich beide Zahlen wirklich auf dasselbe Jahr und dasselbe Gebiet?</p>
    </div>
    <div class="card">
      <h4>2 &nbsp;„Claude Code gibt es nicht in der kostenlosen Stufe.“</h4>
      <p class="small">Steht auf Seite&nbsp;{{P:kosten}} und
      Seite&nbsp;{{P:claudecode}}. Quelle: Anthropics eigene Dokumentation. <b>Frage an dich:</b> Stimmt das heute noch? Preis- und
      Verfügbarkeitsangaben veralten am schnellsten von allem in diesem
      Dokument.</p>
    </div>
    <div class="card">
      <h4>3 &nbsp;„Der mittlere Gumroad-Verkäufer verdient 72 $ im Monat.“</h4>
      <p class="small">Steht auf Seite&nbsp;{{P:geldzahlen}}. <b>Frage an dich:</b> Aus
      welchem Zeitraum stammen die Daten, und wie viele Produkte wurden
      ausgewertet? Und: Ist der Median hier die richtige Kennzahl — oder wäre
      eine andere ehrlicher?</p>
    </div>
  </div>

  <div class="sp-5"></div>
  <div class="callout co-honest no-break">
    <span class="clabel">Wenn du einen Fehler findest</span>
    <p>Dann hast du in vierzig Minuten mehr über KI gelernt als in {{P:TOTAL}}
    Seiten Text — nämlich, dass auch sorgfältig geprüfte KI-Recherche Fehler
    enthält. Von 153 recherchierten Aussagen waren 11 schlicht falsch und 46 in
    ihrer ursprünglichen Form übertrieben. Es wäre erstaunlich, wenn im Rest
    keiner mehr steckte.</p>
  </div>
</div>
""", anchor="pruefmich")

    # ══════════════════ RESSOURCEN ══════════════════
    set_section("Anhang A — Ressourcen")
    page("""
<div class="flow">
  <span class="kicker">Anhang A</span>
  <h2>Kurse und Quellen</h2>
  <hr class="hr-thick">
  <p class="small mut">Mit der Handykamera auf den QR-Code halten. Alle Links
  geprüft am 28.&nbsp;August 2026 — Links veralten, und für Kurse und Preise
  gilt das besonders.</p>
  <div class="sp-4"></div>
  <h3>Zum Anfangen, auf Deutsch</h3>
  <div class="sp-2"></div>
""" +
    resource("Elements of AI", "Der KI-Grundlagenkurs mit über 500.000 Teilnehmenden, komplett auf Deutsch, ausdrücklich ohne Mathematik und ohne Programmieren. Wichtige Einordnung: ein Kurs <i>über</i> KI, kein Kurs im Benutzen von KI — deshalb später sinnvoll, nicht zuerst.",
             "https://www.elementsofai.de/", "Kurs", "de", "kostenlos", "ca. 50 Std.") +
    resource("KI-Campus — Kurskatalog", "Die führende deutschsprachige KI-Lernplattform, vom Stifterverband getragen und öffentlich gefördert — also ohne Verkaufsinteresse. Nach Niveau, Sprache und Dauer filterbar. <b>Nimm hier ein Modul von 1–4 Stunden</b>, nicht den längsten Kurs im Katalog.",
             "https://ki-campus.org/lernangebote/kurse", "Kurse", "de", "kostenlos", "1–25+ Std.") +
    resource("openHPI — Hasso-Plattner-Institut", "Kostenlose deutschsprachige Onlinekurse auf Universitätsniveau, darunter Einführungen ohne Programmiervorkenntnisse. Aktuellen Katalog ansehen statt einen bestimmten Kurs zu suchen.",
             "https://open.hpi.de/", "Kurse", "de", "kostenlos", "variabel") +
    resource("Generative AI for Beginners (Microsoft)", "21 Lektionen, offen und kostenlos, mit vollständiger deutscher Übersetzung. Die „Learn“-Teile funktionieren auch, wenn man die Code-Beispiele nie ausführt. Ehrlicher Hinweis: maschinell übersetzt, mit Microsofts eigenem Fehlervorbehalt.",
             "https://github.com/microsoft/generative-ai-for-beginners/tree/main/translations/de", "Kurs", "de", "kostenlos", "21 Lektionen") +
"""
</div>
""", anchor="anhangA")

    page("""
<div class="flow">
  <h3>Claude selbst — die offiziellen Seiten</h3>
  <p class="small mut">Diese vier Seiten haben wir direkt abgerufen und
  wörtlich geprüft. Sie sind auf Englisch; die Übersetzungsfunktion des
  Browsers funktioniert dafür gut.</p>
  <div class="sp-3"></div>
""" +
    resource("Prompting best practices", "Die offizielle Anleitung zum guten Fragen. Quelle der „brillanten neuen Kollegin“ und des Kollegen-Tests. <b>Nur den Abschnitt „General principles“ lesen</b> — der Rest ist für Entwickler geschrieben.",
             "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices",
             "Doku", "en", "kostenlos", "15 Min.") +
    resource("Claude Code — Desktop-Schnellstart", "Der Beleg, dass du dasselbe Werkzeug wie Konstantin über ein normales Fenster mit Annehmen/Ablehnen-Knöpfen bedienen kannst. „No terminal required.“ Hier steht auch, dass ein Bezahl-Plan nötig ist.",
             "https://code.claude.com/docs/en/desktop-quickstart", "Doku", "en", "kostenlos", "20 Min.") +
    resource("Claude Code — Best practices", "Erkunden → Planen → Umsetzen → Festschreiben, die Interview-Vorlage von Seite {{P:interview}}, CLAUDE.md und die fünf typischen Fehlermuster. Die inhaltlich dichteste Seite von allen.",
             "https://code.claude.com/docs/en/best-practices", "Doku", "en", "kostenlos", "30–45 Min.") +
    resource("Claude Docs — Startseite", "Das Lesezeichen, das überlebt. Ältere Anleitungen verlinken auf Adressen, die inzwischen ins Leere laufen — von hier aus findest du immer die aktuelle Seite. Anthropic betreibt außerdem eine Kursplattform; suche sie von hier aus, statt einer Adresse aus zweiter Hand zu vertrauen.",
             "https://platform.claude.com/docs/en/home", "Doku", "en", "kostenlos", "5 Min.") +
"""
  <div class="sp-4"></div>
  <div class="callout co-warn no-break">
    <span class="clabel">Eine Angabe, die wir nicht bestätigen konnten</span>
    <p class="small">Uns wurde berichtet, Anthropic betreibe unter
    <b>academy.claude.com</b> eine kostenlose Kursplattform, auch auf Deutsch.
    Wir konnten die Seite nicht abrufen, und Anthropics eigene
    Dokumentationsstartseite verlinkte zum Zeitpunkt der Prüfung eine andere
    Adresse für Kurse. Deshalb steht sie hier nicht als Empfehlung. <b>Konstantin
    sollte sie einmal selbst öffnen</b> — wenn es sie gibt, ist sie
    wahrscheinlich der beste Einstieg auf dieser Seite.</p>
  </div>
</div>
""")

    page("""
<div class="flow">
  <h3>Zum Nachprüfen — die Quellen aus diesem Dokument</h3>
  <div class="sp-3"></div>
""" +
    resource("Stanford Digital Economy Lab — „Canaries in the Coal Mine“", "Die Primärquelle zur Frage, ob KI die Einstiegsjobs frisst. Inklusive der Einschränkungen, die die Autoren selbst machen. Wer über die Zahlen auf Seite {{P:studiumzwei}} diskutieren will, sollte diese Seite gelesen haben und nicht die Schlagzeilen darüber.",
             "https://digitaleconomy.stanford.edu/news/canariesaug26/", "Studie", "en", "kostenlos", "15 Min.") +
    resource("Aktuelle Sozialpolitik (Prof. Stefan Sell)", "Ein Sozialwissenschaftler legt PwC, ifo und TÜV nebeneinander und benennt, wer welches Interesse hat. Ein Fachblog, keine begutachtete Quelle — aber das Gegengift zum Guru-Ton, auch zu diesem Dokument.",
             "https://aktuelle-sozialpolitik.de/2026/08/20/ki-und-stellenanzeigen/", "Analyse", "de", "kostenlos", "20 Min.") +
    resource("Statistisches Landesamt BW — Arbeitslosenquote nach Qualifikation", "Die harten deutschen Zahlen von Seite {{P:studium}} zum Selbstnachprüfen: 3,3 % Akademiker, 3,6 % mit Ausbildung, 21,3 % ohne Berufsabschluss.",
             "https://www.statistik-bw.de/presse/pressemitteilungen/pressemitteilung/arbeitslosenquote-2025-auch-unter-hochqualifizierten-in-allen-bundeslaendern-gestiegen/",
             "Statistik", "de", "kostenlos", "10 Min.") +
    resource("FTC — Operation AI Comply", "Eine staatliche Aufsichtsbehörde benennt konkrete „KI-Nebeneinkommen“-Systeme und die konkreten Schäden. Die beste Impfung gegen die Kurse, die dich finden werden.",
             "https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes",
             "Behörde", "en", "kostenlos", "15 Min.") +
    resource("InsightRaider — State of Gumroad 2026", "Die 72-Dollar-Zahl von Seite {{P:geldzahlen}}, mit offengelegter Methodik und einem eigenen Abschnitt über die Grenzen der Auswertung — in diesem Genre selten.",
             "https://insightraider.com/en/state-of-gumroad-2026", "Analyse", "en", "kostenlos", "20 Min.") +
"""
</div>
""")

    page("""
<div class="flow">
  <h3>Für den OffCam-Arbeitsbereich</h3>
  <div class="sp-3"></div>
""" +
    resource("Apple App Review Guidelines", "Der tatsächliche Regeltext — Abschnitte 1.1.4, 1.2, 2.3.8 und 4.3. Ein vollständiger, übernehmbarer Arbeitsbereich in einem einzigen Dokument, ohne eine Zeile Code.",
             "https://developer.apple.com/app-store/review/guidelines/", "Regelwerk", "en", "kostenlos", "90 Min.") +
    resource("FSM — Altersverifikation und geschlossene Benutzergruppen", "Was der JMStV in Deutschland tatsächlich verlangt: Identifizierung plus Authentifizierung, und warum ein Alters-Klick nicht reicht.",
             "https://www.fsm.de/wissen/a-bis-z/altersverifikationssysteme-geschlossene-benutzergruppen/",
             "Fachinfo", "de", "kostenlos", "20 Min.") +
    resource("Nielsen Norman Group — How Many Test Users?", "Warum fünf Testpersonen fast immer reichen und mehrere kleine Tests besser sind als ein großer. Grundlage für den wertvollsten Beitrag zu OffCam.",
             "https://www.nngroup.com/articles/how-many-test-users/", "Methodik", "en", "kostenlos", "10 Min.") +
    resource("EDPB — Statement on Age Assurance", "Zehn Grundsätze zur Altersprüfung nach EU-Datenschutzrecht. Kernbotschaft: Verhältnismäßigkeit — Kinderschutz darf nicht die Privatsphäre aller kosten.",
             "https://www.edpb.europa.eu/our-work-tools/our-documents/statements/statement-12025-age-assurance_en",
             "Behörde", "en", "kostenlos", "30 Min.") +
"""
  <div class="sp-4"></div>
  <h3>Für den Fall, dass es doch ums Geld geht</h3>
  <div class="sp-2"></div>
""" +
    resource("Studis Online — Selbstständig jobben", "Die maßgebliche deutschsprachige Seite für Studierende mit Nebeneinkommen: Krankenversicherung, Kindergeld, BAföG, mit durchgerechneten Beispielen. <b>Vor der ersten Rechnung lesen, nicht danach.</b>",
             "https://www.studis-online.de/jobben/selbststaendig-jobben-auswirkungen.php",
             "Ratgeber", "de", "kostenlos", "25 Min.") +
"""
</div>
""")

    # ── ANHANG B: PROMPTS ──
    set_section("Anhang B — Prompts")
    page("""
<div class="flow">
  <span class="kicker">Anhang B</span>
  <h2>Prompts zum Abschreiben</h2>
  <hr class="hr-thick">
  <p class="small mut">Die eckigen Klammern ersetzen. Sonst nichts ändern.</p>
  <div class="sp-4"></div>
""" +
    prompt("Verstehen", "Erkläre mir [Begriff/Konzept] dreimal:\n"
           "1. so, wie du es jemandem, der klug ist, aber aus einem anderen Fach kommt, erklären würdest,\n"
           "2. in genau einem Satz,\n"
           "3. mit einer Analogie aus dem Alltag.\n\n"
           "Sag mir danach, was an dieser Erklärung vereinfacht ist und\n"
           "wo sie in die Irre führen könnte.") +
    """<div class="sp-3"></div>""" +
    prompt("Abfragen", "Hier ist meine eigene Mitschrift zu [Thema].\nFrag mich dazu ab: zehn Fragen.\n\n"
           "Regeln: eine Frage nach der anderen. Warte auf meine Antwort,\n"
           "bevor du die nächste stellst. Bewerte meine Antwort kurz und\n"
           "ergänze, was gefehlt hat. Stelle nur Fragen, die sich aus dem\n"
           "Text unten beantworten lassen.\n\n"
           "[Text einfügen]") +
    """<div class="sp-3"></div>""" +
    prompt("Kritisiert werden", "Hier ist ein Text von mir. Finde die drei schwächsten Stellen\n"
           "in der Argumentation und formuliere zu jeder den stärksten\n"
           "Einwand, den eine wohlwollende, aber kritische Leserin hätte.\n\n"
           "Sag mir nicht, was gut ist. Ich weiß, dass es Schwächen gibt,\n"
           "ich sehe sie nur selbst nicht mehr.\n\n"
           "[Text einfügen]") +
    """<div class="sp-3"></div>""" +
    prompt("Gegen Halluzinationen — an alles anhängen",
           "Wenn du etwas nicht sicher weißt, sag das ausdrücklich, statt\n"
           "zu raten. Markiere jede Aussage, bei der du dir unsicher bist.\n"
           "Erfinde unter keinen Umständen Quellenangaben, Zahlen oder\n"
           "Zitate.") +
"""
</div>
""", anchor="anhangB")

    page("""
<div class="flow">
  <div class="sp-2"></div>
""" +
    prompt("Projekt-Anweisung — einmal einrichten, dauerhaft nutzen",
           "Antworte immer auf Deutsch.\n"
           "Wenn du etwas nicht sicher weißt, sag es ausdrücklich.\n"
           "Erfinde keine Quellen, Zahlen oder Zitate.\n"
           "Fasse dich kurz, außer ich bitte um Ausführlichkeit.\n"
           "Wenn meine Frage unklar ist, frag nach, statt zu raten.") +
    """<div class="sp-3"></div>""" +
    prompt("Für OffCam — die Interview-Vorlage (Anthropic)",
           "Ich möchte [Funktion] bauen.\n\n"
           "Bevor du mit der Umsetzung beginnst, stelle mir Fragen zu allem,\n"
           "was unklar ist: Anforderungen, Grenzfälle, gewünschtes Verhalten.\n"
           "Stelle die Fragen einzeln nacheinander.\n\n"
           "Schreibe danach eine Spezifikation, die ich prüfen kann,\n"
           "bevor du irgendetwas umsetzt.") +
    """<div class="sp-3"></div>""" +
    prompt("Für OffCam — Texte prüfen",
           "Du bist Lektorin für deutsche Produkttexte. Hier sind die Texte\n"
           "aus einer App für erwachsene Creator. Der Ton soll sein:\n"
           "diskret, auf Augenhöhe, nicht anbiedernd, nicht anzüglich.\n\n"
           "Prüfe jeden Text auf Verständlichkeit ohne Vorwissen und auf\n"
           "unbeabsichtigte Doppeldeutigkeiten. Sag mir außerdem, ob er\n"
           "Vertrauen schafft oder untergräbt.\n\n"
           "Gib mir eine Tabelle: Original | Problem | Vorschlag.\n\n"
           "[Texte einfügen]") +
"""
  <div class="sp-5"></div>
  <div class="callout co-tip no-break">
    <span class="clabel">Der wichtigste Prompt steht nicht hier</span>
    <p class="small">Es ist der, den du dir selbst schreibst, weil du eine
    Aufgabe zum dritten Mal machst. Wenn du dich dabei erwischst, wie du etwas
    wiederholt formulierst: aufschreiben, in dein Projekt legen. Das ist der
    Punkt, an dem aus Benutzen Können wird.</p>
  </div>
</div>
""", anchor="anhangB2")

    # ── ANHANG C: RECHT ──
    set_section("Anhang C — Rechtliches")
    page("""
<div class="flow">
  <span class="kicker">Anhang C</span>
  <h2>Falls es je ums Geld geht</h2>
  <hr class="hr-thick">
  <p class="lead">Bewusst im Anhang: Diese Seiten sind nur relevant, wenn
  tatsächlich einmal jemand für etwas bezahlt. Vorher sind sie Ballast.</p>

  <div class="sp-4"></div>
  <div class="callout co-warn no-break">
    <span class="clabel">Stand August 2026 · keine Steuer-, Sozial- oder Rechtsberatung</span>
    <p>Alle Grenzwerte auf diesen beiden Seiten ändern sich jährlich. Sie stehen
    hier, damit du weißt, <i>welche Fragen du stellen musst</i> — beantworten
    müssen sie Krankenkasse, BAföG-Amt und im Zweifel eine Steuerberaterin. Und
    zwar bevor die erste Rechnung rausgeht, nicht danach.</p>
  </div>

  <div class="sp-4"></div>
  <div class="stack">
    <div class="card">
      <h4>Kleinunternehmerregelung</h4>
      <p class="small">Seit 2025 gilt: Wer im Vorjahr höchstens 25.000&nbsp;€
      Umsatz hatte und im laufenden Jahr unter 100.000&nbsp;€ bleibt, kann die
      Regelung nutzen; Neugründer starten automatisch darin.</p>
      <p class="small"><b>Die Falle:</b> Wird die Grenze überschritten, fällt
      man sofort im laufenden Jahr heraus — bereits mit dem Umsatz, der sie
      reißt. Im Gründungsjahr gilt dasselbe für die 25.000-€-Grenze. Nachteil
      der Regelung: kein Vorsteuerabzug. Für den Anfang trotzdem fast immer
      richtig, weil die Umsatzsteuer-Voranmeldungen entfallen.</p>
    </div>
    <div class="card card-red">
      <h4>Krankenversicherung — der teuerste Fallstrick</h4>
      <p class="small">Wer über die Eltern oder den Ehepartner familienversichert
      ist, bleibt es bei nebenberuflicher Selbstständigkeit nur, solange die
      monatlichen Einnahmen regelmäßig <b>603&nbsp;€</b> nicht übersteigen
      (Wert gilt seit Januar 2026). Wird die Grenze länger als drei Monate im
      Jahr überschritten, endet die Familienversicherung.</p>
      <p class="small">Übersteigt das monatliche Arbeitseinkommen
      <b>2.966,25&nbsp;€</b> (2026), geht die Kasse von hauptberuflicher
      Selbstständigkeit aus. Ob haupt- oder nebenberuflich,
      <b>entscheidet die Krankenkasse</b>, nicht du; bei bis zu 20 Wochenstunden
      wird in der Regel Nebenberuflichkeit angenommen. Wer studentisch versichert
      ist, fällt bei hauptberuflicher Selbstständigkeit ebenfalls heraus — die
      Grenze und die 20-Stunden-Regel gelten dort genauso.</p>
      <p class="small"><b>Praktische Regel: mit der Krankenkasse sprechen,
      bevor die erste Rechnung rausgeht.</b> Wer die Kasse nicht informiert,
      riskiert Beitragsnachforderungen rückwirkend bis zur Gewerbeanmeldung.</p>
    </div>
  </div>
</div>
""", anchor="anhangC")

    page("""
<div class="flow">
  <div class="sp-2"></div>
  <div class="stack">
    <div class="card">
      <h4>BAföG</h4>
      <p class="small">Seit dem Wintersemester 2024/25 gibt es auch für
      Selbstständige eine Betriebsausgabenpauschale ohne Einzelnachweis. Als
      Orientierung nennt Studis Online rund 6.680&nbsp;€ anrechnungsfreies
      Einkommen pro zwölfmonatigem Bewilligungszeitraum. Die genaue Grenze hängt
      davon ab, welche Monate in den Zeitraum fallen — im Zweifel mit dem
      BAföG-Rechner für den eigenen Zeitraum durchrechnen.</p>
      <p class="small">Kindergeld wird durch Einkommen aus Selbstständigkeit im
      Erststudium nicht gekürzt, mindestens bis zum 25.&nbsp;Geburtstag.</p>
      <p class="small"><b>Meldepflicht:</b> Wie bei der Krankenkasse ist
      Einkommen aus Selbstständigkeit dem BAföG-Amt zu melden. Was eine
      unterlassene Meldung konkret kostet, unterscheidet sich je nach Amt —
      frag danach, bevor die erste Rechnung rausgeht.</p>
    </div>
    <div class="card">
      <h4>Anmeldung</h4>
      <p class="small">Ein Gewerbe anzumelden kostet je nach Gemeinde etwa
      15–65&nbsp;€. Freie Berufe nach §&nbsp;18 EStG brauchen gar keine
      Gewerbeanmeldung, sondern melden sich kostenlos über ELSTER beim Finanzamt.
      Ob eine Software- oder Beratungstätigkeit freiberuflich oder gewerblich
      ist, wird im Einzelfall entschieden und landet bei Software häufig im
      Gewerblichen — der eine Punkt, für den sich eine einzelne Frage beim
      Steuerberater lohnt.</p>
    </div>
  </div>

  <div class="sp-6"></div>
  <div class="card card-dark no-break">
    <span class="kicker">Die Reihenfolge, die Ärger erspart</span>
    <p class="small" style="color:#CFC7CB">Erst mit der Krankenkasse sprechen.
    Dann, falls du BAföG beziehst, mit dem BAföG-Amt. Dann anmelden. Dann die
    erste Rechnung schreiben. Jede andere Reihenfolge ist reparabel, aber
    teuer — und die Reparatur kostet mehr Zeit, als die ersten Aufträge
    einbringen.</p>
  </div>
</div>
""")

    # ── RÜCKSEITE ──
    set_section("")
    page("""
<span class="glow glow-a"></span>
<div style="flex:1"></div>
<div>
  <span class="kicker">Zum Schluss</span>
  <h1 style="font-size:27pt">Du musst das<br>nicht tun.</h1>
  <div class="sp-5"></div>
  <p class="lead" style="color:#CFC7CB;max-width:135mm">Konstantin hat dieses
  Dokument bestellt, weil er begeistert ist und dich dabeihaben will. Das ist
  ein schöner Grund. Er ist trotzdem seiner, nicht deiner.</p>
  <div class="sp-4"></div>
  <p style="color:#A79FA4;max-width:135mm">Wenn du nach vier Wochen zu dem
  Schluss kommst, dass dich das nicht interessiert, dann stimmt diese Antwort.
  Und wenn du zu dem Schluss kommst, dass es dich interessiert, dann nicht,
  weil hier {{P:TOTAL}} Seiten standen — sondern weil du in irgendeiner Woche
  gemerkt hast, dass dir etwas leichter fiel als vorher.</p>
  <div class="sp-6"></div>
  <p style="color:#7E767C;max-width:135mm" class="small">Das ist der einzige
  Beweis, der zählt. Alles andere in diesem Dokument sind Zahlen von anderen
  Leuten über andere Leute.</p>
</div>
<div style="flex:1"></div>
<div class="cover-meta">
  <span>KI-Crashkurs für Marion</span>
  <span>28.08.2026</span>
</div>
""", cls="cover", pn=False, rh=False)
