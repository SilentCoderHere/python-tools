from threading import Thread
from time import sleep


class TimeError(Exception):
    pass


class Animation(Thread):
    def __init__(
        self,
        text: str = "Animation",
        timeToSleep: float = 0.2,
        dot: int = 4,
        internet: bool = False,
    ):
        Thread.__init__(self)
        self.timeToSleep = timeToSleep

        if __name__ != "__main__" and timeToSleep >= 1:
            self.timeToSleep = 0.2

        elif timeToSleep >= 1:
            raise TimeError("Time must smaller than 1 second")

        self.maxNumOfDot = dot
        self.text = text
        self.loopTime = round(1 / timeToSleep)
        self.Running = True
        self.internet = internet

    def run(self):
        dotNum = 1
        barComplete, totalTime, loopRun = 0, 1, 0
        timeToSleep = self.timeToSleep
        maxNumOfDot = self.maxNumOfDot

        while self.Running:
            print(f"[{totalTime}s] {self.text} {'.' * dotNum}", flush=True)
            print("\033[F", end="\033[K")

            if dotNum == maxNumOfDot:
                dotNum = 0
                barComplete += 0.5

            if loopRun == self.loopTime:
                loopRun = 0
                totalTime += 1

            dotNum += 1
            loopRun += 1

            if self.internet:
                sleep(timeToSleep + barComplete * 0.1)

            else:
                sleep(timeToSleep)

    def stop(self):
        self.Running = False


if __name__ == "__main__":
    timeToSleep = 5
    anim = Animation(f"Example For {timeToSleep}s", dot=5, timeToSleep=0.9)
    anim.start()
    sleep(timeToSleep)
    anim.stop()
