class Sensors:
    def __init__(self, environment):
        self.environment = environment

    def scan_room(self):
        return self.environment.is_dirty()