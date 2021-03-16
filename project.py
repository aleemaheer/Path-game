# Creating a game 

welcome = print('Welcome to my first game!')
name = input('What is your name?')
age = input('What is your age?')
age_limit = '12'

try:
    if int(age) > 12:
        print('You are old enough to play!')
        want_to_play = input('Do you want to play? ')
        if want_to_play.lower() == 'yes':
            print('You are staring with 10 health.\nLet\'s play!')
            weapon = input('Pick a weapon if you want to, if not that is okay (sword/needle) ')
            first_choice = input('First choice... Left or Right (left/right)? ')
            if first_choice.lower() == 'left':
                print('You fell down and lost...')
            else:
                lake = input('Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ')
                if lake.lower() == 'across':
                    print('You managed to get across but were bit by a fish and lost 5 health.')
                    notice = input('You noticed a house and river. Where you want to go? (house/river) ')
                    if notice.lower() == 'house':
                        print('You have arrived in the home and win.')
                    elif notice.lower() == 'river':
                        print('You fell in the river and lost... ')
                    else:
                        print('Invalid answer.')
                elif lake.lower() == 'around':
                    print('Oh! No there\'s a ghost...')
                    path = input('What you have to do fight or surrender? (fight/surrender) ')
                    if path.lower() == 'fight' and weapon.lower() == 'sword':
                        print('You did not lose the hope and you killed the ghost because you have the sword!')
                    elif path.lower() == 'surrender':
                        print('You are so afraid and the ghost killed you.\nYou lost... ')
                    elif path.lower() == 'fight':
                        print('You lose because you have not picked up the sword.\nYou lost...')
                    else:
                        print('Invalid path')
                else:
                    print('Invalid answer')
                
        else:
            print("Okay!")
    else:
        print('You are not old enough to play!')
except:
    print('Invalid input!')