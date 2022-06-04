#!/usr/bin/env python

"""
  1. First Come First Out
  Here we do everything in serial, no async!
  Note that we are just *calculating* the times and not just enduring them

  1-Input the processes along with their burst times
  2-Find waiting time (wt) for all processes.
  3-As first process that comes need not to wait so 
    waiting time for process 1 will be 0 i.e. wt[0] = 0.
  4-Find waiting time for all other processes i.e. for
    process i ->  wt[i] = bt[i-1] + wt[i-1] .
  5-Find turnaround time = waiting_time + burst_time 
    for all processes.
  6-Find average waiting time = 
    total_waiting_time / no_of_processes.
  7-Similarly, find average turnaround time = 
    total_turn_around_time / no_of_processes.

    Usage: python first-come-first-out.py 

    First Come First Out Process Control Block!

       Waiting times: 0 | 10 | 15
    Turnaround times: 10 | 15 | 23
      avg turnaround: 16.0
         avg waiting: 8.333333333333334

"""

from bases import Process, FCFOQueue


def main():

    # 1-Input the processes along with their burst time (bt).
    pids = [1, 2, 3]
    burst_times = [10, 5, 8]

    # Create the FCFO Queue
    queue = FCFOQueue(pids, burst_times)

    # Burst time is time takes CPU to get running
    print("     Burst times: %s" % " | ".join(str(x) for x in burst_times))

    # 2 - Find waiting time (wt) for all processes.
    wts = queue.calculate_waiting_times()
    # [0, 10, 15]
    print("   Waiting times: %s" % " | ".join(str(x) for x in wts))

    # 5-  Find turnaround time = waiting_time + burst_time
    #    for all processes.
    trt = queue.calculate_turnaround_times()
    # [0, 15, 23]
    print("Turnaround times: %s" % " | ".join(str(x) for x in trt))

    # Find average waiting time
    average_waiting = sum(wts) / len(queue.processes)
    average_turnaround = sum(trt) / len(queue.processes)
    print("  avg turnaround: %s" % average_turnaround)
    print("     avg waiting: %s" % average_waiting)


if __name__ == "__main__":
    main()
