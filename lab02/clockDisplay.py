from numberDisplay import NumberDisplay

class ClockDisplay:
    def __init__(self):
        self.__hours = NumberDisplay(24)
        self.__minutes = NumberDisplay(60)

        self.__update_display()
    
    def __update_display(self):
        self.__display_string = self.__hours.get_display_value() + ":" + self.__minutes.get_display_value()