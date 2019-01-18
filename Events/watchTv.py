from Events.iEvent import iEvent
from game import Game

import random


class watchTv(iEvent):
    def isAvailable(self, person):
        return Game.time > 16 and Game.day > 1

    def getText(self):
        return "You're bored. Do you watch TV?"

    def getOptions(self):
        return ['Yes', 'No']

    def optionHandler(self, option, person):
        option = option.lower()
        if option == 'yes':
            time_spent = random.uniform(1, 3)
            person.stats.set('Happiness', time_spent*3, True)
            person.stats.set('Energy', -time_spent*.8, True)
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
