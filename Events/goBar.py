from Events.iEvent import iEvent
from game import Game
from general import General

import random
class goBar(iEvent):
    def isAvailable(self, person):
        return Game.day in [2, 3, 4, 5] and 16 < Game.time < 22

    def getText(self):
        return "You've just heard that there's live football on at the bar. Do you go?"

    def getOptions(self):
        return ['Yes', 'No']

    def optionHandler(self, option, person):
        option = option.lower()
        time_spent = random.uniform(1, 3)
        if option == 'yes':
            person.stats.set('Energy', -time_spent*1.2, True)
            person.stats.set('Happiness', time_spent*3, True)
            Game.time += time_spent+.1
            Game.drawGameMessage("You spend " + General.timeToStr(time_spent) + " hours in the bar", person)
            return True
        if option == 'no':
            return True
        else:
            return False
