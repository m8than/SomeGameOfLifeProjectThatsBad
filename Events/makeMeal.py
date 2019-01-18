from Events.iEvent import iEvent
from game import Game

import random


class makeMeal(iEvent):
    def isAvailable(self, person):
        return Game.time > 18 and not Game.attributeSet('eatenDinner')

    def getText(self):
        return "You're getting hungry. Do you make a meal?"

    def getOptions(self):
        return ['Yes', 'No']

    def optionHandler(self, option, person):
        option = option.lower()
        if option == 'yes':
            time_spent = random.uniform(.5, 2)
            person.stats.set('Happiness', time_spent*5, True)
            person.stats.set('Energy', -time_spent*.3, True)
            Game.setAttribute('eatenDinner', Game.day+1, Game.time)
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
