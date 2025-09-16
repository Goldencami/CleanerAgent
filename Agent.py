class Agent:
    def __init__(self, sensor, actuator):
        self.sensor = sensor # ask sensors for current perception/state
        self.actuator = actuator # decides on the action according to the state

    def action(self):
        if self.sensor.scan_room():
            self.actuator.suck()
        else:
            self.actuator.move()

    # keep robot working as long as the entire room is not clean (optional)
    def run(self):
        while not self.sensor.environment.all_clean():
            self.action()