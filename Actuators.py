class Actuator:
    def __init__(self, environment):
        self.environment = environment

    # agent starts at upper left corner of the 2D array (env)
    # x   →
    # ↑ ← ↓
    def move(self):
        x, y = self.environment.position['x'], self.environment.position['y'] # x is the rows and y the room in the row
        n = self.environment.size

        # for even rows, the robot moves right
        # if the row is odd the robot moves left
        # the robot moves down
        if x%2 == 0:
            if y < n - 1: # move right
                self.environment.set_position(x, y + 1)
            elif x < n - 1: # move down
                self.environment.set_position(x + 1, y)
            else: # reached bottom-right corner
                return
        elif x%2 == 1:
            if y > 0: # move left
                self.environment.set_position(x, y - 1)
            elif x < n - 1:  # move down
                self.environment.set_position(x + 1, y)
            else: # reached bottom-left corner
                return

        print("agent is at position ", self.environment.position)

    def suck(self):
        self.environment.clean()
        print("agent is cleaning room ", self.environment.position)