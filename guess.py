import random 
#  Goes to thre python random package so we are able to call all functions in random
def guess(num):
    random_number = random.randint(1,num)
    guess=0
    while guess != random_number: 
        guess = int(input(f'Guess a number between 1 and {6num}:'))
        if guess < random_number:
            print('Sorry, guess again. Too low')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print('Yeey, congrats you have guessed the {random_number} correctly')

guess(10)

