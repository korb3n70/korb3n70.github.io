---
order: 4

# >>> da qui in giu' scrive sync-giochi.py: non modificare a mano
title: "Space Taxi"
piattaforma: "Amiga, PC"
originale: "Commodore 64, Muse Software, 1984 (John F. Kutcher)"
anno_originale: 1984
sommario: >-
  John F. Kutcher's 1984 C64 classic, translated from the original 6502 code with reforge: 25
  screens of pickups and landings, the original speech, and a Reforge edition with new voices
  and a title menu, for fast Amigas and for the PC.
requisiti: >-
  Amiga: a 68020 or better, 512 KB chip + 2 MB fast (SpaceTaxiFast from AmigaDOS: 1 MB),
  Kickstart 1.3 or later (WHDLoad: 2.0). PC: Windows 10 or 11, 64-bit, through the Reforge
  Arcade launcher.
release_url: "https://github.com/korb3n70/spacetaxi/releases/tag/v1.0.2"
versione: "1.0.2"
data_versione: 2026-11-07
cartella: space-taxi
repo: "korb3n70/spacetaxi"
schermate:
  - file: /assets/img/giochi/space-taxi/space_taxi_1_title.png
  - file: /assets/img/giochi/space-taxi/space_taxi_2_reforge_menu.png
  - file: /assets/img/giochi/space-taxi/space_taxi_3_shift_start.png
  - file: /assets/img/giochi/space-taxi/space_taxi_4_play.png
download:
  - nome: "Amiga: the original edition, WHDLoad pack"
    file: "SpaceTaxiFast_v1.0.2.lha"
    dimensione: "503 KB"
    descrizione: "the original graphics, the music as Paula streams, the C64's own sampled voices; WHDLoad, or the DOS icon without WHDLoad"
  - nome: "Amiga: Reforge edition, WHDLoad pack"
    file: "SpaceTaxiRemake_v1.0.2.lha"
    dimensione: "805 KB"
    descrizione: "the same game with new voices (whole phrases at 28 kHz) and a title menu; WHDLoad, or the DOS icon without WHDLoad"
  - nome: "Amiga: floppies"
    file: "SpaceTaxi_Amiga_ADF_v1.0.2_2026-11-07.zip"
    dimensione: "942 KB"
    descrizione: "one bootable ADF per edition, the readme files"
changelog:
  - versione: "1.0.2"
    data: 2026-11-07
    note: |
      Space Taxi for the Amiga (68020 or better), 1.0.2 (2026-11-07).

      - **SpaceTaxiRemake**: a menu on the title screen: High Scores, Single Player Local, Instructions and Credits. Two Players Local and Online Multiplayer are coming soon.
      - **SpaceTaxiRemake**: the menus and the instructions answer the first press of fire; the high scores stay at least a second, and the old title no longer flashes after them.
      - SpaceTaxiFast is the same as 1.0.1 (the C64's title).

      Files: `SpaceTaxiFast_v1.0.2.lha` and `SpaceTaxiRemake_v1.0.2.lha` (WHDLoad and AmigaDOS), and the two bootable floppies in `SpaceTaxi_Amiga_ADF_v1.0.2_2026-11-07.zip`.

      **PC (Windows), 1.0.5**, also in the Reforge Arcade launcher: `SpaceTaxi_PC_v1.0.5_win64.zip`. The Reforge edition's Two Players Local: two people on one PC (player 1 the cursor keys + SPACE or the 1st gamepad, player 2 W A S D + left SHIFT or the 2nd gamepad); the duel's levels and starts from the level editor.
  - versione: "1.0"
    data: 2026-11-05
    note: |
      Space Taxi 1.0 for the Amiga (2026-11-04): the first release.

      - **SpaceTaxiFast_v1.0.lha**: the C64 game as it was, for fast Amigas (hard disk or WHDLoad).
      - **SpaceTaxiRemake_v1.0.lha**: the remake, with the voices at 28 kHz.
      - **SpaceTaxi_Amiga_ADF_v1.0_2026-11-04.zip**: both editions on bootable floppies (ADF).

      The changes are in CHANGES.txt (in Italian, NOVITA.txt).
  - versione: "1.0.1"
    data: 2026-11-06
    note: |
      Space Taxi 1.0.1 for the Amiga (2026-11-06).

      - The level's sprites no longer always crash the taxi: in TELEPORTS the teleports carry it, in PUZZLER the switches work, in REBOUND the balls bounce it off, as on the C64; in BLACK HOLE and MAGNETS the crash is the C64's (no fall first).
      - The version shows on screen for 5 seconds at the start.

      Files:
      - **SpaceTaxiFast_v1.0.1.lha**: the C64 game as it was, for fast Amigas (hard disk or WHDLoad).
      - **SpaceTaxiRemake_v1.0.1.lha**: the remake, with the voices at 28 kHz.
      - **SpaceTaxi_Amiga_ADF_v1.0.1_2026-11-06.zip**: both editions on bootable floppies (ADF).
      - **SpaceTaxi_PC_v1.0.4_win64.zip**: the PC edition 1.0.4 with the same fix (also through the Reforge Arcade launcher).

      The changes are in CHANGES.txt (in Italian, NOVITA.txt).
---
"Hey, taxi!" Few games spoke to you in 1984. **Space Taxi** (Muse Software, 1984) did, and it never let go.

John F. Kutcher's game is simple to explain and hard to master: fly a taxi through 24 hours of shifts, pick up the passengers waiting on the landing pads, take them where they ask, and land gently. Gravity pulls, the fuel runs out, the tip shrinks while they wait. Every screen is a new puzzle: candy canes, teleports, switches, black holes, bouncing balls, magnets.

## A Translation, Not an Emulation

This edition is made with **reforge**: the original 6502 code translated routine by routine into portable C, checked against the C64 frame by frame. The same 25 screens, the same physics, the same timing, the same high scores. It runs natively, with no emulator in between.

## Two Editions

- **Space Taxi** (on the Amiga: SpaceTaxiFast): the original game. The C64's own sampled speech ("Hey taxi!", "Pad 2 please"), the music as Paula streams made from the game's own player.
- **Space Taxi Reforge** (on the Amiga: SpaceTaxiRemake): the same game with new voices speaking whole phrases ("Hey, taxi!", "Pad five, please.", "Up, please!") and a title menu: High Scores, Single Player Local, Instructions, Credits. On the PC also **Two Players Local**: two people on the same computer.

## On the PC

The PC build comes through **Reforge Arcade**, the launcher that installs the games and keeps them up to date: [www.bonomo.cloud/launcher](https://www.bonomo.cloud/launcher/). Gamepads work (the first one is player 1), as do the keyboard's cursor keys.

## Installation (Amiga)

Unpack a .lha pack anywhere and double-click its WHDLoad icon, or from the Shell: `WHDLoad SpaceTaxiFast.slave` or `WHDLoad SpaceTaxiRemake.slave`. The `<drawer> DOS` icon starts the game straight from AmigaDOS, without WHDLoad (on a PiStorm with Caffeine OS this is the fast way). Each edition also has its own bootable floppy.

## Requirements

| | Amiga | PC |
|---|---|---|
| Processor | 68020 or better (accelerator boards, A1200 / A3000 / A4000, PiStorm) | any 64-bit PC |
| Memory | 512 KB chip + 2 MB fast, any kind (SpaceTaxiFast from AmigaDOS: 1 MB) | |
| System | Kickstart 1.3 or later; WHDLoad: 2.0 or later | Windows 10 or 11 |

Not on a 68000 alone, nor on an A1200 without fast memory.

## Controls

Joystick in port 2 (on the PC: a gamepad or the cursor keys with SPACE to fire).

| Key | Action |
|---|---|
| Joystick | Fly the taxi; fire for the landing gear |
| Title (original) | Fire to play, up for the high scores, down for the instructions |
| Title menu (Reforge) | Up / down to choose, fire to select |
| P or HELP | Pause |
| ESC or F10 | Quit |

---

*Original game: John F. Kutcher, Muse Software, 1984. Amiga and PC conversion: Massimo Bonomo, 2026. This is a fan tribute; Space Taxi is © 1984 Muse Software / John F. Kutcher.*
