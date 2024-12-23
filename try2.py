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


