## Fireworks
This is a "problem" that I made up, inspired by [interval scheduling](../interval-scheduling)
but it went in a different direction very quickly. I really like making generators, and
this one is special because it also models a real life thing, fireworks! Here is
the summary:

> Given a larger start and ending range, create some kind of fireworks display so that they come on gradually, and climax and then the show ends. We want events with a staggered start, something that looks like: 

```
(s=start,e=end, and the number indicates the firework number!)
[start]  [s1]   [s2]  [s3]  [s4] [s5][s6][sN] [end]
```

We are going to do the following:

 1. start with a number of fireworks, a start and end time
 2. randomly generate a firework, meaning design and size
 3. calculate trigger times for a firework depending on increasing size. This means that we start at the smallest size, and fire N times so that we fill the fireworks range between it's custom start and end time.
 4. create an event loop so the N triggers fire within the larger range with the other fireworks.

 - [Writeup](https://vsoch.github.io/2018/fireworks/)
 - [My Solution](main.py)


## Docker

```bash
# Random selection of N
docker run -it vanessa/algorithms:fireworks
```

You can change the number of fireworks and the end time, and this is how you control
the speed.

```
docker run -it vanessa/algorithms:fireworks --number 2000 --end 10
```
