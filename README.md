# Agent-Wars APOGEE 2022
### Spectrum
Spectrum is a 2D game where the goal of the player is to clear the given map by reaching the final checkpoint. The ball, which is controlled by the player changes colour if it passes through a beam of any other colour. Certain bodies in the game will fire at the ball, and cause instant death if they are of complementary colours. Falling off the platform of the game results in instant death. 
This is the windows build for the game, Linux/mac builds have not been created yet.

### Requirements
* Windows Operating System
* Python (in case you do not have python, download it from [here](https://www.python.org/downloads/))
* Ml-Agents (run `pip install mlagents`)
* Unity-Gym (run `pip install gym-unity`) 

### Installation

* #### Downloading Spectrum
> * Clone this repository onto your local system and you are good to go!

### Developing your RL Model
* To develop your RL Model, you will be mainly working with the [rl.py](https://github.com/aadith-warrier/Agent-Wars/blob/main/rl.py) file.
* The [interface.py](https://github.com/aadith-warrier/Agent-Wars/blob/main/interface.py) file contains the code to connect the unity game and the python file.
* Within [interface.py](https://github.com/aadith-warrier/Agent-Wars/blob/main/interface.py) there is a function, `get_env(file_name)` this accepts the file name of the game ('Spectrum', in this case) and returns an environment where the python code and the unity game can communicate with each other.
* This file has been imported to rl.py and the environment has been created using `env=get_env('Spectrum')`.
* The contestant is expected to import all other required libraries and code the RL Model within this file.
* In case you do not want to see the window of the game, go to the [interface.py](https://github.com/aadith-warrier/Agent-Wars/blob/main/interface.py) file, and in the 10th line set `no_graphics=True`.

### Some methods of the Gym Environment
* `env.action_space.n` 
> * Returns the the number of dicrete actions the agent can perform.
> * In this case it is four
> > * 0-Stay
> > * 1-Move to the right
> > * 2-Move to the left 
> > * 3-Jump
* `env.step(action)`
> * Run one timestep of the environment's dynamics. When end of episode is reached, you are responsible for calling reset() to reset this environment's state. Accepts an action and returns a tuple (observation, reward, done, info). Args:
    action (object/list): an action provided by the environment
> * Returns:
    > > * observation (object/list): agent's observation of the current environment
    > > * reward (float/list) : amount of reward returned after previous action
    > > * done (boolean/list): whether the episode has ended.
    > > * info (dict): contains auxiliary diagnostic information.
* `env.reset()`
> * Resets the state of the environment and returns an initial observation.
> * Returns: observation (object/list): the initial observation of the space.


### Making a Submission
> * Create your RL model in the [rl.py]() file and commit and push to this repo.
> * Train your RL model and save the parameters to a file, any format works.
> * Create a file named [agent.py]() which is capable of using your trained model to play the game and return the rewards.
> * Commit and push both the [agent.py]() and the parameters file to this repo.
> * Evaluation of your model will be done based on the performance of the [agent.py]() file.
> * In case your agent.py script is not working, your submission will not be considered for evaluation
### The information provided above should be enough to make an RL Model. All the Best!
