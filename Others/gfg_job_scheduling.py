# gfg_job_scheduling.py
# to find the max profit 

def printJobSchedule(arr, t):
    n = len(arr) 
    # sort jobs with decreasing order
    for i in range(n):
        for j in range(n-1-i):
            if arr[j][2] < arr[j+1][2]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 

    # track of free time slot
    result = [False] * t 

    # to store sequence of jobs 
    job = ['-1'] * t 

    # loop through all jobs 
    for i in range(len(arr)):
        for j in range(min(t-1, arr[i][1]-1), -1, -1):
            if result[j] is False:
                result[j] = True 
                job[j] = arr[i][0] 
                break 

    print(job) 

# test 
arr = [['a', 2, 100], 
	    ['b', 1, 19], 
	    ['c', 2, 27], 
	    ['d', 1, 25], 
	    ['e', 3, 15]] 

printJobSchedule(arr, 3) 
# https://www.geeksforgeeks.org/job-sequencing-problem/   
