## Tic Tac Toe
Tic-tac-toe is a command-line, two-player game where players take turns marking a 3x3 grid with X or O. The first player to get three of their marks in a row wins. Choose the row and column (indexed at 0) for each move. 

```
tictactoe % python main.py
TIC TAC TOE

 | | 

---------
 | | 

---------
 | | 
Player X: Enter row (0-2): 0
Player X: Enter col (0-2): 0
X| | 

---------
 | | 

---------
 | | 
Player O: Enter row (0-2): 1
Player O: Enter col (0-2): 1
X| | 

---------
 |O| 

---------
 | | 
Player X: Enter row (0-2): 2
Player X: Enter col (0-2): 0
X| | 

---------
 |O| 

---------
X| | 
Player O: Enter row (0-2): 1
Player O: Enter col (0-2): 0
X| | 

---------
O|O| 

---------
X| | 
Player X: Enter row (0-2): 1
Player X: Enter col (0-2): 2
X| | 

---------
O|O|X

---------
X| | 
Player O: Enter row (0-2): 0
Player O: Enter col (0-2): 1
X|O| 

---------
O|O|X

---------
X| | 
Player X: Enter row (0-2): 2
Player X: Enter col (0-2): 1
X|O| 

---------
O|O|X

---------
X|X| 
Player O: Enter row (0-2): 2
Player O: Enter col (0-2): 2
X|O| 

---------
O|O|X

---------
X|X|O
Player X: Enter row (0-2): 0 
Player X: Enter col (0-2): 2
X|O|X

---------
O|O|X

---------
X|X|O
It's a draw
Game over


```
```
tictactoe % python main.py
TIC TAC TOE

 | | 

---------
 | | 

---------
 | | 
Player X: Enter row (0-2): 0
Player X: Enter col (0-2): 0
X| | 

---------
 | | 

---------
 | | 
Player O: Enter row (0-2): 1
Player O: Enter col (0-2): 1
X| | 

---------
 |O| 

---------
 | | 
Player X: Enter row (0-2): 0
Player X: Enter col (0-2): 1
X|X| 

---------
 |O| 

---------
 | | 
Player O: Enter row (0-2): 1
Player O: Enter col (0-2): 0
X|X| 

---------
O|O| 

---------
 | | 
Player X: Enter row (0-2): 0
Player X: Enter col (0-2): 2
X|X|X

---------
O|O| 

---------
 | | 
Player X is the winner
Game over
```
```
tictactoe % python main.py
TIC TAC TOE

 | | 

---------
 | | 

---------
 | | 
Player X: Enter row (0-2): 0
Player X: Enter col (0-2): 0
X| | 

---------
 | | 

---------
 | | 
Player O: Enter row (0-2): 1
Player O: Enter col (0-2): 1
X| | 

---------
 |O| 

---------
 | | 
Player X: Enter row (0-2): 0
Player X: Enter col (0-2): 1
X|X| 

---------
 |O| 

---------
 | | 
Player O: Enter row (0-2): 0
Player O: Enter col (0-2): 2
X|X|O

---------
 |O| 

---------
 | | 
Player X: Enter row (0-2): 1
Player X: Enter col (0-2): 1
Row 1 and column 1 is full. Please try again.
Player X: Enter row (0-2): 1
Player X: Enter col (0-2): 2
X|X|O

---------
 |O|X

---------
 | | 
Player O: Enter row (0-2): 2
Player O: Enter col (0-2): 0
X|X|O

---------
 |O|X

---------
O| | 
Player O is the winner
Game over
```
