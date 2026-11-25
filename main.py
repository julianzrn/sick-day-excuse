"""Entry for "The Funniest Sick-Day Excuse".

The excuse stays in a plain, believable sick-note voice, then lands
its twist on the last word: a sneeze so violent that a smartwatch's
real crash-detection feature mistakes it for an accident.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The line is assembled from named fragments: the notice itself,
# the (real) symptom, and the smartwatch punchline at the end.
NOTICE = "Taking a sick day today — "
SYMPTOM = "I sneezed so hard my smartwatch "
PUNCHLINE = "asked if I'd been in an accident."

ENTRY = NOTICE + SYMPTOM + PUNCHLINE


def write_entry(entry: str = ENTRY, path: Path = OUTPUT_PATH) -> None:
    """Write ``entry`` to ``path``, creating its folder first."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(entry, encoding="utf-8")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
