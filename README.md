# Game_Playing


1) one_move_mode

for run one-move write this command.
>python maxconnect4.py one-move input1.txt output1.txt 3

Output:

MaxConnect-4 game

Game state before move:
 -----------------
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 -----------------
Score: Player 1 = 0, Player 2 = 0



move 1667: Player 1, column 1

Game state after every move:
 -----------------
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 1 0 0 0 0 0 0 |
 -----------------
Score: Player_1 = 0, Player_2 = 0

time taken by computer while plaing : 0.08177947998046875

->also, print the time taken by computer while playing game.


2)Interactive_mode

for run Interactive_mode write this command.
>python maxconnect4.py interactive input1.txt human-next 2    (for human) (here, 2 is depth)
>python maxconnect4.py interactive input1.txt computer-next 2 (for computer)

Output:

MaxConnect-4 game

Game state before move:
 -----------------
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 -----------------
Score: Player 1 = 0, Player 2 = 0

 -----------------
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 -----------------
Score:: Player-1 = 0, Player-2 = 0

It is Human's turn.
Enter the Column number[1-7] to play: 1
Your move is in column number:: 1
 -----------------
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 1 0 0 0 0 0 0 |
 -----------------
Computer is predicting and making decision for next.. 2 steps...


move 401: Player 2, column 1

 -----------------
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 0 0 0 0 0 0 0 |
 | 2 0 0 0 0 0 0 |
 | 1 0 0 0 0 0 0 |
 -----------------
Score:: Player-1 = 0, Player-2 = 0

It is Human's turn.
Enter the Column number[1-7] to play:

-->here, input1.txt is the initial state of game.
-->human-next / computer-next determines whether human or computer makes a next move.
-->last argument is a depth. (I take depth 2)
-->the next steps taken by human /computer whichever is the first player will be 
     saved in file named human.txt / computer.txt respectively.  
-->Algorithm will analyze next "depth" moves of the game to give best possible move.
-->also, print the time taken by computer.
