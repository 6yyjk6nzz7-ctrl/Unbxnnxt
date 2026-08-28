# -*- coding: utf-8 -*-
"""Teil E: OffCam-Beiträge, Rechts-Workstream, Arbeitsprotokoll."""
from doc import (page, set_section, kicker, fact, callout, prompt, card,
                 resource, wk, toc_row, gloss, opener)


def build_e():
    set_section("Teil 5 — Zusammen bauen")

    # ── 5.3 Fünf Beiträge ──
    page("""
<div class="flow">
  <span class="kicker">5.3 — Ohne eine Zeile Code</span>
  <h2>Was du bei OffCam<br>übernehmen könntest</h2>
  <hr class="hr-thick">

  <p class="lead">Fünf Bereiche, die über Erfolg oder Scheitern eines Produkts
  wie OffCam entscheiden — und in denen Programmierkenntnisse nichts helfen.
  Das ist ein Angebot, keine Aufgabenliste.</p>

  <div class="sp-5"></div>
  <div class="stack">
    <div class="card card-gold">
      <h4>1 &nbsp;Mit echten Menschen reden</h4>
      <p class="small">OffCam beruht auf einer Annahme: dass verifizierte Creator
      einen Ort brauchen, an dem sie einander auf Augenhöhe begegnen. Ob das
      stimmt, weiß man nach zwei Runden mit je fünf Gesprächen: Die
      Nielsen-Norman-Group hält für qualitative Tests fünf Teilnehmende für
      ausreichend und empfiehlt, lieber mehrere kleine Tests zu machen als einen
      großen.</p>
    </div>
    <div class="card card-gold">
      <h4>2 &nbsp;Die deutschen Texte</h4>
      <p class="small">Jeder Knopf, jeder Fehlerhinweis, jede leere Ansicht. Bei
      einem Produkt, das mit Diskretion und Vertrauen wirbt, ist der Ton der
      Texte kein Beiwerk, sondern das Produkt. Ein einziger unbeholfener Satz an
      der Verifizierungsstelle kostet mehr Nutzer als eine fehlende Funktion.</p>
    </div>
    <div class="card card-gold">
      <h4>3 &nbsp;Entscheiden, was das Ding <i>nicht</i> kann</h4>
      <p class="small">Die schwierigsten Fragen sind Richtlinienfragen, keine
      technischen: Was passiert bei einer Meldung? Wer entscheidet, in welcher
      Frist, und was sieht die gemeldete Person? Darf man Bilder senden?
      Diese Antworten gehören aufgeschrieben, bevor jemand sie
      programmiert — sonst entscheidet der Code, was Politik hätte sein sollen.</p>
    </div>
    <div class="card card-gold">
      <h4>4 &nbsp;Jugendschutz und Datenschutz</h4>
      <p class="small">Der größte und unangenehmste Bereich — der, der die
      meiste zusammenhängende Lesezeit braucht, und ein vollständiger,
      eigenständiger Arbeitsbereich ohne eine Zeile Code. Ausführlich ab
      Seite&nbsp;{{P:rechtoffcam}}.</p>
    </div>
  </div>
</div>
""", anchor="offcam")

    page("""
<div class="flow">
  <div class="sp-2"></div>
  <div class="stack">
    <div class="card card-gold">
      <h4>5 &nbsp;Der Blick von außen</h4>
      <p class="small">Konstantin kann das Produkt nicht mehr zum ersten Mal
      sehen. Du schon. Schreib beim ersten Durchklicken alles auf, was dich
      irritiert — auch und gerade das, was dir kleinlich vorkommt. Diesen
      ersten Blick hat man nur einmal; wann du OffCam öffnest, spielt keine
      Rolle — wichtig ist nur, dabei mitzuschreiben.</p>
    </div>
  </div>

  <div class="sp-3"></div>
  <div class="callout co-honest no-break">
    <span class="clabel">Der zweite Ausgang</span>
    <p>Wenn dich von diesen fünf Bereichen keiner reizt, ist die richtige
    Konsequenz, dass ihr dafür jemand anderen sucht oder darauf verzichtet —
    nicht, dass du einen übernimmst, weil ihn sonst niemand übernimmt.</p>
  </div>

  <div class="sp-6"></div>
  <h3>Falls doch: der kleinstmögliche erste Beitrag</h3>
  <p>Er dauert eine halbe Stunde und braucht nichts als einen Browser und einen
  Notizzettel.</p>

  <div class="sp-3"></div>
  <ol class="steps">
    <li><b>Klick dich einmal komplett durch OffCam</b> — Altersabfrage, Landing
    Page, Swipe-Deck, Chats, Profil. Ohne Kommentar von Konstantin.</li>
    <li><b>Schreib alles mit, was dich stolpern lässt.</b> Jeden Satz, den du
    zweimal lesen musst. Jeden Knopf, bei dem du nicht weißt, was passiert.
    Jede Stelle, an der du dich fragst „Sehen das jetzt andere?“.</li>
    <li><b>Sortiere die Liste nicht.</b> Roh übergeben ist wertvoller als
    aufgeräumt — die Reihenfolge, in der etwas auffällt, ist selbst eine
    Information.</li>
  </ol>

  <div class="sp-4"></div>
  <div class="callout co-tip no-break">
    <span class="clabel">Warum das mehr wert ist, als es klingt</span>
    <p class="small">Konstantin kann diesen Test nicht mehr machen. Er weiß, wo
    jeder Knopf hinführt, und sieht deshalb nicht mehr, was jemand sieht, der es
    nicht weiß. Diese Liste kann in eurem Projekt gerade nur eine Person
    schreiben.</p>
  </div>
</div>
""")

    # ── 5.4 Jugendschutz und Zahlungen ──
    page("""
<div class="flow">
  <span class="kicker">5.4 — Der Bereich, der wirklich brennt</span>
  <h2>Jugendschutz, Zahlungen,<br>App Store</h2>
  <hr class="hr-thick">

  <p class="lead">Das hier ist kein Nebenschauplatz für Schritt vier der
  Roadmap. Es sind Fragen, die über die Machbarkeit des Geschäftsmodells
  entscheiden — und sie lassen sich lesen, verstehen und aufschreiben, ohne
  zu programmieren.</p>

  <div class="sp-4"></div>
  <div class="stack">
    <div class="card card-red">
      <h4>Der Altersnachweis ist kein Klick</h4>
      <p class="small">Nach §&nbsp;4 Abs.&nbsp;2 JMStV dürfen pornografische
      Inhalte in Deutschland nur in einer <b>geschlossenen Benutzergruppe</b>
      angeboten werden. Die etablierte Praxis der KJM verlangt zwei getrennte
      Schritte: eine einmalige Identifizierung gegen eine reale Identität und
      eine Authentifizierung bei jeder weiteren Sitzung. <b>Ein Klick auf „Ich
      bin über 18“ erfüllt keinen der beiden.</b> Das aktuelle Age Gate im
      Prototyp ist rechtlich also eine Platzhalterlösung — in Ordnung, solange
      über diesen Zugang nichts öffentlich erreichbar ist, was unter §&nbsp;4
      Abs.&nbsp;2 JMStV fällt. Nicht der Prototypen-Status schützt, sondern die
      Nicht-Erreichbarkeit.</p>
      <p class="small">Ob OffCams Inhalte überhaupt als pornografisch im Sinne
      des §&nbsp;4 gelten, ist eine juristische Einordnung mit großen
      Kostenfolgen — ein Fall für eine Fachanwältin für Medienrecht.</p>
    </div>
    <div class="card card-red">
      <h4>Zahlungsabwicklung ist eine Gründungsentscheidung</h4>
      <p class="small">Stripes veröffentlichte Richtlinien schließen
      Erwachseneninhalte und -dienste aus. Spezialisierte Anbieter verlangen
      deutlich höhere Gebühren — Branchenquellen nennen hohe einstellige bis
      niedrige zweistellige Prozentsätze gegenüber rund 1,5&nbsp;% plus
      Festbetrag — dazu eine Reserve, die einen Teil des Umsatzes monatelang
      einbehält.</p>
      <p class="small"><b>Die Gefahr ist der Zeitpunkt:</b> Ein Konto läuft
      zunächst normal und wird gesperrt, sobald das Geschäftsmodell geprüft
      wird — typischerweise, wenn schon Geld fließt und Nutzer davon abhängen.
      Diese Frage gehört nach vorn, nicht ans Ende.</p>
    </div>
    <div class="card card-red">
      <h4>Der App Store hat eine ausdrückliche Regel gegen euch</h4>
      <p class="small">Richtlinie 1.1.4 schließt „<i>hookup</i>“-Apps aus.
      Richtlinie 4.3(b) akzeptiert neue Dating-Apps nur, wenn sie eine
      „bedeutsam andere oder bessere“ Erfahrung bieten. <b>Das Argument, warum
      OffCam bedeutsam anders ist, muss jemand schreiben</b> — eine Schreib- und
      Denkaufgabe, vollständig ohne Code.</p>
    </div>
  </div>

  <div class="sp-3"></div>
  <hr>
  <p class="tiny">Rechtsstand August 2026, ohne Gewähr und ausdrücklich keine
  Rechtsberatung. Die Aufgabe hier ist, den Bereich zu erschließen und die
  richtigen Fragen aufzuschreiben — nicht, ihn zu entscheiden.</p>
</div>
""", anchor="rechtoffcam")

    # ── 5.5 Warum KI hier nicht reicht ──
    page("""
<div class="flow">
  <span class="kicker">5.5 — Eine Warnung, die zum Thema gehört</span>
  <h2>Warum ihr diesen Code<br>besonders prüfen müsst</h2>
  <hr class="hr-thick">

  <p class="lead">OffCam verarbeitet Daten, aus denen sich die sexuelle
  Orientierung von Menschen ableiten lässt. Das ist nach Artikel&nbsp;9 DSGVO
  eine besondere Kategorie personenbezogener Daten — und damit ist der
  Sorgfaltsmaßstab ein anderer als bei einer Rezepte-App.</p>

  <div class="sp-4"></div>
  <div class="fact no-break">
    <div class="big">≈ 45&nbsp;%<small>der KI-generierten<br>Codebeispiele</small></div>
    <div><p>Veracode hat 2025 über hundert Sprachmodelle an achtzig
    Programmieraufgaben getestet: In rund 45&nbsp;% der Fälle führte der
    generierte Code eine Sicherheitslücke ein. Während die syntaktische
    Korrektheit binnen zwei Jahren von etwa der Hälfte auf rund 95&nbsp;% stieg,
    blieb die Sicherheitsquote praktisch unverändert — auch neuere und größere
    Modelle verbesserten sie nicht.</p>
    <span class="src">Veracode, GenAI Code Security Report 2025</span></div>
  </div>

  <div class="sp-4"></div>
  <p>Der Schluss daraus ist nicht, dass KI-geschriebener Code unbrauchbar
  wäre. Er ist: <b>ungeprüfter</b> KI-Code ist unbrauchbar für alles, was
  sensible Daten hält — also für Login, Verifizierung und genau die
  Artikel-9-Daten von OffCam.</p>

  <div class="sp-4"></div>
  <div class="callout co-warn no-break">
    <span class="clabel">Ein reales Beispiel aus derselben Branche</span>
    <p>Die norwegische Datenschutzbehörde verhängte gegen Grindr ein Bußgeld
    von rund 5,5&nbsp;Millionen Euro, weil Nutzerdaten ohne wirksame
    Einwilligung an Werbepartner gingen. Die Begründung ist die entscheidende
    Stelle: Schon die Information, <i>dass jemand die App benutzt</i>, offenbart
    die sexuelle Orientierung und ist damit eine besondere Kategorie
    personenbezogener Daten.</p>
    <p><b>Für OffCam heißt das:</b> Die Mitgliedschaft selbst ist das sensible
    Datum. Nicht erst die Chats.</p>
  </div>

  <div class="sp-4"></div>
  <div class="callout co-tip no-break">
    <span class="clabel">Was das für dich bedeutet</span>
    <p class="small">Das ist kein Grund aufzuhören — aber auch keine Aufgabe,
    die man aus Gefälligkeit übernimmt. Wer diesen Bereich übernimmt, sollte
    das ausdrücklich wollen. Und ab einem gewissen Punkt gehört eine
    Fachanwältin dazu, nicht eine engagierte Laiin.</p>
  </div>
</div>
""")

    # ── 5.6 Das Arbeitsprotokoll ──
    page("""
<div class="flow">
  <span class="kicker">5.6 — Der praktisch wichtigste Abschnitt</span>
  <h2>Wie ihr zusammen lernt,<br>ohne euch zu streiten</h2>
  <hr class="hr-thick">

  <p class="lead">Der eigene Partner als Lehrer ist eine bekannt schwierige
  Konstellation: Kompetenzgefälle, Ungeduld, und die Beziehungsdynamik sitzt mit
  am Tisch. Das lässt sich nicht auflösen, aber entschärfen.</p>

  <div class="sp-4"></div>
  <div class="callout co-warn no-break">
    <span class="clabel">Bevor du dich darauf verlässt</span>
    <p class="small">Diese Absprache gilt nur, wenn Konstantin sie liest und
    ihr zustimmt. Er hat diesen Text vorher nicht gesehen — das ist ein
    Vorschlag an euch beide, keine Zusage, die jemand für ihn gemacht hat.
    Geht sie einmal gemeinsam durch. Weil sie zum gemeinsamen Lesen gedacht
    ist, steht sie in der dritten Person.</p>
  </div>

  <div class="sp-4"></div>
  <h3>Vorschlag für eine Absprache</h3>
  <div class="sp-3"></div>
  <ul class="check">
    <li><b>Getrennt lernen, gemeinsam anwenden.</b> Marion arbeitet die vier
    Wochen allein durch — sonst wird aus Lernen sofort Zusehen.</li>
    <li><b>Einmal pro Woche 45 Minuten gemeinsam</b> — mit festem Termin, nicht
    „wenn wir mal Zeit haben“.</li>
    <li><b>Marion bestimmt das Thema dieser 45 Minuten.</b> Immer. Auch wenn
    Konstantin gerade etwas viel Spannenderes gebaut hat.</li>
    <li><b>Konstantin erklärt nur auf Nachfrage.</b> Kein Erklären von sich aus,
    kein Vorgreifen, keine Korrektur über die Schulter.</li>
    <li><b>Keine Tastatur wegnehmen.</b> Auch nicht „kurz“. Das ist die Regel,
    die am häufigsten gebrochen wird und am meisten kaputt macht.</li>
    <li><b>„Das ist doch ganz einfach“ ist gestrichen.</b> Ersatzlos.</li>
    <li><b>Nach vier Wochen reden beide über die Abbruchbedingung</b> von
    Seite&nbsp;{{P:deal}} — und Konstantin akzeptiert die Antwort, wie sie ausfällt.</li>
  </ul>

</div>
""", anchor="protokoll")

    page("""
<div class="flow">
  <div class="sp-2"></div>
  <h3>Und wenn du lieber jemand anderen fragst</h3>
  <p>Das ist nicht illoyal, sondern oft schlicht effizienter:</p>
  <ul class="clean">
    <li><b>Die KI selbst.</b> Sie wird nie ungeduldig, erklärt dieselbe Sache
    zum fünften Mal und urteilt nicht — für Anfängerfragen der am meisten
    unterschätzte Vorteil des ganzen Werkzeugs.</li>
    <li><b>Das Schreibzentrum deiner Hochschule.</b> Fast jede hat inzwischen
    eine Anlaufstelle, und sie kennt eure Prüfungsordnung.</li>
    <li><b>Eine Kommilitonin auf demselben Stand.</b> Gemeinsam anfangen ist
    leichter als hinterherlaufen.</li>
    <li><b>Die Volkshochschule vor Ort.</b> Unspektakulär, aber fast überall
    gibt es dort KI-Kurse für Anfänger — in echten Räumen, mit echten
    Menschen.</li>
  </ul>

  <div class="sp-6"></div>
  <h3>Der Satz, der die meisten Streits beendet</h3>
  <p>„Zeig es mir nicht — sag mir, wo ich nachlesen kann.“ Er verlagert die
  Erklärung von der Person auf die Sache, nimmt dem Erklärenden die Ungeduld und
  dir das Gefühl, geprüft zu werden. Er funktioniert in beide Richtungen.</p>

  <div class="sp-5"></div>
  <div class="callout co-honest no-break">
    <span class="clabel">Und wenn ihr euch trotzdem streitet</span>
    <p>Dann liegt es fast nie am Thema. Es liegt daran, dass einer von beiden
    gerade etwas erklärt, was der andere nicht gefragt hat. Das ist reparabel:
    Termin beenden, am nächsten Tag weitermachen, und beim nächsten Mal
    zuerst die Frage, dann die Antwort.</p>
  </div>
</div>
""")
