import argparse
import time
from pathlib import Path

from CRUD import read


RESULT_FILE = Path(__file__).resolve().parents[1] / "result.txt"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Mesure le temps de lecture d'un document JSON."
    )
    parser.add_argument(
        "--id", type=int, default=1000, help="identifiant à rechercher (défaut : 1000)"
    )
    parser.add_argument(
        "--iterations",
        type=int,
        default=1000,
        help="nombre de lectures à effectuer (défaut : 1000)",
    )
    args = parser.parse_args()

    if args.iterations < 1:
        parser.error("--iterations doit être supérieur ou égal à 1")

    start = time.perf_counter()
    document = None
    for _ in range(args.iterations):
        document = read(args.id)
    elapsed = time.perf_counter() - start

    if document is None:
        result = f"Aucun document trouvé avec l'identifiant {args.id}."
        exit_code = 1
    else:
        result = f"Document lu : {document}"
        exit_code = 0

    result += (
        f"\nNombre de lectures : {args.iterations}"
        f"\nTemps total : {elapsed:.6f} secondes"
        f"\nTemps moyen : {elapsed / args.iterations * 1000:.6f} ms/lecture\n"
    )
    RESULT_FILE.write_text(result, encoding="utf-8")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
