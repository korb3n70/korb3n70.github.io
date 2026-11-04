#!/usr/bin/env python3
"""
Allinea la sezione Giochi del blog alle Release su GitHub.

    python tools/sync-giochi.py            # mostra cosa cambierebbe
    python tools/sync-giochi.py --scrivi   # applica le modifiche

Cosa fa, per ogni gioco elencato in GIOCHI:

  1. legge l'ultima release del repo (anche privato) con `gh`;
  2. scarica gli allegati nella cartella dei file di statsrv, da dove verranno
     caricati su bonomo.cloud;
  3. scarica le schermate da promo/ dentro assets/img/giochi/<slug>/;
  4. riscrive la parte GENERATA del front matter di _giochi/<slug>.md:
     versione, data, elenco dei download e changelog;
  5. se la release allega anche article.md, riscrive l'articolo del blog in
     _posts/: titolo, sommario, copertina, corpo, richiamo al download,
     blocco delle donazioni e crediti. Il formato e' in tools/ARTICOLI.md.

La descrizione del gioco e tutto cio' che sta sopra il marcatore restano
intatti: il testo lo scrivi tu, i numeri li aggiorna lo script.

Serve `gh` autenticato (gh auth status). I repo sono privati: senza
autenticazione non si vede nulla.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# --------------------------------------------------------------------------
# Configurazione
# --------------------------------------------------------------------------

# slug -> repo GitHub. Lo slug e' sia il nome del file in _giochi/ sia la
# cartella dei download sul server: cambiarlo cambia anche gli indirizzi.
GIOCHI = {
    "wizard-of-wor": "korb3n70/wow-amiga-port",
    "forbidden-forest": "korb3n70/forbidden-forest-amiga",
    "rocketball": "korb3n70/rollerball-amiga",
}

BLOG = Path(__file__).resolve().parent.parent
# I file scaricabili vivono fuori dal webroot, accanto al codice di statsrv.
STATSRV_FILES = Path(r"C:\Users\Utente\Desktop\statsrv\private\files\korb3n70")

CHANGELOG_MAX = 6

# Il marcatore non puo' contenere "---": quella sequenza a inizio riga
# delimita il front matter, e Jekyll taglierebbe il file proprio li'.
MARCATORE = "# >>> da qui in giu' scrive sync-giochi.py: non modificare a mano"

# La pagina del sito, scritta nel repo del gioco e allegata alla release.
# Quando c'e', e' lei la fonte: testo, sommario, requisiti ed etichette dei
# download vengono da li', in inglese. Questo script traduce i NOMI dei campi
# in quelli che il layout del blog gia' conosce, non il contenuto.
PAGINA = "game.md"

CAMPI = {
    "platform": "piattaforma",
    "original": "originale",
    "original_year": "anno_originale",
    "summary": "sommario",
    "requirements": "requisiti",
}

# Campi di game.md che il blog non usa: versione e data si prendono dalla
# release, che e' la fonte di verita' su cosa e' davvero pubblicato; le
# schermate le costruisce questo script dai file in promo/, con i percorsi
# giusti; page_url punta a game.md stesso; downloads viene ricostruito dagli
# allegati veri e arricchito con le etichette di game.md.
CAMPI_SCARTATI = {"version", "date", "screenshots", "page_url", "downloads", "repo"}

# L'articolo del blog, anch'esso scritto nel repo del gioco e allegato alla
# release. E' un'altra cosa dalla pagina: racconta la storia del gioco, sta in
# italiano e cambia di rado. Il formato e' descritto in tools/ARTICOLI.md.
ARTICOLO = "article.md"

# Ne' game.md ne' article.md sono file da scaricare: sono il sito, non il
# gioco, e non devono finire sul server accanto agli archivi.
ALLEGATI_MD = {PAGINA, ARTICOLO}

# Quello che il post ha di fisso. I tag e le categorie non stanno in
# article.md di proposito: sono una scelta su come si naviga il blog, non
# qualcosa che riguardi il singolo gioco.
CATEGORIE = "[Giochi, Amiga]"
TAG_FISSI = ["amiga", "c64", "reforge", "retrogaming"]

# L'ora nella data del post. Conta solo perche' Jekyll ordina a parita' di
# giorno; il fuso e' quello in cui il blog e' scritto.
ORA_POST = "09:00:00 +0100"

# Come il marcatore delle pagine: dice a chi apre il file che non e' il posto
# dove scrivere. Qui vale per tutto il post, non per una parte.
MARCATORE_ARTICOLO = (
    "# scritto da sync-giochi.py da " + ARTICOLO + ": le modifiche si fanno li'"
)

GH = shutil.which("gh") or r"C:\Program Files\GitHub CLI\gh.exe"


# --------------------------------------------------------------------------
# Utilita'
# --------------------------------------------------------------------------

def gh_json(*args):
    """Esegue gh e restituisce il JSON. Fallisce rumorosamente: se GitHub non
    risponde e' meglio fermarsi che riscrivere le pagine con dati a meta'."""
    res = subprocess.run([GH, *args], capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        raise SystemExit(f"gh {' '.join(args)} non riuscito:\n{res.stderr.strip()}")
    return json.loads(res.stdout)


def peso(byte):
    """Dimensione leggibile. Gli Amiga-isti contano ancora in KB."""
    if byte < 1024:
        return f"{byte} B"
    if byte < 1024 * 1024:
        return f"{round(byte / 1024)} KB"
    return f"{byte / 1024 / 1024:.1f} MB".replace(".", ",")


def etichetta(nome_file):
    """
    Nome leggibile della versione, ricavato dal nome del file.

    Le convenzioni sono quelle usate nelle release dei tre giochi; quando non
    corrisponde niente si ripiega sull'estensione, che distingue comunque il
    disco (.zip con dentro gli ADF) dall'archivio WHDLoad (.lha).
    """
    n = nome_file.lower()
    if "_adf_" in n or n.endswith(".adf"):
        return "Dischetti ADF (floppy o emulatore)"
    if "magicvoice" in n:
        return "WHDLoad · voce Magic Voice"
    if "voice2026" in n:
        return "WHDLoad · voce nuova"
    if "fast" in n:
        return "WHDLoad · versione veloce"
    if "remake" in n:
        return "WHDLoad · remake"
    if n.endswith((".lha", ".lzx")):
        return "WHDLoad · versione fedele"
    return nome_file


def blocchi_yaml(fm):
    """Divide un front matter nei suoi campi di primo livello.

    Restituisce (chiave, righe) conservando le righe come sono scritte: liste,
    blocchi letterali e stringhe su piu' righe restano intatti. Serve proprio a
    non dover interpretare lo YAML per rinominare una chiave.
    """
    blocchi, chiave, righe = [], None, []
    for r in fm.splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):(.*)$", r)
        if m:
            if chiave is not None:
                blocchi.append((chiave, righe))
            chiave, righe = m.group(1), [r]
        elif chiave is not None:
            righe.append(r)
    if chiave is not None:
        blocchi.append((chiave, righe))
    return blocchi


def allegato_md(repo, tag, assets, nome):
    """Un .md allegato alla release: (front matter, corpo), oppure None.

    Serve sia per game.md sia per article.md: la forma e' la stessa, front
    matter YAML e corpo Markdown, e cambia solo cosa ci si legge dentro.
    """
    if not any(a["name"] == nome for a in assets):
        return None

    tmp = Path(tempfile.mkdtemp())
    try:
        subprocess.run(
            [GH, "release", "download", tag, "--repo", repo,
             "--pattern", nome, "--dir", str(tmp), "--clobber"],
            check=True, capture_output=True,
        )
        testo = (tmp / nome).read_text(encoding="utf-8")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", testo, re.S)
    if not m:
        raise SystemExit(f"{repo}: {nome} non ha un front matter riconoscibile.")
    return m.group(1), m.group(2)


def etichette_da_pagina(fm):
    """Etichetta e descrizione di ogni file, dal blocco downloads di game.md."""
    out, corrente, dentro = {}, None, False
    for r in fm.splitlines():
        if re.match(r"^downloads:", r):
            dentro = True
            continue
        if dentro and re.match(r"^[A-Za-z_]", r):
            break
        if not dentro:
            continue
        m = re.match(r"\s*-\s*file:\s*(.+)$", r)
        if m:
            corrente = m.group(1).strip().strip('"')
            out[corrente] = {}
            continue
        m = re.match(r"\s+(label|description):\s*(.+)$", r)
        if m and corrente:
            out[corrente][m.group(1)] = m.group(2).strip().strip('"')
    return out


def campi_md(fm):
    """I campi di primo livello di un front matter, come valori di Python.

    Riconosce le tre forme che article.md usa: valore sulla stessa riga,
    blocco ripiegato (">-", le righe diventano un paragrafo unico) ed elenco
    (in linea fra parentesi quadre oppure una voce per riga). Basta per questo
    formato e non obbliga a installare PyYAML sulla macchina di chi pubblica.
    """
    out = {}
    for chiave, righe in blocchi_yaml(fm):
        resto = righe[0].split(":", 1)[1].strip()
        seguito = [r for r in righe[1:] if r.strip()]

        if resto in (">", ">-", "|", "|-", ""):
            testo = [r.strip() for r in seguito]
            if resto.startswith("|"):
                out[chiave] = "\n".join(testo)
            elif all(r.startswith("- ") for r in testo) and testo:
                out[chiave] = [r[2:].strip().strip('"\'') for r in testo]
            else:
                out[chiave] = " ".join(testo)
            continue

        if resto.startswith("[") and resto.endswith("]"):
            out[chiave] = [v.strip().strip('"\'') for v in resto[1:-1].split(",") if v.strip()]
            continue

        out[chiave] = resto.strip('"\'')
    return out


def yaml_testo(s):
    """Stringa YAML sempre fra virgolette: i titoli contengono ':' e apostrofi."""
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def blocco_yaml(righe, indent=0):
    return "\n".join(" " * indent + r for r in righe)


# --------------------------------------------------------------------------
# Raccolta dati da GitHub
# --------------------------------------------------------------------------

def releases(repo):
    """Tutte le release pubblicate, dalla piu' recente. Le bozze non esistono
    per il pubblico, quindi non entrano nel changelog."""
    dati = gh_json(
        "release", "list", "--repo", repo, "--limit", "30",
        "--json", "tagName,name,publishedAt,isDraft,isPrerelease",
    )
    return [r for r in dati if not r["isDraft"]]


def release_completa(repo, tag):
    return gh_json(
        "release", "view", tag, "--repo", repo,
        "--json", "tagName,name,publishedAt,body,assets",
    )


def scarica_allegati(repo, tag, assets, dest, scrivi):
    """Scarica gli allegati mancanti e toglie quelli di versioni superate."""
    cambi = []
    assets = [a for a in assets if a["name"] not in ALLEGATI_MD]
    attesi = {a["name"] for a in assets}

    if scrivi:
        dest.mkdir(parents=True, exist_ok=True)

    for a in assets:
        f = dest / a["name"]
        if f.exists() and f.stat().st_size == a["size"]:
            continue
        cambi.append(f"  + {a['name']} ({peso(a['size'])})")
        if scrivi:
            subprocess.run(
                [GH, "release", "download", tag, "--repo", repo,
                 "--pattern", a["name"], "--dir", str(dest), "--clobber"],
                check=True,
            )

    if dest.is_dir():
        for f in sorted(dest.iterdir()):
            if f.is_file() and f.name not in attesi:
                cambi.append(f"  - {f.name} (versione superata)")
                if scrivi:
                    f.unlink()

    return cambi


def scarica_schermate(repo, slug, scrivi):
    """Immagini da promo/ del repo. I video restano fuori: vanno su YouTube."""
    try:
        contenuti = gh_json("api", f"repos/{repo}/contents/promo")
    except SystemExit:
        return [], []

    immagini = sorted(
        (c for c in contenuti
         if c["type"] == "file" and c["name"].lower().endswith((".png", ".jpg", ".jpeg"))),
        key=lambda c: c["name"],
    )

    dest = BLOG / "assets" / "img" / "giochi" / slug
    cambi, elenco = [], []

    if scrivi and immagini:
        dest.mkdir(parents=True, exist_ok=True)

    for img in immagini:
        f = dest / img["name"]
        elenco.append(f"/assets/img/giochi/{slug}/{img['name']}")
        if f.exists() and f.stat().st_size == img["size"]:
            continue
        cambi.append(f"  + schermata {img['name']} ({peso(img['size'])})")
        if scrivi:
            subprocess.run(
                [GH, "api", f"repos/{repo}/contents/promo/{img['name']}",
                 "-H", "Accept: application/vnd.github.raw"],
                stdout=f.open("wb"), check=True,
            )

    return cambi, elenco


# --------------------------------------------------------------------------
# Scrittura del file del gioco
# --------------------------------------------------------------------------

def front_matter_generato(slug, repo, rel, tutte, schermate, pagina):
    """Costruisce la parte di front matter che questo script possiede."""
    assets = sorted((a for a in rel["assets"] if a["name"] not in ALLEGATI_MD),
                    key=lambda a: a["name"])
    righe = [MARCATORE]
    etichette = {}

    if pagina:
        fm_pagina = pagina[0]
        etichette = etichette_da_pagina(fm_pagina)
        for chiave, blocco in blocchi_yaml(fm_pagina):
            if chiave in CAMPI_SCARTATI:
                continue
            blocco = list(blocco)
            blocco[0] = blocco[0].replace(chiave + ":", CAMPI.get(chiave, chiave) + ":", 1)
            righe.extend(blocco)

    righe += [
        f"versione: {yaml_testo(rel['tagName'].lstrip('v'))}",
        f"data_versione: {rel['publishedAt'][:10]}",
        f"cartella: {slug}",
        f"repo: {yaml_testo(repo)}",
    ]

    if schermate:
        righe.append("schermate:")
        for s in schermate:
            righe.append(f"  - file: {s}")

    righe.append("download:")
    for a in assets:
        info = etichette.get(a["name"], {})
        righe.append(f"  - nome: {yaml_testo(info.get('label') or etichetta(a['name']))}")
        righe.append(f"    file: {yaml_testo(a['name'])}")
        righe.append(f"    dimensione: {yaml_testo(peso(a['size']))}")
        if info.get("description"):
            righe.append(f"    descrizione: {yaml_testo(info['description'])}")

    # Solo le ultime release: la pagina del gioco non e' un archivio, e dopo
    # qualche versione il changelog diventa piu' lungo del gioco stesso.
    righe.append("changelog:")
    for r in tutte[:CHANGELOG_MAX]:
        corpo = (r.get("body") or "").strip()
        # Il corpo della release e' testo di chi lo ha scritto: va rientrato
        # come blocco letterale, altrimenti un ':' qualsiasi rompe lo YAML.
        righe.append(f"  - versione: {yaml_testo(r['tagName'].lstrip('v'))}")
        righe.append(f"    data: {r['publishedAt'][:10]}")
        if corpo:
            righe.append("    note: |")
            for riga in corpo.splitlines():
                righe.append("      " + riga if riga.strip() else "")

    return "\n".join(righe)


def aggiorna_file(slug, repo, rel, tutte, schermate, pagina, scrivi):
    percorso = BLOG / "_giochi" / f"{slug}.md"

    if not percorso.exists():
        manuale = "\n".join([
            "---",
            f"title: {yaml_testo(slug.replace('-', ' ').title())}",
            "piattaforma: Amiga 500",
            "order: 99",
            "sommario: >-",
            "  Due righe di presentazione, da scrivere.",
            "requisiti: Amiga 500 con 512 KB di memoria aggiuntiva.",
            "",
        ])
        corpo = "\n\nDescrizione del gioco, da scrivere.\n"
    else:
        testo = percorso.read_text(encoding="utf-8")
        # Il front matter si delimita con '---' a inizio riga, e nient'altro:
        # dividere sulla semplice stringa '---' spezzerebbe il file al primo
        # trattino lungo che capita dentro le note di una release.
        m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", testo, re.S)
        if not m:
            raise SystemExit(f"{percorso}: front matter non riconosciuto.")
        fm, corpo = m.group(1), "\n" + m.group(2)
        # Via la parte generata la volta scorsa, resta quella scritta a mano.
        manuale = "---\n" + fm.split(MARCATORE)[0].rstrip() + "\n"

    if pagina:
        # Con game.md la pagina appartiene al repo del gioco: testo, sommario e
        # requisiti arrivano da li'. Al blog resta solo 'order', che e' una
        # scelta su come ordinare l'elenco e non riguarda il gioco.
        ordine = re.search(r"^order:.*$", manuale, re.M)
        manuale = "---\n" + (ordine.group(0) if ordine else "order: 99") + "\n"
        corpo = "\n" + pagina[1].lstrip("\n")

    nuovo = (manuale + "\n"
             + front_matter_generato(slug, repo, rel, tutte, schermate, pagina)
             + "\n---" + corpo)

    if percorso.exists() and percorso.read_text(encoding="utf-8") == nuovo:
        return None

    if scrivi:
        percorso.parent.mkdir(parents=True, exist_ok=True)
        percorso.write_text(nuovo, encoding="utf-8", newline="\n")

    return f"  * {percorso.relative_to(BLOG)}"


# --------------------------------------------------------------------------
# Scrittura dell'articolo sul blog
# --------------------------------------------------------------------------

def post_esistente(slug):
    """Il post gia' pubblicato per questo gioco, se c'e'.

    Si cerca per slug invece di ricostruire il nome del file: nel nome c'e' la
    data della prima pubblicazione, che non si deve toccare perche' decide
    l'indirizzo del post e il suo posto nella home.
    """
    trovati = sorted((BLOG / "_posts").glob(f"*-{slug}*.md"))
    if len(trovati) > 1:
        raise SystemExit(
            f"{slug}: piu' di un post corrisponde ({', '.join(p.name for p in trovati)}). "
            "Tienine uno e rilancia."
        )
    return trovati[0] if trovati else None


def aggiorna_articolo(slug, titolo_gioco, rel, articolo, schermate, scrivi, riscrivi):
    """Scrive il post del blog da article.md. Restituisce (riga, avvisi)."""
    campi = campi_md(articolo[0])
    avvisi = []

    for obbligatorio in ("titolo", "sommario", "crediti"):
        if not campi.get(obbligatorio):
            avvisi.append(f"  ! {ARTICOLO}: manca {obbligatorio}, articolo non scritto")
    if avvisi:
        return None, avvisi

    vecchio = post_esistente(slug)

    # Un post scritto a mano non si sovrascrive senza dirlo: il testo
    # perderebbe tutto quello che non sta in article.md.
    if vecchio and MARCATORE_ARTICOLO not in vecchio.read_text(encoding="utf-8") and not riscrivi:
        return None, [
            f"  ! {vecchio.relative_to(BLOG)} e' scritto a mano: lo riscrivo solo con --riscrivi-articoli",
            f"    (prima controlla che {ARTICOLO} contenga davvero il testo buono)",
        ]

    # La data e' quella della prima pubblicazione, non della release: un
    # articolo corretto non deve risalire in cima alla home.
    if vecchio:
        m = re.search(r"^date:\s*(.+)$", vecchio.read_text(encoding="utf-8"), re.M)
        data = m.group(1).strip() if m else f"{rel['publishedAt'][:10]} {ORA_POST}"
        percorso = vecchio
    else:
        data = f"{rel['publishedAt'][:10]} {ORA_POST}"
        percorso = BLOG / "_posts" / f"{rel['publishedAt'][:10]}-{slug}-amiga.md"

    copertina = campi.get("copertina")
    if copertina:
        attesa = f"/assets/img/giochi/{slug}/{copertina}"
        if schermate and attesa not in schermate:
            avvisi.append(f"  ! copertina {copertina}: non e' fra le schermate in promo/")
        copertina = attesa
    elif schermate:
        copertina = schermate[0]

    tag = TAG_FISSI[:2] + [slug] + TAG_FISSI[2:]
    for t in campi.get("tag") or []:
        if t not in tag:
            tag.append(t)

    testa = [
        "---",
        f"title: {yaml_testo(campi['titolo'])}",
        f"date: {data}",
        f"categories: {CATEGORIE}",
        f"tags: [{', '.join(tag)}]",
        f"description: {yaml_testo(campi['sommario'])}",
    ]
    if copertina:
        alt = campi.get("copertina_alt")
        if not alt:
            avvisi.append(f"  ! {ARTICOLO}: manca copertina_alt, uso il titolo come descrizione")
            alt = campi["titolo"]
        testa += ["image:", f"  path: {copertina}", f"  alt: {yaml_testo(alt)}"]
    testa += [MARCATORE_ARTICOLO, "---"]

    coda = [
        f"> **Lo scarichi** dalla [pagina di {titolo_gioco}](/giochi/{slug}/):",
        "> dischetto avviabile e pacchetti WHDLoad, con versione e peso di ogni file.",
        "{: .prompt-info }",
        "",
        "## Sostieni il progetto",
        "",
        "Una conversione come questa nasce da molte ore di ingegneria inversa,",
        "ricompilazione e prove sull'hardware vero. Se il gioco ti è piaciuto e",
        "vuoi sostenere i prossimi progetti, pensa a una piccola donazione: anche",
        "un contributo minimo aiuta a coprire i costi.",
        "",
        "{% include dona.html %}",
        "",
        "---",
        "",
        f"*{campi['crediti']}*",
    ]

    nuovo = ("\n".join(testa) + "\n\n"
             + articolo[1].strip("\n") + "\n\n"
             + "\n".join(coda) + "\n")

    if percorso.exists() and percorso.read_text(encoding="utf-8") == nuovo:
        return None, avvisi

    if scrivi:
        percorso.parent.mkdir(parents=True, exist_ok=True)
        percorso.write_text(nuovo, encoding="utf-8", newline="\n")

    return f"  * {percorso.relative_to(BLOG)}", avvisi


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scrivi", action="store_true", help="applica le modifiche (senza, mostra soltanto)")
    ap.add_argument("--gioco", help="un solo gioco, per slug")
    ap.add_argument("--riscrivi-articoli", action="store_true",
                    help=f"sovrascrive i post scritti a mano con quello che dice {ARTICOLO}")
    args = ap.parse_args()

    giochi = {args.gioco: GIOCHI[args.gioco]} if args.gioco else GIOCHI
    if args.gioco and args.gioco not in GIOCHI:
        raise SystemExit(f"Gioco sconosciuto: {args.gioco}. Disponibili: {', '.join(GIOCHI)}")

    totale = []
    for slug, repo in giochi.items():
        print(f"\n=== {slug}  ({repo})")
        tutte = releases(repo)
        if not tutte:
            print("  nessuna release pubblicata, salto")
            continue

        rel = release_completa(repo, tutte[0]["tagName"])
        print(f"  ultima: {rel['tagName']} del {rel['publishedAt'][:10]}")

        complete = [release_completa(repo, r["tagName"]) for r in tutte[:CHANGELOG_MAX]]

        cambi = scarica_allegati(repo, rel["tagName"], rel["assets"],
                                 STATSRV_FILES / slug, args.scrivi)
        c2, schermate = scarica_schermate(repo, slug, args.scrivi)
        cambi += c2

        pagina = allegato_md(repo, rel["tagName"], rel["assets"], PAGINA)
        if pagina:
            print(f"  pagina dal repo: {PAGINA} (inglese)")
            nei_file = {a["name"] for a in rel["assets"] if a["name"] not in ALLEGATI_MD}
            nella_pagina = set(etichette_da_pagina(pagina[0]))
            for f in sorted(nella_pagina - nei_file):
                cambi.append(f"  ! {f}: in {PAGINA} ma non allegato alla release")
            for f in sorted(nei_file - nella_pagina):
                cambi.append(f"  ! {f}: allegato alla release ma assente da {PAGINA}")
        else:
            print(f"  nessun {PAGINA} nella release: pagina come prima")

        riga = aggiorna_file(slug, repo, rel, complete, schermate, pagina, args.scrivi)
        if riga:
            cambi.append(riga)

        articolo = allegato_md(repo, rel["tagName"], rel["assets"], ARTICOLO)
        if articolo:
            print(f"  articolo dal repo: {ARTICOLO} (italiano)")
            # Il nome del gioco serve al richiamo del download: lo dice game.md,
            # che e' la fonte del titolo anche sulla pagina.
            titolo_gioco = (campi_md(pagina[0]).get("title") if pagina
                            else slug.replace("-", " ").title())
            riga, avvisi = aggiorna_articolo(
                slug, titolo_gioco, rel, articolo, schermate,
                args.scrivi, args.riscrivi_articoli,
            )
            cambi += avvisi
            if riga:
                cambi.append(riga)
        else:
            print(f"  nessun {ARTICOLO} nella release: articolo come prima")

        if cambi:
            print("\n".join(cambi))
            totale += cambi
        else:
            print("  gia' allineato")

    print()
    if not totale:
        print("Niente da fare: sito e release coincidono.")
    elif args.scrivi:
        print(f"Fatto. File dei giochi pronti in: {STATSRV_FILES}")
        print("Ora caricali su bonomo.cloud nella cartella privata, sotto files/korb3n70/,")
        print("poi controlla il sito in locale e committa il blog.")
    else:
        print("Prova soltanto. Rilancia con --scrivi per applicare.")


if __name__ == "__main__":
    main()
