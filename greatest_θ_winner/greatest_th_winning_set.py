#task - make this work it doesnt work

def find_greatest_theta_winning_set(candidates, ballots, vote_counts):
    
    #Input: 
    #candidates - an array of each candidate
    #ballots - an array of each ballot, ballots cannot include candidates that do not appear in "candidates"
    #vote_counts - an array of the same length as "ballots", if each individual ballot is included in "ballots", each
    #member of vote_counts should be 1, if the data is aggregated, then the count should be equal to the amount of times
    #that exact ballot appeared in the raw data

    #A1: Initialize variables

    #Greatest θ-winning set variables
    max_coefficient = 0
    greatest_theta_winning_sets = []

    #Number of voters (n) and candidates (m)
    n = len(ballots)
    m = len(candidates)

    #A2: Initialize preference matrix 
    preference_count = [[0] * m for _ in range(m)]

    #A3: Populate the preference matrix
    for ballot in ballots:

        current = ballots.index(ballot) #currrent is our current ballot
        ballot_length = len(ballot) #ballot_length = length of current ballot
        listed_candidates = set(ballot)
        unlisted_candidates = set(candidates) - listed_candidates
        
        #Increment counts for candidates listed on ballot
        for i in range(ballot_length - 1):
            for j in range(i + 1, ballot_length):
                winner = ballot[i]
                loser = ballot[j]
                winner_idx = candidates.index(winner)
                loser_idx = candidates.index(loser)
                preference_count[winner_idx][loser_idx] += vote_counts[current]
            
            #Increment counts for candidates not listed on ballot
            #Every candidate not listed on the ballot is considered to be ranked lower than every candidate listed on the ballot

            for listed in listed_candidates:
                listed_idx = candidates.index(listed)
                for unlisted in unlisted_candidates:
                    unlisted_idx = candidates.index(unlisted)
                    preference_count[listed_idx][unlisted_idx] += 1

            #print('WE LOOPED') #OOB error bugfixing

    #A4: Calculate θ coefficient for each pair
    for i in range(m):
        for j in range(i + 1, m):
            pair_coefficient = 0
            for k in range(m):
                if candidates[k] != candidates[i] and candidates[k] != candidates[j]:
                    counter = 0
                    if preference_count[i][k] > preference_count[k][i] or preference_count[j][k] > preference_count[k][j]:
                        counter += 1
            pair_coefficient = counter / n
            if pair_coefficient > max_coefficient:
                max_coefficient = pair_coefficient
                greatest_theta_winning_sets = [(candidates[i], candidates[j])]
            elif pair_coefficient == max_coefficient:
                    greatest_theta_winning_sets.append((candidates[i], candidates[j]))

    #A5: Return greatest θ-winning sets
    return greatest_theta_winning_sets, max_coefficient

def main():
    #Example usage
    candidates = ['A', 'B', 'C', 'D']
    vote_counts = [1, 1, 1, 1]
    ballots = [
        ['A', 'B', 'C', 'D'],
        ['B', 'A', 'D', 'C'],
        ['C', 'D', 'B', 'A']
    ]

    winners, coefficent = find_greatest_theta_winning_set(candidates, ballots, vote_counts)
    print(f"Greatest {coefficent}-winning sets:", winners)

#main()