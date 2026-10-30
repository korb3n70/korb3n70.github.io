---
title: Forbidden Forest
piattaforma: Amiga 500
anno_originale: 1983
order: 2
sommario: >-
  L'horror di Paul Norman del 1983 portato su Amiga in tre edizioni: due
  fedeli al pixel e un remake a schermo pieno con cielo in parallasse.
requisiti: >-
  Versione fedele: Amiga 500 con 512 KB chip + 512 KB di altra memoria.
  Versione veloce e remake: Amiga con scheda acceleratrice, PiStorm o
  emulatore con JIT.

# >>> da qui in giu' scrive sync-giochi.py: non modificare a mano
versione: "1.2.3"
data_versione: 2026-10-26
cartella: forbidden-forest
repo: "korb3n70/forbidden-forest-amiga"
schermate:
  - file: /assets/img/giochi/forbidden-forest/forbidden_forest_amiga_purist_1_cosmi.png
  - file: /assets/img/giochi/forbidden-forest/forbidden_forest_amiga_purist_2_title_paul_norman.png
  - file: /assets/img/giochi/forbidden-forest/forbidden_forest_amiga_purist_3_gameplay_spider.png
  - file: /assets/img/giochi/forbidden-forest/forbidden_forest_amiga_remake_1_cosmi.png
  - file: /assets/img/giochi/forbidden-forest/forbidden_forest_amiga_remake_2_title_paul_norman.png
  - file: /assets/img/giochi/forbidden-forest/forbidden_forest_amiga_remake_3_gameplay_spider.png
download:
  - nome: "WHDLoad · versione veloce"
    file: "ForbiddenForestFast_v1.2.3.lha"
    dimensione: "114 KB"
  - nome: "WHDLoad · remake"
    file: "ForbiddenForestRemake_v1.2.3.lha"
    dimensione: "166 KB"
  - nome: "Dischetti ADF (floppy o emulatore)"
    file: "ForbiddenForest_Amiga_ADF_v1.2.3_2026-10-26.zip"
    dimensione: "453 KB"
  - nome: "WHDLoad · versione fedele"
    file: "ForbiddenForest_v1.2.3.lha"
    dimensione: "112 KB"
changelog:
  - versione: "1.2.3"
    data: 2026-10-26
    note: |
      Forbidden Forest 1.2.3 (26.10.2026): the music no longer stutters on a PiStorm under Caffeine OS (fast and remake versions). The audio interrupt also came without Paula asking for it and each such call skipped a block of music; now only Paula's real requests are served.

      - `ForbiddenForest_v1.2.3.lha` -> `ForbiddenForest/` (unchanged layout)
      - `ForbiddenForestFast_v1.2.3.lha` -> `ForbiddenForestFast/` (unchanged layout)
      - `ForbiddenForestRemake_v1.2.3.lha` -> `ForbiddenForestRemake/` (unchanged layout)

      Nothing renamed or moved. Files in more than one drawer, identical byte for byte: README.txt, LEGGIMI.txt, CHANGES.txt, NOVITA.txt.
  - versione: "1.2.2"
    data: 2026-10-26
    note: |
      Forbidden Forest 1.2.2 (26.10.2026): the game unchanged; the fast versions' WHDLoad packs also have an icon that starts the game without WHDLoad (on a PiStorm WHDLoad slows the games down).

      - `ForbiddenForest_v1.2.2.lha` -> `ForbiddenForest/` (unchanged layout)
      - `ForbiddenForestFast_v1.2.2.lha` -> `ForbiddenForestFast/`: + **ForbiddenForestFast DOS** and its .info (IconX, no WHDLoad)
      - `ForbiddenForestRemake_v1.2.2.lha` -> `ForbiddenForestRemake/`: + **ForbiddenForestRemake DOS** and its .info (IconX, no WHDLoad)

      New files only, nothing renamed or moved. Files in more than one drawer, identical byte for byte (checked): README.txt, LEGGIMI.txt, CHANGES.txt, NOVITA.txt.
  - versione: "1.2.1"
    data: 2026-10-25
    note: |
      Forbidden Forest 1.2.1 (25.10.2026): the game unchanged; the WHDLoad slaves without a $VER: string (WHDLoad can stop on it at a black screen). Use this one instead of 1.2.

      - `ForbiddenForest_v1.2.1.lha` -> `ForbiddenForest/`
      - `ForbiddenForestFast_v1.2.1.lha` -> `ForbiddenForestFast/`
      - `ForbiddenForestRemake_v1.2.1.lha` -> `ForbiddenForestRemake/`

      The version: 5 s on the bottom line at the start, on WHDLoad's splash, `Version ff FULL` (ff, ff_fast, ff_remake). Nothing renamed or moved since 1.2.
  - versione: "1.2"
    data: 2026-10-25
    note: |
      Forbidden Forest 1.2 (22.10.2026): three versions.

      WHDLoad packs (the usual layout: <Name>.info + the drawer <Name>/ with the slave, the icon, the game, README / LEGGIMI / CHANGES / NOVITA):
      - `ForbiddenForest_v1.2.lha` -> `ForbiddenForest/` (the purist edition for the A500: run ff)
      - `ForbiddenForestFast_v1.2.lha` -> `ForbiddenForestFast/` (the purist edition for fast Amigas: ff_fast)
      - `ForbiddenForestRemake_v1.2.lha` -> `ForbiddenForestRemake/` (the remake: ff_remake)

      The version: `Version <file> FULL` on ff, ff_fast, ff_remake and the slaves; on screen on the OSD line for 5 s at the start, in the CLI banner, in WHDLoad's splash.
      The game writes no files.

      First release published as a GitHub Release; nothing renamed since (the earlier tags had no packs).
---
Certi giochi si ricordano per come si giocano. **Forbidden Forest** (Cosmi,
1983) si ricorda per come ti faceva *sentire*.

Su un Commodore 64 Paul Norman mise in piedi qualcosa che nessuno aveva ancora
visto: una foresta che respira, con il cielo che passa dal giorno al tramonto
alla notte stellata, sfondi in parallasse, ragni giganti, api, rane, draghi, un
serpente e scheletri che escono dalla terra. E in fondo il Demogorgone, che non
si vede finché un lampo non lo illumina. Era cinematografico, violento e
davvero spaventoso anni prima che qualcuno parlasse di *survival horror*.

## Perché proprio questo

L'ho affrontato per ammirazione verso Paul Norman. Il suo colpo di genio non fu
tecnico ma emotivo: costruire un'atmosfera e un impatto da film dentro i limiti
di una macchina a 8 bit. Convertirlo significa avere a che fare con un'opera in
cui ogni elemento serviva a una cosa sola, la tensione: il ciclo giorno-notte,
la parallasse, la violenza esplicita.

Musica ed effetti pesano quanto il resto, e li compose lui stesso sul SID.
Conservarli per davvero, compreso il ronzio minaccioso delle api, è il modo
migliore di rendergli omaggio.

## Fedeltà al codice originale

Il principio è lo stesso del mio port di Wizard of Wor: la logica di gioco non
si reinterpreta mai. Il codice 6502 è stato **ricompilato staticamente** in
68000 nativo, quindi tradotto e non emulato: gli stessi mostri, gli stessi
schemi, gli stessi tempi al ciclo di clock.

A dimostrarlo c'è una prova in *lockstep*: il codice ricompilato gira fianco a
fianco con un C64 di riferimento, fotogramma dopo fotogramma, confrontando
memoria, registri e cicli attraverso ogni mostro e ogni fase. Copre tutte le
routine del gioco.

Solo tre cose sono cambiate di proposito, tutte per comodità di chi gioca:

- la **danza di fine ondata** dura 12 secondi invece di 28;
- l'**esplosione finale del Demogorgone** dura 10 secondi invece di 31;
- il **suono della freccia a segno**, che nell'originale era debole, è stato
  rifatto con rumore del SID filtrato.

## L'audio

- **Registrato dal SID**: le tre voci sono ricostruite da registrazioni di un
  6581 (reSID), con forme d'onda a banda limitata.
- **Suonato da Paula sull'A500**: ogni voce del SID gira in loop su un canale
  hardware. La musica resta intonata, non costa quasi nulla al processore e non
  si interrompe nemmeno quando sullo schermo succede di tutto.
- **Miscelato a 28 kHz** nelle edizioni per Amiga veloci.

## Tre edizioni

**Fedele (A500)** e **Fedele veloce**: grafica e gioco originali come li
disegnò Paul Norman, ma la foresta scorre liscia invece di saltare di otto
pixel per volta, e l'arciere usa gli sprite hardware dell'Amiga.

**Remake**: grafica nuova a schermo pieno (368 × 256, senza bordi) nello stile
di *Another World*, tre piani in parallasse, un cielo vivo che passa dal giorno
al tramonto alla notte, la luna che attraversa il cielo dietro agli alberi e ai
lampi, i mostri che passano dietro gli oggetti della foresta, e un pannello più
leggibile con le frecce rimaste nella faretra e le vite accanto a un cuore
rosso. L'arciere è quello originale, con tutte le sue animazioni, ricolorato
per il mondo nuovo.
