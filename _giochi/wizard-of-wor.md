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
release_url: "https://github.com/korb3n70/wow-amiga-port/releases/tag/v2.0"
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
    - name: "WizardOfWorFast"
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
    - name: "WizardOfWorFastMV"
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
    - name: "WizardOfWorFastV26"
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
older_downloads:
  - file: "WizardOfWor_v1.2.1.lha"
    version: "1.2.1"
    edition: "WizardOfWor"
    bytes: 843461
    machines: []
    note: "edizione non rifatta da reforge: port 1.2.1 fatto a mano (repo wizard-of-wor), non reforge"
  - file: "WizardOfWor_MagicVoice_v1.2.1.lha"
    version: "1.2.1"
    edition: "WizardOfWorMagicVoice"
    bytes: 1221523
    machines: []
    note: "edizione non rifatta da reforge: port 1.2.1 fatto a mano (repo wizard-of-wor), non reforge"
  - file: "WizardOfWor_Voice2026_v1.2.1.lha"
    version: "1.2.1"
    edition: "WizardOfWorVoice2026"
    bytes: 1653598
    machines: []
    note: "edizione non rifatta da reforge: port 1.2.1 fatto a mano (repo wizard-of-wor), non reforge"
  - file: "WizardOfWor_Amiga_ADF_v1.2.1_2026-10-25.zip"
    version: "1.2.1"
    edition: ""
    bytes: 2378452
    machines: []
    note: "i dischetti della 1.2.1"
versione: "2.0"
data_versione: 2026-11-20
cartella: wizard-of-wor
repo: "korb3n70/wow-amiga-port"
schermate:
  - file: /assets/img/giochi/wizard-of-wor/wizard_of_wor_amiga_1_title_page.png
  - file: /assets/img/giochi/wizard-of-wor/wizard_of_wor_amiga_2_points.png
  - file: /assets/img/giochi/wizard-of-wor/wizard_of_wor_amiga_3_dungeon.png
download:
  - nome: "Magic Voice edition (68020 or better), WHDLoad pack"
    file: "WizardOfWorFast_MagicVoice_v2.0.lha"
    dimensione: "1,2 MB"
    descrizione: "the same game with the Magic Voice cartridge's speech; WHDLoad, or the DOS icon without WHDLoad"
  - nome: "Voice 2026 edition (68020 or better), WHDLoad pack"
    file: "WizardOfWorFast_Voice2026_v2.0.lha"
    dimensione: "1,7 MB"
    descrizione: "the same game with the new voices made in 2026, and the high scores kept between games; WHDLoad, or the DOS icon without WHDLoad"
  - nome: "Classic edition (68020 or better), WHDLoad pack"
    file: "WizardOfWorFast_v2.0.lha"
    dimensione: "898 KB"
    descrizione: "the C64 game made with reforge, the SID's sound effects and music, no voice; WHDLoad, or the DOS icon without WHDLoad"
  - nome: "Floppies"
    file: "WizardOfWor_Amiga_ADF_v2.0_2026-11-20.zip"
    dimensione: "2,0 MB"
    descrizione: "disk 1 bootable, disks 2 and 3 for the voice editions, the readme files and INSTRUCTIONS.md"
changelog:
  - versione: "2.0"
    data: 2026-11-20
    note: |
      One version for every platform: Amiga, Windows and, new, the Mac.

      **Amiga: three new editions for a 68020 or better, made with reforge.** The C64 game is translated routine by routine
      into portable C and checked against the original running in a C64 emulator. The editions:

      | edition | what |
      |---|---|
      | WizardOfWorFast | classic, no voice |
      | WizardOfWorFastMV | with the Magic Voice cartridge's speech |
      | WizardOfWorFastV26 | with Voice 2026, the new voices |

      The sound bank and the voices are the same as 1.2.1. The version shows on screen at the start, and while the game
      unpacks a bar fills the frame from its inner edge. The hand-made 1.2.1 stays the edition for an A500 with 1 MB, still
      on this page.

      **Fixed (Windows)**

      - **The game no longer hangs at the start, about one start in sixteen.**
      - **The game's own pause (RUN/STOP, Backspace) now works,** and it freezes the game: the dungeon's doors no longer move
        while paused.
      - **The author's easter egg now answers**, as on the C64 (see INSTRUCTIONS.md).
      - **Voice 2026:** phrase 20 now says «Wizard of Wor, by Jeff Bruette», as in the arcade original.

      **New**

      - **Mac** (macOS 11 or later, Apple silicon and Intel): the same three editions as on Windows, C64, Magic Voice and Reforge.
      - **The version on screen** on Windows and Mac for 5 seconds at the start, under the picture: the game's version, and
        beside it in small print reforge's («REFORGE 2026.11»).
      - **The C64's colours** on Windows and Mac as in VICE's Colodore palette, as on the Amiga.
      - **The same commands on every platform**, with Alt (Option on a Mac):

        | keys | what |
        |---|---|
        | Alt+P | pause |
        | Alt+M | sound off / on |
        | Alt+plus / minus | volume |
        | Alt+V | the voice off / on, in the voice editions |
        | Alt+J | swap the joystick ports |
        | Alt+R | RESTORE |
        | Alt+Q or Esc | quit |
        | Alt+Return or F11 | full screen (PC and Mac) |

        The volume, mute and voice are remembered in `reforge.cfg`. Backspace is RUN/STOP, Delete is INST/DEL.
      - **High scores saved:** the five best are kept between games in `WOW_HISCORES`, in the Voice 2026 edition only:
        - new on the Amiga, in WizardOfWorFastV26, in the game's drawer;
        - new on the Mac, in Reforge, in the `save` folder;
        - Windows (Reforge) already kept them in 1.3.1.
      - **Two gamepads on the PC and Mac:** a pad unplugged and plugged back keeps its player. Before, the two players could
        be swapped until the end of the game.
      - **One program per edition on Windows and Mac:** the game's files are inside the program, with no data folder beside
        it.
      - **INSTRUCTIONS.md** in every package (Amiga, Windows, Mac): the controls on each platform, the reforge commands,
        where the high scores are saved, and the author's easter egg.

      **Voices**

      The C64 game speaks 21 phrases through the Magic Voice cartridge. The voice editions say all 21, at the same moments as
      the C64 and as 1.2.1 / 1.3.1. None is new and none is removed.

      - **Magic Voice** (WizardOfWorFastMV, Windows and Mac «Magic Voice»): the cartridge's own speech, unchanged.
      - **Voice 2026** (WizardOfWorFastV26, Windows and Mac «Reforge»): a new voice made in 2026 from the same phrases.
        - Nine of its phrases are made again with corrected words. Before, they followed an uncertain transcription:
          - eight follow the 1980 arcade's phrase list, or its words where the arcade has no such phrase;
          - phrase 20 is the author's signature, as the original says it.
        - The other twelve phrases are byte for byte as before.
        - New: Alt+V turns the voice off and on.

      | # | text as spoken | Magic Voice | Voice 2026 (vs Amiga 1.2.1 and Windows 1.3.1) |
      |---|---|---|---|
      | 00 | I am the Wizard of Wor. | unchanged | unchanged |
      | 01 | Get ready, Worrior. | unchanged | unchanged |
      | 02 | My pets were getting hungry. | unchanged | re-made with the right words (1.2.1 / 1.3.1 said «My pets are getting hungry.») |
      | 03 | Remember, I'm the Wizard, not you. | unchanged | re-made with the right words (1.2.1 / 1.3.1 said «Remember, I am the Wizard, not you.») |
      | 04 | You'll never leave Wor alive! (laugh) | unchanged | unchanged |
      | 05 | If you destroy my babies, I'll pop you in the oven! (laugh) | unchanged | unchanged |
      | 06 | You'll get... The Arena! (laugh) | unchanged | re-made with the right words (1.2.1 / 1.3.1 said «You'll get eaten, Worrior!») |
      | 07 | You'll get... The Pit! (laugh) | unchanged | re-made with the right words (1.2.1 / 1.3.1 said «You'll get it!») |
      | 08 | Now you get the heavyweights! (laugh) | unchanged | unchanged |
      | 09 | If you get too powerful, I'll take care of you myself! (laugh) | unchanged | unchanged |
      | 10 | Your bones will lie in the dungeons of Wor! (laugh) | unchanged | unchanged |
      | 11 | Garwor and Thorwor become invisible! (laugh) | unchanged | unchanged |
      | 12 | Wor-lord, be forewarned! You approach, The Pit! | unchanged | re-made with the right words (1.2.1 / 1.3.1 said «Worluk! Beware, Worluk... you approach!») |
      | 13 | Beware! You are in the Wor-lord dungeons! | unchanged | re-made with the right words (1.2.1 / 1.3.1 said «Beware, you are now in the Wor-lord dungeon.») |
      | 14 | Your fate will be decided! (laugh) | unchanged | unchanged |
      | 15 | Oops! I must have forgotten the walls! (laugh) | unchanged | re-made with the right words (1.2.1 / 1.3.1 said «Oh, I must have forgotten...») |
      | 16 | Come back for more with the Wizard of Wor! (laugh) | unchanged | unchanged |
      | 17 | You can start anew, but for now, you're through! (laugh) | unchanged | unchanged |
      | 18 | He he he, ho ho ho, (laugh) That was fun! | unchanged | re-made with the right words (1.2.1 / 1.3.1 said «Hey... (laugh) That was fun.») |
      | 19 | Keep going, and you will find me! (laugh) | unchanged | unchanged |
      | 20 | Wizard of Wor, by Jeff Bruette. | unchanged | re-made with the right words (1.2.1 / 1.3.1 said «Wizard of Wor... Garwor...») |

      **Requirements and known limits**

      - **Amiga:** the reforge editions need a 68020 or better. For an A500, use 1.2.1.
      - **Amiga memory,** the smallest machine of nine tried that starts and plays, with the game started straight from the
        startup-sequence (the Workbench and other programs take memory of their own):

        | edition | from AmigaDOS | from WHDLoad |
        |---|---|---|
        | WizardOfWorFast | 1 MB chip RAM (an A500+ or an A600) and 4 MB fast RAM | the same |
        | WizardOfWorFastMV | 2 MB chip RAM (an A1200) and 8 MB fast RAM | the same |
        | WizardOfWorFastV26 | 2 MB chip RAM (an A1200) and 8 MB fast RAM | the same |

        With less memory the game says how much it is missing and goes back to the Shell. Under WHDLoad, a slave from
        another release next to the program gives a message instead of crashing.
      - **AmiSync** users: AmiSync 0.4.0 or newer.
      - **Windows and Mac:** not code-signed. Windows and macOS warn the first time.

      **Quality assurance**

      - **Automatic scenes:** all three editions were driven automatically through the game's situations and compared with
        the original running in a C64 emulator. The situations: the Wizard's death and the next dungeon, the Worluk escaping
        or shot, the Wizard escaping, the end of the game, the title's second page, the Magic Voice, a fixed maze, the pause,
        two players. This ran on the Mac program and on an emulated Amiga.
      - **Long games:** an automatic player played long games on the emulated Amiga, with an alarm for a game that stops
        moving.
      - **Same mazes on Mac and Amiga:** another alarm compares the walls and colours of every maze on the Mac and on the
        Amiga. It catches the broken walls that one test build had.
      - **Defects found before release:** a stop after the Wizard's death in the Amiga test builds, seen on a real Amiga, now
        has its own repeatable scene. The hang at start on Windows was caught by a check that starts the program many times in
        a row. Both are fixed.
      - **Amiga memory:** the requirement above was measured on nine Amiga machine configurations, from 512 KB chip RAM to
        2 MB chip + 8 MB fast.
      - **By hand:** the final test build was played on a real Amiga, an Amiga 2000 with a PiStorm.

      **Files:**
      - AmiSync puts all the Amiga editions in one drawer, `WizardOfWor`. Its `README.txt` and `CHANGES.txt` stay those of
        1.2.1; this version's texts are `README_Fast.txt`, `CHANGES_Fast.txt` and so on, plus `INSTRUCTIONS.md`.
      - Amiga: `WizardOfWorFast_v2.0.lha`, `WizardOfWorFast_MagicVoice_v2.0.lha`, `WizardOfWorFast_Voice2026_v2.0.lha`, and
        the floppies in `WizardOfWor_Amiga_ADF_v2.0_2026-11-20.zip` (disk 1 bootable, disks 2 and 3 for the voice editions).
      - Windows: `WizardOfWor_PC_v2.0_win64.zip`.
      - Mac: `WizardOfWor_PC_v2.0_macos-universal.zip`.

      The PC and Mac packages are the same ones the Reforge Arcade launcher installs:
      https://www.bonomo.cloud/launcher/
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
| Backspace | Pause (the C64's RUN/STOP); 1 or 2 resumes |
| Alt+P | Pause |
| Alt+M | Sound off / on |
| Alt+plus / Alt+minus | Volume (music and effects together) |
| Alt+V | The voice off / on (the editions with speech) |
| Alt+J | Swap the joystick ports |
| Alt+R | RESTORE: back to the title pages |
| Alt+Q or Esc | Quit |
| Alt+Return or F11 | Full screen (PC and Mac) |

The 1.2.1 editions (the A500 floppy) keep their own keys: P or HELP to pause, F2 / F4 and F6 / F8 for the effects' and the voice's volume, F9 to switch port 1 off, DEL for RESTORE, ESC or F10 to quit.

The rest of the Amiga keyboard acts as the C64's.

---

*Wizard of Wor: arcade by Midway, 1981; Commodore 64 cartridge by Commodore, 1983; Magic Voice speech module, 1984. Amiga and PC conversion: Massimo Bonomo, 2026. This is a fan tribute; Wizard of Wor is © its rights holders.*
