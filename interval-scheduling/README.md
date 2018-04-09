## Interval Scheduling

> Given N activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

 - [Writeup](https://vsoch.github.io/2018/interval-scheduling/)
 - [My Solution](main.py)
 - [Wikipedia Solution](https://en.wikipedia.org/wiki/Interval_scheduling)


## Docker

```bash
# Random selection of N
docker run vanessa/algorithms:interval-scheduling

# Choose N to be 10 for 10 contender events
docker run vanessa/algorithms:interval-scheduling 10
------------------------------------------------------------------------------
Generating random 10 intervals...

------------------------------------------------------------------------------
New Activity (0605:0972) grated-punk-hiding-9459
New Activity (0832:0874) outstanding-lemon-seminar-2029
New Activity (0983:0997) eccentric-ricecake-wedding-1521
New Activity (0324:0892) bumfuzzled-lemon-circus-5995
New Activity (0528:0800) carniverous-lettuce-snoring-1097
New Activity (0523:0748) angry-cupcake-sleeping-8743
New Activity (0544:0588) sticky-hope-festival-4404
New Activity (0818:0824) arid-leg-opening-3822
New Activity (0667:0706) cowy-house-decorating-9202
New Activity (0067:0192) swampy-platanos-festival-6695
------------------------------------------------------------------------------
Chooosing greedy intervals...
------------------------------------------------------------------------------
Step 1 added Activity (0067:0192) swampy-platanos-festival-6695
Step 2 added Activity (0544:0588) sticky-hope-festival-4404
Step 3 added Activity (0667:0706) cowy-house-decorating-9202
Step 4 added Activity (0818:0824) arid-leg-opening-3822
Step 5 added Activity (0832:0874) outstanding-lemon-seminar-2029
Step 6 added Activity (0983:0997) eccentric-ricecake-wedding-1521
Total steps taken: 6
------------------------------------------------------------------------------

We have a final set of 6 activities!
------------------------------------------------------------------------------
Chosen Activity (0067:0192) swampy-platanos-festival-6695
Chosen Activity (0544:0588) sticky-hope-festival-4404
Chosen Activity (0667:0706) cowy-house-decorating-9202
Chosen Activity (0818:0824) arid-leg-opening-3822
Chosen Activity (0832:0874) outstanding-lemon-seminar-2029
Chosen Activity (0983:0997) eccentric-ricecake-wedding-1521
```

