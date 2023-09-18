from numberDisplay import NumberDisplay

class ClockDisplay:
    def __init__(self):
        self.__hours = NumberDisplay(24)
        self.__minutes = NumberDisplay(60)
        self.__update_display()