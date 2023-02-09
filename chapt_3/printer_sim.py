from Queue import Queue

class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self. time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None