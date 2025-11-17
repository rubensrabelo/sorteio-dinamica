from pathlib import Path


def save_file(result: str, filename="themes.py"):
    folder = Path(__file__).parent.parent.parent / "data"
    folder.mkdir(exist_ok=True)

    output_file = folder / filename

    clean_lines = [
        line.strip()
        for line in result.strip().splitlines()
        if not line.strip().startswith("```")
    ]

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(clean_lines))

    print(f"Lista gerada e salva em '{output_file}' com sucesso!")
