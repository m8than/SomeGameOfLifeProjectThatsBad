from Objects.person import Person
from draw import Draw
from game import Game
from general import *

from Events import *

import random


def main():
    Draw.clear()
    name = General.validateInput("What is your name?\n",
                          "Please only enter letters and spaces",
                          "alphaspaces", 28)
    me = Person(name)
    Game.day = 0
    Game.time = 8
    Game.next_event = wakeUp
    Game.drawGameMessage(f"Hey {me.name}, you have class from 1 PM to 5 PM each day. Try not to miss it too "
                         f"often!\nIf at any time you think it is a good time to sleep use option 'sleep'. Oh and "
                         f"your only goal is to survive 7 days of education, good luck.", me)
    while Game.day <= 7:
        Game.updateStatus(me)

        available_events = [goToGym,
                            useComputer,
                            doAssignment,
                            goBar,
                            meetFriends,
                            getFastFood,
                            grabSnacks,
                            makeMeal,
                            takeNap,
                            meetFriendsAssignment,
                            watchTv]

        if Game.time > 13 and not Game.attributeSet('classSkipped') and not Game.attributeSet('wentToClass') and not Game.attributeSet('missedClassMessage'):
            Game.drawGameMessage("You've missed your class for today!", me)
            me.stats.set('Happiness', -50, True)
            Game.setAttribute('missedClassMessage', Game.day+1, 0)

        if 11 < Game.time < 13 and goToClass().isAvailable(me):
            available_events = [goToClass]

        if Game.time > 22 and Game.attributeSet('noSleep'):
            available_events = [goToSleep]

        if not me.stats.isset('Assignment') and Game.day >= 3 and Game.time >= 15:
            Game.drawGameMessage('You have received an assignment from your tutor.', me)
            me.stats.set('Assignment', 0)

        #if event has a subevent
        if Game.next_event != None:
            available_events = [Game.next_event]
            Game.next_event = None

        if me.stats.get('Energy') <= 0:
            available_events = [collapsedToSleep]
            Game.next_event = None

        #get event
        while True:
            cur_event = random.choice(available_events)() #select random based on probability
            if cur_event.isAvailable(me):
                break

        eventDone = False
        while not eventDone:
            event = Draw.eventBox3(cur_event.getText(), 'Event', options=cur_event.getOptions())

            game_box = Game.drawGameBox()
            stats_box = me.drawStatsBox()
            side_bar = Draw.addVertical(game_box, stats_box, 2)

            event_bottom = list(['']*(len(side_bar)-len(event)))
            event_bottom.extend(event)
            screen = Draw.addHorizontal(event_bottom, side_bar, 8)

            Draw.clear()
            Draw.toScreen(screen)
            print(Game.cur_error, end='')
            Game.cur_error = ''
            command = input("Option (type 'sleep' to sleep): ")
            if command.lower() == "sleep":
                Game.next_event = goToSleep
                eventDone = True
            else:
                eventDone = cur_event.optionHandler(command, me)
                if not eventDone:
                    Game.cur_error = 'Option invalid\n'

        while Game.time > 24:
            Game.day += 1
            Game.time = Game.time - 24

        if me.stats.get('Energy') > me.stats.get('Stamina'):
            me.stats.set('Energy', me.stats.get('Stamina'))

        if me.stats.get('Happiness') < 20:
            break

        if me.stats.isset('Assignment') and me.stats.get('Assignment') >= 100:
            me.stats.set('Assignment', 100)
            if me.stats.get('Happiness') >= 50:
                Game.day = 8

    if me.stats.get('Happiness') < 50:
        box1 = Draw.box1(f"You failed to make it to the end of the week. You made it to day {Game.day}.\n"
                         "You decided that education is not for you and left.",
                         "Failed")
    else:
        if Game.attributeSet('assignmentCheating') and random.randint(0, 100) < 30:
            additional = "Your tutor noticed that your assignment was really similar to your classmates and gave you a zero"
            box1 = Draw.box1(f"Well done, you made it to the end of the week.\n" + additional,
                             "Failed")
        else:
            additional = "You also completed your assignment in time!" if me.stats.get('Assignment') > 99 else "However you failed to complete your assignment in time!"
            box1 = Draw.box1(f"Well done, you made it to the end of the week.\n" + additional,
                             "Congratulations")

    stats_box = me.drawStatsBox()
    Draw.clear()
    Draw.toScreen(Draw.addHorizontal(box1, stats_box, 3))


if __name__ == "__main__":
    main()
    input()
