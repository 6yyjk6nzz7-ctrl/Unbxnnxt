# -*- coding: utf-8 -*-
"""Teil B: Studiumsfrage, Was wir nicht wissen, Teil 2 (Verstehen)."""
from doc import (page, set_section, kicker, fact, callout, prompt, card,
                 resource, wk, toc_row, gloss, opener)


def build_b():
    set_section("Teil 1 — Die Lage")

    # ── 1.5 Die Studiumsfrage ──
    page("""
<div class="flow">
  <span class="kicker">1.5 — Die eigentliche Frage</span>
  <h2>Lohnt sich Studieren noch?</h2>
  <hr class="hr-thick">

  <p class="lead">Das ist die Frage, wegen der dieses Dokument existiert. Hier
  ist die Antwort, so ehrlich wie die Daten es zulassen — inklusive der Teile,
  die für Konstantins These sprechen.</p>

  <div class="sp-5"></div>
  <h3>Was klar für das Studium spricht</h3>
  <div class="sp-3"></div>

  <table>
    <tr><th>Arbeitslosenquote in Deutschland, Jahresdurchschnitt 2025</th><th></th></tr>
    <tr><td>Ohne abgeschlossene Berufsausbildung</td><td class="n red">21,3&nbsp;%</td></tr>
    <tr><td>Alle Erwerbspersonen</td><td class="n">6,3&nbsp;%</td></tr>
    <tr><td>Mit betrieblicher oder schulischer Ausbildung</td><td class="n">3,6&nbsp;%</td></tr>
    <tr><td>Akademikerinnen und Akademiker</td><td class="n">3,3&nbsp;%</td></tr>
  </table>
  <div class="sp-2"></div>
  <p class="tiny">Statistisches Landesamt Baden-Württemberg auf Basis der
  Bundesagentur für Arbeit, Pressemitteilung 2026.</p>

  <div class="sp-4"></div>
  <p>Der Abstand zwischen 3,3&nbsp;% und 21,3&nbsp;% ist der stabilste Befund unter
  den Arbeitsmarktzahlen. Er hat sich in der KI-Ära nicht umgekehrt und nicht
  eingeebnet. Wer nach Belegen sucht, dass formale Qualifikation entwertet
  wurde, findet sie hier nicht.</p>

  <div class="sp-4"></div>
  <div class="fact no-break">
    <div class="big">55,4&nbsp;%<small>halten Abschlüsse für<br>schwer ersetzbar</small></div>
    <div><p>Das ifo-Institut hat im Mai 2026 KI-nutzende Unternehmen gefragt, ob
    sie Beschäftigte mit Berufs- oder Hochschulabschluss durch geringer
    qualifizierte, KI-gestützte Kräfte ersetzen könnten. Die Mehrheit — 55,4&nbsp;% —
    hält das für schwierig oder unmöglich. Beim Ersatz von <i>Berufserfahrung</i>
    sind es sogar 62,7&nbsp;%. Nur 19,7&nbsp;% halten formale Qualifikationen
    zumindest in Teilbereichen für kompensierbar.</p>
    <span class="src">ifo Konjunkturumfrage Mai 2026 · Einschätzungen von Unternehmen,
    keine Einstellungsentscheidungen</span></div>
  </div>
</div>
""", anchor="studium")

    page("""
<div class="flow">
  <h3>Was gegen die einfache Version spricht — und für Konstantin</h3>
  <p>Es wäre unehrlich, hier aufzuhören. Es gibt Befunde, die unangenehm sind,
  und sie betreffen ausgerechnet den Berufseinstieg.</p>

  <div class="sp-4"></div>
  <div class="fact no-break">
    <div class="big">&minus;19&nbsp;%<small>Beschäftigung bei<br>22- bis 25-Jährigen</small></div>
    <div><p>Das Stanford Digital Economy Lab findet: In stark KI-exponierten
    Berufen liegt die Beschäftigung der 22- bis 25-Jährigen inzwischen rund
    19&nbsp;% unter dem Niveau, das zu erwarten wäre, wenn sie sich wie in
    weniger exponierten Berufen entwickelt hätte. Im Juli 2025 waren es noch
    15&nbsp;%, im Juni 2026 sind es 19&nbsp;%. In den beiden am stärksten
    exponierten Fünfteln fiel die Beschäftigung dieser Altersgruppe seit
    November 2022 um rund 11&nbsp;%, während sie in den drei am wenigsten
    exponierten um rund 10&nbsp;% wuchs.</p>
    <span class="src">Stanford Digital Economy Lab, „Canaries in the Coal Mine“,
    Fassung August 2026</span></div>
  </div>

  <div class="sp-4"></div>
  <div class="callout co-warn no-break">
    <span class="clabel">Der Befund, der wirklich weh tut</span>
    <p>Dieselbe Studie beschreibt, <i>wo</i> die Beschäftigung fällt: in Berufen,
    die stark auf <b>kodifiziertem Wissen</b> beruhen — also formalem,
    standardisiertem, dokumentiertem Wissen, das sich über Ausbildung, Lehrbücher
    und schriftliche Verfahren vermitteln lässt. Gestiegen ist die Beschäftigung
    dagegen bei erfahrenen Kräften in Berufen, die auf <b>implizitem Wissen</b>
    beruhen: erworben durch Praxis, Anleitung und wiederholte echte Situationen.</p>
    <p>Das ist, so wörtlich es geht, eine Beschreibung dessen, was ein Studium
    vermittelt. Die Autoren merken außerdem an, dass Frauen im Schnitt stärker
    exponiert sind.</p>
  </div>

  <div class="sp-5"></div>
  <p>Dazu passt: Die Arbeitslosenquote unter Akademikern ist von 2,9&nbsp;%
  (2024) auf 3,3&nbsp;% (2025) gestiegen — der erste Wert über 3&nbsp;% seit
  2006. Rund ein Fünftel des Anstiegs geht laut Bundesagentur für Arbeit auf
  Fluchtmigration zurück. Und in den USA lag die Arbeitslosenquote unter
  Hochschulabsolventinnen und -absolventen <b>in den ersten Berufsjahren</b> im
  zweiten Quartal 2026 bei rund 5,6&nbsp;%, die Quote der nicht
  ausbildungsadäquat Beschäftigten bei 42&nbsp;%. Das ist eine Zahl über
  Berufseinsteiger, nicht über alle Akademiker.</p>
  <p class="tiny">New York Fed, Labor Market for Recent College Graduates,
  2.&nbsp;Quartal 2026.</p>
</div>
""", anchor="studiumzwei")

    page("""
<div class="flow">
  <span class="kicker">Die Antwort</span>
  <h2>Was daraus folgt</h2>
  <hr class="hr-thick">

  <p class="lead">Die Daten stützen weder „Studium ist überflüssig“ noch
  „einfach weitermachen wie immer“. Sie stützen etwas Drittes, und das ist
  unbequemer als beides.</p>

  <div class="sp-5"></div>

  <ol class="steps">
    <li><b>Der Abschluss schützt weiterhin.</b> 3,3&nbsp;% gegen 21,3&nbsp;%.
    Wer ihn wegwirft, tauscht das stabilste bekannte Sicherheitsnetz gegen eine
    Prognose ein. Das ist kein guter Tausch.</li>

    <li><b>Der Einstieg wird trotzdem härter.</b> Genau die Tätigkeiten, mit
    denen Berufsanfänger bisher angefangen haben — recherchieren,
    zusammenfassen, standardisierte Texte produzieren, Daten aufbereiten — sind
    die, die zuerst automatisiert werden. Der Abschluss allein reicht nicht
    mehr, um die erste Tür zu öffnen.</li>

    <li><b>Deshalb: beides.</b> Nicht Studium <i>oder</i> KI, sondern Studium
    <i>und</i> KI. Der Vorteil entsteht nicht durch das Werkzeug und nicht durch
    das Zeugnis, sondern durch die Kombination — jemand, der ein Fachgebiet
    versteht und ein Werkzeug beherrscht, das die anderen im Fachgebiet noch
    nicht beherrschen.</li>

    <li><b>Und die Konsequenz für den Einstieg:</b> Sammle so früh wie möglich
    das, was die Statistik „implizites Wissen“ nennt — echte Fälle, echte
    Verantwortung, echte Menschen. Werkstudentenstelle, HiWi-Job, Tutorium,
    Praktikum, ein reales Projekt wie OffCam. Das ist derzeit der einzige
    Befund, der nach einer verlässlichen Strategie aussieht.</li>
  </ol>

  <div class="sp-6"></div>
  <div class="callout co-honest no-break">
    <span class="clabel">Ein Wort zum ursprünglichen Auftrag</span>
    <p>Konstantins Ausgangsthese war, „dass KI die Zukunft ist und dass
    Studieren keinen Sinn macht, wenn man mit KI so viel Geld verdienen kann“.
    Der Teil über das Studium ist nach dieser Datenlage falsch. Der Teil über
    das Geld steht ab Seite&nbsp;{{P:geldzahlen}}, und er hält noch weniger
    stand.</p>
    <p>Was an seinem Impuls richtig ist: Dass sich etwas verändert, dass es
    schnell geht, und dass Zusehen keine Strategie ist. Das stimmt. Nur ist die
    Antwort darauf nicht Abbrechen, sondern Dazulernen.</p>
  </div>
</div>
""")

    # ── 1.6 Was wir nicht wissen ──
    page("""
<div class="flow">
  <span class="kicker">1.6 — Ehrlichkeit über die Grenzen</span>
  <h2>Was wir nicht wissen</h2>
  <hr class="hr-thick">

  <p class="lead">Jedes Dokument, das nur Gewissheiten enthält, lügt an irgendeiner
  Stelle. Hier sind die Punkte, an denen die Recherche offen unsicher blieb.</p>

  <div class="sp-5"></div>
  <div class="stack">
    <div class="card">
      <h4>Wie lange die Prämien halten</h4>
      <p class="small">Der deutsche Finanzsektor zeigt bereits eine negative
      Prämie. Ob das die Ausnahme oder die Vorschau ist, weiß derzeit niemand.
      Wer eine Zahl für 2030 nennt, rät.</p>
    </div>
    <div class="card">
      <h4>Ob US-Befunde auf Deutschland übertragbar sind</h4>
      <p class="small">Die schärfsten Zahlen zum Einstiegsarbeitsmarkt stammen
      aus den USA. Der deutsche Arbeitsmarkt ist stärker reguliert, langsamer
      und anders strukturiert — PwC misst hier eine Korrelation von 0,02
      zwischen KI-Exponierung und Kompetenzwandel. Vermutlich kommt vieles
      später und schwächer an. Sicher ist das nicht.</p>
    </div>
    <div class="card">
      <h4>Wie lange es bis zum ersten Einkommen dauert</h4>
      <p class="small">Die Spannen in den Quellen reichen von 60&nbsp;Tagen (mit
      bestehendem Publikum) bis zu zwölf Monaten (ohne). Für jemanden, der
      nebenbei studiert, ist beides wenig aussagekräftig. Wir haben keine
      belastbare Zahl gefunden und nennen deshalb keine.</p>
    </div>
    <div class="card">
      <h4>Welche Werkzeuge in zwei Jahren zählen</h4>
      <p class="small">„Agentic AI“ tauchte 2024 in 0,06&nbsp;% der
      US-Stellenanzeigen auf, 2025 in 0,23&nbsp;% — plus 280&nbsp;% und trotzdem
      verschwindend wenig. Die Lehre daraus ist nicht „lerne Agenten“, sondern:
      Rechne damit, dass die konkrete Technik in 18&nbsp;Monaten anders heißt.
      Deshalb geht es in diesem Dokument um Prinzipien und nicht um Klickpfade.</p>
    </div>
  </div>
</div>
""", anchor="nichtwissen")

    # ══════════════════ OPENER TEIL 2 ══════════════════
    set_section("Teil 2 — Verstehen")
    page(opener("2", "Verstehen",
        "Bevor du etwas benutzt, das selbstbewusst Unsinn erzählen kann, "
        "solltest du wissen, warum es das tut.",
        [("Was da eigentlich passiert", "ein Modell ohne Mathematik"),
         ("Warum sie sich irrt", "Halluzinationen"),
         ("Was KI nicht kann", "die Liste, die selten jemand zeigt"),
         ("Die Einwände", "Urheberrecht, Energie, Abhängigkeit"),
         ("Glossar", "zehn Begriffe, mehr brauchst du nicht")]),
        cls="opener", rh=False, anchor="teil2")

    # ── 2.1 Was ist das ──
    page("""
<div class="flow">
  <span class="kicker">2.1 — Ohne Mathematik</span>
  <h2>Was da eigentlich passiert</h2>
  <hr class="hr-thick">

  <p class="lead">Du brauchst kein technisches Verständnis, um KI gut zu
  benutzen. Aber du brauchst ein Bild davon, warum sie sich irrt — sonst kannst
  du ihre Ergebnisse nicht beurteilen. Und genau das Beurteilen ist die
  Fähigkeit, für die bezahlt wird.</p>

  <div class="sp-5"></div>

  <h3>Das Minimalmodell</h3>
  <p>Ein Sprachmodell wie Claude oder ChatGPT hat sehr viel Text gelesen und
  daraus gelernt, welches Wort auf welches folgt. Wenn du ihm etwas schreibst,
  erzeugt es Wort für Wort eine Fortsetzung, die zu deinem Text passt. Das ist,
  stark vereinfacht, alles.</p>

  <p>Daraus folgen drei Dinge, die praktisch fast alles erklären:</p>

  <div class="sp-3"></div>
  <div class="stack">
    <div class="card card-red">
      <h4>Es gibt keine Datenbank, in der die Wahrheit steht</h4>
      <p class="small">Das Modell schlägt nichts nach. Es erzeugt, was
      <i>plausibel klingt</i>. Meistens ist Plausibles auch richtig — deshalb
      funktioniert es überhaupt. Aber wenn es nichts Passendes gelernt hat,
      hört es nicht auf. Es erfindet etwas, das genauso klingt wie die richtige
      Antwort. Das nennt man <b>Halluzination</b>.</p>
    </div>
    <div class="card card-red">
      <h4>Es weiß nicht, ob es etwas weiß</h4>
      <p class="small">Ein Mensch merkt, wenn er unsicher ist. Ein Sprachmodell
      hat dieses Gefühl nicht. Die erfundene Antwort kommt im selben souveränen
      Tonfall wie die richtige. <b>Selbstsicherheit ist bei KI kein Signal für
      Richtigkeit.</b></p>
    </div>
    <div class="card card-red">
      <h4>Es rechnet nicht, es formuliert</h4>
      <p class="small">Deshalb sind Zahlen, Datumsangaben und Quellenangaben die
      unzuverlässigsten Ausgaben überhaupt. Eine erfundene Literaturangabe sieht
      exakt aus wie eine echte: plausibler Autor, plausibler Titel, plausibles
      Jahr — und existiert nicht.</p>
    </div>
  </div>
</div>
""")

    # ── 2.2 Halluzinationstest ──
    page("""
<div class="flow">
  <span class="kicker">2.2 — Die wichtigste Übung im ganzen Dokument</span>
  <h2>Der Halluzinations-Test</h2>
  <hr class="hr-thick">

  <p class="lead">Bevor du der KI irgendetwas glaubst, bring sie einmal
  absichtlich zum Lügen. Zehn Minuten, und danach hast du für immer das richtige
  Misstrauen.</p>

  <div class="sp-5"></div>
  <ol class="steps">
    <li><b>Frag etwas, das du sicher weißt.</b> Ein Detail aus deinem Fach, aus
    deiner Heimatstadt, aus deiner Familie. Sieh dir an, wie gut die Antwort
    ist — meistens erstaunlich gut.</li>
    <li><b>Frag jetzt etwas, das es nicht gibt.</b> Erfinde eine Studie, ein
    Buch, eine Regelung. Sieh dir an, was passiert.</li>
    <li><b>Bitte um Quellen.</b> Und dann prüfe eine davon wirklich nach.</li>
  </ol>

  <div class="sp-5"></div>
""" +
    prompt("Zum Kopieren — Schritt 2",
           "Fasse mir die Kernaussagen der Studie „Klemm &amp; Vogt (2023):\n"
           "Digitale Lernumgebungen und Prüfungsangst an deutschen\n"
           "Hochschulen“ zusammen und nenne die drei wichtigsten Ergebnisse.") +
"""
  <div class="sp-4"></div>
  <div class="callout co-warn no-break">
    <span class="clabel">Was du wahrscheinlich sehen wirst</span>
    <p>Diese Studie gibt es nicht — wir haben sie für dieses Dokument erfunden.
    Trotzdem bekommst du mit einiger Wahrscheinlichkeit eine flüssige
    Zusammenfassung mit drei plausiblen Ergebnissen. Manche Modelle fragen
    inzwischen nach oder widersprechen; das ist besser geworden, aber nicht
    zuverlässig.</p>
    <p><b>Der Moment, in dem du das zum ersten Mal siehst, ist wertvoller als
    jeder Kurs.</b> Danach weißt du körperlich, nicht nur theoretisch: Der
    souveräne Tonfall bedeutet nichts.</p>
  </div>

  <div class="sp-5"></div>
  <div class="callout co-tip no-break">
    <span class="clabel">Der Gegen-Prompt, den du dir merken solltest</span>
    <p class="small">Hänge bei allem, wo Richtigkeit zählt, diesen Satz an:
    <b>„Wenn du es nicht sicher weißt, sag das ausdrücklich, statt zu raten.
    Markiere alles, bei dem du dir nicht sicher bist.“</b> Das hilft nicht immer,
    aber messbar oft.</p>
  </div>
</div>
""", anchor="halluzination")

    # ── 2.3 Was KI nicht kann ──
    page("""
<div class="flow">
  <span class="kicker">2.3 — Die Liste, die in Werbevideos fehlt</span>
  <h2>Was KI nicht kann</h2>
  <hr class="hr-thick">
  <div class="sp-2"></div>

  <div class="cols-2u">
    <div class="card">
      <h4>Zuverlässig rechnen</h4>
      <p class="small">Sie formuliert Zahlen, sie berechnet sie nicht. Für alles
      mit Geld oder Mengen: nachrechnen.</p>
    </div>
    <div class="card">
      <h4>Quellen angeben</h4>
      <p class="small">Der häufigste teure Fehler. Erfundene Belege sehen echt
      aus. Jede einzelne Angabe selbst öffnen.</p>
    </div>
    <div class="card">
      <h4>Aktuelle Fakten kennen</h4>
      <p class="small">Ohne Websuche endet ihr Wissen an einem Stichtag. Preise,
      Gesetze, Personen, Fristen: immer prüfen.</p>
    </div>
    <div class="card">
      <h4>Deutsches Verwaltungsdetail</h4>
      <p class="small">Prüfungsordnungen, Fristen, Kassenregeln, lokale
      Zuständigkeiten. Hier ist sie am gefährlichsten, weil sie so überzeugend
      klingt.</p>
    </div>
    <div class="card">
      <h4>Wissen, was du eigentlich willst</h4>
      <p class="small">Sie füllt Lücken mit Plausiblem. Was du nicht sagst,
      erfindet sie — im Zweifel anders, als du es gemeint hast.</p>
    </div>
    <div class="card">
      <h4>Verantwortung übernehmen</h4>
      <p class="small">Wenn etwas falsch abgegeben, falsch abgerechnet oder
      falsch versendet wird, warst du es. Immer.</p>
    </div>
  </div>

  <div class="sp-6"></div>
  <div class="card card-dark no-break">
    <span class="kicker">Die eine Regel, die alles zusammenfasst</span>
    <p class="lead" style="color:#F2ECE7;margin-top:2mm">Benutze KI nur dort, wo
    du <span class="red">erkennen könntest</span>, dass sie falsch liegt.</p>
    <p class="small" style="color:#B5ACB1;margin-top:4mm">Einen Text über dein
    eigenes Fach kannst du beurteilen — also ist KI dort nützlich. Eine
    Rechtsauskunft über ein Gebiet, von dem du nichts verstehst, kannst du nicht
    beurteilen — also ist sie dort gefährlich. Diese Regel entscheidet fast alle
    Zweifelsfälle, und sie erklärt nebenbei, warum Fachwissen durch KI wertvoller
    wird statt wertloser.</p>
  </div>
</div>
""", anchor="koennennicht")

    # ── 2.4 Die Einwände ──
    page("""
<div class="flow">
  <span class="kicker">2.4 — Die Einwände, die du haben wirst</span>
  <h2>Und die Antworten,<br>soweit es sie gibt</h2>
  <hr class="hr-thick">

  <p>Es wäre unaufrichtig, dir ein ganzes Dokument über KI zu geben, ohne die
  Kritikpunkte zu nennen. Ein paar davon sind gut.</p>

  <div class="sp-4"></div>
  <div class="stack">
    <div class="card card-tint">
      <h4>„Die Modelle sind auf fremder Arbeit trainiert.“</h4>
      <p class="small"><b>Stimmt weitgehend.</b> Trainingsdaten stammen zu großen
      Teilen aus Texten und Bildern, für deren Nutzung niemand gefragt wurde.
      Es laufen Verfahren dazu, die Rechtslage ist international ungeklärt. Wer
      das für einen Rechtsbruch hält, hat dafür ernst zu nehmende Argumente.</p>
    </div>
    <div class="card card-tint">
      <h4>„Das verbraucht enorm viel Energie und Wasser.“</h4>
      <p class="small"><b>Stimmt, aber die Größenordnung ist umstritten.</b>
      Rechenzentren verbrauchen real viel; die kursierenden Vergleiche pro
      Anfrage schwanken jedoch um Größenordnungen und stammen oft von
      interessierter Seite. Belastbar ist: nennenswert, wachsend, und nicht so
      apokalyptisch wie manche Grafik behauptet.</p>
    </div>
    <div class="card card-tint">
      <h4>„Dahinter steckt prekäre Klickarbeit.“</h4>
      <p class="small"><b>Stimmt.</b> Das Bewerten und Filtern von Trainingsdaten
      wird vielfach schlecht bezahlt und unter belastenden Bedingungen erledigt,
      häufig im globalen Süden. Das ist gut dokumentiert und wird von der Branche
      ungern erwähnt.</p>
    </div>
    <div class="card card-tint">
      <h4>„Die Systeme haben Vorurteile.“</h4>
      <p class="small"><b>Stimmt.</b> Sie lernen aus vorhandenem Text und geben
      dessen Schieflagen wieder — bei Geschlecht, Herkunft und Sprache. Es wird
      dagegen gearbeitet, gelöst ist es nicht.</p>
    </div>
    <div class="card card-tint">
      <h4>„Wir machen uns von amerikanischen Konzernen abhängig.“</h4>
      <p class="small"><b>Stimmt.</b> Die relevanten Modelle kommen aus wenigen
      Unternehmen in zwei Ländern. Wer heute einen Arbeitsprozess darauf
      aufbaut, akzeptiert, dass Preis und Verfügbarkeit anderswo entschieden
      werden.</p>
    </div>
  </div>

  <div class="sp-4"></div>
  <div class="callout co-honest no-break">
    <span class="clabel">Die einzig ehrliche Schlussfolgerung</span>
    <p>Man kann diese Technik kritisch sehen <b>und</b> verstehen wollen. Beides
    zugleich ist keine Inkonsequenz.</p>
  </div>
</div>
""")

    # ── 2.5 Glossar ──
    page("""
<div class="flow">
  <span class="kicker">2.5 — Zehn Begriffe</span>
  <h2>Glossar</h2>
  <hr class="hr-thick">
  <p class="small mut">Mehr brauchst du am Anfang wirklich nicht. Alles andere
  lernst du, wenn es dir zum ersten Mal begegnet.</p>
  <div class="sp-4"></div>
""" +
    gloss("Prompt", "Die Anweisung, die du eintippst. Das deutsche Wort wäre „Eingabe“, sagt aber niemand.") +
    gloss("Modell", "Das eigentliche System, z.&nbsp;B. Claude Sonnet oder GPT. Verschiedene Modelle sind unterschiedlich schnell, klug und teuer.") +
    gloss("Token", "Die Häppchen, in die Text zerlegt wird — grob eine Silbe. Preise und Längenbegrenzungen werden darin gemessen.") +
    gloss("Kontextfenster", "Wie viel Text das Modell gleichzeitig „im Kopf“ behalten kann. Ist es voll, fällt der Anfang des Gesprächs hinten heraus.") +
    gloss("Halluzination", "Eine erfundene Angabe, die richtig klingt. Der wichtigste Begriff auf dieser Seite.") +
    gloss("Agent", "Ein Modell, das nicht nur antwortet, sondern selbst Schritte ausführt — Dateien öffnen, suchen, Programme starten.") +
    gloss("API", "Die Schnittstelle, über die Programme mit dem Modell reden. Wird getrennt abgerechnet und ist für dich vorerst irrelevant.") +
    gloss("Multimodal", "Das Modell versteht nicht nur Text, sondern auch Bilder, PDFs oder Screenshots. Praktisch nützlicher, als es klingt.") +
    gloss("Fine-Tuning", "Ein Modell mit eigenen Daten nachtrainieren. Aufwendig, teuer, und für fast alles die falsche Antwort — ein guter Prompt reicht meistens.") +
    gloss("Open&nbsp;Source", "Modelle, deren Gewichte frei verfügbar sind und die man selbst betreiben kann. Meist schwächer, dafür unabhängig.") +
"""
  <div class="sp-6"></div>
  <div class="callout co-tip no-break">
    <span class="clabel">Wenn ein Begriff fehlt</span>
    <p class="small">Frag die KI selbst: <b>„Erkläre mir den Begriff X so, wie du
    ihn jemandem erklären würdest, der klug ist, aber aus einem anderen Fach
    kommt. Höchstens fünf Sätze, keine englischen
    Fachwörter ohne Übersetzung.“</b> Das funktioniert für praktisch jedes Wort,
    das dir in den nächsten Wochen begegnet.</p>
  </div>
</div>
""", anchor="glossar")
