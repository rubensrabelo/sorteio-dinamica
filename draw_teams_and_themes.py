from services import draw_teams, draw_themes


if __name__ == "__main__":
    print("\n=== SORTEIO DE EQUIPES ===")
    times_teams, team1, team2 = draw_teams()
    print(f"Quantidade de vezes sorteadas: {times_teams}")
    print("Equipe 1:", team1)
    print("Equipe 2:", team2)

    print("\n=== TEMAS SORTEADOS ===")
    themes, times_themes = draw_themes()
    print(f"Quantidade de vezes sorteadas: {times_themes}")
    for theme in themes:
        print("-", theme)
