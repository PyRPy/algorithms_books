# gfg_estimate_pi_monte_carlo.py
import random 
INTERVAL = 1000000 

num_circle_point = 0 
num_square_point = 0 

for i in range(INTERVAL):
    randx = random.uniform(-1, 1) 
    randy = random.uniform(-1, 1) 

    origin_dist = randx**2 + randy**2 
    if origin_dist <= 1:
        num_circle_point += 1 
    num_square_point += 1 

# estimate of pi 
pi = 4 * num_circle_point / num_square_point

print('estimated pi is: ', pi)

# https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/