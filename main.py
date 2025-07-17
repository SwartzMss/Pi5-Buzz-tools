import argparse
from buzzer import Buzzer

def main():
    parser = argparse.ArgumentParser(description="Buzzer example")
    parser.add_argument('--times', type=int, default=3,
                        help='Number of beeps to play')
    parser.add_argument('--interval', type=float, default=1.0,
                        help='Interval between beeps in seconds')
    parser.add_argument('--pin', type=int, default=17,
                        help='GPIO pin (BCM numbering) to control the buzzer')
    args = parser.parse_args()

    buzzer = Buzzer(pin=args.pin)
    buzzer.beep_times(args.times, args.interval)

if __name__ == '__main__':
    main()
