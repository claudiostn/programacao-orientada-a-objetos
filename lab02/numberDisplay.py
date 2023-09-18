class NumberDisplay:
    def __init__(self, roll_over_limit):
        self.__limit = roll_over_limit
        self.__value = 0
    
    def increment(self):
        self.__value = (self.__value + 1) % self.__limit