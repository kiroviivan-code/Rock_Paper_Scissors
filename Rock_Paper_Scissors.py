#NBTG

import random

rock='Rock'
paper='Paper'
scissors='Scissors'

while 1:
    player_move=input('Choose r/ock; p/aper; s/cissors: ')

    if player_move !="r" and player_move != 'p' and player_move != 's':
        raise SystemExit("Incorrect input.Try again...")

    pc_rand_num=random.randint(1,3)

    pc_move=''

    if pc_rand_num==1:
        pc_move='Rock'
    elif pc_rand_num==2:
        pc_move='Paper'
    elif pc_rand_num==3:
        pc_move='Scissors'

    print(f"The computer chose {pc_move}.")

    if (player_move=='r' and pc_move=='Scissors') or (player_move=='p' and pc_move=='Rock') or (player_move=='s' and pc_move=='Paper'):
        print('You win!')
        break
    elif (player_move=='r' and pc_move=='Rock') or (player_move=='p' and pc_move=='Paper') or (player_move=='s' and pc_move=='Scissors'):
        print('Draw! Again...')
    else:
        print('You lose!')
        break
