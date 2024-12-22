import gymnasium as gym
import numpy as np
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import pprint

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
    val[state] = np.random.random()

# Since 5, 7, 11, 12 and 15 are terminal states, we know their values are 0

val[5] = 0
val[7] = 0
val[11] = 0
val[12] = 0
val[15] = 0

def get_new_value_fn(val, mdp, pi, gamma = 1.0):
    new_val = dict()
    state_new_val = 0
    for state in pi:
        state_new_val = 0
        action = pi[state]
        for my_tupple in mdp[state][action]:
            prob = my_tupple[0]
            next_state = my_tupple[1]
            new_reward = my_tupple[2]
            done = my_tupple[3]
            state_new_val += prob*(new_reward * (not done) + gamma * val[next_state])
        new_val[state] = state_new_val  
    return new_val

def policy_evaluation(val, mdp, pi, epsilon=1e-10, gamma=1.0):
    count = 0
    while count<2:
        old_value = np.array(list(val.values()))
        new_value = np.array(list(get_new_value_fn(val,mdp,pi,gamma).values()))
        pprint.pprint(old_value)
        count +=1
policy_evaluation(val,mdp_transitions,pi,1e-10,1)