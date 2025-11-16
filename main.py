from services import BuilderDraw
from app import show_menu, handle_choice, handle_new_themes_option, show_result


def main():
    builder = BuilderDraw()

    show_menu()
    choice = input("\nEscolha uma opção: ")

    handle_new_themes_option(choice)
    handle_choice(choice, builder)

    show_result(builder.build())


if __name__ == "__main__":
    main()
