class Scorer:
    def __init__(self):
        self.score = 0

    def calculate_score(self, elapsed_time, revealed_spaces, game_won):
        score_multiplier = self.calculate_multiplier(elapsed_time)

        revealed_score = revealed_spaces  # +1 score for each revealed space

        if game_won:
            final_score = revealed_score * score_multiplier
        else:
            final_score = revealed_score

        self.score = final_score
        return self.score

    def calculate_multiplier(self, elapsed_time):
        if elapsed_time <= 60:  # Within 1 minute
            return 10
        elif elapsed_time <= 120:  # Within 2 minutes
            return 5
        elif elapsed_time <= 180:  # Within 3 minutes
            return 2
        else:
            return 1  # More than 3 minutes or game not won
