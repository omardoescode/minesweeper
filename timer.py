# timer.py

import time
import threading

class Timer:
    def __init__(self):
        self.is_running = False
        self.elapsed_time = 0
        self.time_limit = 300  # 5 minutes (300 seconds)

    def start_timer(self):
        self.is_running = True
        self.elapsed_time = 0
        threading.Thread(target=self._update_timer).start()

    def stop_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.elapsed_time = 0

    def _update_timer(self):
        while self.is_running and self.elapsed_time < self.time_limit:
            time.sleep(1)
            self.elapsed_time += 1

        if self.elapsed_time >= self.time_limit:
            print("Time limit reached! Game timed out.")
            # Add your game-over logic or timeout action here

    def get_elapsed_time(self):
        return self.elapsed_time
