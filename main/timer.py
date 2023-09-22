from pygame.time import get_ticks


class Timer(object):
    def __init__(self, duration, repeated=False, function=None):
        self.duration = duration
        self.repeated = repeated
        self.function = function

        self.start_time = 0
        self.active = False

    def activate(self):
        self.active = True
        self.start_time = get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        current_time = get_ticks()

        if current_time - self.start_time >= self.duration and self.active:
            if self.function and self.start_time != 0:
                self.function()

            self.deactivate()

            if self.repeated:
                self.activate()


if __name__ == '__main__':
    pass
