import random
mc_num_trials = 1000000

count_end = [[], []]
for _ in range(mc_num_trials):
    cur_count = 0
    while True:
        cur_count += 1
        x = random.randint(1, 6)
        if x == 6:
            count_end[(cur_count + 1) % 2].append(cur_count)
            break

ev_end_in_a = sum(count_end[0]) / len(count_end[0])
ev_end_in_b = sum(count_end[1]) / len(count_end[1])
prob_end_in_a = len(count_end[0]) / mc_num_trials
prob_end_in_b = len(count_end[1]) / mc_num_trials
print(f"EV end in A {ev_end_in_a:.6f}, expected {61/11:.6f}")
print(f"EV end in B {ev_end_in_b:.6f}, expected {72/11:.6f}")
print(f"Prob end in A {prob_end_in_a:.6f}, expected {6/11:.6f}")
print(f"Prob end in B {prob_end_in_b:.6f}, expected {5/11:.6f}")
