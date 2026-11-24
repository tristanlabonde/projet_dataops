from CRUD import create, read, update, delete, sauvegarder
from Index import load_indexes, create_index, indexes,read_index
from pathlib import Path

if not Path("documents.json").exists():
    sauvegarder([])

load_indexes()

if "id" not in indexes:
    create_index("id")

create({"id": 1, "nom": "Paul", "age": 22})
create({"id": 2, "nom": "Alice", "age": 24})

create_index("age")

load_indexes()

print(read(1))
print(read_index("age", 24))

