#The purpose of this is to test other multiwinner voting rules against greatest_θ_winning_set
#Note: k is defined as the number of winners in a given election

def plurality_k_2(candidates, ballots, vote_counts):
    
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

def plurality_k_1(candidates, ballots, vote_counts): 
    
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
    top_candidate = [candidate[0] for candidate in sorted_candidates[:1]]
    
    return top_candidate

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

def borda_k_1(candidates, ballots, vote_counts): #As far as I am aware, you can't use borda on datasets where not every ballots ranks every candidate, meaning for the NYC and minneapolis data this cannot be used
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
    top_candidate = [candidate[0] for candidate in sorted_candidates[:1]]
    
    return top_candidate

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
    #print(remaining_candidates)
    return list(remaining_candidates)

def stv_k_1(candidates, ballots, vote_counts):
    #Input: 
    #candidates - an array of each candidate
    #ballots - an array of each ballot, ballots cannot include candidates that do not appear in "candidates"
    #vote_counts - an array of the same length as "ballots", if each individual ballot is included in "ballots", each
    #member of vote_counts should be 1, if the data is aggregated, then the count should be equal to the amount of times
    #that exact ballot appeared in the raw data

    #A1: Initialize the vote tally for each candidate
    vote_tally = {candidate: 0 for candidate in candidates}
    remaining_candidates = set(candidates)
    
    while len(remaining_candidates) > 1:
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
    #print(remaining_candidates)
    return list(remaining_candidates)

def copeland_k_2(candidates, ballots, vote_counts):
    #Input: 
    #candidates - an array of each candidate
    #ballots - an array of each ballot, ballots cannot include candidates that do not appear in "candidates"
    #vote_counts - an array of the same length as "ballots", if each individual ballot is included in "ballots", each
    #member of vote_counts should be 1, if the data is aggregated, then the count should be equal to the amount of times
    #that exact ballot appeared in the raw data

    #A1: Initialize a dictionary to store pairwise wins for each candidate/initialize variables
    copeland_scores = {candidate: 0 for candidate in candidates}
    
    condorcet_winner = None #Flag to store the Condorcet winner if found

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
    
    #A3: Check each candidate for Condorcet criterion
    for candidate, score in copeland_scores.items():
        if score == len(candidates) - 1:
            condorcet_winner = candidate
            break

    #A4: Sort candidates by Copeland scores in descending order
    sorted_candidates = sorted(copeland_scores.items(), key=lambda item: item[1], reverse=True)
    
    #A5: If a Condorcet winner is found, ensure they're at the top of the list
    if condorcet_winner:
        sorted_candidates = [(condorcet_winner, copeland_scores[condorcet_winner])] + \
                            [item for item in sorted_candidates if item[0] != condorcet_winner]

    #A6: Return the top 2 candidates
    top_2_candidates = [candidate[0] for candidate in sorted_candidates[:2]]
    
    return top_2_candidates

def copeland_k_1(candidates, ballots, vote_counts):
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

    #A3: Check each candidate for Condorcet criterion 
    for candidate, score in copeland_scores.items():
        if score == len(candidates):
            return [candidate] #This is the condorcet winner, return it

    #A4: If no condorcet winner is found, sort candidates by Copeland scores in descending order
    sorted_candidates = sorted(copeland_scores.items(), key=lambda item: item[1], reverse=True)
    
    #A5: Return the top candidate
    top_candidate = [candidate[0] for candidate in sorted_candidates[:1]]

    return top_candidate

def greatest_theta_winning_set_k_2(candidates, ballots, vote_counts): #Find greatest θ-winning set when k = 2, copying this over because this should only be used with comparing_voting_rules.py, so I can afford to get rid of all the checks for incomplete ballots, thus making it more efficient
    
    #Input: 
    #candidates - an array of each candidate
    #ballots - an array of each ballot, ballots cannot include candidates that do not appear in "candidates"
    #vote_counts - an array of the same length as "ballots", if each individual ballot is included in "ballots", each
    #member of vote_counts should be 1, if the data is aggregated, then the count should be equal to the amount of times
    #that exact ballot appeared in the raw data

    #A1: Initialize variables

    #Greatest θ-winning set variables
    max_coefficient = 0
    greatest_theta_winning_sets = ['No winning sets found']

    #Number of ballots (n) and candidates (m)
    n = len(ballots)
    m = len(candidates)

    #A2: Directly compute θ coefficient for each pair by iterating through each ballot
    
    current_champ_tiebreaker = 0 #Tiebreaker is compared to the current theta winners tiebreaker
    for i in range(m):
        for j in range(i + 1, m):
            tiebreaker = 0 #Initialize tiebreaker
            min_theta = 100000000 #Initialize min theta
            counter = 0 #Initialize counter
            for k in range(m):
                if k != i and i != j and k != j: #If k is not i or j
                    current_theta = 0 #Initialize current theta
                    for ballot, count in zip(ballots, vote_counts):
                        if ballot.index(candidates[i]) < ballot.index(candidates[k]) or ballot.index(candidates[j]) < ballot.index(candidates[k]): #If any candidate in this pair beats k
                            counter += count
                            if ballot.index(candidates[i]) < ballot.index(candidates[k]) and ballot.index(candidates[j]) < ballot.index(candidates[k]): #If both candidates in the pair beat k, for tiebreaking purposes
                                tiebreaker += count
                    #Normalize θ by the total number of votes to get the coefficient
                    current_theta = counter / sum(vote_counts) 
                    if current_theta < min_theta:
                        min_theta = current_theta
                    counter = 0 #Reset counter
            tiebreaker = 0 
            pair_coefficent = min_theta #Set the pair coefficient to the minimum theta found
            if pair_coefficent > max_coefficient:
                max_coefficient = pair_coefficent
                greatest_theta_winning_sets = [(candidates[i], candidates[j])]
                current_champ_tiebreaker = tiebreaker
            elif pair_coefficent == max_coefficient and max_coefficient != 0:
                #greatest_theta_winning_sets.append((candidates[i], candidates[j]))
                if tiebreaker > current_champ_tiebreaker: #If the current pair has a higher tiebreaker than the current champion
                    greatest_theta_winning_sets = [(candidates[i], candidates[j])]
                    current_champ_tiebreaker = tiebreaker
                elif tiebreaker == current_champ_tiebreaker: #If the tiebreakers are equal, this should be rare
                    #print("Tie found")
                    greatest_theta_winning_sets.append((candidates[i], candidates[j]))

    #A3: Return greatest θ-winning sets
    return greatest_theta_winning_sets, max_coefficient

def greatest_theta_winning_set_k_1(candidates, ballots, vote_counts): #Find greatest θ-winning set when k is 1, copying this over because this should only be used with comparing_voting_rules.py, so I can afford to get rid of all the checks for incomplete ballots, thus making it more efficient
    
    #Input: 
    #candidates - an array of each candidate
    #ballots - an array of each ballot, ballots cannot include candidates that do not appear in "candidates"
    #vote_counts - an array of the same length as "ballots", if each individual ballot is included in "ballots", each
    #member of vote_counts should be 1, if the data is aggregated, then the count should be equal to the amount of times
    #that exact ballot appeared in the raw data

    #A1: Initialize variables

    #Greatest θ-winning set variables
    max_coefficient = 0
    greatest_theta_winning_sets = ['No winning sets found']

    #Number of ballots (n) and candidates (m)
    n = len(ballots)
    m = len(candidates)

    #A2: Directly compute θ coefficient for each pair by iterating through each ballot
    
    for j in range(m):
        counter = 0 #Initialize counter
        min_theta = 100000000 #Initialize min theta
        for k in range(m):
            if k != j: #If k is not j
                current_theta = 0 #Initialize current theta
                for ballot, count in zip(ballots, vote_counts):
                    if ballot.index(candidates[j]) < ballot.index(candidates[k]): #If any candidate beats k
                        counter += count
                #Normalize θ by the total number of votes to get the coefficient
                current_theta = counter / sum(vote_counts) 
                if current_theta < min_theta:
                    min_theta = current_theta
                counter = 0 #Reset counter
        this_coefficent = min_theta #Set the pair coefficient to the minimum theta found
        if this_coefficent > max_coefficient:
            max_coefficient = this_coefficent
            greatest_theta_winning_sets = [(candidates[j])]
        elif this_coefficent == max_coefficient and max_coefficient != 0: #If there is a tie, not sure if this would ever happen when k = 1
            greatest_theta_winning_sets.append((candidates[j]))

    #A3: Return greatest θ-winning sets
    return greatest_theta_winning_sets, max_coefficient

def find_candidate_pair_theta(candidate_c_i, candidate_c_j, candidates, ballots, vote_counts): #function to find the theta coefficent of a pair of candidates for the greatest theta winning set when k = 2, , copying this over because this should only be used with comparing_voting_rules.py, so I can afford to get rid of all the checks for incomplete ballots, thus making it more efficient
        
    #Input: 
    #candidates - an array of each candidate
    #ballots - an array of each ballot, ballots cannot include candidates that do not appear in "candidates"
    #vote_counts - an array of the same length as "ballots", if each individual ballot is included in "ballots", each
    #member of vote_counts should be 1, if the data is aggregated, then the count should be equal to the amount of times
    #that exact ballot appeared in the raw data
    #candidate_c_i/candidate_c_j - the candidates whose theta coefficient we are trying to find

    #A1: Initialize variables

    #Remove c_i and c_j from the list of candidates

    candidates = [s for s in candidates if s not in (candidate_c_i, candidate_c_j)]

    #Number of ballots (n) and candidates (m)
    n = len(ballots)
    m = len(candidates)

    #A2: Directly compute θ coefficient for each pair by iterating through each ballot
    
    min_theta = 100000000 #Initialize min theta
    counter = 0 #Initialize counter
    for k in range(m):
        if candidate_c_i != candidate_c_j: #If c_i is not c_j
            current_theta = 0 #Initialize current theta
            for ballot, count in zip(ballots, vote_counts):
                if ballot.index(candidate_c_i) < ballot.index(candidates[k]) or ballot.index(candidate_c_j) < ballot.index(candidates[k]): #If any candidate in this pair beats k
                    counter += count
            #Normalize θ by the total number of votes to get the coefficient
            current_theta = counter / sum(vote_counts) 
            if current_theta < min_theta:
                min_theta = current_theta
            counter = 0 #Reset counter
    pair_coefficent = min_theta #Set the pair coefficient to the minimum theta found
    
    if(min_theta == 100000000):
        raise ValueError("Error: Both candidates in the pair are the same")
    
    #A3: Return theta coefficient
    return pair_coefficent

def find_single_candidate_theta(candidate_c_i, candidates, ballots, vote_counts): #function to find the theta coefficent of a single candidate when k = 1, , copying this over because this should only be used with comparing_voting_rules.py, so I can afford to get rid of all the checks for incomplete ballots, thus making it more efficient
        
    #Input: 
    #candidates - an array of each candidate
    #ballots - an array of each ballot, ballots cannot include candidates that do not appear in "candidates"
    #vote_counts - an array of the same length as "ballots", if each individual ballot is included in "ballots", each
    #member of vote_counts should be 1, if the data is aggregated, then the count should be equal to the amount of times
    #that exact ballot appeared in the raw data
    #candidate_c_i/candidate_c_j - the candidates whose theta coefficient we are trying to find

    #A1: Initialize variables

    #Remove c_i from the list of candidates

    candidates = [s for s in candidates if s not in (candidate_c_i)]

    #Number of ballots (n) and candidates (m)
    n = len(ballots)
    m = len(candidates)

    #A2: Directly compute θ coefficient for each pair by iterating through each ballot
    
    min_theta = 100000000 #Initialize min theta
    counter = 0 #Initialize counter
    for k in range(m):
        #To account for datasests where not all candidates are ranked, we need to check if the pair of candidates are in the ballot, every non listed candidate is considered to be of lower rank than any listed candidates
        current_theta = 0 #Initialize current theta
        for ballot, count in zip(ballots, vote_counts):
            if ballot.index(candidate_c_i) < ballot.index(candidates[k]): #If candidate i beats k
                counter += count
        #Normalize θ by the total number of votes to get the coefficient
        current_theta = counter / sum(vote_counts) 
        if current_theta < min_theta:
            min_theta = current_theta
        counter = 0 #Reset counter
    this_coefficent = min_theta #Set the coefficient to the minimum theta found
    
    #A3: Return theta coefficient
    return this_coefficent