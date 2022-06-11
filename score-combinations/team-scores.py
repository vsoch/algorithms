#!/usr/bin/env python

def get_score_combination_count(final_score_A=6, final_score_B=3, points=[2,3,7]):
    # Team A possible final scores X Team B possible final scores
    M = []
    for i in range(final_score_A + 1):  # iterate through rows
        row = []
        for j in range(final_score_B + 1):  # iterate through cols
            row.append(0)
        M.append(row)
    # There is one way for both teams to get a score of 0
    M[0][0] = 1

    for team_a_current_score in range(final_score_A + 1):  # iterate through rows
        for team_b_current_score in range(final_score_B + 1):  # iterate through cols
            for play in points:  # e.g., 2,3,7
                last_play_a = team_a_current_score - play
                last_play_b = team_b_current_score - play
                if last_play_a >= 0:
                    M[team_a_current_score][team_b_current_score] += M[last_play_a][team_b_current_score]
                if last_play_b >= 0:
                    M[team_a_current_score][team_b_current_score] += M[team_a_current_score][last_play_b]

    print(M)
    return M[final_score_A][final_score_B]

   
print(get_score_combination_count())
print(get_score_combination_count(12, 15))
