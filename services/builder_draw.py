from .draw_technologies import draw_technologies
from .draw_teams import draw_teams
from .draw_themes import draw_themes
from .draw_dev_type import draw_dev_type


class BuilderDraw:
    def __init__(self):
        self.result = {}

    def draw_dev_type(self):
        dev_type, times = draw_dev_type()
        self.result["Tipo de desenvolvimento"] = dev_type
        self.result["Repetições"] = times
        return self

    def draw_teams(self):
        times, team1, team2 = draw_teams()
        self.result["Equipes"] = {"Equipe 1": team1, "Equipe 2": team2}
        self.result["Repetições"] = times
        return self

    def draw_themes(self):
        last_result, times = draw_themes()
        self.result["Temas"] = last_result
        self.result["Repetições"] = times
        return self

    def draw_technologies(self):
        times, result = draw_technologies()
        self.result["Tecnologias"] = result
        self.result["Repetições"] = times
        return self

    def build(self):
        return self.result
