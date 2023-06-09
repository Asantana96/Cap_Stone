import time
import os

class PomodoroTimer:
    def __init__(self):
        self.work_timer = 25
        self.rest_timer = 5

    def convert(self, t):
        return t * 60

    def countdown(self, t):
        while t:
            min, sec = divmod(t, 60)
            timer_value = f"{min:02d}:{sec:02d}"
            print(timer_value, end="\r")
            time.sleep(1)
            t -= 1
        return timer_value
    def pomodoro(self,work, rest):
        # Convert minutes to seconds
        w = self.convert(work)
        r = self.convert(rest)

        # Work timer
        self.work_timer = self.countdown(w)
        os.system("clear||cls")

        # Rest timer
        self.rest_timer = self.countdown(r)
        os.system("clear||cls")

        return self.work_timer, self.rest_timer
