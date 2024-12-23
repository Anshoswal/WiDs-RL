import gymnasium as gym
import numpy as np
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import pprint

# Step 1 is to get the MDP
env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True)
env = env.unwrapped
mdp_transitions = env.P
init_state = env.reset()
goal_state = 15

LEFT, DOWN, RIGHT, UP = range(4)
pi = {
    0:RIGHT, 1:RIGHT, 2:DOWN, 3:LEFT,
    4:DOWN, 5:LEFT, 6:DOWN, 7:LEFT,
    8:RIGHT, 9:RIGHT, 10:DOWN, 11:LEFT,
    12:LEFT, 13:RIGHT, 14:RIGHT, 15:LEFT
}

val = dict()
for state in mdp_transitions:
    pi[state] = 0
    
def get_new_value_fn(val, mdp, pi, gamma = 1.0):
    new_val = dict()
    state_new_val = 0
    for state in pi:
        state_new_val = 0
        action = pi[state]
        for my_tupple in mdp[state][action]:
            prob,next_state,new_reward,done = my_tupple
            if next_state == 15:
                new_reward=1
            state_new_val += prob*(new_reward * (not done) + gamma * val[next_state])
        new_val[state] = state_new_val  
    return new_val


#Use to above function to get the new value function, also print how many iterations it took to converge
def policy_evaluation(val, mdp, pi, epsilon=1e-10, gamma=1.0):
    count = 0
    while True:
        old_value = np.array(list(val.values()))
        new_value = np.array(list(get_new_value_fn(val,mdp,pi,gamma).values()))
        d1 = np.subtract(new_value, old_value)
        difference = np.abs(d1)
        max_element = np.max(difference)
        print(difference)
        if max_element < epsilon:
            val = new_value
            count +=1
            break
        else:
            old_value = new_value
            count += 1
            print(val)
    return val, count 
policy_evaluation(val,mdp_transitions,pi,1e-7,1)