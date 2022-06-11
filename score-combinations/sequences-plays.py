#!/usr/bin/env python

from copy import deepcopy

def sequences_plays(final_score=12, play_scores=[2,3,7]):

   # One row length final_scores
   combos = [[[]]] + [[] for _ in range(final_score)]
   for final_score in range(1, len(combos)):
       for play_score in play_scores:
           if final_score - play_score >= 0:
               for entry in combos[final_score-play_score]:
                   new_score = deepcopy(entry)
                   new_score.append(play_score)
                   if new_score:
                       combos[final_score].append(new_score)

   return combos[final_score]
   
print(sequences_plays())
