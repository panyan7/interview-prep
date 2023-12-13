import numpy as np
import matplotlib.pyplot as plt

mc_num_trials = 1000

theta = np.random.uniform(0, 1, mc_num_trials) * 2 * np.pi
r = np.random.uniform(0, 1, mc_num_trials)
r = np.sqrt(r)

x = np.cos(theta) * r
y = np.sin(theta) * r

plt.scatter(x, y)
plt.savefig('ball_sample.png')
