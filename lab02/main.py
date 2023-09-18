from numberDisplay import NumberDisplay

def main():
    display = NumberDisplay(24)
    
    display.set_value(19)
    display.increment()
    print(display.get_display_value())

main()