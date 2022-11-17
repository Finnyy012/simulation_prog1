import math
import numpy as np

# dit is een FSM
def FSM(rules: [], tape: [], state: int, accepting: bool):
    for condition in tape:
        print(condition)
        for rule in rules:
            if((state == rule[0]) and (condition == rule[1])):
                state = rule[2]
                accepting = rule[3]
                print(str(state) + ' ' + str(accepting))
                break
    return accepting

rules = [
    (0,1,1,0),
    (1,1,0,0),
    (1,0,2,0),
    (2,0,1,0),
    (2,1,3,1),
    (3,1,2,0),
    (3,0,0,0),
    (0,0,3,1)
]

print(FSM(rules, [0,1,1], 0, 0))

