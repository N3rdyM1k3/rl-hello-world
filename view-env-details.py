import gym

#env = gym.make('MountainCarContinuous-v0', render_mode='human')
env = gym.make('CartPole-v0', render_mode='human')


observation = env.reset()
for t in range(25):
    env.render()
    print(observation)
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        print("Finished after {} steps".format(t+1))
        break

print(env.action_space)
print(env.observation_space)
