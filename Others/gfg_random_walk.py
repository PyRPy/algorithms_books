# gfg_random_walk.py
import random 
import numpy as np 
import matplotlib.pyplot as plt 

# prob for moving up or down 
prob = [0.05, 0.95]
start = 2 
positions = [start]

rr = np.random.random(1000) 
downp = rr < prob[0] 
upp = rr > prob[1] 

for idownp, iupp in zip(downp, upp):
    down = idownp and positions[-1] > 1 
    up = iupp and positions[-1] < 4 
    positions.append(positions[-1] - down + up) 

# plot graph 
plt.plot(positions) 
plt.show() 

# https://www.geeksforgeeks.org/random-walk-implementation-python/