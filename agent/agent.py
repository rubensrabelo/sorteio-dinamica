from pathlib import Path
from huggingface_hub import InferenceClient
from .core import save_file, load_prompt


def generate_themes(token: str):
    try:
        client = InferenceClient(token=token)
        model = "meta-llama/Llama-3.1-8B-Instruct"

        prompt_path = (
            Path(__file__).parent
            / "prompts"
            / "advanced_themes_prompt.yml"
        )
        prompt_data = load_prompt(prompt_path)

        messages = [
            {"role": "system", "content": prompt_data["system"]},
            {"role": "user", "content": prompt_data["user"]},
        ]

        completion = client.chat.completions.create(
            model=model,
            messages=messages,
        )

        result = completion.choices[0].message.content
        save_file(result)

    except Exception as e:
        print(f"Erro ao processar resposta: {str(e)}")
