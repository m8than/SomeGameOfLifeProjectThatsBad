from Events.iEvent import iEvent
import random
from general import General

from game import Game


class goToWash(iEvent):
    def getText(self):
        return "Do you have time to wash?"

    def getOptions(self):
        return ['Yes', 'No']

    def optionHandler(self, option, person):
        option = option.lower()
        if option == 'yes':
            time_taken = random.uniform(0.3, 1)
            if person.stats.get('Happiness') < 70:
                time_taken += random.uniform(0.3, 1)
            person.stats.set('Happiness', 5, True)
            Game.time += time_taken
            if time_taken > .5:
                Game.drawGameMessage("It took you especially long to wash. It took " + General.timeToStr(time_taken) + " hours", person)
            else:
                Game.drawGameMessage("You washed. It took " + General.timeToStr(time_taken) + " hours", person)
            return True
        elif option == 'no':
            return True
        else:
            return False