import time
from CRUD import *
debut = time.perf_counter()

document = read(1)

fin = time.perf_counter()

print(document)
print(f"Temps : {fin - debut:.6f} secondes")