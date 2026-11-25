from pathlib import Path

ENTRY = (
    "Taking a sick day today — I sneezed so hard my smartwatch "
    "asked if I'd been in an accident."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
