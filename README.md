# projet_dataops

## Mesure des lectures JSON

Depuis la racine du projet, lancez le test de mesure avec :

```bash
PYTHONPATH=src python3 test/benchmark.py --id 1000 --iterations 1000
```

La base de test contient 1 000 documents avec des identifiants uniques. Par
défaut, le benchmark cherche le document 1000, en fin de fichier, pour mesurer
une recherche complète. Il écrit le résultat et les mesures dans `result.txt`
à la racine du projet sans modifier `documents.json`.