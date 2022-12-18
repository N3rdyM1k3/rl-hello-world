# Do 500 random steps
import gym
env = gym.make('Acrobot-v1', render_mode="human")
env.reset()
for _ in range(500):
    env.render()
    env.step(env.action_space.sample())

# Print all envs available
from gym import envs
print(envs.registry.keys())
