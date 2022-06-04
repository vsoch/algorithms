"""

  Helper classes for a simple Process and different Queue types, for other
  examples included in this folder!

"""


class Process(object):
    def __init__(self, pid, burst_time, arrival_time):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time


class FCFOQueue(object):
    def __init__(self, pids, burst_times, arrival_times=None):

        # If no arrival times, assume all arriving at time 0
        if not arrival_times:
            arrival_times = [0 for x in range(len(pids))]

        print("First Come First Out Process Control Block!\n")
        self.processes = []
        for p in range(len(pids)):
            pid = pids[p]
            burst_time = burst_times[p]
            arrival_time = arrival_times[p]
            process = Process(pid, burst_time, arrival_time)
            self.processes.append(process)

        # Sort processes by arrival times
        self.processes.sort(key=lambda x: x.arrival_time, reverse=True)

    def __str__(self):
        return "first-come-first-out-queue:%s" % (len(self.processes))

    def __repr__(self):
        return "FCFOQueue:%s" % (len(self.processes))

    def calculate_waiting_times(self):
        """we calculate the waiting time as the time it takes for the
           previous processes (the burst times), and for the first process
           we don't have to wait (the time starts at zero.) Note that we don't
           actually wait for these times (no use of time.sleep) we just 
           calculate them.
        """

        # let's count time in general units
        wait_times = []
        current = wait_time = self.processes[0].arrival_time

        for p in self.processes:

            # We won't actually wait :)
            # if the arrival
            wait_time = wait_time - p.arrival_time

            # The first process has wait time of zero
            wait_times.append(wait_time)
            wait_time = current + p.burst_time

            # Wait time for next process
            current = wait_time

        return wait_times

    def calculate_turnaround_times(self, wts=None):
        """the turnaround time is how long it takes to wait, start, and finish
           so we care about the burst time of the process too!
        """
        trts = []

        if wts == None:
            wts = self.calculate_waiting_times()

        for p in self.processes:
            waiting_time = wts.pop(0)
            trt = waiting_time + p.burst_time
            trts.append(trt)

        return trts
