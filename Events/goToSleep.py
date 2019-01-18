from Events.iEvent import iEvent
from game import Game
from Events.wakeUp import wakeUp

import random
class goToSleep(iEvent):
    def getText(self):
        return "Time to head to bed?"
    def getOptions(self):
        return ['Yes', 'No']
    def optionHandler(self, option, person):
        option = option.lower()
        if option == 'yes':
            energy = person.stats.get('Energy')
            stamina = person.stats.get('Stamina')

            if stamina - energy < 3:
                time = random.uniform(0.2, 2)
                Game.drawGameMessage(f"You try to sleep for {time:.02f} hours but can't get to sleep", person)
                Game.time += time
                person.stats.set('Happiness', -20, True)
                return True

            est_sleep_hours = (stamina - energy)/stamina * 8
            sleep_hours = random.uniform(est_sleep_hours-1, est_sleep_hours+1)

            Game.time += sleep_hours
            person.stats.set('Happiness', 30, True)
            person.stats.set('Energy', stamina*.84)
            Game.next_event = wakeUp
            additional=''

            if energy > stamina/2:
                additional = ' but it took you a while to fall asleep'
                Game.time += random.uniform(0.2, 2)

            Game.drawGameMessage(f"You go to sleep{additional}", person)
            return True
        elif option == 'no':
            Game.setAttribute('noSleep', Game.day, 24)
            person.stats.set('Happiness', 5, True)
            return True
        else:
            return False
