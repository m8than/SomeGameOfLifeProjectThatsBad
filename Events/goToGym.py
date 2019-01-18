from Events.iEvent import iEvent
import random
from general import General

from game import Game


class goToGym(iEvent):
    def isAvailable(self, person):
        return not Game.attributeSet('goneGym')

    def getText(self):
        if Game.attributeSet('noGym'):
            return "You're so bored that the thought of the gym crosses your mind again. Do you go?"
        else:
            return "Attempting to find something to do, the gym crosses your mind. Do you go?"

    def getOptions(self):
        return ['Yes', 'No']

    def optionHandler(self, option, person):
        option = option.lower()
        if option == 'yes':
            time = ''
            while not time.replace('.', '').isdigit() or time == '' or abs(float(time) > 5):
                time = Game.drawGameDialog("How long do you want to spend in the gym?", ["Please enter a decimal number of hours between 0-5 (eg 1.5)"], person)

            gym_factor = random.uniform(abs(float(time)-.5), float(time)+.5)
            person.stats.set('Stamina', gym_factor/4, True)
            person.stats.set('Energy', -gym_factor*1.5, True)
            Game.time += gym_factor
            Game.drawGameMessage("You spent " + General.timeToStr(gym_factor) + " hours in the gym", person)
            Game.setAttribute('goneGym', Game.day+1, 10)
            return True
        elif option == 'no':
            person.stats.set('Happiness', -5, True)
            person.stats.set('Energy', -.5, True)
            Game.time += .2
            return True
        else:
            return False
