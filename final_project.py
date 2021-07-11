import random


report_file = open('game_report.txt', 'a')
try_again = 'y'
while try_again == 'y':
    username = input('Enter a username: ')
    num = random.randint(-100, 100)
    print('Guess the number between -100 and 100. You have 10 guesses.')
    while True:
        try:
            user_guess = int(input('Enter a guess: '))
            break
        except ValueError:
            print("Not a number, try again.")

    guess_count = 1
    while user_guess != num and guess_count < 10:
        print('low guess' if user_guess < num else 'high guess')
        while True:
            try:
                user_guess = int(input('Next guess: '))
                break
            except ValueError:
                print("Not a number, try again.")
        guess_count += 1

    if user_guess == num:
        print(f'Great job! You got the answer in {guess_count} guesses!')
    else:
        print('Sorry! You weren\'t able to guess the number in 10 guesses.')
    report_file.write(f'{username}  {guess_count}\n')
    try_again = input('Try again? y/n ')
