import random

#This package is used to wrap the unity environment into a gym environment
from gym_unity.envs import UnityToGymWrapper

#This package is used to open the game in a unity environment, i.e. the interface between Unity and Python
from mlagents_envs.environment import UnityEnvironment as UE

#Load the game
env = UE(file_name='Spectrum', seed = 1, side_channels=[],no_graphics=False)

#Convert Unity Environment to Gym environment
gym_env=UnityToGymWrapper(env)



states = gym_env.observation_space.shape[0]
actions = 4
print(states)
print(actions)

episodes = 10
for episode in range(1, episodes):   
    done = False
    score = 0

    while not done:
        gym_env.render()
        action = random.choice([0,1,2,3])
        print("actionn taken=",action)
        observations, reward, done, _ = gym_env.step(action)
        print("observations: ",len(observations))
        score += reward
        print("reward: ",reward)
    gym_env.reset()

def RL(env):
    '''Implement your RL model here'''
    pass