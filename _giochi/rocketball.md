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
versione: "2.0"
data_versione: 2026-10-30
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
    file: "Rocketball_Amiga_ADF_v2.0_2026-10-30.zip"
    dimensione: "306 KB"
  - nome: "WHDLoad · remake"
    file: "Rocketball_Remake_v2.0.lha"
    dimensione: "1,3 MB"
  - nome: "WHDLoad · versione fedele"
    file: "Rocketball_v2.0.lha"
    dimensione: "723 KB"
changelog:
  - versione: "2.0"
    data: 2026-10-30
    note: |
      Rocketball for Amiga - version 2.0 (30.10.2026): what changed, both editions

      ==========================================================================================
      ROCKETBALL - THE ORIGINAL EDITION
      ==========================================================================================

      Rocketball - Amiga conversion (Massimo Bonomo 2026): what changed

      Version 2.0 (30.10.2026) - a clean break: a new engine
        Every edition of Rocketball 2.0 is rebuilt with reforge: the C64 game rewritten as C, routine
        by routine, and checked against a C64 emulator at every frame and every CPU cycle; a new
        Amiga layer for the screen, the sound, the keys and the joysticks. Nothing of the 1.x
        recompiled 6502 code is left (1.x stays on GitHub: the branch 1.x, the tag v1.1.4).
        What changes for the player:
        - Two executables for the original edition: rb for a 68020 or better (A1200, accelerators,
          PiStorm) and, new, rb_a500 for a stock A500 (68000, 1 MB). On an A500 the game now keeps
          the C64's speed (1.x ran at about 2/3): the screen shows fewer pictures a second, the game
          and the sound do not slow down. Floppy: a menu, 1 the A500 version, 2 the 68020 one.
        - The sound effects of the ball and of its bounces are audible (1.x lost them), the music
          from the C64's SID rebuilt for Paula.
        - The version on the title screen (V2.0), as before.
        - The joystick: one player in port 2 or the cursor keys + SPACE / CTRL, two players port 1
          and port 2, as in 1.x. The keys as in 1.x: BACKSPACE or R is RUN/STOP (back to the title),
          P or HELP pause, ESC or F10 quit, F1 / F3 / F5 / F7 on the title as on the C64.
        - WHDLoad: Rocketball.slave (rb, 68020: WHDLoad says so on a 68000) and RocketballA500.slave
          (rb_a500). The Rocketball DOS icon starts rb without WHDLoad, and rb_a500 on a 68000.
        What to update: everything (the WHDLoad drawer, the .lha pack, the floppy).

      Version 1.1.4 (26.10.2026)
        The music stuttered on a PiStorm under Caffeine OS: the audio interrupt also came without
        Paula asking for it, and each such call skipped a block of music. Now only Paula's real
        requests are served.

      Version 1.1.3 (26.10.2026)
        The WHDLoad packs (.lha) also have an icon that starts the game without WHDLoad: Rocketball
        DOS (and RocketballRemake DOS): on a PiStorm WHDLoad slowed the remake down in the parade.

      Version 1.1.2 (25.10.2026)
        WHDLoad: the game stayed on a black screen after WHDLoad's splash (since 1.1): the slaves
        had a version string ($VER:) that WHDLoad reads; it is gone (the version is on the splash).

      Version 1.1.1 (25.10.2026)
        One set of texts for both editions (README, LEGGIMI, CHANGES, NOVITA: the original and the
        remake together), the same in every package, so that both can live in one drawer. The
        floppy's installer copies them into both drawers. The game is unchanged.

      Version 1.1 (24.10.2026)
        The game no longer stops after about 36 minutes switched on: the emulated C64's clock ran out
        of 32 bits. Now every time is moved back together, the sound's too (its envelopes and
        voice 3's noise, the game's source of chance).
        The WHDLoad drawer's Rocketball icon now starts the game straight from AmigaDOS, also when
        WHDLoad is there: Caffeine OS runs WHDLoad games in its slow "Turtle JIT" mode on the
        PiStorm. For WHDLoad: Rocketball.slave from the Shell, or the .lha pack.
        The game's title: Rocketball, as on the C64 (Roller Ball was its Italian newsstand title).
        One floppy for both editions, the remake too: a menu at start-up (1 Rocketball, 2 the
        Remake); from the Workbench, its Install icon puts both on the hard disk.
        CHANGES.txt and NOVITA.txt in every package.
        What to update: everything (the floppy, the WHDLoad drawer, the .lha pack).

      Version 1.0.2 (21.10.2026)
        One player plays with the joystick in port 2 (the C64 game used port 1, the mouse's port on
        the Amiga); R also goes back to the title.

      Version 1.0.1 (20.10.2026)
        The credits to the original, Rocketball by IJK Software.

      Version 1.0 (20.10.2026)
        First release.

      ==========================================================================================
      ROCKETBALL REMAKE
      ==========================================================================================

      Rocketball Remake - Amiga remake (Massimo Bonomo 2026): what changed

      Remake 2.0 (30.10.2026) - a clean break: a new engine
        The remake rebuilt with reforge, like the original edition (see its 2.0): the C64 game in C,
        checked against a C64 emulator at every frame, with the remake's rules, screens, announcer
        and bikes ported on top of it. The same game to play, the same options file (rb_remake.cfg:
        the options you saved with 1.x are read).
        What changes for the player:
        - Every option works, FALL RULES too: in 1.x it never changed anything (the release always
          played its first value); now C64, REMAKE and CHARGE really change who falls.
        - The sound effects of the ball and of its bounces are audible. The announcer and the bike's
          engine on both sides of the stereo, as in 1.x.
        - The teams' colours as in 1.x (Napoli light blue, Moscow red), black between the screens.
        - The keys as in 1.x: P or HELP pause, BACKSPACE or R back to the title.
        - The options are written as soon as you leave F7 after a change, with WHDLoad too.
        - Requirements: 1 MB chip and about 1.2 MB of other memory; a stock A1200 (2 MB chip, no fast
          memory) cannot start it. With a 68020 and fast memory the game keeps its speed but shows
          about 12 pictures a second; a fast 68030, a 68040 / 68060 or a PiStorm shows them all.
        - The floppy no longer has the remake (1.3 MB: it does not fit): its .lha pack, hard disk only.

      Remake 1.1.4 (26.10.2026)
        The music stuttered on a PiStorm under Caffeine OS: the audio interrupt also came without
        Paula asking for it, and each such call skipped a block of music. Now only Paula's real
        requests are served.

      Remake 1.1.3 (26.10.2026)
        The icon RocketballRemake DOS: the remake without WHDLoad (on a PiStorm WHDLoad slowed it
        down in the parade, the music too).

      Remake 1.1.2 (25.10.2026)
        WHDLoad: no more black screen after the splash (see the original edition's 1.1.2).

      Remake 1.1.1 (25.10.2026)
        The texts shared with the original edition (see its 1.1.1). The game is unchanged.

      Remake 1.1 (24.10.2026)
        First release of the remake (numbered 1.1 like the original edition it is built on), for
        fast Amigas with 1 MB chip memory (PiStorm, 68040 / 68060, emulators with JIT). On top of
        the original game, recompiled from the C64:
        - the arena, the players and the panel redrawn; an announcer; the bikes of the film
          Rollerball at the kick-off (they tow the favoured team, the ball comes down into their
          hands) and as a power-up in play (the power bar full: hold fire; one bike at a time,
          10 seconds, it knocks the opponents down, jumping ones too);
        - new rules, each one switchable back to the C64's (F7 on the title): ball catches on
          contact, passes and shots, dash and stamina, wide goals, wall rebounds, the charge (whoever
          charges knocks the opponent down and stays up), smarter computer teams, 11 sprites (no
          player jumping to the screen's edge), the shot knocking down an opponent in its way, the
          automatic pass (fire + down with the ball);
        - both teams can be played by the computer (F5 / F6: levels 1-6), with a demo on the title;
        - the options kept on disk (rb_remake.cfg); the title's keys by the joystick too.
        Known: with both teams played by the computer at levels 1 and 3, team 1 loses a little more
        often than team 2 (it does not happen with a human in team 1).
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
