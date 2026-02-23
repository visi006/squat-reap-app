import time

class WorkoutSession:
    def __init__(self):
        self.start_time = time.time()
        self.total_reps = 0
        self.correct_reps = 0
        self.direction = 0
        self.state = "STANDING"

    def duration(self):
        return int(time.time() - self.start_time)

    def accuracy(self):
        if self.total_reps == 0:
            return 0
        return int((self.correct_reps / self.total_reps) * 100)
