from clockDisplay import ClockDisplay

def main():
    clock = ClockDisplay()
    print(clock.get_time())
    for i in range(60*6):
        clock.time_tick()
    print(clock.get_time())

    clock.set_time(8, 20, 59)
    print(clock.get_time())


main()