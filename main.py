from agent import generate_themes
from config import HUGGINGFACE_API_KEY
from scripts import (
    run_technologies_draw,
    run_project_setup_draw,
    run_all_draws
)


def main():
    print("\n=== MENU DE SORTEIOS ===")
    print("1. Sortear Tecnologias")
    print("2. Sortear Tipo + Equipes + Temas")
    print("3. Sortear TUDO")

    choice = input("\nEscolha uma opção: ")

    if choice != "1":
        generate_themes(HUGGINGFACE_API_KEY)

    if choice == "1":
        run_technologies_draw()

    elif choice == "2":
        run_project_setup_draw()

    elif choice == "3":
        run_all_draws()

    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()
