"""This creates a unity-python interface"""

#This package is used to wrap the unity environment into a gym environment
from gym_unity.envs import UnityToGymWrapper

#This package is used to open the game in a unity environment, i.e. the interface between Unity and Python
from mlagents_envs.environment import UnityEnvironment as UE
def get_env(file_name):
    #Load the game
    env = UE(file_name, seed = 1, side_channels=[],no_graphics=False)

    #Convert Unity Environment to Gym environment
    gym_env=UnityToGymWrapper(env)

    return gym_env