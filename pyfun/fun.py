
import sys
import random

start = int(sys.argv[1])
end = int(sys.argv[2])

print(f'let\'s play a game! pick a number between {start} and {end}! Ready?...')

random_num = random.randint(start, end)

while True:
    try:
        response = int(input(f"what's your guess? (number between {start} and {end}):  "))
        if response == random_num:
            print(f'congratulations, you guessed {random_num} correctly!')
            break
        else:
            print(f"i'm sorry, {response} was not correct, guess again.")
    except:
            print(f"ouch, that wasn't even valid input")
else:
    print('all done, play again?')
