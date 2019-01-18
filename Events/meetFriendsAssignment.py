from Events.iEvent import iEvent
from game import Game

import random
class meetFriendsAssignment(iEvent):
    def isAvailable(self, person):
        return person.stats.isset('Assignment') and person.stats.get('Assignment') < 100 and Game.day > 5

    def getText(self):
        return "A classmate invites you to do your assignment with him. The assignment specifically says that collaboration is not allowed. Do you risk it?"

    def getOptions(self):
        return ['Yes', 'No']

    def optionHandler(self, option, person):
        option = option.lower()
        if option == 'yes':
            time_taken = 3 + random.uniform(-.5, 1)
            person.stats.set('Assignment', time_taken*20, True)
            person.stats.set('Happiness', time_taken*2, True)
            person.stats.set('Energy', -time_taken, True)
            Game.setAttribute('assignmentCheating', 10000, 0)
            Game.time += time_taken
            return True
        elif option == 'no':
            time_taken = random.uniform(-.5, 1)
            person.stats.set('Happiness', -time_taken*2, True)
            person.stats.set('Energy', -time_taken, True)
            Game.time += time_taken
            return True
        else:
            return False
