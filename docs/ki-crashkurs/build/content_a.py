# -*- coding: utf-8 -*-
"""Teil A: Cover, Vorwort, Inhalt, Teil 1 (Die Lage)."""
from doc import (page, set_section, kicker, fact, callout, prompt, card,
                 resource, wk, toc_row, gloss, opener)

STAND = "Stand: 28. August 2026"


def build_a():
    # ══════════════════ COVER ══════════════════
    page(f"""
<span class="glow glow-a"></span><span class="glow glow-b"></span>
<div>
  <div class="sign">
    <span class="sign-top">Für Marion</span>
    <span class="sign-word">OFF CAM</span>
    <span class="sign-bot">Est. 2026 · 18+</span>
  </div>
</div>
<div style="flex:1"></div>
<div>
  <h1>Künstliche&nbsp;Intelligenz,<br>ohne&nbsp;<span class="red">Verkaufs&shy;gespräch.</span></h1>
  <p class="sub">Ein ehrlicher Crashkurs — was an dem Hype dran ist,
     was&nbsp;nicht, und wie du in vier Wochen entscheiden kannst,
     ob dir das Werkzeug etwas bringt.</p>
</div>
<div style="flex:1"></div>
<div class="cover-meta">
  <span>{STAND}</span>
  <span>{{{{P:TOTAL}}}} Seiten · Deutsch</span>
</div>
""", cls="cover", pn=False, rh=False)

    # ══════════════════ VORWORT ══════════════════
    set_section("Vorwort")
    page("""
<div class="flow">
  <span class="kicker">Bevor du anfängst</span>
  <h2>Wie dieses Dokument entstanden ist</h2>
  <hr class="hr-thick">

  <p class="lead">Damit du weißt, was du in der Hand hältst: Konstantin hat es
  bei einer KI in Auftrag gegeben. Das hier ist der Auftrag, und das hier ist,
  was stattdessen daraus geworden ist.</p>

  <div class="sp-5"></div>

  <div class="callout co-warn no-break">
    <span class="clabel">Der ursprüngliche Auftrag</span>
    <p>Konstantin bat um ein Dokument, das dir klarmacht, „dass KI die Zukunft
    ist und dass Studieren keinen Sinn macht, wenn man mit KI so viel Geld
    verdienen kann“. Er wollte etwas, das überzeugt.</p>
  </div>

  <div class="sp-4"></div>

  <div class="callout co-honest no-break">
    <span class="clabel">Was wir stattdessen geschrieben haben</span>
    <p>Ein Dokument, das dich nicht überzeugen will, sondern informieren.
    Der Grund ist einfach: Die Behauptung, Studieren lohne sich nicht mehr, weil
    man mit KI so viel Geld verdient, hält der Datenlage nicht stand. Wir haben
    es geprüft — ausführlich, mit Quellen, und am Ende gegen die eigene
    Wunschvorstellung. Wer dir das ohne Zahlen erzählt, verkauft dir meistens
    etwas; die Kursindustrie tut genau das. Konstantin verkauft dir nichts — er
    hat einen Satz übernommen, der aus dieser Ecke stammt.</p>
  </div>

  <div class="sp-6"></div>

  <h3>Warum das für dich die bessere Version ist</h3>
  <p>Ein Dokument, das nur die guten Zahlen zeigt, hättest du nach zwei Seiten
  durchschaut — und danach hättest du auch dem Rest nicht mehr geglaubt. Der
  interessante Teil an KI ist ohnehin nicht das Geldversprechen. Es ist, dass du
  in wenigen Wochen Dinge tun kannst, für die du vorher jemanden gebraucht
  hättest. Das ist unspektakulärer und wahrer.</p>

  <p>Was hier drinsteht, ist geprüft. Wo eine Zahl unsicher ist, steht das dabei.
  Was wir nicht belegen konnten, haben wir gestrichen — davon gab es einiges.
  Am Ende des Dokuments findest du ein Kapitel, das dich ausdrücklich auffordert,
  drei Behauptungen daraus selbst nachzuprüfen.</p>
</div>
""")

    page("""
<div class="flow">
  <h3>Was hier ausdrücklich <span class="red">nicht</span> steht</h3>
  <div class="sp-3"></div>
  <ul class="clean">
    <li><b>Dass du dein Studium abbrechen sollst.</b> Die Daten sagen ziemlich
        deutlich das Gegenteil. Das ganze Kapitel ab Seite&nbsp;{{P:studium}} handelt davon.</li>
    <li><b>Dass du mit KI schnell Geld verdienst.</b> Der mittlere Verkäufer
        auf der Plattform Gumroad verdient 72&nbsp;Dollar im Monat.
        44&nbsp;% aller Produkte dort bringen null.
        Die Zahlen stehen ab Seite&nbsp;{{P:geldzahlen}}.</li>
    <li><b>Dass du programmieren lernen musst.</b> Auf jede KI-Entwicklerstelle
        in Deutschland kommen etwa sieben Stellen, in denen KI nur <i>angewendet</i>
        wird.</li>
    <li><b>Dass du das überhaupt tun musst.</b> Es gibt eine ausdrückliche
        Abbruchbedingung auf der nächsten Seite.</li>
  </ul>

  <div class="sp-8"></div>

  <h3>Wer „wir“ ist</h3>
  <p>Dieses Dokument wurde von Claude geschrieben, einer KI von Anthropic — auf
  Konstantins Bitte hin, aber ohne dass er den Text vorher gesehen hat. Die
  Recherche dahinter bestand aus mehreren Dutzend Websuchen, danach aus einem
  zweiten Durchgang, der jede einzelne Zahl gegen die Originalquelle prüfen
  sollte und dabei angewiesen war, alles zu widerlegen, was sich widerlegen
  lässt.</p>

  <p>Das Ergebnis dieses zweiten Durchgangs: Von 153 recherchierten Aussagen
  waren 53 sauber belegt, 46 in ihrer ursprünglichen Formulierung übertrieben,
  43 nicht überprüfbar und 11 schlicht falsch. Gedruckt wurden nur die ersten
  beiden Gruppen — die übertriebenen in entschärfter Fassung.</p>

  <div class="sp-4"></div>
  <div class="fact no-break">
    <div class="big">11<small>von 153 Aussagen<br>waren falsch</small></div>
    <div><p>Darunter Zahlen, die im Netz überall als Fakt zitiert werden. Das ist
    keine Nebenbemerkung, sondern die wichtigste Lektion des ganzen Dokuments:
    <b>Auch KI-Rechercheergebnisse muss man nachprüfen.</b> Genau das ist die
    Fähigkeit, um die es hier geht.</p>
    <span class="src">Eigene Auswertung des Rechercheprozesses zu diesem Dokument</span></div>
  </div>

  <div class="sp-5"></div>
  <p class="tiny">Alle Angaben mit Stand 28.&nbsp;August&nbsp;2026. Links können sich
  ändern; wo das wahrscheinlich ist, steht es dabei. Dieses Dokument ist keine
  Rechts-, Steuer- oder Berufsberatung.</p>
</div>
""")

    # ══════════════════ ZEITBUDGET & ABBRUCH ══════════════════
    page("""
<div class="flow">
  <span class="kicker">Der Deal</span>
  <h2>Anderthalb Stunden die Woche,<br>plus eine Stunde zum Anfangen.</h2>
  <hr class="hr-thick">

  <p class="lead">Damit das hier kein Projekt wird, das dich das ganze Semester
  begleitet und ein schlechtes Gewissen macht: Es hat einen definierten Umfang
  und einen definierten Ausstieg.</p>

  <div class="sp-5"></div>
  <div class="cols-2">
    <div class="card card-tint">
      <h4>Was es kostet</h4>
      <p class="small"><b>Erste Sitzung:</b> 60&nbsp;Minuten, wann es passt.<br>
      <b>Woche&nbsp;1:</b> fünfmal 20&nbsp;Minuten.<br>
      <b>Woche&nbsp;2–4:</b> dreimal 30&nbsp;Minuten pro Woche.<br><br>
      Macht insgesamt gut sieben Stunden. Kein Kurs, keine Anmeldung,
      keine Hausaufgaben.</p>
    </div>
    <div class="card card-tint">
      <h4>Was es an Geld kostet</h4>
      <p class="small"><b>Für alle vier Wochen: nichts.</b><br><br>
      Alles in diesem Plan geht mit einem kostenlosen Konto. Erst wenn du
      danach am Code von OffCam mitarbeiten willst, brauchst du einen
      Bezahl-Plan — das steht auf Seite&nbsp;{{P:kosten}}, und es ist ausdrücklich
      Schritt fünf, nicht Schritt eins.</p>
    </div>
  </div>

  <div class="sp-6"></div>

  <div class="callout co-tip no-break">
    <span class="clabel">Die Abbruchbedingung</span>
    <p>Wenn dir nach diesen vier Wochen keine einzige Aufgabe aus deinem echten
    Alltag leichter gefallen ist — kein Text schneller geschrieben, kein Thema
    schneller verstanden, keine Sache erledigt, vor der du dich gedrückt hast —
    dann hör auf. Das ist keine Niederlage und kein Zwischenschritt, sondern
    eine gültige Antwort. Manche Werkzeuge passen nicht zur eigenen Arbeitsweise,
    und niemand schuldet einer Technologie eine zweite Chance.</p>
  </div>

  <div class="sp-6"></div>

  <h3>Eine Sache vorweg: Du benutzt das längst</h3>
  <p>Dieses Dokument tut nicht so, als würdest du bei null anfangen. Wenn du
  schon einmal mit einem Übersetzungsprogramm gearbeitet, eine Autokorrektur
  überschrieben, einen Spamfilter erlebt oder dich über einen absurden
  Videovorschlag geärgert hast, hast du KI benutzt und ihre Grenzen gesehen.
  Was neu ist, sind nicht die Systeme. Neu ist, dass man mit ihnen reden kann,
  statt sie zu bedienen.</p>
</div>
""", anchor="deal")

    # ══════════════════ INHALT ══════════════════
    set_section("Inhalt")
    page("""
<div class="flow">
  <span class="kicker">Sechs Teile, drei Anhänge</span>
  <h2>Was drinsteht</h2>
  <hr class="hr-thick">
  <div class="sp-2"></div>
""" +
    toc_row("1", "Die Lage", "Was die Zahlen wirklich sagen — und die Studiumsfrage, ehrlich beantwortet", "{{P:teil1}}") +
    toc_row("2", "Verstehen", "Was KI ist, warum sie sich irrt, was sie nicht kann. Mit Glossar", "{{P:teil2}}") +
    toc_row("3", "Anfangen", "Die ersten 60 Minuten, der Vier-Wochen-Plan, gut prompten", "{{P:teil3}}") +
    toc_row("4", "Regeln", "KI im Studium und beim Datenschutz — bevor es teuer wird", "{{P:teil4}}") +
    toc_row("5", "Zusammen bauen", "Claude Code, OffCam, und wie ihr zusammen lernt, ohne euch zu streiten", "{{P:teil5}}") +
    toc_row("6", "Geld, ehrlich", "Die Leiter vom ersten Versuch zum ersten bezahlten Auftrag", "{{P:teil6}}") +
    toc_row("—", "Prüf mich nach", "Drei Behauptungen aus diesem Dokument, die du selbst kontrollieren sollst", "{{P:pruefmich}}") +
    toc_row("A", "Ressourcen und Quellen", "Kurse, offizielle Seiten und alles zum Nachprüfen — mit QR-Codes", "{{P:anhangA}}") +
    toc_row("B", "Prompts zum Abschreiben", "Sieben fertige Vorlagen für die Aufgaben aus Teil 3 und 5", "{{P:anhangB}}") +
    toc_row("C", "Falls es je ums Geld geht", "Krankenkasse, BAföG, Kleinunternehmerregelung", "{{P:anhangC}}") +
"""
  <div class="sp-8"></div>
  <div class="card card-dark">
    <span class="kicker">Wenn du nur zehn Minuten hast</span>
    <p class="small">Lies Seite&nbsp;{{P:studium}} („Lohnt sich Studieren
    noch?“), Seite&nbsp;{{P:halluzination}} („Der Halluzinations-Test“) und
    Seite&nbsp;{{P:ersten60}} („Die ersten 60 Minuten“). Der Rest kann
    warten.</p>
  </div>
</div>
""", anchor="toc")

    # ══════════════════ OPENER TEIL 1 ══════════════════
    set_section("Teil 1 — Die Lage")
    page(opener("1", "Die Lage",
        "Fangen wir mit der Zahl an, die dir jeder zuerst zeigt — und danach "
        "mit der, die fast nie danebensteht.",
        [("Die 62-Prozent-Zahl", "und was sie nicht bedeutet"),
         ("Der deutsche Markt", "nüchtern betrachtet"),
         ("Was Arbeitgeber suchen", "acht von zehn sind keine Technik"),
         ("Lohnt sich Studieren noch?", "die ehrliche Antwort"),
         ("Was wir nicht wissen", "offene Fragen")]),
        cls="opener", rh=False, anchor="teil1")

    # ── 1.1 Die zwei Zahlen ──
    page("""
<div class="flow">
  <span class="kicker">1.1 — Die Zahl und die Gegenzahl</span>
  <h2>Erst die Ernüchterung,<br>dann die Chance</h2>
  <hr class="hr-thick">

  <p class="lead">In fast jedem Artikel über KI und Gehalt taucht eine große
  Prozentzahl auf. Wir zeigen sie dir — aber erst, nachdem du die Zahl gesehen
  hast, die meistens weggelassen wird.</p>

  <div class="sp-5"></div>

  <div class="fact no-break">
    <div class="big">55&nbsp;%<small>der Arbeitgeber<br>zahlen nichts extra</small></div>
    <div><p>Payscale hat 2026 Unternehmen gefragt, was sie für aufgebaute
    KI-Kompetenzen tatsächlich bezahlen. 55&nbsp;% zahlen weder Aufschlag noch
    Bonus noch Beteiligung. 14&nbsp;% zahlen ein höheres Grundgehalt, 10&nbsp;%
    Boni. Gleichzeitig haben 61&nbsp;% der Organisationen ihre Rollenprofile um
    KI-Kompetenzen erweitert. Übersetzt: <b>Es wird erwartet, aber nicht
    vergütet.</b></p>
    <span class="src">Payscale Compensation Best Practices Report 2026, 24.02.2026</span></div>
  </div>

  <div class="sp-4"></div>

  <div class="fact no-break">
    <div class="big">62&nbsp;%<small>Aufschlag in KI-<br>Stellenanzeigen</small></div>
    <div><p>Das ist die berühmte Zahl. PwC hat über eine Milliarde Stellenanzeigen
    aus 27&nbsp;Ländern ausgewertet: Anzeigen, die KI-Kompetenzen nennen, bieten
    im Schnitt 62&nbsp;% mehr Gehalt als Anzeigen, die das nicht tun
    (2025: 57&nbsp;%, 2024: 25&nbsp;%). Die Spannbreite reicht von 118&nbsp;% in
    konsumnahen Rollen bis 16&nbsp;% im öffentlichen Dienst.</p>
    <span class="src">PwC 2026 Global AI Jobs Barometer, 15.06.2026</span></div>
  </div>

  <div class="sp-5"></div>

  <div class="callout co-warn no-break">
    <span class="clabel">Warum die 62 % nicht heißen, was sie zu heißen scheinen</span>
    <p>Verglichen werden <i>Anzeigen</i>, nicht Menschen. Es wurde niemand
    beobachtet, der vorher kein KI-Wissen hatte und nachher schon. Es wurde nicht
    kontrolliert, ob diese Stellen ohnehin seniorer, technischer oder besser
    bezahlt sind — was sie meistens sind. Ein großer Teil der Prämie misst
    vermutlich, welche <i>Art</i> von Stelle KI erwähnt, und nicht, was KI-Wissen
    einbringt. Du bekommst also nicht 62&nbsp;% mehr Gehalt, weil du einen Kurs
    machst.</p>
  </div>
</div>
""")

    # ── 1.2 Prämien verschwinden ──
    page("""
<div class="flow">
  <span class="kicker">1.2 — Der Beweis, dass Prämien verschwinden</span>
  <h2>Der deutsche Finanzsektor</h2>
  <hr class="hr-thick">

  <p>Es gibt in den PwC-Daten eine Branche, in der die KI-Prämie in Deutschland
  <b>negativ</b> ist: den Finanzsektor, mit &minus;9&nbsp;%. Und zwar
  ausgerechnet die Branche, in der 97,3&nbsp;% aller KI-Stellen reine
  Anwenderrollen sind — also die Branche, die KI am selbstverständlichsten
  benutzt.</p>

  <p>PwC nennt als mögliche Erklärung, dass KI-Kompetenz dort inzwischen
  <b>Standardanforderung</b> ist. Und dafür zahlt niemand einen Aufpreis. Man
  bekommt schließlich auch keinen Zuschlag mehr dafür, E-Mails schreiben zu
  können.</p>

  <div class="sp-4"></div>
  <div class="callout co-honest no-break">
    <span class="clabel">Die eigentliche Lehre</span>
    <p>Eine Lohnprämie ist ein <b>Knappheitspreis</b>, kein Naturgesetz. Sie
    existiert, solange wenige es können, und verschwindet, wenn es alle können.
    In den meisten anderen deutschen Branchen liegt sie über 20&nbsp;%, in
    Energie, Versorgung und Rohstoffen bei bis zu 39&nbsp;% — bei den
    professionellen Dienstleistungen dagegen trotz hoher KI-Exponierung nur bei
    13&nbsp;%. Der Finanzsektor zeigt, wo das endet.</p>
    <p><b>Was das nicht ist:</b> ein Grund zur Eile. Wenn jemand dir sagt, du
    müsstest „jetzt sofort einsteigen, bevor das Fenster zugeht“, verkauft er dir
    einen Kurs. Was hier steht, ist bloß: Der Aufpreis ist vorübergehend, der
    Nutzen für deine eigene Arbeit nicht.</p>
  </div>

  <div class="sp-6"></div>
  <h3>Und wie groß ist der KI-Arbeitsmarkt in Deutschland überhaupt?</h3>
  <div class="sp-3"></div>
  <table>
    <tr><th>Kennzahl</th><th>Deutschland 2025</th></tr>
    <tr><td>Anteil KI-bezogener Stellenanzeigen</td><td class="n">1,3&nbsp;%</td></tr>
    <tr><td>Absolut</td><td class="n">≈ 125.000 Anzeigen</td></tr>
    <tr><td>In Technologie, Medien, Telekom</td><td class="n">über 6&nbsp;%</td></tr>
    <tr><td>Anwenderrollen (KI benutzen)</td><td class="n">≈ 109.400</td></tr>
    <tr><td>Entwicklerrollen (KI bauen)</td><td class="n">≈ 15.400</td></tr>
    <tr><td>Verhältnis Anwender zu Entwickler</td><td class="n">rund 7 : 1</td></tr>
  </table>
  <div class="sp-3"></div>
  <p class="tiny">PwC Deutschland, Auswertung 2025. —
  Ein zweiter Messwert, der Indeed-KI-Tracker, kommt für Ende 2025 auf 3,5&nbsp;%.
  Der Unterschied ist kein Widerspruch, sondern eine andere Definition davon,
  was als „KI-Stelle“ zählt. Wo zwei seriöse Quellen unterschiedlich messen,
  sollte man beide Zahlen kennen und keiner allein glauben.</p>
</div>
""")

    # ── 1.3 Zwei Lesarten ──
    page("""
<div class="flow">
  <span class="kicker">1.3 — Dieselbe Zahl, zwei Lesarten</span>
  <h2>1,3 Prozent</h2>
  <hr class="hr-thick">
  <div class="sp-2"></div>

  <div class="cols-2u">
    <div class="card card-red">
      <h4>Die skeptische Lesart</h4>
      <p class="small"><b>98,7&nbsp;% der deutschen Stellenanzeigen erwähnten
      2025 keine KI.</b></p>
      <p class="small">Wer den Eindruck hat, dass gerade der ganze Arbeitsmarkt
      umgebaut wird, liest zu viel LinkedIn. PwC misst zwischen der
      KI-Exponierung eines Berufs und dem tatsächlichen Kompetenzwandel in
      Deutschland eine Korrelation von 0,02 — praktisch null. Der deutsche
      Markt bewegt sich deutlich langsamer, als die Schlagzeilen suggerieren.</p>
    </div>
    <div class="card card-gold">
      <h4>Die andere Lesart</h4>
      <p class="small"><b>Deutschland ist bei neuen KI-Jobtiteln
      europäischer Spitzenreiter.</b></p>
      <p class="small">Im ersten Quartal 2026 zählte Indeed hier 288&nbsp;Jobtitel,
      in denen KI ausdrücklich im Mittelpunkt der Tätigkeit steht — vor
      Großbritannien&nbsp;(160) und Frankreich&nbsp;(138). Und 59&nbsp;% dieser
      Titel liegen <b>außerhalb</b> des Tech-Sektors. In Marketing, Personal und
      Projektmanagement wächst die Nachfrage nach KI-Kompetenzen um bis zu
      138,7&nbsp;% — während die Gesamtzahl der Anzeigen dort zurückgeht.</p>
    </div>
  </div>

  <div class="sp-6"></div>
  <p class="big-quote">Beides stimmt. Der ehrliche Satz lautet nicht
  „KI&nbsp;verändert alles“, sondern: In einem insgesamt schrumpfenden Stellenmarkt
  ist der KI-nahe Teil einer der wenigen, die wachsen.
  <span class="q-attr">Zusammenfassung der Datenlage, PwC / Indeed Hiring Lab 2026</span></p>

  <div class="sp-6"></div>
  <p>Der deutsche Stellenmarkt liegt insgesamt rund ein Drittel unter seinem
  Höchststand vom Frühjahr 2022. Betroffen sind vor allem Büro- und
  Wissensberufe. Das ist der nüchterne Grund, sich das Thema anzusehen — und
  ausdrücklich kein Versprechen auf mehr Gehalt.</p>
</div>
""")

    # ── 1.4 Was Arbeitgeber wirklich suchen ──
    page("""
<div class="flow">
  <span class="kicker">1.4 — Was in den Anzeigen wirklich verlangt wird</span>
  <h2>Acht von zehn gesuchten Fähigkeiten<br>sind keine Technik</h2>
  <hr class="hr-thick">

  <p class="lead">Das ist der wichtigste Befund für dich, und er kommt aus der
  Auswertung von über 1,3&nbsp;Milliarden Stellenanzeigen.</p>

  <div class="sp-4"></div>
  <div class="fact no-break">
    <div class="big">8 / 10<small>gefragteste Skills<br>in KI-Anzeigen</small></div>
    <div><p>Von den zehn Kompetenzen, die in KI-Stellenanzeigen am häufigsten
    verlangt werden, sind acht menschliche Fähigkeiten, darunter Kommunikation,
    Management und Führung. Nur zwei sind technische KI-Fähigkeiten. Arbeitgeber,
    die KI-Kompetenz suchen, suchen überwiegend Menschen, die denken, schreiben
    und mit Menschen umgehen können — und außerdem KI bedienen.</p>
    <span class="src">Lightcast, „Beyond the Buzz“, Juli 2025</span></div>
  </div>

  <div class="sp-5"></div>
  <h3>Warum das die Frage nach dem Studium schon halb beantwortet</h3>
  <p>Genau solche Fähigkeiten trainiert ein Studium. Ein Seminar, in dem du
  eine These verteidigen musst, ist Training in Argumentation. Eine Hausarbeit
  ist Training in Recherche, Strukturierung und Schreiben. Eine Gruppenarbeit
  ist — bei aller Qual — Training in Koordination.</p>
  <p>Das Studium ist also nicht das Gegenteil von KI-Kompetenz. Es ist die
  Hälfte davon. Die andere Hälfte ist das Werkzeug, und das ist der Teil, den
  man in Wochen lernt statt in Jahren.</p>

  <div class="sp-5"></div>
  <div class="callout co-tip no-break">
    <span class="clabel">Die praktische Konsequenz</span>
    <p>Der Satz, der aus der gesamten Recherche am robustesten hervorgeht:
    <b>Fachwissen plus KI schlägt KI allein.</b> Bezahlt wird nicht dafür, dass
    jemand ein Werkzeug bedienen kann — 85&nbsp;% der deutschen Freelancer tun
    das bereits. Bezahlt wird dafür, dass jemand beurteilen kann, ob das
    Ergebnis stimmt. Und das kann nur, wer vom Thema etwas versteht.</p>
  </div>
</div>
""")
