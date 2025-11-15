from .run_technologies_draw import run_technologies_draw
from .run_project_setup_draw import run_project_setup_draw


def run_all_draws():
    print("\n=== SORTEIO COMPLETO ===")

    print("\n--- Tecnologias ---")
    run_technologies_draw()

    print("\n--- Tipo + Equipes + Temas ---")
    run_project_setup_draw()
