# -*- coding: utf-8 -*-
"""
Chapter 8 Greedy algorithms
"""

# a list of states to cover
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# stations you can choose from
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

# find the 'best' station

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print("final stations are: ", final_stations)
