from CRUD import *

create({"id": 1, "nom": "Paul", "age": 22})
create({"id": 2, "nom": "Alice", "age": 24})

print(read(1))

update(1, {"age": 23})

print(read(1))
delete(2)
print(read(2))

