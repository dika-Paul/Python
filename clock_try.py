from time import time, localtime, sleep


class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    @property
    def second(self):
        return self._second

    @staticmethod
    def time_valid(hour, minute, second):
        if hour >= 24:
            return "illege_time"
        if minute >= 60:
            return "illege_time"
        if second >= 60:
            return "illege_time"
        return "lege_time"

    @classmethod
    def now(cls):
        nowtime = localtime(time())
        return cls(nowtime.tm_hour, nowtime.tm_min, nowtime.tm_sec)

    def run(self):
        self._second += 1
        if self.second == 60:
            self._minute += 1
            self._second = 0
            if self.minute == 60:
                self._hour += 1
                self._minute = 0
                if self.hour == 24:
                    self._hour = 0

    def diplay(self):
        print("{}: {}: {}".format(self.hour, self.minute, self.second))


def main():
    clock = Clock.now()
    for i in range(10):
        clock.diplay()
        sleep(1)
        clock.run()


if __name__ == "__main__":
    main()
