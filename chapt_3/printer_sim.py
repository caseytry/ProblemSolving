from Queue import Queue

class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self. time_remaining = 0