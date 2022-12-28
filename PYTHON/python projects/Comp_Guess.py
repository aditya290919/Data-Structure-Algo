
import random
def guess_num(n):

    guess=''

    comp_guess=random.randint(1,n)

    while guess!=comp_guess:

        try:

            guess=int(input(f'Enter a number between 1 and {n}: '))

            if guess>n:
                print('It is out of limit!')

            elif guess<0:
                print('Smaller than range!')

            elif guess>comp_guess:
                print('little smaller!')

            elif guess<comp_guess:

                print('Little Higher!')

        except Exception:
            print('Char are not allowed!')


    

    print(f'You have guessed {comp_guess} correctly!')

guess_num(10)