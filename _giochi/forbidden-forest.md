---
order: 2

# >>> da qui in giu' scrive sync-giochi.py: non modificare a mano
title: "Forbidden Forest"
piattaforma: "Amiga"
originale: "Commodore 64, Cosmi, 1983 (Paul Norman)"
anno_originale: 1983
sommario: >-
  Paul Norman's 1983 C64 horror masterpiece on the Amiga: two purist editions, recompiled from
  the original code and faithful to the last pixel, and a remake with new graphics, a living sky
  and three planes of parallax.
requisiti: >-
  Purist (A500): 512 KB chip + 512 KB. Fast: the same and a fast CPU. Remake: 1 MB chip (ECS
  Agnus) + 1 MB fast and a fast CPU (68030 or better, PiStorm); with WHDLoad 512 KB chip + 1.2 MB
  fast. Kickstart 1.3 or later, OCS / ECS / AGA.
release_url: "https://github.com/korb3n70/forbidden-forest-amiga/releases/tag/v2.0"
compat:
  machines:
    - id: "ocs_4mb"
      name: "Amiga OCS/ECS, 4 MB"
    - id: "ocs_8mb"
      name: "Amiga OCS/ECS, 8 MB"
    - id: "a1200_4mb"
      name: "Amiga 1200, 4 MB, CPU di serie"
    - id: "a1200_8mb"
      name: "Amiga 1200, 8 MB, CPU di serie"
    - id: "pistorm"
      name: "Amiga con PiStorm"
    - id: "thea500mini"
      name: "THEA500 Mini"
    - id: "thea1200"
      name: "THEA1200"
  editions:
    - name: "ForbiddenForestFast"
      cells:
        - machine: "ocs_4mb"
          status: "untested"
          offer: "2.0"
          why: ""
          note: "non provato su questa macchina"
        - machine: "ocs_8mb"
          status: "untested"
          offer: "2.0"
          why: ""
          note: "non provato su questa macchina"
        - machine: "a1200_4mb"
          status: "untested"
          offer: "2.0"
          why: ""
          note: "non provato su questa macchina"
        - machine: "a1200_8mb"
          status: "untested"
          offer: "2.0"
          why: ""
          note: "non provato su questa macchina"
        - machine: "pistorm"
          status: "untested"
          offer: "2.0"
          why: "prova a occhio passata su una macchina vera; manca la misura delle immagini al secondo su questa macchina"
          note: "non provato su questa macchina"
        - machine: "thea500mini"
          status: "untested"
          offer: "2.0"
          why: ""
          note: "non provato su questa macchina"
        - machine: "thea1200"
          status: "untested"
          offer: "2.0"
          why: ""
          note: "non provato su questa macchina"
    - name: "ForbiddenForestRemake"
      cells:
        - machine: "ocs_4mb"
          status: "untested"
          offer: "2.0"
          why: "richiede piu' di 512 KB di memoria chip (con 512 KB: no); con 1 MB di chip o piu' da misurare."
          note: "non provato su questa macchina"
        - machine: "ocs_8mb"
          status: "untested"
          offer: "2.0"
          why: "come con 4 MB: piu' di 512 KB di chip richiesti, da misurare"
          note: "non provato su questa macchina"
        - machine: "a1200_4mb"
          status: "no"
          offer: "1.2.3"
          why: "12-18 immagini al secondo contro le 25 del traguardo: l'edizione richiede un 68030 o superiore"
        - machine: "a1200_8mb"
          status: "no"
          offer: "1.2.3"
          why: "come con 4 MB: la memoria non cambia la CPU di serie (68EC020), 12-18 immagini al secondo contro 25"
        - machine: "pistorm"
          status: "untested"
          offer: "2.0"
          why: "prova a occhio su una macchina vera con un difetto aperto: una fascia sul bordo destro dell'immagine (difetto del display di reforge, in correzione sul ramo ff-fascia-destra); manca anche la misura delle immagini al secondo"
          note: "non provato su questa macchina"
        - machine: "thea500mini"
          status: "untested"
          offer: "2.0"
          why: ""
          note: "non provato su questa macchina"
        - machine: "thea1200"
          status: "untested"
          offer: "2.0"
          why: ""
          note: "non provato su questa macchina"
older_downloads:
  - file: "ForbiddenForestRemake_v1.2.3.lha"
    version: "1.2.3"
    edition: "ForbiddenForestRemake"
    bytes: 170371
    machines: ["a1200_4mb", "a1200_8mb"]
  - file: "ForbiddenForest_v1.2.3.lha"
    version: "1.2.3"
    edition: "ForbiddenForest"
    bytes: 114545
    machines: []
    note: "edizione non rifatta da reforge: port 1.2.3 fatto a mano (repo forbidden-forest), non reforge"
  - file: "ForbiddenForest_Amiga_ADF_v1.2.3_2026-10-26.zip"
    version: "1.2.3"
    edition: ""
    bytes: 464102
    machines: []
    note: "i dischetti della 1.2.3"
versione: "2.0"
data_versione: 2026-11-20
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
  - nome: "Purist edition for fast Amigas, WHDLoad pack"
    file: "ForbiddenForestFast_v2.0.lha"
    dimensione: "261 KB"
    descrizione: "the original game with the sound mixed at 28 kHz; WHDLoad, or the DOS icon without WHDLoad"
  - nome: "Remake, WHDLoad pack"
    file: "ForbiddenForestRemake_v2.0.lha"
    dimensione: "710 KB"
    descrizione: "new graphics, a living sky, three planes of parallax; fast Amigas (68030 or better, PiStorm); WHDLoad, or the DOS icon without WHDLoad"
  - nome: "Floppies"
    file: "ForbiddenForest_Amiga_ADF_v2.0_2026-11-20.zip"
    dimensione: "354 KB"
    descrizione: "one bootable ADF per edition (Fast and Remake), the readme files and INSTRUCTIONS.md"
changelog:
  - versione: "2.0"
    data: 2026-11-20
    note: |
      One version for every platform: Amiga, Windows and, new, the Mac.

      **Amiga: ForbiddenForestFast and ForbiddenForestRemake are now made with reforge.** The C64 game is translated
      routine by routine into portable C and checked against the original running in a C64 emulator. Before, the Amiga had
      a 68000 recompilation. The game plays as before, with the same sound as 1.2.3: the SID's voices from reSID recordings
      and the «splat» when an arrow hits. The purist edition for a stock A500 stays the hand-made 1.2.3, still on this page.

      **Fixed**

      - **The game no longer stands still after you shoot the ghost.** The ghost now fades away and the game goes on. On the
        PC, 1.3 could stop there for good.
      - The stars twinkle in different places, as on the C64.
      - **Amiga, not enough memory:** the game now says how much memory it is missing and goes back to the Shell. Before, it
        could start anyway and hang. Under WHDLoad, a slave from another release next to the program now gives a message
        instead of crashing.

      **New**

      - **Mac** (macOS 11 or later, Apple silicon and Intel): the same two editions as on Windows, C64 and Reforge.
      - **The version on screen** on Windows and Mac for 5 seconds at the start, under the picture: the game's version, and
        beside it in small print reforge's («REFORGE 2026.11»).
      - **The C64's colours** on Windows and Mac as in VICE's Colodore palette, as on the Amiga.
      - **The same commands on every platform**, with Alt (Option on a Mac):

        | keys | what |
        |---|---|
        | Alt+P | pause |
        | Alt+M | sound off / on |
        | Alt+plus / minus | volume |
        | Alt+J | swap the joystick ports |
        | Alt+R | RESTORE |
        | Alt+Q or Esc | quit |
        | Alt+Return or F11 | full screen (PC and Mac) |

        The volume and mute are remembered in `reforge.cfg`. Backspace is RUN/STOP (back to the title), and F1 / F3 / F5 /
        F7 still choose the level on the title.
      - **Two gamepads on the PC and Mac:** a pad unplugged and plugged back keeps its player. Before, the two players could
        be swapped until the end of the game.
      - **One program per edition on Windows and Mac:** the game's files are inside the program, with no data folder beside
        it.
      - **INSTRUCTIONS.md** in every package (Amiga, Windows, Mac): the controls on each platform, the reforge commands and
        where the game saves its files.
      - **Reforge edition / ForbiddenForestRemake:**
        - the far trees are whole (their crowns were cut flat);
        - in the intro the creature stays behind the trees while far and the dragon passes in front of them when near;
        - the Demogorgon's head is a wider target, as in the Amiga 1.2.3;
        - the dance between waves is shorter, as in 1.2.3;
        - when the Demogorgon falls: a night with lightning, a short round of fireworks, then VICTORY.
      - **ForbiddenForestRemake on the Amiga:**
        - the monsters no longer blink in the heavy waves;
        - the forest scrolls at an even pace (25 pictures a second on a 68030);
        - no bar at the right edge of the picture on a PiStorm.

      **Requirements and known limits**

      - **Amiga:** ForbiddenForestFast needs a 68020 or better. **ForbiddenForestRemake needs a 68030 or better:** on an A1200
        with its stock 68EC020 it runs at 12-18 pictures a second instead of 25 (for that machine, use 1.2.3). For a stock A500,
        use the 1.2.3 edition.
      - **Amiga memory,** the smallest machine of nine tried that starts and plays, with the game started straight from the
        startup-sequence (the Workbench and other programs take memory of their own):

        | edition | from AmigaDOS | from WHDLoad |
        |---|---|---|
        | ForbiddenForestFast | 1 MB chip RAM (an A500+ or an A600) and 1 MB fast RAM | the same |
        | ForbiddenForestRemake | 1 MB chip RAM (an A500+ or an A600) and 2 MB fast RAM | the same |

      - **AmiSync** users: AmiSync 0.4.0 or newer.
      - **Windows and Mac:** not code-signed. Windows and macOS warn the first time.

      **Quality assurance**

      - **Automatic scenes:** every edition was driven automatically through the game's situations and compared with the
        original running in a C64 emulator. The situations: the title and the start, the three starting levels, each
        monster's wave, each monster's kill, the archer's death, the end of a wave and of a whole cycle, running out of
        arrows, the night, RUN/STOP, walking and shooting. This ran on the PC/Mac program (on the Mac) and on an emulated
        Amiga, in both editions.
      - **Long games:** an automatic player played long games on the emulated Amiga, with an alarm for a game that stops
        moving.
      - **Same picture on Mac and Amiga:** another alarm compares the forest drawn on the Mac with the one drawn on the
        Amiga.
      - **The ghost freeze was found this way.** It is fixed in this version and checked on every build.
      - **Amiga memory:** the requirement above was measured on nine Amiga machine configurations, from 512 KB chip RAM to
        2 MB chip + 8 MB fast.
      - **By hand:** the final test build was played on a real Amiga, an Amiga 2000 with a PiStorm.

      **Files:**
      - AmiSync puts all the Amiga editions in one drawer, `ForbiddenForest`. Its `README.txt` and `CHANGES.txt` stay those
        of the 1.2.3 A500 edition; this version's texts are `README_Fast.txt`, `CHANGES_Fast.txt` and so on, plus
        `INSTRUCTIONS.md`.
      - Amiga: `ForbiddenForestFast_v2.0.lha`, `ForbiddenForestRemake_v2.0.lha`, and the bootable floppies in `ForbiddenForest_Amiga_ADF_v2.0_2026-11-20.zip`.
      - Windows: `ForbiddenForest_PC_v2.0_win64.zip`.
      - Mac: `ForbiddenForest_PC_v2.0_macos-universal.zip`.

      The PC and Mac packages are the same ones the Reforge Arcade launcher installs:
      https://www.bonomo.cloud/launcher/
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
Some games are remembered for their gameplay. **Forbidden Forest** (Cosmi, 1983) is remembered for how it made you *feel*.

On a humble Commodore 64, Paul Norman built something nobody had seen before:
- a forest that breathes, with a sky that moves from day to dusk to a starry night;
- parallax backgrounds;
- giant spiders, bees, frogs, dragons, a snake and skeletons rising from the ground;
- and finally the Demogorgon, unseen in the darkness until the lightning reveals it.

It was cinematic, violent and genuinely frightening, years before anyone spoke of "survival horror".

This project brings that masterpiece to the Amiga in three editions: two purist ones, faithful to the last pixel, and a remake that reimagines its world with new graphics while keeping its soul intact.

## Why This Game

I took on Forbidden Forest out of admiration for Paul Norman and his pioneering vision.

His real genius was creating an astonishing atmosphere and a truly cinematic impact within the limits of 8-bit hardware. Converting this game means facing a complete work of art, where every element served one purpose: building emotional tension. The dynamic day/night cycle, the parallax backgrounds and the explicit graphic violence all work towards it.

Music and sound design play a fundamental part. Paul Norman composed and crafted them himself on the C64's SID chip. Faithfully preserving his score and his dynamic sound effects, such as the menacing buzz of the bees, is the ultimate tribute to an author who turned a simple video game into an unforgettable sensory experience.

## Absolute Source Code Fidelity

The guiding principle was the same as in my Wizard of Wor port: the original game logic is never reinterpreted.

The original 6502 code was statically recompiled into native 68000 code. It is translated, not emulated, so the Amiga runs Paul Norman's own program: the same monsters, the same patterns and the same timing, down to the CPU cycle.

To prove it, a lockstep test runs the recompiled code side by side with a reference C64, frame after frame, comparing memory, registers and cycle counts through every monster and every phase of the game. Every routine of the game is covered.

Only a few things were deliberately changed, all small quality-of-life touches:
- **The end-of-wave dance** is shorter, about 12 seconds instead of 28.
- **The Demogorgon's final explosion** is shorter, about 10 seconds instead of 31.
- **The arrow-hit sound:** the original effect was weak, so it was replaced by a new "splat" made from filtered SID noise.

## Authentic SID Sound

The music and effects are the heart of Forbidden Forest's atmosphere, so the audio received the same care as the code:
- **Recorded from the SID:** the three voices are rebuilt from recordings of the 6581 SID chip (reSID), with band-limited waveforms for clean, faithful tones.
- **Played by Paula on the A500:** each SID voice loops on one of Paula's own hardware channels. You get the music at its true pitch with almost no CPU cost, and with no gaps even when the action is heavy.
- **Mixed at 28 kHz on fast Amigas:** in the faster editions the voices are mixed in software at high quality.

## Two Souls: Purist and Remake

**Forbidden Forest (purist, A500)** and **Forbidden Forest Fast (purist, fast Amigas)**
- The original C64 graphics and gameplay, exactly as Paul Norman drew them.
- The forest now scrolls smoothly instead of the C64's 8-pixel jumps.
- The archer is drawn with the Amiga's hardware sprites.

**Forbidden Forest Remake (fast Amigas, PiStorm)**
- New full-screen graphics (368 × 256, no borders) in the style of Another World.
- Three planes in parallax: the sky, the distant hills and the foreground.
- A living sky: day, late afternoon, sunset and night, with the lightning flashing across it.
- The moon crosses the sky behind the trees and clouds. At dusk, and in the Demogorgon's wave, the stars come out, fixed in the sky just as on the C64.
- The original archer, with every one of his C64 animations, recoloured to match the new world.
- Monsters move inside the forest and pass behind trees and objects.
- Redrawn intro titles.
- A clearer HUD: the arrows left in your quiver, and your lives next to a red heart.

## Why This Version?

Paul Norman squeezed a whole cinematic world into 64 KB. This port stems from the desire to let that world shine on the Amiga:
- untouched in its rules and timing;
- smoother in its scrolling;
- and, in the remake, dressed the way the 1983 vision deserved, with today's tools.

If you love the classics, or if you remember being scared by a forest on your C64, this version will take you straight back to 1983, with a modern edge.

## Installation

Each ADF boots its own edition. For fast Amigas, `ForbiddenForest_FastAmigas.adf` holds both fast editions: from the floppy a menu (1 Fast, 2 Remake, 3 install on the hard disk); from the Workbench its Install icon puts them on the hard disk, with icons that start the game straight from AmigaDOS, without WHDLoad. For the hard disk, unpack a .lha pack anywhere and double-click its icon, or from the Shell: `WHDLoad ForbiddenForest.slave`, `WHDLoad ForbiddenForestFast.slave` or `WHDLoad ForbiddenForestRemake.slave`. The fast packs also carry a DOS icon that starts the game without WHDLoad (on a PiStorm WHDLoad slows the fast editions down).

## Requirements

| Edition | Floppy / hard disk | WHDLoad |
|---|---|---|
| Purist (A500) | 512 KB chip + 512 KB | 512 KB chip + 512 KB fast |
| Fast | 512 KB chip + 512 KB, fast CPU | 512 KB chip + 512 KB fast |
| Remake | 1 MB chip (ECS Agnus) + 1 MB fast, fast CPU (68030 or better, PiStorm) | 512 KB chip + 1.2 MB fast |

Kickstart 1.3 or later. OCS, ECS or AGA. WHDLoad 17 or later.

On a stock A500 the purist edition keeps the game and the music at full speed by skipping some display frames while the forest scrolls. Fast RAM or an accelerator gives the full 50 frames per second.

## Controls

Joystick in port 2, or the cursor keys with SPACE or CTRL to fire.

| Key | Action |
|---|---|
| F1 / F3 / F5 / F7 | Choose the difficulty on the title page |
| Alt+P | Pause |
| Alt+M | Sound off / on |
| Alt+plus / Alt+minus | Volume (music and effects together) |
| Alt+J | Swap the joystick ports |
| BACKSPACE | RUN/STOP |
| Alt+Q or Esc | Quit (with WHDLoad: back to the Workbench) |
| Alt+Return or F11 | Full screen (PC and Mac) |

The A500 edition (1.2.3) keeps its own keys: P or HELP to pause, F2 / F4 for the volume, ESC or F10 to quit.

---

*Original game: Paul Norman, Cosmi, 1983. Amiga conversion: Massimo Bonomo, 2026. This is a fan tribute; Forbidden Forest is © 1983 Cosmi / Paul Norman.*
