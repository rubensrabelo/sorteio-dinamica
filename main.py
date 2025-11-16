import json

from agent import generate_themes
from config import HUGGINGFACE_API_KEY
from services import BuilderDraw


def main():
    builder = BuilderDraw()

    print("MENU DE OPÇÕES:")
    print("1 - Sortear tipo de desenvolvimento")
    print("2 - Sortear equipes")
    print("3 - Sortear temas")
    print("4 - Sortear tecnologias")
    print("5 - Sortear tudo")

    choice = input("\nEscolha uma opção: ")

    if choice == "3" or choice == "5":
        option = input("Deseja novos temas? [s/n]: ").lower().strip()
        if option == "s":
            generate_themes(HUGGINGFACE_API_KEY)

    if choice == "1":
        builder.draw_dev_type()
    elif choice == "2":
        builder.draw_teams()
    elif choice == "3":
        builder.draw_themes()
    elif choice == "4":
        builder.draw_technologies()
    elif choice == "5":
        (
            builder.draw_dev_type()
            .draw_teams()
            .draw_themes()
            .draw_technologies()
        )
    else:
        print("Opção inválida.")

    result = builder.build()
    print("\n=== RESULTADO FINAL ===")
    print(json.dumps(result, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
