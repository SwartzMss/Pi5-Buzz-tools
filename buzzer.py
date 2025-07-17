import time

class Buzzer:
    """Simple buzzer interface with a customizable beep function."""

    def __init__(self, beep_func=None):
        # If no custom beep function is provided, fall back to printing.
        self.beep_func = beep_func or self._default_beep

    def _default_beep(self):
        """Default beep action (console output)."""
        print("Beep!")

    def beep_times(self, times, interval=0.5):
        """Beep a number of times with a delay between beeps."""
        for _ in range(times):
            self.beep_func()
            time.sleep(interval)
