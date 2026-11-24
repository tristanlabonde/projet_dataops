import json
from Index import refresh_indexes, indexes, read_index

FICHIER = "documents.json"

def charger():
    try:
        with open(FICHIER, "r") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []

def sauvegarder(documents):
    with open(FICHIER, "w") as fichier:
        fichier.write("[\n")
        fichier.write(",\n".join(
            json.dumps(doc) for doc in documents
        ))
        fichier.write("\n]")

    refresh_indexes()

def create(document):
    documents = charger()

    for doc in documents:
        if doc["id"] == document["id"]:
            return False

    documents.append(document)
    sauvegarder(documents)

    return True

def read(id):
    if "id" in indexes:
        resultats = read_index("id", id)
        return resultats[0] if resultats else None

    documents = charger()

    for document in documents:
        if document["id"] == id:
            return document

    return None

def update(id, modifications):
    documents = charger()

    for document in documents:
        if document["id"] == id:
            document.update(modifications)
            sauvegarder(documents)
            return True

    return False

def delete(id):
    documents = charger()

    for document in documents:
        if document["id"] == id:
            documents.remove(document)
            sauvegarder(documents)
            return True

    return False