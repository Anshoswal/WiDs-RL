import gymnasium as gym
import numpy as np
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
import pprint

env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True)
env = env.unwrapped
mdp_transitions = env.P
init_state = env.reset()
goal_state = 15

pprint.pprint(mdp_transitions)
