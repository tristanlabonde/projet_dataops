import json

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
        fichier.write(",\n".join(json.dumps(doc) for doc in documents))
        fichier.write("\n]")

def create(document):
    '''
    gérer la création de deux objets identiques
    '''
    documents = charger()
    documents.append(document)
    sauvegarder(documents)

def read(id):
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