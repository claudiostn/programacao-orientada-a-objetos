from randomTester import RandomTester

def main():
    test = RandomTester()

    test.print_one_random()
    test.print_multi_random(10)
    test.print_random_range(1,100)
    test.print_random_range_max(1000)
    test.throw_dice()

main()