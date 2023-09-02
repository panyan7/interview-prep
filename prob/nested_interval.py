import numpy as np
mc_num_trials = 10000
num_iters = 30

x_final = []

for _ in range(mc_num_trials):
    xs = [0.5]
    for i in range(1, num_iters+1):
        x = xs[-1] + np.random.uniform(-0.5 ** (i+1), 0.5 ** (i+1))
        xs.append(x)
    x_final.append(xs[-1])

x_final = np.array(x_final)
print(f"Mean: {x_final.mean():.6f}, expected 0.5")
print(f"Variance: {x_final.var():.6f}, expected {1/36:.6f}")
