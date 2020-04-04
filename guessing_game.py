import random, sys

highscore = []

def start_game():
    print("Welcome to number guessing game ")
    print('*' * 40)
    print("highscore " + str(highscore))
    count = 0
    #https://docs.python.org/3/library/random.html
    answer = random.randint(1,10)
    game = 'on'

    while game=='on':
        
        try:
            guess = int(input("guess a number from 1-10 "))
        except ValueError:
            print("please input number only")
        else:
            if guess < 1 or guess > 10:
                print("It must be higher than zero and less than 11")
            elif guess > answer:
                print("The number should be lower")
                count += 1
            elif guess < answer:
                print("The number should be higher")
                count += 1
            else:
                print('You got it! \nyou have {} attempted guess'.format(count + 1))
                highscore.append(count + 1)
                
                decision = 1

                while decision == 1:
                    restart = input('Do you want to play again [Y]es/[N]o ? ')
                    try:
                        if restart.lower() == 'y':
                            count = 0
                            answer = random.randint(1,10)
                            print("highscore " + str(min(highscore)))
                            decision = 0
                        elif restart.lower() != 'y' and restart.lower() != 'n':
                            raise ValueError('Answer with [y] or [n] only')
                        else:
                            sys.exit('Thanks for playing...closing game')
                    except ValueError as err:
                        print('{}'.format(err))
                        





                   







if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
