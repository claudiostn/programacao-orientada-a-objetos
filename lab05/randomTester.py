import random


class RandomTester:
    def __init__(self):
        pass

    def print_one_random(self):
        number = random.randint(0, 1000)
        print(number)

    def print_multi_random(self, amount):
        for i in range(amount):
            self.print_one_random()

    def throw_dice(self):
        number = random.randint(1, 6)
        print(number)

    def print_random_range_max(self, max):
        self.print_random_range(1,max)

    def print_random_range(self, min, max):
        number = random.randint(min, max)
        print(number)