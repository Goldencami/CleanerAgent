import random

class Environment:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)] # not shared across instances
        self.__set_dirt()
        self.position = {'x': 0, 'y': 0}

    # private method
    def __set_dirt(self):
        dice = random.randint(0, self.size * self.size)

        for i in range(dice):
            rand_row = random.randint(0, self.size - 1)
            rand_room = random.randint(0, self.size - 1)
            self.matrix[rand_row][rand_room] = 1

    # verifies if room is dirty
    def is_dirty(self, x, y):
        return self.matrix[x][y] == 1

    # # agent cleans a room
    def clean(self, new_x, new_y):
        self.matrix[new_x][new_y] = 0
        self.position['x'] = new_x
        self.position['y'] = new_y

    # Verifies if all the rooms are clean
    def all_clean(self):
        for row in self.matrix:
            for room in row:
                # already returns matric[row][room]
                if room == 1:
                    return False
        return True

    # display rooms in environment
    def display(self):
        for row in self.matrix:
            print(row)