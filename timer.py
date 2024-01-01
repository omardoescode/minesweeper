import time

class Timer:
    # When you pause the game and click continue, the timer restarts
    # initial_time is to calculate the time taken before
    def __init__(self, initial_time=0):
        self.start_time = None
        self.end_time = None
        self.initial_time = initial_time

    def start(self):
        self.start_time = time.time()
    
    def end(self):
        self.end_time = time.time()
    def get_elapsed_time(self):
        if self.end_time:
            return self.end_time - self.start_time + self.initial_time
        elif self.start_time:
            return time.time() - self.start_time + self.initial_time
        return 0
