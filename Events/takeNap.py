from Events.iEvent import iEvent
from game import Game

import random

from general import General

class takeNap(iEvent):
    def isAvailable(self, person):
        return 10 < Game.time < 20 and person.stats.get("Energy") < 7

    def getText(self):
        return "You're getting pretty tired, do you want to take a nap?"

    def getOptions(self):
        return ['Yes', 'No']

    def optionHandler(self, option, person):
        option = option.lower()
        if option == 'yes':
            time_spent = random.uniform(.5, 2)
            person.stats.set('Happiness', time_spent*5, True)
            person.stats.set('Energy', time_spent*2, True)

            Game.drawGameMessage("You slept for " + General.timeToStr(time_spent) + " hours", person)
            Game.time += time_spent
            return True
        if option == 'no':
            time_spent = random.uniform(.2, .5)
            person.stats.set('Happiness', -time_spent*4, True)
            person.stats.set('Energy', -time_spent, True)

            Game.time += time_spent
            return True
        else:
            return False
