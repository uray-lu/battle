import pandas as pd
from random import sample 
import random




def battle(name_list):
    length = int((len(name_list)*(len(name_list)-1))/2)
    arrangement = []
    combine = []
    random.seed(28)
    
    while len(combine)< length:
    
        single = sample(name_list, 2)

        if (single in combine or single[::-1] in combine):
            pass
        else:
            combine.append(single)

    while len(combine) > 0:
        element = combine.pop(0)
        if arrangement == []:
            arrangement.append(element)
        else:
            if (element[0] in arrangement[-1] or element[1] in arrangement[-1]):
                combine.append(element)
            else:
                arrangement.append(element)
    
    out = pd.DataFrame(arrangement)
    out.columns = ['player1', 'player2']
    
    return out


if __name__ == '__main__':

    people = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    
    battle(people)






