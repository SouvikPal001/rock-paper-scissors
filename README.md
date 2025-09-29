# Rock-Paper-Scissors Game

A simple Python console game where the player competes against the computer in the classic Rock-Paper-Scissors game.

The game begins by asking the player to "Type Rock/Paper/Scissor Or 'Q' To Quit:". The computer randomly picks one of the three options, and the game compares the choices:

- If the player wins, it says "You Won!"
- If the computer wins, it says "You Lost!"
- If both choices are the same, it says "It's A Tie!"

The game keeps track of the number of wins for both the player and the computer, as well as ties. The player can quit anytime by typing 'Q'.

For example, a sample gameplay might look like this:
```text
Type Rock/Paper/Scissor Or 'Q' To Quit: rock
Computer picked scissor.
You Won!
Type Rock/Paper/Scissor Or 'Q' To Quit: paper
Computer picked rock.
You Won!
Type Rock/Paper/Scissor Or 'Q' To Quit: scissor
Computer picked scissor.
It's A Tie!
Type Rock/Paper/Scissor Or 'Q' To Quit: q
You Won 2 Times.
The Computer Won 0 Times.
There Were 1 Ties.
Exiting The Game...
See Ya!
```
This game is great for learning Python concepts like loops, conditionals, random number generation, string manipulation, and basic game logic.

## Features

- User input validation to ensure valid moves.
- Randomized computer choices.
- Tracks wins, losses, and ties.
- Simple, interactive console-based gameplay.
- Quit anytime by typing 'Q'.
