---
title: Wizard of Wor
piattaforma: Amiga 500 OCS
anno_originale: 1983
order: 1
sommario: >-
  La cartuccia Commodore del 1983 portata su Amiga 500 per ricompilazione
  statica, con la voce del Mago ricostruita dal Magic Voice.
requisiti: >-
  Amiga 500 OCS con 512 KB chip + 512 KB di altra memoria. Disco ADF
  autoavviante oppure installazione WHDLoad.

# >>> da qui in giu' scrive sync-giochi.py: non modificare a mano
versione: "1.2.1"
data_versione: 2026-10-25
cartella: wizard-of-wor
repo: "korb3n70/wow-amiga-port"
schermate:
  - file: /assets/img/giochi/wizard-of-wor/wizard_of_wor_amiga_1_title_page.png
  - file: /assets/img/giochi/wizard-of-wor/wizard_of_wor_amiga_2_points.png
  - file: /assets/img/giochi/wizard-of-wor/wizard_of_wor_amiga_3_dungeon.png
download:
  - nome: "Dischetti ADF (floppy o emulatore)"
    file: "WizardOfWor_Amiga_ADF_v1.2.1_2026-10-25.zip"
    dimensione: "2,3 MB"
  - nome: "WHDLoad · voce Magic Voice"
    file: "WizardOfWor_MagicVoice_v1.2.1.lha"
    dimensione: "1,2 MB"
  - nome: "WHDLoad · voce nuova"
    file: "WizardOfWor_Voice2026_v1.2.1.lha"
    dimensione: "1,6 MB"
  - nome: "WHDLoad · versione fedele"
    file: "WizardOfWor_v1.2.1.lha"
    dimensione: "824 KB"
changelog:
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
Nei sotterranei di Wor si entra in due. Si spara ai Burwor, si aspetta che i
Worluk diventino invisibili, e intanto una voce cavernosa ti prende in giro
dagli altoparlanti. **Wizard of Wor** uscì nel 1983 su cartuccia per Commodore
64, ed è uno dei pochi giochi dell'epoca in cui il nemico ti parlava.

Questo è un port fedele per **Amiga 500 OCS**, distribuito come disco ADF
autoavviante e come installazione WHDLoad.

## Come è fatto

Il metodo è la **ricompilazione statica**: il codice 6502 della cartuccia è
stato disassemblato e tradotto in codice 68000 nativo, senza reinterpretare la
logica di gioco. Sopra ci sta uno strato che riproduce sull'Amiga quello che il
gioco si aspetta dal C64: VIC-II, SID, CIA e joystick.

Il disassemblato è verificato nel modo più semplice e più severo possibile: si
riassembla e deve tornare **identico byte per byte** alla ROM di partenza. Se
cambia un solo byte, l'analisi è sbagliata da qualche parte.

## La voce del Mago

Sul C64 la voce non usciva dal SID: arrivava da una cartuccia a parte, il
**Magic Voice**, un sintetizzatore vocale basato sul chip Toshiba T6721A che in
Italia non vide quasi nessuno. Senza quella cartuccia il gioco resta muto.

Per riaverla ho catturato e risintetizzato le frasi partendo dalla ROM del
Magic Voice, e le ho trasformate in campioni che Paula può suonare. Di qui le
tre edizioni WHDLoad: quella **fedele** senza voce, quella con la voce
**Magic Voice** ricostruita com'era, e una con una **voce nuova** registrata
per l'occasione.

Lungo la strada è venuta fuori anche la documentazione dello schema del Magic
Voice, abbastanza dettagliata da poterne ricostruire una cartuccia moderna
equivalente.
