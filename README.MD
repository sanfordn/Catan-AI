# README

Requirements for this system:
  - Python 3
  - NumPy (For our Neural Network)
    - To install:
      -python3 -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose


  - Command for repeating/automated run:
        - change the input.txt file to the user inputs you would like to use 
            - [y/n] for whether or not you want the full game to print
            - 0 for no human players; for automation purposes, this should be kept at 0.
            - [0-4] for how many random bots to play
            - [0-4] for how many intelligent bots to play (unimplemented as of 4/29/2019)
        - ./repeat.sh "python3 catan.py < input.txt" [number of times to run]
