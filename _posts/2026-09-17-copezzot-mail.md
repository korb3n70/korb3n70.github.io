---
title: "Copezzot Mail: un client email per Outlook con Claude AI"
date: 2026-09-17 10:30:00 +0200
categories: [Progetti, PowerShell]
tags: [powershell, outlook, claude, ai, winforms, email, anthropic]
description: Un client email leggero per Windows, scritto in un solo script PowerShell, che usa Outlook e Claude per scrivere e rispondere alle email.
image:
  path: /assets/img/posts/copezzot-mail.jpeg
  alt: Copezzot Mail AI Assistant
---

**Copezzot Mail AI Assistant** è un client email per Windows che sta tutto in **un unico script PowerShell** con interfaccia **WinForms**. Non parla direttamente con i server di posta: si appoggia a **Outlook desktop** tramite automazione COM e usa **Claude** (API Anthropic) per scrivere nuove email e rispondere a quelle ricevute.

> **Progetto su GitHub:** [github.com/korb3n70/Mail-AI-Assistant](https://github.com/korb3n70/Mail-AI-Assistant)
{: .prompt-info }

L'idea è semplice: scrivi due righe di istruzioni ("rispondi che accetto, ma sposta la riunione a giovedì"), scegli lingua e tono, e Claude prepara il testo. Tu lo ritocchi e lo invii. Col tempo l'app impara anche **come scrivi tu**.

## Cosa fa

- **Posta in arrivo** con elenco ordinabile, email non lette evidenziate e anteprima HTML
- **Nuova email, Rispondi, Rispondi a tutti, Inoltra** con editor rich-text e toolbar di formattazione
- **Genera AI**: lingua (IT, EN, FR, DE, ES), tono (formale, professionale, amichevole, informale, conciso) e istruzioni libere
- **Bozze** salvate sia in locale sia nella cartella Bozze di Outlook
- **Multi-account**: si sceglie quale account Outlook usare (Office 365, Gmail, IMAP...)
- **Autocompletamento** dei destinatari da una cache dei contatti
- **Immagini remote bloccate** nell'anteprima, con pulsante "Scarica immagini" su richiesta
- **Il mio stile**: profilo di scrittura personale appreso dalle tue correzioni
- **Splash screen** con avanzamento reale durante il caricamento delle email

## Requisiti

- Windows con **Outlook desktop** installato e con almeno un account configurato
- **PowerShell 5.1** o superiore
- Una **API key Anthropic** ([console.anthropic.com](https://console.anthropic.com))

Nessun'altra dipendenza: niente moduli da installare, niente librerie esterne.

## Architettura

### Outlook come motore

Tutta la parte di posta passa da `New-Object -ComObject Outlook.Application`. Lettura della Inbox, invio, bozze, risoluzione dei mittenti Exchange: se ne occupa Outlook, con la sessione già autenticata. Il vantaggio è che **lo script non vede e non memorizza mai le password delle caselle email**, e funziona con qualsiasi account che Outlook sa gestire.

### Claude via HttpWebRequest

Le chiamate all'API Messages sono fatte con `System.Net.HttpWebRequest` e non con `Invoke-RestMethod` o `WebClient`. In PowerShell 5 questi ultimi creano problemi di codifica (UTF-8 con BOM, lettere accentate rovinate), quindi il corpo della richiesta viene costruito a mano in **UTF-8 senza BOM**.

Dalle impostazioni si sceglie il modello:

| Modello | Uso consigliato |
|---------|-----------------|
| Claude Haiku 4.5 | Default: veloce ed economico, ottimo per le email |
| Claude Sonnet | Qualità superiore |
| Claude Opus | Testi lunghi o complessi |

### Prompt pensati per le email vere

Scrivere email con un LLM sembra banale, ma nei thread reali saltano fuori problemi precisi. Il system prompt è stato raffinato versione dopo versione per:

- dare **priorità assoluta alle istruzioni dell'utente** rispetto al contenuto dell'email originale
- **non firmare mai con nomi presi dal thread**: in una catena di risposte ci sono firme di colleghi e altri mittenti, e l'AI tendeva a copiarle. Ora firma solo con il nome impostato nel campo "Nome per firma"
- distinguere **risposta** e **inoltro**: nell'inoltro scrive un testo introduttivo, non una risposta al mittente originale
- rispettare davvero la **lingua scelta**, scrivendo il system prompt in inglese

### Il mio stile

È la parte più interessante. Quando invii un'email generata dall'AI **dopo averla modificata**, l'app manda a Claude Haiku tre cose: il profilo di stile attuale, la bozza dell'AI e la tua versione finale. Claude aggiorna un breve riassunto (massimo 100 parole) di come scrivi: tono, lunghezza delle frasi, struttura, livello di dettaglio.

Il profilo viene poi aggiunto al prompt delle generazioni successive. Un dettaglio che ha richiesto qualche tentativo: lo stile va descritto **in modo astratto**. Se il profilo dice "saluta con *Ciao*", scrivendo un'email in inglese l'AI infilava un "Ciao" nel testo. Ora il profilo descrive il registro ("saluto informale e breve") e mai le parole letterali.

Apprendimento e utilizzo si attivano con due interruttori separati, il profilo si può modificare a mano o azzerare, e c'è un file diverso per ogni account email. Se la bozza non è stata toccata non parte nessuna chiamata, quindi nessun costo.

### Una nota su PowerShell 5 e le closure

Nel codice ci sono tante righe come `$script:rOrigEmail = $controllo`. Non sono ridondanti: in PowerShell 5 gli scriptblock degli eventi WinForms (`Add_Click`, `Add_TextChanged`...) **non catturano le variabili locali** della funzione in cui sono definiti. L'unico modo affidabile per farle vedere agli handler è lo scope `$script:`. Diversi bug delle versioni precedenti (corpo della risposta vuoto, destinatari persi) venivano da qui.

## Privacy e dati locali

Tutti i dati dell'app restano sul PC, in `%USERPROFILE%\MailClient\`:

| File | Contenuto |
|------|-----------|
| `creds.xml` | API key cifrata con **DPAPI**, leggibile solo dallo stesso utente Windows sullo stesso PC |
| `app_settings.json` | Preset AI, colori, messaggio di benvenuto, font |
| `contacts_cache.json` | Indirizzi per l'autocompletamento |
| `drafts.json` | Bozze locali |
| `style_<email>.json` | Profilo di stile personale |

Nelle impostazioni c'è il pulsante **"Azzera dati personali"** per cancellare tutto prima di passare lo script a qualcun altro. L'anteprima blocca immagini e CSS remoti: niente pixel di tracciamento, e l'interfaccia non si blocca più per secondi in attesa di risorse esterne.

L'unico dato che esce dal PC è il testo inviato a Claude quando premi "Genera AI" (e, se l'apprendimento è attivo, la bozza con la tua versione finale).
{: .prompt-info }

## Installazione

Lo script ha un **self-installer**. Basta estrarre i file in una cartella qualsiasi e fare doppio click su **`esegui.cmd`**. Al primo avvio lo script:

1. crea `%USERPROFILE%\MailClient\`
2. copia lì se stesso e i file accanto (`favicon.ico`, `copezzot_logo.jpeg`, `changelog.txt`, `esegui.cmd`)
3. crea sul Desktop lo shortcut **Copezzot Mail AI Assistant**, se non c'è già
4. si rilancia dalla copia installata

Dagli avvii successivi si usa lo shortcut. `esegui.cmd` esiste solo per aggirare l'ExecutionPolicy e usa un percorso relativo (`%~dp0`), quindi funziona da qualunque cartella:

```bat
powershell -ExecutionPolicy Bypass -File "%~dp0clientmail_outlook_v20.ps1"
```

Poi, nel tab **Impostazioni**, si inserisce la API key e si sceglie l'account Outlook.

## Com'è cresciuto

| Versione | Novità principali |
|----------|-------------------|
| v10 | Prima versione: composizione e invio con allegati tramite Outlook |
| v11 | Lettura della Inbox e anteprima HTML |
| v12 | Bozze in Outlook e API key cifrata con DPAPI |
| v13 | Prima integrazione AI per le risposte |
| v14 | Bozze ibride (JSON + Outlook), mittenti Exchange |
| v15 | Inbox a colonne ordinabili, non lette in evidenza, changelog in-app |
| v19 | Lingua e tono nel dialog AI, inoltro separato dalla risposta, fix di codifica |
| v20 | Toolbar completa, multi-account, "Il mio stile", blocco immagini remote, splash screen, self-installer |

Oggi sono circa **3.800 righe** di PowerShell in un solo file. Non è il linguaggio più comodo per un'interfaccia grafica, ma ha un pregio che ha guidato tutto il progetto: su qualunque PC Windows con Outlook **funziona subito**, senza installare nulla.
