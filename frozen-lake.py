import gym
import numpy as np

env = gym.make('FrozenLake8x8-v1', render_mode='human')
Q = np.zeros([env.observation_space.n, env.action_space.n])

eta = 0.628
gma = 0.90
epis = 5000
rev_list = []

for i in range(epis):
    s = env.reset()[0]
    rAll = 0
    d = False
    # For 100 steps
    j = 0
    while j < 99:
        env.render()
        j+=1
        # Select an action based on a decreasingly random scale
        a = np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n)*(1./(i+1)))
        #a = np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n)*(1./(i+1)))
        s1,r,t1,t2,_ = env.step(a)
        d = t1 or t2
        Q[s,a] = Q[s,a] + eta*(r + gma*np.max(Q[s1,:]) - Q[s,a])
        rAll += r
        s = s1
        if d == True:
            break
    rev_list.append(rAll)
    env.render()
print("Reward sum on all episodes:"+ str(sum(rev_list)/epis))
print("Final Values Q-Table")
print(Q)