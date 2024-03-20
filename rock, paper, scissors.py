import random
from time import sleep
from functionsRPS import *


#code needs to be worked on
possible_actions = ['rock', 'paper', 'scissors']

while True:
    choice_player = input(f'make a choice out of the following options: {possible_actions}:  ')
    if choice_player not in possible_actions:
        print()
        print('enter a valid option')
        print()
        continue
    
    print()
    choice_robot = random.choice(possible_actions)

    print('')
    print('the robot picked...')
    sleep(0.5)
    print(f'{choice_robot}!!!')

    print(PossibleGames(choice_robot, choice_player))

