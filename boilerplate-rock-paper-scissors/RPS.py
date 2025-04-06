# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from collections import Counter
import numpy as np

def player(prev_play, opponent_history=[], player_history=[]):
    opponent_history.append(prev_play)
    player_history.append(guess)
    return guess
