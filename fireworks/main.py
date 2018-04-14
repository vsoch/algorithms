#!/usr/bin/env python

# Copyright (c) 2018, Vanessa Sochat
# All rights reserved.

# Given a larger start and ending range, create some kind of fireworks 
# display so that they come on gradually, and climax and then the show
# ends.
# We want events with a staggered start, something that looks like: 

# (s=start,e=end, and the number indicates the firework number!)
# [start]  [s1]   [s2]  [s3]  [s4] [s5][s6][sN] [end]

# We are going to do the following:
# 1. start with a number of fireworks, a start and end time
# 2. randomly generate a firework, meaning design and size
# 3. calculate trigger times for a firework depending on increasing size. 
#
# See LICENSE in the repository root


import random
import argparse
import itertools
import string
import math
import time
import sys


################################################################################
# Firework Object
################################################################################


class Firework(object):

    def __init__(self, end, start=0, size=None, simple=None, design=None):
        '''a Firework object holds the start and end time for firing a firework,
           along with functions to fire them! We only need the duration to
           estimate a range of trigger (firing times) for the firework.
           Other implementations might have other uses for start and end times. 

           Parameters
           ==========
           start: the starting time of the interval to select from        
           end: the ending time of the interval to select from        
           size: the maximum width of the firework
           simple: generate a simple vs. complicated design

        '''
        self.start = start                            # time zero
        self.end = end                                # ending time
        self.duration = end-start

        # Colors and Characters

        self.randomize()

        # Sizing

        self.offset = random.randint(0, 40)
        self.inner = random.choice( range( 0, 15 ))
        self.size = size or random.choice(range(7, 21, 2))

        # Design Complexity

        self.simple = self.choose_complexity(simple)
        self.thresh = design or random.choice(range(1,50))

    def __repr__(self):
        return self.__str__()

    def randomize(self):
        '''set colors and characters for the firework. Called upon 
           init, and can be called later to create a new design.
        '''

        self.color1 = self.choose_color()
        self.color2 = self.choose_color()
        self.bgcolor = self.choose_color()

        # Characters

        self.char1 = random.choice(',.*^`\'"')
        self.char2 = self.choose_character()
        self.bgchar = self.choose_character()

        # Design

        self.thresh = random.choice(range(1,50))


    def speak(self):
        print("Baby I'm a %s!" %str(self))

    def oggle(self):
        '''generate an audience expression, with some padding on the left.
        '''

        oggles = ['Again!',
                  'Ahhhhh!',
                  'Amazing!',
                  'Avocado!',
                  "Baby you're a...",
                  "Bam!",
                  "Bang!",
                  'Beautiful!',
                  'Boom!',
                  'Crackle...',
                  'Damn!',
                  'Did you see that?',
                  "Fizz...",
                  'Ha!',
                  "Hiss...",
                  'Kaboom!',
                  'Look!',
                  'Magical!',
                  'Omg!',
                  'Ooooooh!',
                  'Pow!',
                  'Sizzle...',
                  'Spa!',
                  'Whoa!',
                  'Woohoo!',
                  'Wow!',
                  'Wowza!',
                  "Whoosh!"]

        oggle = random.choice(oggles)
        padding = " "*int(random.uniform(0,75))
        print(padding + oggle)


    def boum(self, clear=True):
        '''a firework "boum" will print all stages of the firework!
        '''
        show = self.ready()
        for design in show:

            # Every once in a while, print an oggle :)
            if random.uniform(0,1) > 0.95:
                self.oggle()
                time.sleep(0.5)
                
            print(design)
            time.sleep(0.1)
            if clear:
                print('\033c')


    def count_designs(self):
        '''get the number of designs anticipated for the firework, depending
           on its size
        '''
        return len(range(0, self.size))


    def ready(self):
        '''prepare the show! This is an interator to reveal slowly increasing
           in size fireworks. boum!
        '''
        number = self.count_designs()
        delta = self.size / number
        inner = self.inner + delta

        for size in range(number):
            inner = self.inner - delta
            yield self.generate_design(size=size, inner=inner)


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


    def choose_complexity(self, simple=None):
        '''a simple design uses generate_design, and a 
           simple complexity uses "generate_shape"

           Parameters
           ==========
           simple: boolean or None. If None, randomly select True/False
                   otherwise, use what is given.
        ''' 

        if simple is None:
            simple = random.choice([True, False])
        return simple


    def generate_shape(self, char='O', n1=15, n2=15, offset=None,
                             inner=5, outer=15, matrix=False):

        '''generate a firework design based on inner and outer lengths,
           and variables n1 and n2 to control the angles.

           Parameters
           ==========
           outer: a multiplier for the outer radius. 
           inner: the same for the inner radius. The outer-inner is the 
                  section that we are going to fill in (based on a zigzag)
           char: the character to fill in when appropriate
           n1,n1: factors to scale zigzag. When n1==n2 we get circle pattern
           matrix: if True, return list of lists instead of string

        '''
        design = ''
        if matrix is True:
            design = []

        # This is the (inside portion) of the outer circle (diameter)
        # [-----][-----]

        for i in range(outer*2):

            # This is the (outer portion) of the same circle (diameter)
            # [-----][-----][-----][-----]
            row = []

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
                    row.append(char)
                else:
                    row.append(' ')

            # - At the end of a row, add a newline
            row.append('\n')
 
            # Did we want an offset?
            if offset is not None:
                row = [' ']*offset + row

            # If we have a matrix, append the row. Otherwise add to design str
            if matrix is True:
                design.append(row)
            else:
                design+= ''.join(row)

        return design


    def generate_center(self, char1, char2, size, offset, matrix=False):
        ''' This firework deisgn is a glowing orb. It just needs to be circular 
            and fluctuate between two colors, and could be center for a more
            complex design. The core will consist of two design characters, 
            alternating in rows increasing in size to form something that 
            looks circular up to a max width, and from some offset from the left.

            Parameters
            ==========
            matrix: if True, return each value in a cell (versus string)
 
              ^,^,^
            ^,^,^,^,^
            ^,^,^,^,^
              ^,^,^

            Returns
            =======
            design: list of lists (matrix) if matrix is True, otherwise string

        '''

        design = ''

        # If returning a matrix, we will return a list of lists
        if matrix is True:
            design = []

        # Slightly different ranges determine top and bottom of shape
        top_range = range(2, size, 2)
        bot_range = range(size, 2, -2)
        ranges = itertools.chain(top_range, bot_range)

        for i in ranges:
            if i == size: i = size - 1
            padding = [" "]*(size-i + offset)
            row = padding + i*["%s%s" %(char1,char2)]

            # Matrix return appends a row
            if matrix is True:
                design.append(row)

            # Otherwise extend the string
            else:
                design += '\n' + ''.join(row)

        return design


    def generate_design(self, offset=None, size=None, simple=None, inner=None):
        '''a firework will consist of two design characters, alternating in rows
           increasing in size to form something that looks circular up to a max
           width, and from some offset from the left. Thresh is a parameter to
           determine cutoff threshold for filling along zig zag, and drives
           design.

            ^,^,^
          ^,^,^,^,^
          ^,^,^,^,^
            ^,^,^

        '''

        # Width and offset from the left
        size = size or self.size
        offset = offset or self.offset

        char1 = '%s%s\033[0m' %(self.color1, self.char1)
        char2 = '%s%s\033[0m' %(self.color2, self.char2)
        bgchar = '%s%s\033[0m' %(self.bgcolor, self.bgchar)
       
        # Step 4: generate the firework design
        simple = simple or self.simple
        inner = inner or self.inner

        # Case 1: the user just wants a simple design.
        if simple:
            design = self.generate_center(size=size,
                                          char1=char1,
                                          char2=char2,
                                          offset=offset)

       
        # Case 2: complex design
  
        else:
            design = self.generate_shape(char=bgchar,
                                         outer=size,
                                         inner=inner,
                                         n1=self.thresh, 
                                         n2=self.thresh,
                                         offset=offset)

  
        return design

 
    def choose_color(self):
        '''choose a random color! We will add a style and background sometimes.
        '''
        colors = []
        for style in range(8):
            for fg in range(30,38):
                s1 = ''
                format = ';'.join([str(style), str(fg)])
                s1 += '[%s;1m' % (format)
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
 

def fireworks_show(fireworks):
    '''create the loop of tasks to start the fireworks show!
       
       Parameters
       ==========
       fireworks: the schedule of fireworks!

    '''
    for firework in fireworks:
        firework.boum()
    print('Woohoo!')


################################################################################
# Main
################################################################################


def get_parser():
    '''return the parser for main, giving the user access to all fireworks
       generation options
    '''
    parser = argparse.ArgumentParser(description='Fireworks Generator!')
    parser.add_argument('--alpha', '-a', type=float, default=0.01, dest='alpha',
                        help='size of region to sample to determine durations')
    parser.add_argument('--boum', default=False, action="store_true",
                        help='forget the show, generate and boum a firework!')
    parser.add_argument('--design', '-d', type=int, default=None, dest='design',
                        help='parameter N to drive the design.')
    parser.add_argument('--size', '-s', type=int, default=None, dest='size',
                        help='maximum size of firework (undefined for random)')
    parser.add_argument('--simple', default=None, action="store_true",
                        help='just return a simple design.')
    parser.add_argument('--complex', default=None, action="store_true",
                        help='choose a complex design firework')
    parser.add_argument('--number', '-n', type=int, default=1000, dest='number',
                        help='number of fireworks for the show')
    parser.add_argument('--end', '-e', type=int, default=100, 
                        help='limit for end time / duration', dest='end')

    return parser



def get_firework_schedule(end_time=1000,
                          start_time=0,
                          number=100,
                          design=None,
                          simple=None,
                          alpha=0.1):

    '''get a random interval time between start time and end time.
       Start time and end time should be in integer units.

       Parameters
       ==========
       end_time: the set ending time for all fireworks from start_time, 
                 fireworks will end in small range (alpha) of this time.
       start_time: the start time of the show, reasonably is 0
       number: the number of fireworks to deploy
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
        firework = Firework(start=start, end=end, design=design, simple=simple)
        schedule.append(firework)

        start_time=firework.start
        count+=1

    return schedule


def main():
    '''the entrypoint to the fireworks algorithm example. In
       this function, we:
 
       1. generate a list of firework start and end times
       2. start the show and fire in sequence, with increasing size 
       3. the show ends when we run out of fireworks

    '''
    parser = get_parser()

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(1)

    # Get user preference for design, complex gets priority
    design_type = "random"
    simple = None

    if args.complex is True:
        simple = False
        design_type = "complex"

    elif args.simple is True:
        simple = True
        design_type = "simple"

    
    # Just generate one firework and exit

    if args.boum is True:
        firework = Firework(end=args.end,
                            size=args.size,
                            simple=simple,
                            design=args.design)
        firework.boum()
        sys.exit(0)

    section('Generating fireworks schedule!...\n')
    schedule = get_firework_schedule(end_time=args.end,
                                     design=args.design,
                                     simple=simple,
                                     number=args.number,
                                     alpha=args.alpha)

    print('The schedule is prepared!')
    print('   [fireworks]: %s' %len(schedule))
    print('      [design]: %s' %design_type)
    time.sleep(2.0)

    fireworks_show(schedule)

if __name__ == "__main__":
    main()
