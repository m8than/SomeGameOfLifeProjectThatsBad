from Events.iEvent import iEvent
from game import Game
import random

class goToClass(iEvent):
    def isAvailable(self, person):
        return not Game.attributeSet('classSkipped')
    def getText(self):
        return "Time for class soon, will you go?"
    def getOptions(self):
        return ['Yes', 'No']
    def optionHandler(self, option, person):
        option = option.lower()
        if option == 'yes':
            person.stats.set('Happiness', -30, True)
            person.stats.set('Energy', -3, True)

            action_number = random.randrange(0, 4)
            if not person.stats.isset('Assignment') and Game.day >= 2:
                action = "You now have an assignment to complete by the end of the week. At least you finished a part of it in class"
                person.stats.set('Happiness', -20, True)
                person.stats.set('Energy', -1, True)
                person.stats.set('Assignment', 20)
                Game.time = 17 + random.uniform(0.5, 1.5)
            elif action_number == 0:
                action = "It was quite interesting in class today, you stayed behind a bit"
                person.stats.set('Happiness', 10, True)
                person.stats.set('Energy', -3, True)
                Game.time = 17 + random.uniform(0.5, 1.5)
            elif action_number == 1:
                action = "Class was cancelled"
                person.stats.set('Happiness', 20, True)
                person.stats.set('Energy', -1, True)
                Game.time = 13 + random.uniform(0, .5)
            elif action_number == 2 and person.stats.isset('Assignment'):
                action = "You worked on your assignment a bit in class today"
                person.stats.set('Happiness', 5, True)
                person.stats.set('Energy', -5, True)
                person.stats.set('Assignment', 20)
                Game.time = 17 + random.uniform(0.2, 0.7)
            else:
                action = "Class was boring"
                person.stats.set('Happiness', -30, True)
                person.stats.set('Energy', -3, True)
                Game.time = 17 + random.uniform(0.2, 0.7)

            Game.drawGameMessage(f"{action}. You made your way back to your room", person)
            Game.setAttribute('wentToClass', Game.day+1, 0)
            return True
        elif option == 'no':
            Game.setAttribute('classSkipped', Game.day+1, 0)
            person.stats.set('Happiness', -10, True)
            return True
        else:
            return False
