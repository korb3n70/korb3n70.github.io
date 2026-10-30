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
release_url: "https://github.com/korb3n70/forbidden-forest-amiga/releases/tag/v1.2.3"
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
  - nome: "Purist edition for fast Amigas, WHDLoad pack"
    file: "ForbiddenForestFast_v1.2.3.lha"
    dimensione: "114 KB"
    descrizione: "the original game with the sound mixed at 28 kHz; WHDLoad, or the DOS icon without WHDLoad"
  - nome: "Remake, WHDLoad pack"
    file: "ForbiddenForestRemake_v1.2.3.lha"
    dimensione: "166 KB"
    descrizione: "new graphics, a living sky, three planes of parallax; fast Amigas (68030 or better, PiStorm); WHDLoad, or the DOS icon without WHDLoad"
  - nome: "Floppies"
    file: "ForbiddenForest_Amiga_ADF_v1.2.3_2026-10-26.zip"
    dimensione: "453 KB"
    descrizione: "one bootable ADF per edition, one disk with both fast editions and an installer (ForbiddenForest_FastAmigas.adf), the readme files"
  - nome: "Purist edition (A500), WHDLoad pack"
    file: "ForbiddenForest_v1.2.3.lha"
    dimensione: "112 KB"
    descrizione: "the original C64 graphics and gameplay, the SID voices on Paula; a stock A500 with 1 MB"
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

## Downloads

| File | Size | What it is |
|---|---|---|
| `ForbiddenForest_v1.2.3.lha` | 112 KB | **Purist edition (A500), WHDLoad pack**: the original C64 graphics and gameplay, the SID voices on Paula; a stock A500 with 1 MB |
| `ForbiddenForestFast_v1.2.3.lha` | 114 KB | **Purist edition for fast Amigas, WHDLoad pack**: the original game with the sound mixed at 28 kHz; WHDLoad, or the DOS icon without WHDLoad |
| `ForbiddenForestRemake_v1.2.3.lha` | 166 KB | **Remake, WHDLoad pack**: new graphics, a living sky, three planes of parallax; fast Amigas (68030 or better, PiStorm); WHDLoad, or the DOS icon without WHDLoad |
| `ForbiddenForest_Amiga_ADF_v1.2.3_2026-10-26.zip` | 453 KB | **Floppies**: one bootable ADF per edition, one disk with both fast editions and an installer (ForbiddenForest_FastAmigas.adf), the readme files |

**Installation.** Each ADF boots its own edition. For fast Amigas, `ForbiddenForest_FastAmigas.adf` holds both fast editions: from the floppy a menu (1 Fast, 2 Remake, 3 install on the hard disk); from the Workbench its Install icon puts them on the hard disk, with icons that start the game straight from AmigaDOS, without WHDLoad. For the hard disk, unpack a .lha pack anywhere and double-click its icon, or from the Shell: `WHDLoad ForbiddenForest.slave`, `WHDLoad ForbiddenForestFast.slave` or `WHDLoad ForbiddenForestRemake.slave`. The fast packs also carry a DOS icon that starts the game without WHDLoad (on a PiStorm WHDLoad slows the fast editions down).

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
| P or HELP | Pause |
| F2 / F4 | Volume down / up |
| BACKSPACE | RUN/STOP |
| ESC or F10 | Quit (with WHDLoad: back to the Workbench) |

## Support the Project

Creating this kind of port requires countless hours of reverse engineering, recompilation, hardware testing, and a genuine passion for preserving retrogaming history.

If you enjoy the game and would like to support the development of this and future retrocomputing projects, please consider making a small donation. Even a tiny contribution helps cover resource costs and keeps the drive alive for future releases!

Thank you so much for your support, and... watch out for the spiders in the forest!

---

*Original game: Paul Norman, Cosmi, 1983. Amiga conversion: Massimo Bonomo, 2026. This is a fan tribute; Forbidden Forest is © 1983 Cosmi / Paul Norman.*
