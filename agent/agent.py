from pathlib import Path
from huggingface_hub import InferenceClient
from .core import load_prompt,  save_file


def generate_themes(token: str):
    try:
        client = InferenceClient(token=token)
        model = "meta-llama/Llama-3.1-8B-Instruct"

        prompt_path = (
            Path(__file__).parent
            / "prompts"
            / "advanced_themes_prompt.txt"
        )
        prompt = load_prompt(prompt_path)

        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )

        result = completion.choices[0].message.content
        save_file(result)

    except Exception as e:
        print(f"Erro ao processar resposta: {str(e)}")
