import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x}; '))
        print(guess)
        if guess < random_number:
            print('sorry guess again, Too low')
        elif guess > random_number:
            print('sorry, guess again, Too high')
    print(f'yaay! cograts. you have guessed the the number {random_number}')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1

    print(f'yaay! Cograts computer, you guessed {guess}, correctly!')

computer_guess(1000)