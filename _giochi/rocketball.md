---
order: 3

# >>> da qui in giu' scrive sync-giochi.py: non modificare a mano
title: "Rocketball"
piattaforma: "Amiga"
originale: "Commodore 64, IJK Software, 1985"
anno_originale: 1985
sommario: >-
  A violent future sport on skates: the 1985 Commodore 64 original, rebuilt for the Amiga
  (now also for a stock A500), and a remake with new graphics, an announcer, the bikes and
  new rules.
requisiti: >-
  Original edition: 1 MB (512 KB chip + 512 KB other), a 68000 (A500 version) or a 68020 or
  better, Kickstart 1.3, OCS / ECS / AGA. Remake: 1 MB chip + about 1.2 MB other memory and a
  fast Amiga (PiStorm, a fast 68030, 68040 / 68060, emulators with JIT).
release_url: "https://github.com/korb3n70/rollerball-amiga/releases/tag/v2.1"
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
    - name: "Rocketball"
      cells:
        - machine: "ocs_4mb"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
        - machine: "ocs_8mb"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
        - machine: "a1200_4mb"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
        - machine: "a1200_8mb"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
        - machine: "pistorm"
          status: "untested"
          offer: "2.1"
          why: "prova a occhio passata su una macchina vera; manca la misura delle immagini al secondo su questa macchina"
          note: "non provato su questa macchina"
        - machine: "thea500mini"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
        - machine: "thea1200"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
    - name: "RocketballA500"
      cells:
        - machine: "ocs_4mb"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
        - machine: "ocs_8mb"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
        - machine: "a1200_4mb"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
        - machine: "a1200_8mb"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
        - machine: "pistorm"
          status: "untested"
          offer: "2.1"
          why: "prova a occhio passata su una macchina vera; manca la misura delle immagini al secondo su questa macchina"
          note: "non provato su questa macchina"
        - machine: "thea500mini"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
        - machine: "thea1200"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
    - name: "RocketballRemake"
      cells:
        - machine: "ocs_4mb"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
        - machine: "ocs_8mb"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
        - machine: "a1200_4mb"
          status: "untested"
          offer: "2.1"
          why: "misurato, ma manca la prova a occhio; la memoria (4 o 8 MB) della misura non e' scritta nello schema"
          note: "non provato su questa macchina"
        - machine: "a1200_8mb"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
        - machine: "pistorm"
          status: "untested"
          offer: "2.1"
          why: "prova a occhio passata su una macchina vera; manca la misura delle immagini al secondo su questa macchina"
          note: "non provato su questa macchina"
        - machine: "thea500mini"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
        - machine: "thea1200"
          status: "untested"
          offer: "2.1"
          why: ""
          note: "non provato su questa macchina"
older_downloads:
versione: "2.1"
data_versione: 2026-11-20
cartella: rocketball
repo: "korb3n70/rollerball-amiga"
schermate:
  - file: /assets/img/giochi/rocketball/rocketball_amiga_1_title.png
  - file: /assets/img/giochi/rocketball/rocketball_amiga_2_play.png
  - file: /assets/img/giochi/rocketball/rocketball_amiga_3_kickoff.png
  - file: /assets/img/giochi/rocketball/rocketball_amiga_4_bike_in_play.png
  - file: /assets/img/giochi/rocketball/rocketball_amiga_5_options.png
download:
  - nome: "Original edition, floppy"
    file: "Rocketball_Amiga_ADF_v2.1_2026-11-20.zip"
    dimensione: "425 KB"
    descrizione: "a bootable ADF (a menu: 1 the A500 version, 2 the 68020 one, and an installer) with the readme files"
  - nome: "Remake, WHDLoad pack"
    file: "Rocketball_Remake_v2.1.lha"
    dimensione: "1,2 MB"
    descrizione: "new graphics, an announcer, the bikes and new rules, for fast Amigas; WHDLoad, or the DOS icon without WHDLoad"
  - nome: "Original edition, WHDLoad pack"
    file: "Rocketball_v2.1.lha"
    dimensione: "736 KB"
    descrizione: "the C64 game for a stock A500 (rb_a500, 68000) and for a 68020 or better (rb); WHDLoad, or the DOS icon without WHDLoad"
changelog:
  - versione: "2.1"
    data: 2026-11-20
    note: |
      One version for every platform: Amiga, Windows and, new, the Mac.

      **New**

      - **Fire in port 2 on the title** starts the game on the Amiga even with a mouse plugged into port 1 (Rocketball and
        RocketballA500).
      - **INSTRUCTIONS.md** also tells how to start a game, what F1 / F3 / F5 / F7 do and where to plug the joystick for two
        players.
      - **Sound off and volume on the Amiga now act on the music too** (the title tune and the tunes in play) and on the
        Remake's samples. At the start, the line under the picture says MUTE or VOL n when `reforge.cfg` keeps them.
      - **Mac** (macOS 11 or later, Apple silicon and Intel): the same two editions as on Windows, C64 and Reforge, two players on one machine.
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

        The volume and mute are remembered in `reforge.cfg`.
      - **Changed keys on the Amiga:** the pause is now Alt+P (P and HELP no longer pause; HELP is the C64's CLR/HOME).
        Backspace or R is RUN/STOP, back to the title, as before. Esc still quits; F10 no longer does. F1 / F3 / F5 / F7 on
        the title as on the C64.
      - **The version on screen** on Windows and Mac, under the picture at the start: the game's version, and beside it in
        small print reforge's («REFORGE 2026.11»). The C64 edition's title shows it as on the Amiga.
      - **The C64's colours** on Windows and Mac as in VICE's Colodore palette, as on the Amiga.
      - **Two gamepads on the PC and Mac:** a pad unplugged and plugged back keeps its player. Before, the two players could
        be swapped until the end of the game.
      - **One program per edition on Windows and Mac:** the game's files are inside the program, with no data folder beside
        it.
      - **INSTRUCTIONS.md** in every package (Amiga, Windows, Mac): the controls on each platform, the reforge commands and
        where the game saves its files.
      - **RocketballRemake on the Amiga:** the view follows a ball that leaves the screen.

      **Fixed**

      - **Amiga, not enough memory:** the game now says how much memory it is missing and goes back to the Shell. Before, it
        could start anyway and hang. Under WHDLoad, a slave from another release next to the program now gives a message
        instead of crashing.

      **Requirements and known limits**

      - **Amiga:**
        - Rocketball needs a 68020 or better;
        - RocketballA500 is for a stock A500 (68000);
        - RocketballRemake needs a fast Amiga.
      - **Amiga memory,** the smallest machine of nine tried that starts and plays, with the game started straight from the
        startup-sequence (the Workbench and other programs take memory of their own):

        | edition | from AmigaDOS | from WHDLoad |
        |---|---|---|
        | Rocketball | 512 KB chip RAM and 512 KB slow RAM (an A500 with the trapdoor expansion) | 1 MB chip RAM (an A500+ or an A600) and 1 MB fast RAM |
        | RocketballA500 | 512 KB chip RAM and 512 KB slow RAM (an A500 with the trapdoor expansion) | 1 MB chip RAM (an A500+ or an A600) and 1 MB fast RAM |
        | RocketballRemake | 1 MB chip RAM (an A500+ or an A600) and 2 MB fast RAM | the same |

        On an A500 with 512 KB + 512 KB the margin is very small: start the game straight from a startup-sequence. With the
        Workbench open or other programs running it may not start.
      - **AmiSync** users: AmiSync 0.4.0 or newer.
      - **Windows and Mac:** not code-signed. Windows and macOS warn the first time.

      **Quality assurance**

      - **Automatic scenes:** every edition, the A500 one included, was driven automatically through the game's situations
        and compared with the original running in a C64 emulator. The situations: the title and its keys, the kick-off,
        playing against the computer, the end of a match and extra time, RUN/STOP, the Remake's bike. This ran on the PC/Mac
        program (on the Mac) and on an emulated Amiga.
      - **Long games:** an automatic player played long games on the emulated Amiga, with an alarm for a game that stops
        moving.
      - **Same arena on Mac and Amiga:** another alarm compares the arena drawn on the Mac with the one drawn on the Amiga.
      - **Amiga memory:** the requirement above was measured on nine Amiga machine configurations, from 512 KB chip RAM to
        2 MB chip + 8 MB fast.
      - **By hand:** the final test build was played on a real Amiga, an Amiga 2000 with a PiStorm.

      **Files:**
      - Amiga: `Rocketball_v2.1.lha` (Rocketball and RocketballA500), `Rocketball_Remake_v2.1.lha`, and the bootable floppy
        in `Rocketball_Amiga_ADF_v2.1_2026-11-20.zip`.
      - Windows: `Rocketball_PC_v2.1_win64.zip`.
      - Mac: `Rocketball_PC_v2.1_macos-universal.zip`.

      The PC and Mac packages are the same ones the Reforge Arcade launcher installs:
      https://www.bonomo.cloud/launcher/
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
---
Two teams of five skaters race around a banked track. One steel ball. Score by throwing it into the goal in the wall, and stop the other team by any means: elbows, charges, and in the remake, motorbikes.

**Rocketball** was written for the Commodore 64 by IJK Software in 1985 (programmed by John Sinclair, music by L. Pilling). In Italy it reached the newsstands as **Roller Ball**. Its inspiration is plain to see: the 1975 film *Rollerball*.

This project brings it to the Amiga in two editions, on one page:
- **Rocketball 2.1**, the original edition: the C64 game as it was, now also for a stock A500.
- **Rocketball Remake 2.1**: the same game underneath, with a new look, new rules and the bikes of the film.

**New in 2.0: a new engine.** Every edition is rebuilt from scratch: the C64 game rewritten as C, routine by routine, and checked against a C64 emulator at every frame and every CPU cycle, with a new Amiga layer for the screen, the sound and the controls. What you get: an A500 version that keeps the C64's speed, the ball's sound effects (lost in 1.x), the announcer in stereo, and every remake option working.

## The Original Edition: The C64 Game, Rebuilt

The original 6502 game is rewritten as C, routine by routine, and compiled into native 68000 code. It is translated, not emulated: the Amiga runs IJK Software's own game logic, with the same rules, the same timing and the same computer opponents.

The rewritten game is checked against a C64 emulator at every frame and every CPU cycle.

- Two versions: `rb` for a 68020 or better (A1200, accelerators, PiStorm) and `rb_a500` for a stock A500 (68000, 1 MB). On an A500 the game keeps the C64's speed: the screen shows fewer pictures a second, the game and the sound do not slow down.
- The original graphics.
- The sound: the SID's music and effects rebuilt for Paula, the ball's bounces included.
- One player against the computer (levels 1-6), or two players with two joysticks.

## The Remake: New Look, New Rules

The remake keeps the recompiled C64 game as its engine and changes what you see and how it plays.

**New look**
- The arena, the crowd, the skaters and the panel redrawn, full screen (256 lines).
- Four teams with their own colours: Tokyo, Napoli, Madrid, Moscow.
- An announcer calling the action, in stereo.
- A panel with a radar of the whole track.

**The bikes**
- **Kick-off on bikes.** After a goal, two bikes tow the team that conceded onto the track, and the ball comes down to their first towed skater.
- **Bikes in play** (a power-up). Each team's power bar fills in 2 minutes of play. When it is full, hold fire to call your bike. It rides for 10 seconds and knocks down every opponent within its reach, never its own team; when its time is up it rides off fast. The computer teams call theirs too. One bike on the track at a time.

**New rules**
- The ball is caught on contact, not only when crouching.
- Passes and shots: fire + left passes forward, fire + right shoots at goal, fire + up jumps with the ball.
- The automatic pass: fire + down sends the ball to the nearest free team-mate.
- Dash and stamina: fire alone gives a burst of speed, paid with the team's stamina.
- Wider goals, rebounds off the wall.
- The charge: whoever runs into an opponent knocks him down and stays up (the slower one falls).
- The shot knocks down an opponent in its way.
- Smarter computer teams: a moving zone defence, a keeper, escorts for the carrier.
- 11 sprites: no skater jumping to the edge of the screen when the C64 runs out of sprites.
- Both teams can be played by the computer (levels 1-6), with a demo on the title screen.
- The title menu by joystick: up and down choose a key, left and right do it, fire plays.
- The options are kept: saved in `rb_remake.cfg` next to the game when you leave the options page (the options saved with 1.x are read).
- Every option works, the fall rules too (C64, REMAKE, CHARGE).

**Every new rule can be switched back to the C64's** on the options page (F7 on the title screen), one by one or all at once (ball catch, fire controls and dash change together).

## Requirements

| Edition | Memory | CPU | Kickstart | Chipset |
|---|---|---|---|---|
| Rocketball 2.1 (original) | 1 MB: 512 KB chip + 512 KB other memory (WHDLoad: 512 KB chip + 704 KB fast) | 68000 (`rb_a500`, a stock A500) or 68020 or better (`rb`) | 1.3 or later | OCS, ECS, AGA |
| Rocketball Remake 2.1 | 1 MB chip + about 1.2 MB other memory | a fast Amiga: PiStorm, a fast 68030, 68040 / 68060 accelerators, emulators with JIT | 2.0 or later recommended | ECS or AGA (1 MB chip; an OCS Amiga has at most 512 KB) |

The remake is made for fast Amigas. A stock A1200 (2 MB chip, no fast memory) cannot start it; with a 68020 and fast memory the game keeps its speed but shows about 12 pictures a second.

**Tested:**
- On a real Amiga with a PiStorm.
- In WinUAE: the original on an A500 (68000) and on a 68030, the remake on a 68030; from AmigaDOS and with WHDLoad.

## Installation

The ADF holds the original edition and boots into a menu: 1 the A500 version, 2 the 68020 one. From the Workbench, its Install icon puts it on the hard disk. The remake (1.3 MB) does not fit a floppy: hard disk only. For the hard disk, unpack a .lha pack anywhere: its DOS icon starts the game straight from AmigaDOS, with no WHDLoad needed (on a 68000 it starts the A500 version). With WHDLoad (17 or later), from the Shell: `WHDLoad Rocketball.slave` (68020), `WHDLoad RocketballA500.slave` (A500) or `WHDLoad RocketballRemake.slave`.

Updating from 1.x: replace everything (the WHDLoad drawer, the .lha pack, the floppy). The 1.x port stays available on GitHub.

## Controls

Joystick in port 2, or the cursor keys with SPACE or CTRL to fire. In the original's two-player mode, team 1 uses port 1.

| Title screen | Original | Remake |
|---|---|---|
| F1 / F3 | Team 1 / team 2 colour | Team 1 / team 2 colour (the team) |
| F5 | Level against the computer (1-6) or two players | Team 1: human or computer (levels 1-6) |
| F6 | | Team 2: human or computer (levels 1-6) |
| F7 | Border colour | The options (the rules) |
| Fire | Start the match | Start the match |

In the remake the joystick also works the title menu: up / down choose a key, left / right do it, fire plays.

| In play | Without the ball | With the ball (remake) |
|---|---|---|
| Fire + up | Jump | Jump with the ball |
| Fire + down | Crouch (catch a rolling ball) | Automatic pass |
| Fire + left / right | Strike (elbow) | Pass forward / shot at goal |
| Fire alone | Dash (remake) | |
| Fire held | Call your bike when the power bar is full (remake) | |

Alt+P: pause. BACKSPACE or R: back to the title (RUN/STOP). Alt+M: sound off / on; Alt+plus / minus: volume. Alt+Q or Esc: quit.

The full controls, the options one by one and some advice on play are in the manual.

## Feedback

Please report what you find: every report helps.

## Credits

- **Rocketball**, Commodore 64, © 1985 IJK Software: programmed by John Sinclair, music by L. Pilling. Published in Italy as Roller Ball.
- Inspired by the film *Rollerball* (1975).
- **Amiga conversion and remake:** Massimo Bonomo, 2026.

---

*This is a fan tribute. Rocketball is © 1985 IJK Software. Rollerball (1975) is cited only as the original game's inspiration; this project is not affiliated with its rights holders.*
