
#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega


import sys
import time
from MaxConnect4Game import *

def one_move_game(curr_game, depth):
    start_time = time.time()
    if curr_game.pieceCount == 42:    # check if the board is already full or not
        print ('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    curr_game.aiPlay(depth) #It will make a move. If this is only randomly is implemented or not.

    print ('Game state after every move:')
    curr_game.printGameBoard()

    curr_game.countScore()
    print('Score: Player_1 = %d, Player_2 = %d\n' % (curr_game.player1Score, curr_game.player2Score))

    curr_game.printGameBoardToFile()
    curr_game.gameFile.close()
    end_time = time.time()
    time_taken = end_time-start_time
    print("time taken by computer while plaing :" , time_taken)

# this one is for interactive_game, where human and computer will play. And also give results with good visualization along  with human and computer score. 
def interactive_game(curr_game, nextplayer, depth):
    
    curr_game.printGameBoard()
    curr_game.countScore()
    print('Score:: Player-1 = %d, Player-2 = %d\n' % (curr_game.player1Score, curr_game.player2Score))
    if nextplayer == "human-next":
        while curr_game.getPieceCount() != 42:
            print("It is Human's turn.")
            humanmove = int(input("Enter the Column number[1-7] to play: "))
            if not 0 < humanmove < 8:
                print(" this Column number must be between [1-7]")
                continue
            if not curr_game.playPiece(humanmove - 1):
                print("Column number: %d is full. Try another column." % humanmove)
                continue
            print("Your move is in column number:: " + str(humanmove))
            curr_game.printGameBoard()
            curr_game.gameFile = open("human.txt", 'w')
            curr_game.printGameBoardToFile()
            curr_game.gameFile.close()
            if curr_game.getPieceCount() == 42:
                print("BOARD FULL\n\nGame Over!\n")
                curr_game.countScore()
                print('Score:: Player-1 = %d, Player-2 = %d\n' % (curr_game.player1Score, curr_game.player2Score))
                break
            else:
                print("Computer is predicting and making decision for next.. " + str(depth) + " steps...")
                if curr_game.currentTurn == 1:
                    curr_game.currentTurn = 2
                elif curr_game.currentTurn == 2:
                    curr_game.currentTurn = 1
                curr_game.aiPlay(depth)
                curr_game.printGameBoard()
                curr_game.gameFile = open('computer.txt', 'w')
                curr_game.printGameBoardToFile()
                curr_game.gameFile.close()
                curr_game.countScore()
                print('Score:: Player-1 = %d, Player-2 = %d\n' % (curr_game.player1Score, curr_game.player2Score))
    else:
        curr_game.aiPlay(depth)
        curr_game.gameFile = open('computer.txt', 'w')
        curr_game.printGameBoardToFile()
        curr_game.gameFile.close()
        curr_game.printGameBoard()
        curr_game.countScore()
        print('Score:: Player-1 = %d, Player-2 = %d\n' % (curr_game.player1Score, curr_game.player2Score))
        interactive_game(curr_game, 'human-next', depth)

    if curr_game.getPieceCount() == 42:
        if curr_game.player1Score > curr_game.player2Score:
            print("Player 1 won this Game !")
        if curr_game.player1Score == curr_game.player2Score:
            print("The game is a Tie !")
        if curr_game.player1Score < curr_game.player2Score:
            print("Player 2 won this Game !")
        print("Game Finised")


def main(argv):
    # while implementing this code make sure one have enough arguments or not.
    if len(argv) != 5:
        print ('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    curr_game = maxConnect4Game() #this is creating a game

    #it will try to open the input file
    try:
        curr_game.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # this will read the beging game state from the file and save it into a 2D list
    file_lines = curr_game.gameFile.readlines()
    curr_game.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    curr_game.currentTurn = int(file_lines[-1][0])
    curr_game.gameFile.close()

    print ('\nMaxConnect-4 game\n')
    print ('Game state before move:')
    curr_game.printGameBoard()

    # this will update a few famme variavles based on the beging state and it will print the score
    curr_game.checkPieceCount()
    curr_game.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (curr_game.player1Score, curr_game.player2Score))

    if game_mode == 'interactive':
        interactive_game(curr_game, argv[3], int(argv[4])) # make sure all command-line argument is implemented or not.
    else: # game_mode == 'one-move' # it will set the game mode is not one move or not.
        #and also it will make tje output file. 
        outFile = argv[3]
        try:
            curr_game.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        # Be careful with the command-line arguments.
        one_move_game(curr_game,int(argv[4]))  
main(sys.argv)

