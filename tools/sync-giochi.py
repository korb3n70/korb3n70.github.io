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
     versione, data, elenco dei download e changelog.

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

def front_matter_generato(slug, repo, rel, tutte, schermate):
    """Costruisce la parte di front matter che questo script possiede."""
    assets = sorted(rel["assets"], key=lambda a: a["name"])
    righe = [
        MARCATORE,
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
        righe.append(f"  - nome: {yaml_testo(etichetta(a['name']))}")
        righe.append(f"    file: {yaml_testo(a['name'])}")
        righe.append(f"    dimensione: {yaml_testo(peso(a['size']))}")

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


def aggiorna_file(slug, repo, rel, tutte, schermate, scrivi):
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

    nuovo = manuale + "\n" + front_matter_generato(slug, repo, rel, tutte, schermate) + "\n---" + corpo

    if percorso.exists() and percorso.read_text(encoding="utf-8") == nuovo:
        return None

    if scrivi:
        percorso.parent.mkdir(parents=True, exist_ok=True)
        percorso.write_text(nuovo, encoding="utf-8", newline="\n")

    return f"  * {percorso.relative_to(BLOG)}"


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scrivi", action="store_true", help="applica le modifiche (senza, mostra soltanto)")
    ap.add_argument("--gioco", help="un solo gioco, per slug")
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

        riga = aggiorna_file(slug, repo, rel, complete, schermate, args.scrivi)
        if riga:
            cambi.append(riga)

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
