#!/usr/bin/env python

def number_combinations_final_score(final_score=12, play_scores=[2,3,7]):

   # Prepare matrix with final scores in cols, options in rows
   # 1 0 0 0 0 0 0 0 0 0 
   # 1 0 0 0 0 0 0 0 0 0
   # 1 0 0 0 0 0 0 0 0 0
   combos = [[1] + [0] * final_score for _ in play_scores]
   for row in range(len(play_scores)):
       for col in range(1, final_score + 1):
           # Look at value in previous row
           # If row == 0, there is no previous play
           # previous play is one row up
           if row < 1:
               without_play = 0
           else:
               without_play = combos[row-1][col] 
           
           # Can we go left in the matrix to get play without the value
           current_play = play_scores[row]
           
           # We can get the previous value
           if col >= current_play:
               with_play = combos[row][col - current_play]           
           else:
               with_play = 0
           combos[row][col] = without_play + with_play

   print(combos)
   return combos[-1][-1]
           
print(number_combinations_final_score())
