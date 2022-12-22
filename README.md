Welcome to my hello world for ai gym. I will be trying to follow along with a toturial provided here: 

https://towardsdatascience.com/reinforcement-learning-with-openai-d445c2c687d2

Ok I think you are done with that article but you need to establish a credits section. Also: 
atari: observation_space is needed to be represented by a 210x160x3 tensor which makes our Q-table even more complicated. Also, each action is repeatedly performed for a duration of k frames, where k is uniformly sampled from {2,3,4}. With 33,600 pixels in RGB channels with values ranging from 0–255 the environment clearly has become overly complicated. A simple Q-learning approach can’t be used here. Deep learning with its CNN architecture is the solution for this problem and a topic you should focus on for follow up of this introductory article.

Other TODOs:
- show state action reward in a graphic simultaniouesly 
- speed runs? maybe only render every x runthroughs? 
- https://stable-baselines3.readthedocs.io/en/master/
- TensorFlow & PyTorch