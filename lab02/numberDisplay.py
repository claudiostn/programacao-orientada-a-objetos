class NumberDisplay:
    def __init__(self, roll_over_limit):
        self.__limit = roll_over_limit
        self.__value = 0
    
    def increment(self):
        self.__value = (self.__value + 1) % self.__limit
    
    def get_display_value(self):
        if self.__value < 10:
            return "0" + str(self.__value)
        else:
            return "" + str(self.__value)