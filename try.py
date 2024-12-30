import random

r1 = [7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5]
r2 = [6,6.5,7,7.5,8,8.5,9,9.5,10]
r3 = [4,4.5,5,5.5,6]

def step_to_take(explore,exploit):
    a = random.randint(1,10)
    if a == 1 and explore > 0:
        explore -= 1
        return 1
    elif a != 1 and exploit == 0:
        explore -= 1
        return 1
    else:
        exlpoit -= 1
        return 0 
        
r1_count,r2_count,r3_count = 0,0,0
r1_occurence,r2_occurence,r3_occurence = 0,0,0

def get_reward(step):  # We get step form step_to_take function
    if step == 1:
        explore()
    else:
        exploit()

def explore():
    pass

def exploit():
    pass