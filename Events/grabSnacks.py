from Events.iEvent import iEvent
from game import Game

import random


class grabSnacks(iEvent):
    def isAvailable(self, person):
        return not Game.attributeSet('snacks')

    def getText(self):
        return "You're getting hungry. Do you grab some snacks?"

    def getOptions(self):
        return ['Yes', 'No']

    def optionHandler(self, option, person):
        option = option.lower()
        if option == 'yes':
            time_spent = random.uniform(.2, .5)
            person.stats.set('Happiness', time_spent*6, True)
            person.stats.set('Energy', -time_spent, True)
            Game.drawGameMessage("You ate "+random.choice(["some crisps", "an apple", "ice cream", "some berries", "some nuts", "a chocolate bar"]), person)
            Game.setAttribute('snacks', Game.day, Game.time+8)
            Game.time += time_spent
            return True
        if option == 'no':
            return True
        else:
            return False
