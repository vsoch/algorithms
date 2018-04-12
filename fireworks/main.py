#!/usr/bin/env python

# Given a larger start and ending range, create some kind of fireworks 
# display so that they come on gradually, and fade out gradually. 
# We want nested events, something that looks like: 

# (s=start,e=end, and the number indicates the firework number!)
# [start]  [s1] [s2] [s3] [sN] .. [eN] [e3] [e2] [e1]  [end]

# We would want to know, for some range from start to end, what is the value 
# of N such that firework N starts after N-1, and finishes before it? 
# I think we can do this recursively, with a stopping condition 
# that the start is equal to the end time.

import random
import argparse
import asyncio
import string
import time


class Firework(object):

    def __init__(self, start, end, loop=None):
        '''a Firework object holds the start and end time for firing a firework,
           along with functions to fire them!

           Parameters
           ==========
           start: the starting time of the interval to select from        
           end: the ending time of the interval to select from        

        '''
        self.start = start                            # time zero
        self.end = end                                # ending time
        self.duration = end-start

        self.color = self.choose_color()
        self.design = self.choose_design()
        self.frequency = self.choose_frequency()


    def __repr__(self):
        return self.__str__()

    def speak(self):
        print("Baby I'm a %s!" %str(self))


    def boum(self):
        print("Boum! %s%s\033[0m" % ( self.color,
                                      self.design ))

                       
    def __str__(self):
        return "Firework (%05d:%05d)" % (self.start,
                                         self.end)

    def choose_design(self):
        '''choose a random design!
        '''
        chars = random.choice('!@#$%^*&( )_+}{')
        choosefrom = string.ascii_letters + string.digits + chars 
        design = random.choice(choosefrom)
        size = random.randint(1,75)       
        return design*size

    def choose_frequency(self):
        '''choose a random frequency
        '''
        frequencies = list(range(2,30,2))
        return random.choice(frequencies)


    def choose_color(self):
        '''choose a random color!
        '''

        colors = {'CYAN': "\033[36m",
                  'PURPLE': "\033[95m",
                  'RED': "\033[91m",
                  'DARKRED': "\033[31m",
                  'YELLOW': "\033[93m"}

        key = random.choice(list(colors.keys()))
        return colors[key]



def get_firework_schedule(start_time=0, 
                          end_time=1000,
                          alpha=0.1,
                          delta=0):

    '''get a random interval time between start time and end time.
       Start time and end time should be in integer units.

       Parameters
       ==========
       start_time: the starting time of the interval to uniformly select from        
       end_time: the ending time of the interval to uniformly select from        
       delta: the minimum change between start and end time before stopping
       alpha: the size of the region (percentage of difference between
              start and end) to sample from for new start and end times.

    '''

    schedule = []
    change = 100

    # The end time can't be less than start time.
    if end_time < start_time:
        print('end time %s cannot be at or before start %s' %(end_time,
                                                              start_time))

    # If we have a start time earlier or equal to end, break and return
    while end_time > start_time and change > delta:

        # We will operate in a tiny range between start and end
        difference = end_time - start_time
        change = int(alpha*difference)

        # Select randomly from the small range for new start and end
        start = random.randint(start_time, start_time+change)
        end = random.randint(end_time-change, end_time)

        # Otherwise, add to list and keep going!
        firework = Firework(start,end)
        schedule.append(firework)

        start_time=firework.start
        end_time=firework.end

    return schedule


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
 


def get_parser():

    parser = argparse.ArgumentParser(description='Fireworks Generator!')

    parser.add_argument('--alpha', '-a', type=float, default=0.01, dest='alpha',
                        help='''the size of the region (percentage of 
                                difference between start and end) to sample''')

    parser.add_argument('--start','-s', type=int, default=0, 
                        help='start time', dest='start')

    parser.add_argument('--end', '-e', type=int, default=500, 
                        help='end time', dest='end')

    return parser



@asyncio.coroutine
def booms(firework, start_time):

    # Time passed since starting the show
    progress = time.time() - start_time

    # Sleep and hand off to other fireworks if not time to start
    while progress < firework.start:
        yield from asyncio.sleep(firework.frequency)
        progress = time.time() - start_time

    # When we are over the start time, calculate ending 
    ending = time.time() + firework.duration

    # Keep firing until we reach the ending time
    while time.time() < ending:
        firework.boum()
        yield from asyncio.sleep(firework.frequency)
        

def fireworks_show(fireworks):
    '''create the loop of tasks to start the fireworks show!
       
       Parameters
       ==========
       fireworks: the schedule of fireworks!

    '''
    print('Starting the show!')
    loop = asyncio.get_event_loop()
    start=time.time()
    tasks = [asyncio.ensure_future(booms(firework, start)) for firework in fireworks ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


def main():
    '''the entrypoint to the fireworks algorithm example. In
       this function, we:
 
       1. generate a nested list of firework start and end times
       2. start the show to output an increasing firework size up until midpoint
       3. stop firing at stoppoint

    '''
    parser = get_parser()

    try:
        args = parser.parse_args()
    except:
        parser.print_help()

    section('Generating fireworks schedule!...\n')
    schedule = get_firework_schedule(start_time=args.start,
                                     end_time=args.end,
                                     alpha=args.alpha)

    print('The schedule has %s fireworks!' %len(schedule))
    print('[start time]: %s' %args.start)
    print('  [end time]: %s' %args.end)
    print('     [alpha]: %s' %args.alpha)

    fireworks_show(schedule)

if __name__ == "__main__":
    main()
