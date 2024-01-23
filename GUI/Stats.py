import pygame
from .gui_constants import WIDTH, HEIGHT
from storage import load_games
from .Page import Page


class Stats(Page):
    def __init__(self, username):
        super().__init__()
        self.title_text = "Stats"
        self.navigation_buttons = []  # {obj: button, val: "Navigation Button", kwargs}
        self.username = username
        self.games = load_games()
        self.my_games = list(
            filter(lambda game: game["username"] == self.username, self.games)
        )
        self.won_games = list(
            filter(lambda game: game["game state"] == "w", self.my_games)
        )
        self.lost_games = list(
            filter(lambda game: game["game state"] == "l", self.my_games)
        )
        self.best_time = min(
            [float(game["time elapsed"]) for game in self.won_games], default=0
        )
        self.best_score = max(
            [int(game["score"]) for game in self.won_games], default=0
        )
        self.top_easy = sorted(
            [
                game
                for game in self.games
                if game["difficulty"] == "easy" and game["game state"] == "w"
            ],
            key=lambda d: d["time elapsed"],
        )[:5:]
        self.top_medium = sorted(
            [
                game
                for game in self.games
                if game["difficulty"] == "medium" and game["game state"] == "w"
            ],
            key=lambda d: d["time elapsed"],
        )[:5:]
        self.top_hard = sorted(
            [
                game
                for game in self.games
                if game["difficulty"] == "hard" and game["game state"] == "w"
            ],
            key=lambda d: d["time elapsed"],
        )[:5:]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT_GAME", None
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for btn in self.navigation_buttons:
                    if btn["obj"].collidepoint(event.pos):
                        return btn["val"], btn["kwargs"]
        return None, None

    def update(self, screen, fonts):
        pygame.display.set_caption(self.title_text)
        screen.blit(self.background, (0, 0))

        self.draw_title("My Stats", screen, fonts["md"], WIDTH * 0.15, HEIGHT / 3)
        self.draw_title(
            f"Won Games: {len(self.won_games)}",
            screen,
            fonts["sm"],
            WIDTH * 0.15,
            HEIGHT / 3 + 50,
        )
        self.draw_title(
            f"Lost Games: {len(self.lost_games)}",
            screen,
            fonts["sm"],
            WIDTH * 0.15,
            HEIGHT / 3 + 100,
        )
        self.draw_title(
            f"Best Time: {self.best_time:.2f}s",
            screen,
            fonts["sm"],
            WIDTH * 0.15,
            HEIGHT / 3 + 150,
        )
        self.draw_title(
            f"Highest Score: {self.best_score}",
            screen,
            fonts["sm"],
            WIDTH * 0.15,
            HEIGHT / 3 + 200,
        )

        self.draw_title("Leaderboard", screen, fonts["md"], WIDTH * 0.65, 50)

        self.draw_title("Easy", screen, fonts["md"], WIDTH * 0.5, 100)
        for i in range(1, len(self.top_easy) + 1):
            self.draw_title(
                f"{i}. {self.top_easy[i-1]['username']} {self.top_easy[i-1]['time elapsed']:.2f}s",
                screen,
                fonts["sm"],
                WIDTH * 0.5,
                100 + 50 * i,
            )

        self.draw_title("Medium", screen, fonts["md"], WIDTH * 0.8, 100)
        for i in range(1, len(self.top_medium) + 1):
            self.draw_title(
                f"{i}. {self.top_medium[i-1]['username']} {self.top_medium[i-1]['time elapsed']:.2f}s",
                screen,
                fonts["sm"],
                WIDTH * 0.8,
                100 + 50 * i,
            )

        self.draw_title("Hard", screen, fonts["md"], WIDTH * 0.5, HEIGHT * 0.5 + 50)
        for i in range(1, len(self.top_hard) + 1):
            self.draw_title(
                f"{i}. {self.top_hard[i-1]['username']} {self.top_hard[i-1]['time elapsed']:.2f}s",
                screen,
                fonts["sm"],
                WIDTH * 0.5,
                HEIGHT * 0.5 + 50 + 50 * i,
            )

        back_main_menu = self.draw_small_button("Back", (10, 10), screen, fonts)
        self.navigation_buttons.append(
            {"obj": back_main_menu, "val": "MAIN_MENU", "kwargs": {}}
        )
