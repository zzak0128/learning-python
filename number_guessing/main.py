import random

def start_game():
    # ask for user's desired number
    user_number = int(input('Select a number between 1 and 10:\n'))

    # generate a random number for comparison
    target_number = random.randint(1, 10)

    while user_number > 10 or user_number < 1:
        user_number = int(input('Please select a number between 1 and 10:\n'))

    # spit message depending on that comparison
    print('You guessed', user_number, 'and the target number is', target_number)
    if user_number == target_number:
        print('You win!')
    else:
        print('You lost!')

if __name__ == '__main__':
    start_game()
