import pygame


class ScoreDisplay:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.score = 0

    def update_score(self, new_score):
        self.score = new_score

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))  # Adjust position as needed


class Scorer:
    def __init__(self):
        self.score = 0

    # int, int -> int
    # return the score of the game, which is revealed_spaces * rate
    # if score <= 60 -> score *= 10
    # if score <= 120 -> score *= 5
    # if score <= 180 -> score *= 2
    def calculate_score(self, revealed_spaces, time_taken):
        # Calculate base score (1 point for each revealed space)
        base_score = revealed_spaces

        if time_taken <= 60:  # Less than 1 minute
            self.score = base_score * 10
        elif time_taken <= 120:  # Less than 2 minutes
            self.score = base_score * 5
        elif time_taken <= 180:  # Less than 3 minutes
            self.score = base_score * 2
        else:
            self.score = base_score

        return self.score
