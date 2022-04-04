import random
from interface import get_env

env=get_env('Spectrum')

#Number of observations
#Observations are returned from raycast,i.e rays are sent in 
#8 directions and we get a value in each direction corresponding
#to the object it hits.
#TODO: explain the observations
states = env.observation_space.shape[0]

#The agent has to choose one of the 4 actions allowed
#TODO: explain the actions
actions = 4

episodes = 10

# This script takes random actions. You have to implement your rl model here
for episode in range(1, episodes):   
    
    done = False
    score = 0

    while not done:
        env.render()
        action = random.choice([0,1,2,3])
        print("actionn taken=",action)
        observations, reward, done, _ = env.step(action)
        print("observations: ",len(observations))
        score += reward
        print("reward: ",reward)
    env.reset()