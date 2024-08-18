#Tasks: 
#T1 - Explain in comments in this code what exactly this algorithm is doing
#T2 - Make a different function for when we consider unranked candidates and ranked candidates because the ladder is more efficent than the former
#T3 - I can def make the code for A2 less horrible 

def find_greatest_theta_winning_set(candidates, ballots, vote_counts): #Find greatest θ-winning set when k = 2
    
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
                #To account for datasests where not all candidates are ranked, we need to check if the pair of candidates are in the ballot, every non listed candidate is considered to be of lower rank than any listed candidates
                if k != i and i != j and k != j: #If k is not i or j
                    current_theta = 0 #Initialize current theta
                    for ballot, count in zip(ballots, vote_counts):
                        if candidates[k] not in ballot:
                            if candidates[j] or candidates[i] in ballot:
                                counter += count
                                if candidates[j] and candidates[i] in ballot: #If both candidates in the pair are in the ballot, for tiebreaking purposes
                                    tiebreaker += count
                        elif candidates[i] in ballot and candidates[j] in ballot: #If pair of candidates are in the ballot
                            if ballot.index(candidates[i]) < ballot.index(candidates[k]) or ballot.index(candidates[j]) < ballot.index(candidates[k]): #If any candidate in this pair beats k
                                counter += count
                                if ballot.index(candidates[i]) < ballot.index(candidates[k]) and ballot.index(candidates[j]) < ballot.index(candidates[k]): #If both candidates in the pair beat k, for tiebreaking purposes
                                    tiebreaker += count
                        elif candidates[i] in ballot and candidates[j] not in ballot: #If candidate i is in the ballot but j is not
                            if ballot.index(candidates[i]) < ballot.index(candidates[k]): #If i beats k     
                                counter += count
                        elif candidates[j] in ballot and candidates[i] not in ballot: #If candidate j is in the ballot but i is not           
                            if ballot.index(candidates[j]) < ballot.index(candidates[k]): #If j beats k 
                                counter += count  
                    #Normalize θ by the total number of votes to get the coefficient
                    current_theta = counter / sum(vote_counts) 
                    if current_theta < min_theta:
                        min_theta = current_theta
                    counter = 0 #Reset counter
            #tiebreaker = 0 #disable tiebreaker for testing
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

def find_greatest_theta_winning_set_k_is_1(candidates, ballots, vote_counts): #Find greatest θ-winning set when k is 1
    
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

    #print(f'Initial ballots {ballots}') #Print for troubleshooting

    #A2: Directly compute θ coefficient for each pair by iterating through each ballot
    
    for j in range(m):
        counter = 0 #Initialize counter
        min_theta = 100000000 #Initialize min theta
        for k in range(m):
            #To account for datasests where not all candidates are ranked, we need to check if the pair of candidates are in the ballot, every non listed candidate is considered to be of lower rank than any listed candidates
            if k != j: #If k is not j
                current_theta = 0 #Initialize current theta
                for ballot, count in zip(ballots, vote_counts):
                    if candidates[k] not in ballot:
                        if candidates[j] in ballot:
                            counter += count
                    elif candidates[j] in ballot: #If candidate in the ballot
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

def check_for_ties(tests, number_of_ballots, number_of_candidates): #This method is used to check for ties in the greatest θ-winning set, this tests how good the tiebreaking method is
    #Fiddle with the numbers to test different values of m and n
    import random
    winners = []
    ballots = []
    total_ties = 0

    for i in range(tests): #Do this many tests
        candidates = [f'Candidate_{i}' for i in range(0, number_of_candidates)] #Generate number_of_candidates many candidates
        vote_counts = []
        ballots = [] 
        for j in range(number_of_ballots):
            ballot = random.sample(candidates, len(candidates)) 
            ballots.append(ballot)
            vote_counts.append(1)
        winners, coefficient = find_greatest_theta_winning_set(candidates, ballots, vote_counts)
        if len(winners) > 1: 
            total_ties += 1
        if(i%5000 < 1):
            print(f"{i/1000}% complete") #Print to track progress when doing 100,000 tests
        #print(ballot) #Print for troubleshooting
    #print(f'There was {total_ties} total ties.') #How many ties was that?
    return(total_ties)

def find_candidate_pair_theta(candidate_c_i, candidate_c_j, candidates, ballots, vote_counts): #function to find the theta coefficent of a pair of candidates for the greatest theta winning set when k = 2
        
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
        #To account for datasests where not all candidates are ranked, we need to check if the pair of candidates are in the ballot, every non listed candidate is considered to be of lower rank than any listed candidates
        if candidate_c_i != candidate_c_j: #If c_i is not c_j
            current_theta = 0 #Initialize current theta
            for ballot, count in zip(ballots, vote_counts):
                if candidates[k] not in ballot:
                    if candidate_c_j or candidate_c_i in ballot:
                        counter += count
                elif candidate_c_i in ballot and candidate_c_j in ballot: #If pair of candidates are in the ballot
                    if ballot.index(candidate_c_i) < ballot.index(candidates[k]) or ballot.index(candidate_c_j) < ballot.index(candidates[k]): #If any candidate in this pair beats k
                        counter += count
                elif candidate_c_i in ballot and candidate_c_j not in ballot: #If candidate i is in the ballot but j is not
                    if ballot.index(candidate_c_i) < ballot.index(candidates[k]): #If i beats k     
                        counter += count
                elif candidate_c_j in ballot and candidate_c_i not in ballot: #If candidate j is in the ballot but i is not           
                    if ballot.index(candidate_c_j) < ballot.index(candidates[k]): #If j beats k 
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

def find_single_candidate_theta(candidate_c_i, candidates, ballots, vote_counts): #function to find the theta coefficent of a single candidate when k = 1
        
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
            if candidates[k] not in ballot:
                if candidate_c_i in ballot:
                    counter += count
            elif candidate_c_i in ballot: #If candidate i and k are in the ballot
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

#Testing

def main(): #Testing various inputs
    import random
    #Example with 100 ballots and varied combinations
    candidates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    vote_counts = []
    
    #Generate 100 ballots with varied combinations and lengths
    ballots = []
    for _ in range(100):
        ballot = random.sample(candidates, len(candidates)) 
        ballots.append(ballot)
        vote_counts.append(1)

    #print(ballots) #Print ballots for debugging

    winners, coefficient = find_greatest_theta_winning_set(candidates, ballots, vote_counts)
    print(f"Greatest {coefficient}-winning sets:", winners)

    #Example with 50 ballots that are hard-coded, there will be a 0.6-winning set here, shows how this algorithm
    #can handle agregated data
    candidates = ['A', 'B', 'C', 'D']
    vote_counts = [20, 20, 5, 5]
    ballots = [
        ['A', 'B', 'C', 'D'],
        ['B', 'A', 'D', 'C'],
        ['B', 'D', 'C', 'A'],
        ['D', 'C', 'B', 'A'],
    ]

    winners, coefficent = find_greatest_theta_winning_set(candidates, ballots, vote_counts)
    print(f"Greatest {coefficent}-winning sets:", winners)

    #Example with 6 ballots that are hard-coded, there will be a 0.5 winning set found here, shows how this algorithm
    #can handle instances where not all candidates are ranked
    candidates = ['A', 'B', 'C', 'D']
    vote_counts = [1,1,1,1,1,1]
    ballots = [
        ['A', 'B', 'C'],  
        ['A', 'C', 'B'],  
        ['B', 'A', 'C'], 
        ['B', 'C', 'A'],
        ['C', 'A', 'B'],
        ['C', 'B', 'A']  
    ]
    winners, coefficent = find_greatest_theta_winning_set(candidates, ballots, vote_counts)
    print(f"Greatest {coefficent}-winning sets:", winners)

    #Example with fruit survey, shows order of the candidates doesnt matter and showcases k = 1
    vote_counts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ballots = [['Fruit', 'Chips', 'Muffins', 'Munchkins', 'Popcorn'], ['Fruit', 'Popcorn', 'Munchkins', 'Chips', 'Muffins'], ['Munchkins', 'Chips', 'Fruit', 'Muffins', 'Popcorn'], ['Fruit', 'Chips', 'Popcorn', 'Munchkins', 'Muffins'], ['Popcorn', 'Chips', 'Fruit', 'Munchkins', 'Muffins'], ['Fruit', 'Popcorn', 'Chips', 'Munchkins', 'Muffins'], ['Chips', 'Popcorn', 'Muffins', 'Munchkins', 'Fruit'], ['Munchkins', 'Muffins', 'Chips', 'Popcorn', 'Fruit'], ['Fruit', 'Munchkins', 'Popcorn', 'Muffins', 'Chips'], ['Fruit', 'Chips', 'Munchkins', 'Muffins', 'Popcorn'], ['Fruit', 'Muffins', 'Chips', 'Popcorn', 'Munchkins'], ['Chips', 'Munchkins', 'Fruit', 'Muffins', 'Popcorn'], ['Fruit', 'Popcorn', 'Chips', 'Muffins', 'Munchkins'], ['Fruit', 'Chips', 'Popcorn', 'Munchkins', 'Muffins'], ['Munchkins', 'Chips', 'Fruit', 'Muffins', 'Popcorn'], ['Fruit', 'Munchkins', 'Muffins', 'Chips', 'Popcorn'], ['Munchkins', 'Muffins', 'Fruit', 'Chips', 'Popcorn'], ['Fruit', 'Popcorn', 'Chips', 'Muffins', 'Munchkins'], ['Chips', 'Popcorn', 'Munchkins', 'Fruit', 'Muffins'], ['Fruit', 'Popcorn', 'Muffins', 'Munchkins', 'Chips'], ['Chips', 'Popcorn', 'Munchkins', 'Fruit', 'Muffins'], ['Popcorn', 'Fruit', 'Chips', 'Munchkins', 'Muffins'], ['Munchkins', 'Muffins', 'Fruit', 'Chips', 'Popcorn'], ['Fruit', 'Popcorn', 'Chips', 'Munchkins', 'Muffins'], ['Fruit', 'Muffins', 'Chips', 'Munchkins', 'Popcorn'], ['Chips', 'Fruit', 'Munchkins', 'Popcorn', 'Muffins'], ['Muffins', 'Fruit', 'Munchkins', 'Popcorn', 'Chips']]
    candidates = ['Chips', 'Popcorn', 'Muffins', 'Munchkins', 'Fruit']
    winners, coefficent = find_greatest_theta_winning_set(candidates, ballots, vote_counts)
    print(f"Greatest {coefficent}-winning sets:", winners)
    candidates = ['Muffins', 'Fruit', 'Popcorn', 'Munchkins', 'Chips']
    winners, coefficent = find_greatest_theta_winning_set(candidates, ballots, vote_counts)
    print(f"Greatest {coefficent}-winning sets:", winners)

def test_for_ties():
    with open('output.txt', 'a') as file: #Store output in output.txt text file
        number_of_ballots = [3, 5, 10, 50, 100, 1000]
        number_of_candidates = [3, 5, 10, 20]
        for n in number_of_ballots:
            output = check_for_ties(100000, n, 3) 
            file.write(f"For 3 candidates and {n} ballots tested 100,000 times, there were {output} ties\n")
            print(f'Done with {n} ballots and 3 candidates')
        for m in number_of_candidates:
            output = check_for_ties(100000, 10, m) 
            file.write(f"For {m} candidates and 10 ballots tested 100,000 times, there were {output} ties\n")
            print(f'Done with {m} candidates and 10 ballots')
#test_for_ties()
