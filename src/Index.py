import json
import pickle
from pathlib import Path
from BTrees.OOBTree import OOBTree

FICHIER = "documents.json"
DOSSIER_INDEX = Path("indexes")

indexes = {}

FICHIER = "documents.json"

def save_index(champ):
    DOSSIER_INDEX.mkdir(exist_ok=True)

    with open(DOSSIER_INDEX / f"{champ}.pkl", "wb") as fichier:
        pickle.dump(indexes[champ], fichier)

def load_indexes():
    DOSSIER_INDEX.mkdir(exist_ok=True)

    indexes.clear()

    for chemin in DOSSIER_INDEX.glob("*.pkl"):
        with open(chemin, "rb") as fichier:
            indexes[chemin.stem] = pickle.load(fichier)

def create_index(champ):
    tree = OOBTree()

    with open(FICHIER, "rb") as fichier:
        while True:
            position = fichier.tell()
            ligne = fichier.readline()

            if not ligne:
                break

            ligne = ligne.strip().rstrip(b",")

            if ligne in (b"[", b"]", b""):
                continue

            document = json.loads(ligne)

            if champ in document:
                cle = document[champ]

                if cle not in tree:
                    tree[cle] = []

                tree[cle].append(position)

    indexes[champ] = tree
    save_index(champ)

    return tree

def read_index(champ, valeur):
    index = indexes[champ]

    positions = index.get(valeur, [])
    documents = []

    with open(FICHIER, "rb") as fichier:
        for position in positions:
            fichier.seek(position)

            ligne = fichier.readline()
            ligne = ligne.strip().rstrip(b",")

            documents.append(json.loads(ligne))

    return documents

def refresh_indexes():
    for champ in list(indexes.keys()):
        create_index(champ)