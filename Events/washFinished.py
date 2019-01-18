from Events.iEvent import iEvent
import random
from general import General
from game import Game


class washFinished(iEvent):
    def getText(self):
        time_taken = random.uniform(0.3, 1)
        Game.time += time_taken
        return "You washed yourself up. It took " + General.timeToStr(time_taken) + " hours"
    def getOptions(self):
        return []