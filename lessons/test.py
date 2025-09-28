# call the functiom
# system generates random num
# system tells you how many attemps remaining if you fail


import random 

def random_number():

    system_guess = random.randint(1, 50)
    print(system_guess)
    attempts = 0 
    attempts_allowed = 5

    print("I'm thinking of a number between 1 and 50... Can you guess it?")

    while attempts < attempts_allowed:
        try:
            user_guess = int(input('Guess the number: '))
        except ValueError:
            print('Input a valid number.')
            continue  # skips all below then starts again if a ValueErro is raised

        attempts += 1

        if user_guess < system_guess:
            if attempts < attempts_allowed:
                print(f'Try higher, you have {attempts_allowed - attempts} attempts left')
        elif user_guess > system_guess:
            if attempts < attempts_allowed: 
                print(f'Try lower, you have {attempts_allowed - attempts} attempts left')
        else:
            print(f'Correct guess in just {attempts} tries!!!')
            break
    else:
        print(f'Out of attempts. The number was {system_guess}')


random_number()