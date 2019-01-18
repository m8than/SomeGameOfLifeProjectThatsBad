from Events.iEvent import iEvent
from Events.makeBreakfast import makeBreakfast

from game import Game

class wakeUpSkipSleep(iEvent):
    def getText(self):
        return "You've just woken up. What do you do?\na - get breakfast\nb - skip breakfast"

    def getOptions(self):
        return ['a', 'b']

    def optionHandler(self, option, person):
        if option == 'a':
            Game.time += .5
            person.stats.set('Happiness', 10, True)
            person.stats.set('Energy', -1, True)
            Game.next_event = makeBreakfast
            return True
        elif option == 'b':
            Game.time += .1
            Game.setAttribute('breakfastSkipped', Game.day+1, 0)
            person.stats.set('Happiness', -10, True)
            return True
        else:
            return False