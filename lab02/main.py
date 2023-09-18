from numberDisplay import NumberDisplay
from clockDisplay import ClockDisplay

def main():
    display = NumberDisplay(24)
    
    display.set_value(19)
    display.increment()
    print(display.get_display_value())

    clock = ClockDisplay()
    print(clock.get_time())
    for i in range(3620):
        clock.time_tick()
    print(clock.get_time())

    clock.set_time(8, 20)
    print(clock.get_time())

main()