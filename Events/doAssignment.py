from Events.iEvent import iEvent

from game import Game
import random

class doAssignment(iEvent):
    def isAvailable(self, person):
        return person.stats.isset('Assignment') and person.stats.get('Assignment') < 100

    def getText(self):
        return "Do you want to work on your assignment?"

    def getOptions(self):
        return ['Yes', 'No']

    def optionHandler(self, option, person):
        option = option.lower()
        if option == 'yes':
            time = ''
            while not time.replace('.', '').isdigit() or time == '' or abs(float(time) > 5):
                time = Game.drawGameDialog("How long do you want to spend working?", ["Please enter a decimal number of hours between 0-5 (eg 1.5)"], person)

            hours = random.uniform(abs(float(time) - .5), float(time) + .5)
            if person.stats.get('Happiness') < 85:
                hours += 1

            Game.drawGameMessage(f"You spent {hours:.1f} hours completing {int(hours*5)}% of your assignment", person)
            Game.time += hours
            person.stats.set('Assignment', hours*5, True)
            person.stats.set('Happiness', -hours*5, True)
            person.stats.set('Energy', -hours/1.7, True)
            return True
        elif option == 'no':
            return True
        else:
            return False
