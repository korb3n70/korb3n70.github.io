---
title: Rocketball
piattaforma: Amiga 500
anno_originale: 1985
order: 3
sommario: >-
  Lo sport violento su pattini del Commodore 64, ricompilato per Amiga.
  Più un remake con grafica nuova, radiocronista, le moto e regole rivedute.
requisiti: >-
  Versione fedele: Amiga con 512 KB chip + 512 KB di altra memoria, 68020 o
  superiore, Kickstart 1.3. Remake: 1 MB chip e circa 2 MB in tutto, e un
  Amiga veloce (PiStorm, schede acceleratrici, emulatori con JIT).

# >>> da qui in giu' scrive sync-giochi.py: non modificare a mano
versione: "1.1.4"
data_versione: 2026-10-26
cartella: rocketball
repo: "korb3n70/rollerball-amiga"
schermate:
  - file: /assets/img/giochi/rocketball/rocketball_amiga_1_title.png
  - file: /assets/img/giochi/rocketball/rocketball_amiga_2_play.png
  - file: /assets/img/giochi/rocketball/rocketball_amiga_3_kickoff.png
  - file: /assets/img/giochi/rocketball/rocketball_amiga_4_bike_in_play.png
  - file: /assets/img/giochi/rocketball/rocketball_amiga_5_options.png
download:
  - nome: "Dischetti ADF (floppy o emulatore)"
    file: "Rocketball_Amiga_ADF_v1.1.4_2026-10-26.zip"
    dimensione: "542 KB"
  - nome: "WHDLoad · remake"
    file: "Rocketball_Remake_v1.1.4.lha"
    dimensione: "544 KB"
  - nome: "WHDLoad · versione fedele"
    file: "Rocketball_v1.1.4.lha"
    dimensione: "254 KB"
changelog:
  - versione: "1.1.4"
    data: 2026-10-26
    note: |
      Rocketball 1.1.4 (26.10.2026): the music no longer stutters on a PiStorm under Caffeine OS. The audio interrupt also came without Paula asking for it and each such call skipped a block of music; now only Paula's real requests are served.

      - `Rocketball_v1.1.4.lha` -> `Rocketball/` (unchanged layout)
      - `Rocketball_Remake_v1.1.4.lha` -> `RocketballRemake/` (unchanged layout)

      Nothing renamed or moved. Files in both drawers, identical byte for byte (checked): README.txt, LEGGIMI.txt, CHANGES.txt, NOVITA.txt.
  - versione: "1.1.3"
    data: 2026-10-26
    note: |
      Rocketball 1.1.3 (26.10.2026): the game unchanged; each WHDLoad pack also has an icon that starts the game without WHDLoad (on a PiStorm WHDLoad slowed the remake down in the parade, the music too).

      - `Rocketball_v1.1.3.lha` -> `Rocketball/`: Rocketball.slave, Rocketball.info (WHDLoad), rb, **Rocketball DOS** + Rocketball DOS.info (IconX, no WHDLoad)
      - `Rocketball_Remake_v1.1.3.lha` -> `RocketballRemake/`: RocketballRemake.slave, RocketballRemake.info (WHDLoad), rb_remake, **RocketballRemake DOS** + RocketballRemake DOS.info (IconX, no WHDLoad)

      New files only, nothing renamed or moved. Files in both drawers, identical byte for byte (checked): README.txt, LEGGIMI.txt, CHANGES.txt, NOVITA.txt.
  - versione: "1.1.2"
    data: 2026-10-25
    note: |
      Rocketball 1.1.2 (25.10.2026): fixes WHDLoad (a black screen after WHDLoad's splash in 1.1 / 1.1.1: the slaves' $VER: string, removed). Use this one instead of 1.1 and 1.1.1.

      - `Rocketball_v1.1.2.lha` -> `Rocketball/` (Rocketball.slave, Rocketball.info, rb)
      - `Rocketball_Remake_v1.1.2.lha` -> `RocketballRemake/` (RocketballRemake.slave, RocketballRemake.info, rb_remake)

      Files in both drawers, identical byte for byte (checked): README.txt, LEGGIMI.txt, CHANGES.txt, NOVITA.txt.
      The version: on the title (top right), on WHDLoad's splash (the slave's name and info), `Version rb FULL` / `Version rb_remake FULL`. The slaves carry no $VER: string (WHDLoad stopped on it).
      Nothing renamed or moved since 1.1.1.
  - versione: "1.1.1"
    data: 2026-10-25
    note: |
      Superseded by v1.1.2: with WHDLoad this version stays on a black screen after the splash (the slaves' $VER: string). Use v1.1.2.
  - versione: "1.1"
    data: 2026-10-25
    note: |
      Rocketball 1.1 (24.10.2026): the original edition and the Remake.

      WHDLoad packs (the usual layout: <Name>.info + the drawer <Name>/ with the slave, the icon, the game, README / LEGGIMI / CHANGES / NOVITA):
      - `Rocketball_v1.1.lha` -> `Rocketball/` (the original edition: 68020 or better, OCS / ECS / AGA)
      - `Rocketball_Remake_v1.1.lha` -> `RocketballRemake/` (the remake: 1 MB chip, a fast Amiga)

      The version: `Version <file> FULL` on rb, rb_remake and the slaves; on screen at the title's top right, in WHDLoad's splash.
      Files the game writes: `rb_remake.cfg` (the remake's options), not in the packs.

      First release published as a GitHub Release; nothing renamed since (the earlier v1.0* tags had no packs).
---
Due squadre da cinque pattinatori corrono su una pista inclinata. Una palla
d'acciaio. Si segna infilandola nella porta ricavata nel muro, e si ferma
l'avversario in qualunque modo: gomitate, cariche e, nel remake, le moto.

**Rocketball** uscì nel 1985 per Commodore 64, scritto da John Sinclair per la
IJK Software con le musiche di L. Pilling. In Italia arrivò in edicola come
*Roller Ball*. L'ispirazione è dichiarata: il film *Rollerball* del 1975.

Qui trovi due edizioni nello stesso pacchetto: l'originale ricompilato e un
remake che cambia pelle ma non motore.

## L'edizione originale

Il codice 6502 del C64 è stato **ricompilato staticamente** in codice 68000
nativo. Non è emulazione: l'Amiga esegue il programma della IJK Software
tradotto istruzione per istruzione, con le stesse regole, gli stessi tempi e
gli stessi avversari. Durante lo sviluppo il risultato è stato confrontato
fotogramma per fotogramma con un emulatore C64.

- La grafica originale, intatta.
- L'audio ricostruito dalle tre voci del SID, registrate da un 6581 con reSID e
  miscelate a 28 kHz.
- Uno contro il computer (livelli 1-6) oppure due giocatori con due joystick.

## Il remake

Il remake tiene come motore lo stesso gioco ricompilato e cambia tutto quello
che si vede e si tocca.

**L'aspetto**: arena, pubblico, pattinatori e pannello ridisegnati a schermo
pieno (256 righe), quattro squadre con i loro colori (Tokyo, Napoli, Madrid,
Mosca), un radiocronista che commenta l'azione e un radar di tutta la pista.

**Le moto**: dopo un gol due moto trainano in pista la squadra che l'ha subìto,
e la palla scende al primo pattinatore trainato. In partita la barra di
potenza si riempie in due minuti: quando è piena, tieni premuto il fuoco e
arriva la tua moto, che per dieci secondi stende ogni avversario a tiro senza
mai toccare i compagni. Anche le squadre del computer chiamano la loro, e in
pista ce n'è sempre una sola.

**Le regole**: la palla si prende al contatto e non solo accucciandosi;
fuoco più sinistra passa, fuoco più destra tira in porta, fuoco più giù cerca
da solo il compagno libero; il fuoco da solo dà uno scatto che consuma la
resistenza della squadra. Porte più larghe, rimbalzi sul muro, la carica che
stende chi va più piano, difesa a zona che si sposta, un portiere e le scorte
al portatore.

Ogni novità si può **riportare com'era sul C64** dalla pagina delle opzioni
(F7 sulla schermata del titolo), una per una o tutte insieme.
