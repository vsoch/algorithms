#!/usr/bin/env python

# 1. First Come First Out
# Here we do everything in serial, no async!
# Note that we are just *calculating* the times and not just enduring them

# 1-Input the processes along with their burst times
# 2-Find waiting time (wt) for all processes.
# 3-As first process that comes need not to wait so 
#   waiting time for process 1 will be 0 i.e. wt[0] = 0.
# 4-Find waiting time for all other processes i.e. for
#   process i ->  wt[i] = bt[i-1] + wt[i-1] .
# 5-Find turnaround time = waiting_time + burst_time 
#   for all processes.
# 6-Find average waiting time = 
#   total_waiting_time / no_of_processes.
# 7-Similarly, find average turnaround time = 
#   total_turn_around_time / no_of_processes.


class Process(object):

    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
 

class FCFOQueue(object):

    def __init__(self, pids, burst_times):

        print('First Come First Out Process Control Block!\n')
        self.processes = []
        for p in range(len(pids)):
            pid = pids[p]
            burst_time = burst_times[p]
            process = Process(pid, burst_time)
            self.processes.append(process)
        
    def __str__(self):
        return "first-come-first-out-queue:%s" %(len(self.processes))

    def __repr__(self):
        return "FCFOQueue:%s" %(len(self.processes))

    def calculate_waiting_times(self):
        '''we calculate the waiting time as the time it takes for the
           previous processes (the burst times), and for the first process
           we don't have to wait (the time starts at zero.) Note that we don't
           actually wait for these times (no use of time.sleep) we just 
           calculate them.
        '''
 
        # let's count time in general units
        wait_times = []
        current = wait_time = 0

        for p in self.processes:
            
            # We won't actually wait :)

            # The first process has wait time of zero
            wait_times.append(wait_time)
            wait_time = current + p.burst_time

            # Wait time for next process
            current = wait_time
                        
        return wait_times


    def calculate_turnaround_times(self, wts=None):
        '''the turnaround time is how long it takes to wait, start, and finish
           so we care about the burst time of the process too!
        '''
        trts = []

        if wts == None:
            wts = self.calculate_waiting_times()

        for p in self.processes:
            waiting_time = wts.pop(0)
            trt = waiting_time + p.burst_time
            trts.append(trt)
            
        return trts


def main():

    # 1-Input the processes along with their burst time (bt).
    pids = [1, 2, 3]

    # Burst time is time takes CPU to get running
    burst_times = [10, 5, 8]

    # Create the FCFO Queue
    queue = FCFOQueue(pids, burst_times)

    # 2 - Find waiting time (wt) for all processes.
    wts = queue.calculate_waiting_times()
    # [0, 10, 15]
    print('   Waiting times: %s' %' | '.join(str(x) for x in wts))

    # 5-  Find turnaround time = waiting_time + burst_time 
    #    for all processes.
    trt = queue.calculate_turnaround_times()
    # [0, 15, 23]
    print('Turnaround times: %s' %' | '.join(str(x) for x in trt))

    # Find average waiting time
    average_waiting = sum(wts) / len(queue.processes)
    average_turnaround = sum(trt) / len(queue.processes)    
    print('  avg turnaround: %s' %average_turnaround)
    print('     avg waiting: %s' %average_waiting)


if __name__ == '__main__':
    main()
