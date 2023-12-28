class FlagCounter:
    def __init__(self, total_flags):
        self.total_flags = total_flags
        self.used_flags = 0

    def place_flag(self):
        if self.used_flags < self.total_flags:
            self.used_flags += 1

    def remove_flag(self):
        if self.used_flags > 0:
            self.used_flags -= 1

    def get_remaining_flags(self):
        return self.total_flags - self.used_flags
