from Events.iEvent import iEvent

from .makeBreakfast import makeBreakfast
from .wakeUpSkipSleep import wakeUpSkipSleep
from .goToWash import goToWash

from game import Game

import random

class wakeUp(iEvent):
    def getText(self):
        self.version = random.randint(0, 2)
        if self.version == 0:
            return "You've just woken up. What do you do?\na - get breakfast\nb - skip breakfast\nc - back to sleep"
        elif self.version == 1:
            return "You've just woken up. You find some leftover food from last nights meal and ate it for breakfast"
        else:
            return "You've just woken up. You can't be bothered with breakfast so you skip it"

    def getOptions(self):
        if self.version == 0:
            return ['a', 'b', 'c']
        else:
            return ['Press enter to continue']

    def optionHandler(self, option, person):
        if self.version == 1:
            person.stats.set('Happiness', 10, True)
            person.stats.set('Energy', 2, True)
            return True
        if self.version != 0:
            person.stats.set('Energy', -1, True)
            person.stats.set('Happiness', -3, True)
            return True

        if option == 'a':
            Game.next_event = makeBreakfast
            return True
        elif option == 'b':
            Game.time += .1
            Game.setAttribute('breakfastSkipped', Game.day+1, 0)
            person.stats.set('Happiness', -10, True)
            Game.next_event = goToWash
            return True
        elif option == 'c':
            energy = person.stats.get('Energy')
            stamina = person.stats.get('Stamina')
            approx = stamina - energy
            time = random.uniform(approx+1, approx+3)
            Game.time += time

            if Game.time > 13:
                person.stats.set('Happiness', -30, True)
                Game.next_event = wakeUpSkipSleep
            else:
                person.stats.set('Happiness', -random.randint(5, 10) if Game.attributeSet('sleptTwiceAlready') else random.randint(2, 10), True)
                person.stats.set('Energy', 1, True)
                Game.next_event = wakeUp

            Game.setAttribute('sleptTwiceAlready', Game.day + 1, 0)
            return True
        else:
            return False
