#!/usr/bin/env python

# Copyright (c) 2018, Vanessa Sochat
# All rights reserved.
#
# Given N activities with their start and finish times. Select the maximum 
# number of activities that can be performed by a single person, assuming 
# that a person can only work on a single activity at a time.
#
# See LICENSE in the repository root


import sys
import robotnamer
import shutil
import random

namer = robotnamer.EventNamer()

class Activity(object):

    def __init__(self, start_time=0, end_time=1000):
        '''an Activity is a named event with a start and end time. The start
           and end times are randomly generated on a uniform scale

           Parameters
           ==========
           start_time: the starting time of the interval to select from        
           end_time: the ending time of the interval to select from        

        '''
        self.start, self.end = get_interval_time(start_time, end_time)
        self.name = namer.generate()
        self._action("New")

    # Printing Functions

    def __repr__(self):
        return self.__str__()


    def __str__(self):
        return "Activity (%04d:%04d) %s" % (self.start,
                                            self.end,
                                            self.name )

    def choose(self):
        '''run the activitiy! This will basically print the start,
           activity name, and end time to the console
        '''
        self._action("Chosen")


    def _action(self, action=""):
        '''Print the event name, start and end times, prepended with action

           Parameters
           ==========
           action: the name of the action to prepend.

        '''
        print('%s %s' %( action, str(self)) )



def get_interval_time(start_time=0, end_time=1000):
    '''get a random interval time between start time and end time.
       Start time and end time should be in integer units

       Parameters
       ==========
       start_time: the starting time of the interval to uniformly select from        
       end_time: the ending time of the interval to uniformly select from        

    '''
    if end_time <= start_time:
        print('end time %s cannot be at or before start %s' %(end_time,
                                                              start_time))

    # Select randomly from a range between start:end
    start = random.randint(start_time, end_time)

    # Do the same, but update range to start at start :)
    end = random.randint(start, end_time)

    # If we hit edge case of start=end, just do it over with defaults :)
    if start == end:
        return get_interval_time()
    return (start, end)


def interval_schedule(activities):
    ''' Given N activities with their start and finish times. Select the maximum 
        number of activities that can be performed by a single person, assuming 
        that a person can only work on a single activity at a time.

        Strategy: choose activities just by always selecting the one that ends
                  soonest. Then dump other ones with starting times before that.

        Parameters
        ==========
        activites: a list of tuples of (start,end) time for activites

    '''
    chosen = []
    step = 0

    # Sort activities so by soonest ending
    activities = sorted(activities, key=lambda act: act.end)    

    while len(activities) > 0:

        step+=1
        
        # Choose the earliest end time, tell the user
        activity = activities.pop(0)
        activity._action('Step %s added' % step)

        # Add activity to start always, since earlier are added later
        chosen.append(activity)
        
        # Keep track of some removed metrics for the user
        keep_removing = True

        # Remove (pop) other activities with start times earlier than the start
        while keep_removing and len(activities) > 0:
            next = activities[0]
            if next.start < activity.end:
                _ = activities.pop(0)
            else:
                keep_removing = False


    print('Total steps taken: %s' %step)

    # Return... the chosen ones!
    return chosen


# Decorators and helpers for printing

def newline():
    print('-'*78)


def section(text):
    '''print a section line between blobs of text.

       Parameters
       ==========
       text: the statement or text to print

    '''
    newline()
    print(text)
    newline()
 

def main():
    '''the entrypoint to the interval-scheduling algorithm example. In
       this function, we:
 
       1. start with a random integer N
       2. generate a list of N activites, each with start, end, and name
       3. greedily choose intervals that don't have overlap

       We keep the user updated as we progress, and print the final schedule.

    '''

    # If the user provides an argument, it's N
    N = random.choice(range(1,15))
    if len(sys.argv) > 1:
        N = int(sys.argv[1])

    section('Generating random %s intervals...\n' %N)

    # Generate activity objects, each with start/end times and name
    activities = [Activity() for x in range(N)]

    # Get the schedule with no overlaps (greedy)
    section('Chooosing greedy intervals...')
    chosen = interval_schedule(activities)

    section("\nWe have a final set of %s activities!" % len(chosen))

    # Tell the user!
    [activity.choose() for activity in chosen]


if __name__ == "__main__":
    main()
