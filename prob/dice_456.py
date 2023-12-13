import random
mc_num_trials = 100000

success_trials = []
fail_trials = []
for _ in range(mc_num_trials):
    N = 0
    success = True
    while True:
        dice = random.randint(1, 6)
        N += 1
        if dice in [1,2,3]:
            success = False
        if dice == 6:
            break
    if success:
        success_trials.append(N)
    else:
        fail_trials.append(N)
print(len(success_trials) / mc_num_trials)
print(sum(success_trials) / len(success_trials))
print(len(fail_trials) / mc_num_trials)
print(sum(fail_trials) / len(fail_trials))
