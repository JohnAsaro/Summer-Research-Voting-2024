#The purpose of this is to test other multiwinner voting rules against greatest_θ_winning_set
#Note: k is defined as the number of winners in a given election

def plurality_k_2(candidates, ballots, vote_counts): #Doesn't work correctly, for some reason the order of the votes matters
    
    #Input: 
    #candidates - an array of each candidate
    #ballots - an array of each ballot, ballots cannot include candidates that do not appear in "candidates"
    #vote_counts - an array of the same length as "ballots", if each individual ballot is included in "ballots", each
    #member of vote_counts should be 1, if the data is aggregated, then the count should be equal to the amount of times
    #that exact ballot appeared in the raw data

    #A1: Initialize a dictionary to count votes for each candidate
    vote_tally = {candidate: 0 for candidate in candidates}
    
    #A2: Count votes for each candidate
    for ballot, count in zip(ballots, vote_counts):
        #In plurality, only the top candidate on each ballot gets the vote
        top_candidate = ballot[0]
        vote_tally[top_candidate] += count
    
    #A3: Sort candidates by vote count in descending order
    sorted_candidates = sorted(vote_tally.items(), key=lambda item: item[1], reverse=True)
    
    #A4: Return the top 2 candidates
    top_2_candidates = [candidate[0] for candidate in sorted_candidates[:2]]
    
    return top_2_candidates

def borda_k_2(candidates, ballots, vote_counts): #As far as I am aware, you can't use borda on datasets where not every ballots ranks every candidate, meaning for the NYC and minneapolis data this cannot be used
    #Input: 
    #candidates - an array of each candidate
    #ballots - an array of each ballot, ballots cannot include candidates that do not appear in "candidates"
    #vote_counts - an array of the same length as "ballots", if each individual ballot is included in "ballots", each
    #member of vote_counts should be 1, if the data is aggregated, then the count should be equal to the amount of times
    #that exact ballot appeared in the raw data

    #A1: Initialize a dictionary to store Borda points for each candidate
    borda_tally = {candidate: 0 for candidate in candidates}
    num_candidates = len(candidates)
    
    #A2: Assign Borda points based on rankings in each ballot
    for ballot, count in zip(ballots, vote_counts):
        for rank, candidate in enumerate(ballot):
            #Borda point: num_candidates - rank (higher rank means fewer points)
            borda_tally[candidate] += (num_candidates - rank) * count
    
    #A3: Sort candidates by Borda points in descending order
    sorted_candidates = sorted(borda_tally.items(), key=lambda item: item[1], reverse=True)
    
    #A4: Return the top 2 candidates
    top_2_candidates = [candidate[0] for candidate in sorted_candidates[:2]]
    
    return top_2_candidates

def stv_k_2(candidates, ballots, vote_counts):
    #Input: 
    #candidates - an array of each candidate
    #ballots - an array of each ballot, ballots cannot include candidates that do not appear in "candidates"
    #vote_counts - an array of the same length as "ballots", if each individual ballot is included in "ballots", each
    #member of vote_counts should be 1, if the data is aggregated, then the count should be equal to the amount of times
    #that exact ballot appeared in the raw data

    #A1: Initialize the vote tally for each candidate
    vote_tally = {candidate: 0 for candidate in candidates}
    remaining_candidates = set(candidates)
    
    while len(remaining_candidates) > 2:
        #A2: Reset the tally for this round
        for candidate in remaining_candidates:
            vote_tally[candidate] = 0

        #A3: Tally the first-choice votes for remaining candidates
        for ballot, count in zip(ballots, vote_counts):
            for candidate in ballot:
                if candidate in remaining_candidates:
                    vote_tally[candidate] += count
                    break

        #A4: Identify the candidate with the fewest votes
        eliminated_candidate = min(remaining_candidates, key=lambda candidate: vote_tally[candidate])

        #A5: Remove the eliminated candidate from the remaining candidates
        remaining_candidates.remove(eliminated_candidate)

        #A6: Transfer votes from the eliminated candidate to the next choice on each ballot
        for i, ballot in enumerate(ballots):
            if ballot[0] == eliminated_candidate:
                #Find the next available candidate in the ballot to transfer the vote
                for candidate in ballot[1:]:
                    if candidate in remaining_candidates:
                        ballots[i] = ballot[1:]  #Remove the eliminated candidate
                        break

    #A7: Return the final two remaining candidates
    print(remaining_candidates)
    return list(remaining_candidates)

def copeland_k_2(candidates, ballots, vote_counts):
    #Input: 
    #candidates - an array of each candidate
    #ballots - an array of each ballot, ballots cannot include candidates that do not appear in "candidates"
    #vote_counts - an array of the same length as "ballots", if each individual ballot is included in "ballots", each
    #member of vote_counts should be 1, if the data is aggregated, then the count should be equal to the amount of times
    #that exact ballot appeared in the raw data

    #A1: Initialize a dictionary to store pairwise wins for each candidate
    copeland_scores = {candidate: 0 for candidate in candidates}
    
    #A2: Compare every pair of candidates
    for i in range(len(candidates)):
        for j in range(i + 1, len(candidates)):
            cand1 = candidates[i]
            cand2 = candidates[j]
            
            cand1_wins = 0
            cand2_wins = 0
            
            #Compare cand1 and cand2 across all ballots
            for ballot, count in zip(ballots, vote_counts):
                #Skip ballots that don't rank both candidates
                if cand1 not in ballot or cand2 not in ballot:
                    continue
                
                #Check the position of cand1 and cand2 in the ballot
                if ballot.index(cand1) < ballot.index(cand2):
                    cand1_wins += count
                elif ballot.index(cand1) > ballot.index(cand2):
                    cand2_wins += count
            
            #Determine the result of the pairwise matchup
            if cand1_wins > cand2_wins:
                copeland_scores[cand1] += 1  #cand1 wins
            elif cand1_wins < cand2_wins:
                copeland_scores[cand2] += 1  #cand2 wins
            else:
                copeland_scores[cand1] += 0.5  #tie
                copeland_scores[cand2] += 0.5  #tie

    #A3: Sort candidates by Copeland scores in descending order
    sorted_candidates = sorted(copeland_scores.items(), key=lambda item: item[1], reverse=True)
    
    #A4: Return the top 2 candidates
    top_2_candidates = [candidate[0] for candidate in sorted_candidates[:2]]
    
    return top_2_candidates