#!/usr/bin/env python

# Given a larger start and ending range, create some kind of fireworks 
# display so that they come on gradually, and climax and then the show
# ends.
# We want events with a staggered start, something that looks like: 

# (s=start,e=end, and the number indicates the firework number!)
# [start]  [s1]   [s2]  [s3]  [s4] [s5][s6][sN] [end]

# We are going to do the following:
# 1. start with a number of fireworks, a start and end time
# 2. randomly generate a firework, meaning design and size
# 3. calculate trigger times for a firework depending on increasing size. This
#    means that we start at the smallest size, and fire N times so that we fill
#    the fireworks range between it's custom start and end time.
# 4. create an event loop so the N triggers fire within the larger range with
#    the other fireworks.


import random
import argparse
import asyncio
import string
import math
import time
import sys


################################################################################
# Firework Object
################################################################################


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

        # Generate values in advance, for use later

        self.color1 = self.choose_color()
        self.color2 = self.choose_color()

        # Firework characters

        self.char1 = random.choice(',.*^`\'"')
        self.char2 = self.choose_character()

        self.offset = random.randint(0, 80)
        self.size = random.choice(range(7, 19, 2))

    def __repr__(self):
        return self.__str__()

    def speak(self):
        print("Baby I'm a %s!" %str(self))


    def boum(self):
        '''a firework "boum" will print all stages of the firework!
        '''
        show = self.ready()
        for design in show:
            print(design)


    def _get_number_boums(self):
        '''get the number of designs anticipated for the firework, depending
           on its size
        '''
        return len(range(7, self.size, 2))


    def ready(self):
        '''prepare the show! This is an interator to reveal slowly increasing
           in size fireworks. boum!
        '''
        for size in range(5, self.size, 2):
            yield self.generate_design(size=size)

    def __str__(self):
        return "Firework (%05d:%05d)" % (self.start,
                                         self.end)

    def choose_character(self):
        '''choose a random character to be the predominant (larger of the two
           designs).
        '''
        return random.choice(string.ascii_letters + 
                             string.digits + 
                             '!@#$%^*&( )_+}{')

    def choose_shape(self, char='O', n1=15, n2=15, inner=5, outer=15):
        '''generate a firework design based on inner and outer lengths,
           and variables n1 and n2 to control the angles.

           Parameters
           ==========
           outer: a multiplier for the outer radius. 
           inner: a set inner radius "cutoff" to determine printing the char

        '''
        design = ''

        # This is the (inside portion) of the outer circle (diameter)
        # [-----][-----]

        for i in range(outer*2):

            # This is the (outer portion) of the same circle (diameter)
            # [-----][-----][-----][-----]

            for j in range(outer*4):

                # We are scanning over values of x and y to define outer circle
                x,y = (j-outer*2)/2,i-outer

                # For each pair of x and y values we find the angle and radius. 
                #   arctangent returns radians, and reflects quadrant.
                #   A circle goes from 0 to 2pi radians
                angle = math.atan2(y,x)
                radius = math.sqrt(x**2 + y**2)

                # We want a function of the angle to zig zag up and down.
                #   We multiple the angle above by some factor (n1 or n2)
                #   divide by pi and 2 so the result goes from 0 to 1
                zigzag = min((angle*n1/math.pi)%2., (-angle*n2/math.pi)%2.)
                

                # Then from the angle we figure out the cutoff radius - 
                #   some value between inner and outer based on the zigzag
                #   that we want. 
                cutoff = zigzag*(outer - inner) + inner

                # (outer-inner) is the distance between outer and inner that 
                # ranges from 0 (when zigzag is 0) to outer (when zigzag is 1). 
                # This means that when zigzag is 0 it's scaled to none of the 
                # distance, and when zigzag is 1 it's scaled to the entire 
                # difference.

                # Compare the actual radius to the cutoff radius. 
                #   If actual radius is < cutoff radius --> fill in
                #   otherwise put a blank space.
                if radius < cutoff:
                    design += char
                else:
                    design += ' '

                # - At the end of a row, add a newline
            design += '\n'

        return design



    def generate_design(self, char1=None, char2=None, 
                              color1=None, color2=None,
                              offset=None, size=None):
        '''a firework will consist of two design characters, alternating in rows
           increasing in size to form something that looks circular up to a max
           width, and from some offset from the left.

            ^,^,^
          ^,^,^,^,^
          ^,^,^,^,^
            ^,^,^

        '''
        # The character pattern, size, and offset for the firework 
        char1 = char1 or self.char1
        char2 = char2 or self.char2
        color1 = color1 or self.color1
        color2 = color2 or self.color2

        # Width and offset from the left
        size = size or self.size
        offset = offset or self.offset

        char1 = '%s%s\033[0m' %(color1, char1)
        char2 = '%s%s\033[0m' %(color2, char2)

        # Step 4: generate the firework design
        # Here we take two steps:

        # 1. Create a background circle

        design = ''

        # Top half of firework 

        for i in range(2, size, 2):
            if i == size: i = size - 1
            padding = " "*(size-i + offset)
            design += '\n' + padding + i*("%s%s" %(char1,char2))

        # Bottom half

        for i in range(size, 2, -2):
            if i == size: i = size - 1
            padding = " "*(size-i + offset)
            design += '\n' + padding + i*("%s%s" %(char1,char2))

        # and 2: overlay with design

        return design

 

    def choose_color(self):
        '''choose a random color! We will add a background and make it bold.
        '''

        colors = []
        for style in range(8):
            for fg in range(30,38):
                s1 = ''
                format = ';'.join([str(style), str(fg)])
                s1 += '[%sm' % (format)
                colors.append(s1)

        return "\033" + random.choice(colors)

    

################################################################################
# Helpers
################################################################################


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
 


def generate_oggle():
    '''generate an audience expression, with some padding on the left.
    '''
    oggle = random.choice(['Ooooooh!', "Again!",
                           'Ahhhhh!', "Beautiful!",
                           'Boom!', 'Amazing!',
                           "Baby you're a...", "Woohoo!",
                           'Pow!', 'Wow!', "Damn!",
                           'Sizzle...', 'Whoa!',
                           'Spa!', 'Ha!'])
    padding = " "*int(random.uniform(0,75))
    return padding + oggle





################################################################################
# Asyncio Running Loop
################################################################################


async def schedule_firework(loop, fireworks, length):
    '''run the fireworks schedule, going from the start at time 0 and stopping
       the loop at length specified

       Parameters
       ==========
       loop: the event loop
       fireworks: the list of firework objects
       length: the total length of the show (in seconds)

    '''

    # The start of the show
    start_time = loop.time()

    for firework in fireworks:

        # How many times does the firework need to fire?
        count = firework._get_number_boums()

        times = []
        for ii in range(count+1):
            # Bias closer to the end of the duration
            weight = math.pow(random.uniform(0,1),0.5)
            times.append(firework.duration*weight)

        # Generate designs for the show
        show = firework.ready()
        for design in show:

            # Callback function to print the firework
            def boum(design):

                # Every once in a while, print an oggle :)
                if random.uniform(0,1) > 0.95:
                    oggle = generate_oggle()
                    print(oggle)

                print(design, end='\r')

            # Each design will be scheduled for later
            trigger = times.pop(0)
            loop.call_at(start_time + trigger, boum, design)

    await asyncio.sleep(length)

        

def fireworks_show(fireworks, length):
    '''create the loop of tasks to start the fireworks show!
       
       Parameters
       ==========
       fireworks: the schedule of fireworks!
       length: how long the show will endure (cut after this many seconds)

    '''
    loop = asyncio.get_event_loop()
    try:
        print('Starting the show!')
        loop.run_until_complete(schedule_firework(loop, fireworks, length))
    finally:
        print('Woohoo!')
        loop.close()



################################################################################
# Main
################################################################################


def get_parser():
    '''return the parser for main, giving the user access to all fireworks
       generation options
    '''
    parser = argparse.ArgumentParser(description='Fireworks Generator!')
    parser.add_argument('--alpha', '-a', type=float, default=0.01, dest='alpha',
                        help='''the size of the region (percentage of 
                                difference between start and end) to sample''')
    parser.add_argument('--number', '-n', type=int, default=1000, dest='number',
                        help='number of fireworks for the show')
    parser.add_argument('--start','-s', type=int, default=0, 
                        help='start time', dest='start')
    parser.add_argument('--end', '-e', type=int, default=100, 
                        help='end time', dest='end')

    return parser


def get_firework_schedule(start_time=0, 
                          end_time=1000,
                          number=100,
                          alpha=0.1,
                          delta=0):

    '''get a random interval time between start time and end time.
       Start time and end time should be in integer units.

       Parameters
       ==========
       start_time: the starting time of the interval to uniformly select from        
       end_time: the set ending time for all fireworks, fireworks will end in
                 small range (alpha) of this time.
       number: the number of fireworks to deploy
       delta: the minimum change between start and end time before stopping
       alpha: the size of the region (percentage of difference between
              start and end) to sample from for new start and end times.

    '''

    schedule = []
    count = 0

    # The end time can't be less than start time.
    if end_time < start_time:
        print('end time %s cannot be at or before start %s' %(end_time,
                                                              start_time))

    # Keep going until we meet our quota
    while count < number:

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
        count+=1

    return schedule


def main():
    '''the entrypoint to the fireworks algorithm example. In
       this function, we:
 
       1. generate a list of firework start and end times
       2. start the show to output an increasing firework size up until midpoint
       3. stop firing at stoppoint

    '''
    parser = get_parser()

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(1)

    section('Generating fireworks schedule!...\n')
    schedule = get_firework_schedule(start_time=args.start,
                                     end_time=args.end,
                                     number=args.number,
                                     alpha=args.alpha)

    print('The schedule has %s fireworks!' %len(schedule))
    print('[start time]: %s' %args.start)
    print('  [end time]: %s' %args.end)
    print('     [alpha]: %s' %args.alpha)

    fireworks_show(schedule, args.end)

if __name__ == "__main__":
    main()
