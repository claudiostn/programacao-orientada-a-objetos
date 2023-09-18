from numberDisplay import NumberDisplay

class ClockDisplay:
    def __init__(self):
        self.__hours = NumberDisplay(24)
        self.__minutes = NumberDisplay(60)
        self.__seconds = NumberDisplay(60)
        self.__display_string = ""
        self.__update_display()
    
    def get_time(self):
        return self.__display_string

    def set_time(self, hour, minute, second):
        self.__hours.set_value(hour)
        self.__minutes.set_value(minute)
        self.__seconds.set_value(second)

        self.__update_display()

    def time_tick(self):
        self.__seconds.increment()
        
        if self.__seconds.get_value() == 0:
            self.__minutes.increment()
            
            if self.__minutes.get_value() == 0:
                self.__hours.increment()

        self.__update_display()

    def __update_display(self):
        self.__display_string = self.__hours.get_display_value() + ":" + self.__minutes.get_display_value() + ":" + self.__seconds.get_display_value()
    