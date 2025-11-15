from pathlib import Path
from huggingface_hub import InferenceClient


def load_prompt(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def save_file(result, filename="themes.py"):
    folder = Path(__file__).parent.parent / "data"
    output_file = folder / filename

    with open(output_file, "w", encoding="utf-8") as f:
        lines = result.strip().splitlines()
        clean_lines = []
        for line in lines:
            line = line.strip()
            if line.startswith("```"):
                continue
            clean_lines.append(line)

        for item in clean_lines:
            f.write(item + "\n")

    print(f"Lista gerada e salva em '{output_file}' com sucesso!")


def generate_themes(token: str):
    try:
        client = InferenceClient(token=token)
        model = "deepseek-ai/DeepSeek-V3-0324"

        prompt_path = (
            Path(__file__).parent
            / "prompts"
            / "advanced_themes_prompt.txt"
        )
        prompt = load_prompt(prompt_path)

        completion = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )

        result = completion.choices[0].message.content

        save_file(result)
    except Exception as e:
        print(f"Erro ao processar resposta: {str(e)}")
