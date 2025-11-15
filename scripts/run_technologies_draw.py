from services import draw_technologies


def run_technologies_draw():
    result = draw_technologies()

    print("\n=== SORTEIO DE TECNOLOGIAS ===")
    print("Quantide de repetições:", result["Repetições"])
    print("Backend escolhido:", result["backend"])
    print("Frontend escolhido:", result["frontend"])
    print("Mobile escolhido:", result["mobile"])
