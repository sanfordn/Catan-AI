# README

Requirements for this system:
- Python 3
- NumPy (For our Neural Network)
  - To install:
    - python3 -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

Command for repeating/automated run:
- change the input.txt file to the user inputs you would like to use 
  - [y/n] for whether or not you want the full game to print
  - 0 for no human players; for automation purposes, this should be kept at 0.
  - [0-4] for how many random bots to play
  - [0-4] for how many intelligent bots to play (unimplemented as of 4/29/2019)
- ./repeat.sh "python3 catan.py < input.txt" [number of times to run]

How to run the program:
- Ensure you have installed all of the requirements
- Run the command python3 catan.py
- Choose whether or not you want the board to print each turn
- Choose how many humans will play the game (fully implemented)
- Choose how many random bots will play the game (fully implemented)
- Choose how many intelligent bots will play the game (partially implemented)
- Either let the game run or play along with the game as it's running

To test road building for intelligent system:
- 

