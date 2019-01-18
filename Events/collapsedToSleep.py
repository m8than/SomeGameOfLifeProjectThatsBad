from Events.iEvent import iEvent
from game import Game
from Events.wakeUp import wakeUp

import random
class collapsedToSleep(iEvent):
    def getText(self):
        return "You were so tired you collapsed in your bed"
    def getOptions(self):
        return ['Press enter to continue']
    def optionHandler(self, option, person):
        Game.time += random.uniform(8, 10)
        person.stats.set('Happiness', 20, True)
        person.stats.set('Energy', person.stats.get('Stamina')*.7)
        Game.next_event = wakeUp
        return True
