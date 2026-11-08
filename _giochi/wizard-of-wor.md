---
order: 1

# >>> da qui in giu' scrive sync-giochi.py: non modificare a mano
title: "Wizard of Wor"
piattaforma: "Amiga, PC"
originale: "Commodore 64 cartridge, Commodore, 1983 (arcade: Midway, 1981)"
anno_originale: 1983
sommario: >-
  The Commodore 64 cartridge of Midway's arcade maze shooter, recompiled for the Amiga and for the
  PC, in three versions: the SID sound, the voice of the 1984 Magic Voice module, and a new voice
  made in 2026.
requisiti: >-
  Kickstart 1.3 or later, OCS / ECS / AGA, 512 KB chip RAM plus memory for the sounds: SID
  512 KB chip + 3 MB, Magic Voice + 5 MB, Voice 2026 + 7 MB (WHDLoad: 4 / 8 / 8 MB fast). A stock
  A500 with 1 MB: its own floppy, with the SID sound. PC: Windows 10 or 11, 64-bit, through the
  Reforge Arcade launcher.
release_url: "https://github.com/korb3n70/wow-amiga-port/releases/tag/v1.2.1"
versione: "1.2.1"
data_versione: 2026-10-25
cartella: wizard-of-wor
repo: "korb3n70/wow-amiga-port"
schermate:
  - file: /assets/img/giochi/wizard-of-wor/wizard_of_wor_amiga_1_title_page.png
  - file: /assets/img/giochi/wizard-of-wor/wizard_of_wor_amiga_2_points.png
  - file: /assets/img/giochi/wizard-of-wor/wizard_of_wor_amiga_3_dungeon.png
download:
  - nome: "Floppies"
    file: "WizardOfWor_Amiga_ADF_v1.2.1_2026-10-25.zip"
    dimensione: "2,3 MB"
    descrizione: "three disks for the three versions (with a menu and an installer) and one disk for a stock A500 with 1 MB, the readme files"
  - nome: "Magic Voice version, WHDLoad pack"
    file: "WizardOfWor_MagicVoice_v1.2.1.lha"
    dimensione: "1,2 MB"
    descrizione: "the SID plus the voice of the Magic Voice module (1984), emulated"
  - nome: "Voice 2026 version, WHDLoad pack"
    file: "WizardOfWor_Voice2026_v1.2.1.lha"
    dimensione: "1,6 MB"
    descrizione: "the SID plus the same phrases with a modern voice, laugh and dungeon echo"
  - nome: "SID version, WHDLoad pack"
    file: "WizardOfWor_v1.2.1.lha"
    dimensione: "824 KB"
    descrizione: "the game with the SID's sound effects and music"
changelog:
  - versione: "pc-v1.3"
    data: 2026-11-08
    note: |
      The first PC build (Windows 10/11, 64-bit): the original C64 game, and the Magic Voice and Voice 2026 editions. Two players on one PC: player 1 the cursor keys + SPACE or the 1st gamepad, player 2 W A S D + left SHIFT or the 2nd gamepad.

      Installed and updated by the Reforge Arcade launcher: https://www.bonomo.cloud/launcher/ (this zip is the same package). Not code-signed: Windows warns the first time.
  - versione: "1.2.1"
    data: 2026-10-25
    note: |
      Wizard of Wor 1.2.1 (25.10.2026): the game unchanged; the WHDLoad slaves without a $VER: string (WHDLoad can stop on it at a black screen). Use this one instead of 1.2.

      - `WizardOfWor_v1.2.1.lha` -> `WizardOfWor/`
      - `WizardOfWor_MagicVoice_v1.2.1.lha` -> `WizardOfWorMagicVoice/`
      - `WizardOfWor_Voice2026_v1.2.1.lha` -> `WizardOfWorVoice2026/`

      The version: 5 s on the bottom strip at the start, in the CLI menu, on WHDLoad's splash, `Version wow FULL`. Nothing renamed or moved since 1.2.
  - versione: "1.2"
    data: 2026-10-25
    note: |
      Wizard of Wor 1.2 (23.10.2026): three versions of the sound.

      WHDLoad packs (the usual layout: <Name>.info + the drawer <Name>/ with the slave, the icon, wow and its sounds, README / LEGGIMI / CHANGES / NOVITA):
      - `WizardOfWor_v1.2.lha` -> `WizardOfWor/` (SID)
      - `WizardOfWor_MagicVoice_v1.2.lha` -> `WizardOfWorMagicVoice/` (SID + the Magic Voice)
      - `WizardOfWor_Voice2026_v1.2.lha` -> `WizardOfWorVoice2026/` (SID + Voice 2026)

      The version: `Version <file> FULL` on wow and the slaves; on screen on the OSD strip for 5 s at the start, in the CLI menu, in WHDLoad's splash.
      The game writes no files.

      First release published as a GitHub Release; nothing renamed since (the earlier tags had no packs).
---
Two Worriors, yellow and blue, are sent into the dungeons of the Wizard of Wor. Burwors, Garwors and Thorwors hunt them through the mazes, some of them invisible until they come close; the Worluk tries to escape, and in the end the Wizard himself appears, teleporting through the walls.

**Wizard of Wor** was a Midway arcade game in 1981. Commodore brought it to the Commodore 64 as a cartridge in 1983, and with the **Magic Voice** speech module (1984) the Wizard really spoke, taunting the players between the dungeons.

This project brings the C64 cartridge to the Amiga, in three versions chosen at start-up:
- **SID**: the sound effects and the music of the C64.
- **Magic Voice**: the SID plus the voice of the Magic Voice module, emulated.
- **Voice 2026**: the SID plus the same phrases with a modern voice, a laugh and the echo of the dungeon.

## The C64 Game, Recompiled

The original 6502 code is statically recompiled into native 68000 code. It is translated, not emulated: the Amiga runs the cartridge's own program, with the same mazes, the same monsters and the same timing. A lockstep test runs the recompiled code side by side with a reference C64 and compares them frame by frame.

## On the PC

The PC build comes through **Reforge Arcade**, the launcher that installs the games and keeps them up to date: [www.bonomo.cloud/launcher](https://www.bonomo.cloud/launcher/). It has three versions: **C64**, **Magic Voice** and **Reforge**, the edition with the voice made in 2026 (Voice 2026 on the Amiga), which also keeps the high scores between games.

The PC program is made with **reforge**, a newer tool: the cartridge's 6502 code translated into portable C and checked against the C64, built for Windows on SDL3. In all three versions the SID is emulated while the game plays; Magic Voice and Reforge add the same voices as the Amiga's.

Two players on one PC: the yellow Worrior with the cursor keys and SPACE or the first gamepad, the blue one with W A S D and the left SHIFT or the second gamepad. The program is not code-signed, so Windows warns about it the first time.

## The Sound and the Voices

- **SID:** every sound is rendered from the game's own sound engine with reSID (a 6581 SID) and played by Paula at 28 kHz.
- **Magic Voice:** the game "sees" the module and uses it as on the C64, with its timing, including the CPU time the module took from the game while it spoke. The voice is mixed with the effects.
- **Voice 2026:** the same phrases, spoken with a new voice.
- All the sounds are stored losslessly compressed and unpacked into memory at start-up, with a progress bar.

**A stock A500 with 1 MB** has its own floppy: the same SID sounds, from the same reSID renders, made smaller (490 KB instead of 1.8 MB). Each sound plays at the lowest rate that keeps its spectrum, and the repeated steps of an effect are stored once and played again as the original engine does. No voice and no menu; no unpacking.

## Installation

Floppies: boot disk 1 and choose the version in the AmigaDOS window (1 SID, 2 Magic Voice, 3 Voice 2026; RETURN alone is 1); for versions 2 and 3 AmigaDOS asks for the voice disk. On a 7 MHz A500 loading and unpacking take a minute or two, much less with an accelerator. The installer is on disk 2: double-click its Install icon (Workbench 1.3 or later). It creates the icons "Wizard of Wor SID", "Magic Voice", "Voice 2026" and "menu", which start the game straight from AmigaDOS, without WHDLoad. For the hard disk, unpack a .lha pack anywhere and double-click its icon, or from the Shell: `WHDLoad WizardOfWor.slave`, `WHDLoad WizardOfWor_MV.slave` or `WHDLoad WizardOfWor_V26.slave`. WHDLoad itself is not included (whdload.de).

## Requirements

| Version | Floppy / hard disk | WHDLoad |
|---|---|---|
| 1 SID | 512 KB chip + 3 MB | 512 KB chip + 4 MB fast |
| 2 Magic Voice | 512 KB chip + 5 MB | 512 KB chip + 8 MB fast |
| 3 Voice 2026 | 512 KB chip + 7 MB (8 MB) | 512 KB chip + 8 MB fast |
| A500 1 MB disk | 512 KB chip + 512 KB (slow or fast; or 1 MB chip) | |

Kickstart 1.3 or later. OCS, ECS or AGA. With less memory the game starts without sound or without the voice, and says so. Full speed with fast RAM or a PiStorm.

Tested in WinUAE with Kickstart 3.2.3 and 1.3.

## Controls

Joystick in port 2 for the yellow Worrior: fire on the title for a one-player game. Two players: fire on the title with the joystick in port 1 (blue, the mouse port: the mouse's left button acts as its fire button).

| Key | Action |
|---|---|
| P or HELP | Pause |
| F2 / F4 | Effects volume down / up |
| F6 / F8 | Voice volume down / up (Magic Voice, Voice 2026) |
| F9 | Port 1 off / on (off: the mouse does nothing) |
| DEL | RESTORE: back to the title pages |
| ESC or F10 | Quit |

The rest of the Amiga keyboard acts as the C64's.

---

*Wizard of Wor: arcade by Midway, 1981; Commodore 64 cartridge by Commodore, 1983; Magic Voice speech module, 1984. Amiga and PC conversion: Massimo Bonomo, 2026. This is a fan tribute; Wizard of Wor is © its rights holders.*
