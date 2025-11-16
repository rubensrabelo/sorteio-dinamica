from agent import generate_themes
from config import HUGGINGFACE_API_KEY


def handle_new_themes_option(choice):
    if choice in ["3", "5"]:
        option = input("Deseja novos temas? [s/n]: ").lower().strip()
        if option == "s":
            generate_themes(HUGGINGFACE_API_KEY)
