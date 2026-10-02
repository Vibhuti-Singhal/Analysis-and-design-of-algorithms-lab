"""
Program: Fractional Knapsack and Job Scheduling
Author: Vibhuti Singhal
Description: Implements two greedy algorithms.

Input:
Weights, values, capacity, and job details.

Output:
Maximum knapsack profit and optimal job sequence.
"""

from typing import List
from dataclasses import dataclass


# -------------------------------------------------
# 1. Fractional Knapsack
# -------------------------------------------------

def fractional_knapsack(weights: List[int],
                        values: List[int],
                        capacity: int) -> float:

    # Calculate value/weight ratio
    items = []

    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    # Sort by highest value/weight ratio
    items.sort(reverse=True)

    total_profit = 0.0

    for ratio, weight, value in items:

        if capacity == 0:
            break

        # Take the complete item
        if weight <= capacity:
            capacity -= weight
            total_profit += value

        # Take fraction of the item
        else:
            fraction = capacity / weight
            total_profit += value * fraction
            capacity = 0

    return total_profit


# -------------------------------------------------
# 2. Job Scheduling with Deadlines
# -------------------------------------------------

@dataclass
class Job:
    id: int
    deadline: int
    profit: int


def job_scheduling(jobs: List[Job]) -> List[int]:

    # Sort jobs according to decreasing profit
    jobs.sort(key=lambda job: job.profit, reverse=True)

    # Maximum deadline
    max_deadline = max(job.deadline for job in jobs)

    # Slots for scheduled jobs
    slots = [None] * (max_deadline + 1)

    # Schedule jobs
    for job in jobs:

        # Find latest available slot before deadline
        for slot in range(job.deadline, 0, -1):

            if slots[slot] is None:
                slots[slot] = job
                break

    # Return job IDs in scheduled order
    sequence = []

    for slot in range(1, max_deadline + 1):
        if slots[slot] is not None:
            sequence.append(slots[slot].id)

    return sequence


# -------------------------------------------------
# Example
# -------------------------------------------------

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

profit = fractional_knapsack(weights, values, capacity)

print("Maximum Knapsack Profit:", profit)


jobs = [
    Job(1, 2, 100),
    Job(2, 1, 19),
    Job(3, 2, 27),
    Job(4, 1, 25),
    Job(5, 3, 15)
]

sequence = job_scheduling(jobs)

print("Optimal Job Sequence:", sequence)