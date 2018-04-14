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

I had originally created an event loop so the fireworks went off at the same time, but it looks much nicer to run in serial (so the more techy cool thing doesn't look better in this case!)

 - [Writeup](https://vsoch.github.io/2018/fireworks/)
 - [My Solution](main.py)


## Usage
If you want to see this post in action:

```bash
docker run -it vanessa/algorithms:fireworks
```

or forget an entire show, just generate one random "boum"

```bash
docker run -it vanessa/algorithms:fireworks --boum
```

That will automatically select between complex and simple designs. To force a simple 
or a complex design:

```bash
docker run -it vanessa/algorithms:fireworks --boum --simple
docker run -it vanessa/algorithms:fireworks --boum --complex
```

You can also control the firework size:

```bash
docker run -it vanessa/algorithms:fireworks --boum --simple --size 5
```

Or the specific kind of `--complex` design (try a random integer!):

```bash
docker run -it vanessa/algorithms:fireworks --boum --complex --design 5
```

or generate an entire fireworks show with one kind of complex design:

```bash
docker run -it vanessa/algorithms:fireworks --complex --design 5
```

Read more about the algorithm or watch [shows here](https://vsoch.github.io/2018/fireworks/)
