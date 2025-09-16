class Sensors:
    def __init__(self, environment):
        self.environment = environment

    def scanner(self, position):
        x, y = self.environment.position['x'], self.environment.position['y']
        return self.environment.is_dirty(x, y)