from Events.iEvent import iEvent
from game import Game

import random


class meetFriends(iEvent):
    def isAvailable(self, person):
        return Game.time > 18 and Game.day > 1

    def getText(self):
        return "Your friends want to meet at the pub. Do you go?"

    def getOptions(self):
        return ['Yes', 'No']

    def optionHandler(self, option, person):
        option = option.lower()
        if option == 'yes':
            time_spent = random.uniform(.5, 3)
            person.stats.set('Happiness', time_spent*2, True)
            person.stats.set('Energy', -time_spent*.8, True)

            Game.time += time_spent
            return True
        if option == 'no':
            time_spent = random.uniform(.2, .5)
            person.stats.set('Happiness', -time_spent, True)
            person.stats.set('Energy', -time_spent*.8, True)

            Game.time += time_spent
            return True
        else:
            return False
