import sys, random
wins = 0
losses = 0
ties = 0
print ('Welcome to Rock - Paper - Scissors Game!')

while True:
    print ('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: #player input loop
        print ('Your move: r-rock, p-paper, s-scissors, q-quit')
        playerMove = input()
        if (playerMove == 'q'):
            sys.exit()
        if (playerMove == 'r' or playerMove == 's' or playerMove =='p'):
            break
        print ('Wrong letter, just p,s,r, or q will work')
    if (playerMove == 'r'):
        print('ROCK versus ...')
    if (playerMove == 'p'):
        print('PAPER versus ...')
    if (playerMove == 's'):
        print('SCISSORS versus ...')
    
    #computer move
    computerPick = random.randint(1,3)
    if computerPick == 1:
        computerPick = 'p'
        print ('PAPER')
    if computerPick == 2:
        computerPick = 's'
        print ('SCISSORS')    
    if computerPick == 3:
        computerPick = 'r'
        print ('ROCK')    
    
    #win/loss/ties
    if (playerMove == computerPick):
        print ('Tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerPick == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerPick == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerPick == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerPick == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerPick == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerPick == 'r':
        print('You lose!')
        losses = losses + 1    
       
