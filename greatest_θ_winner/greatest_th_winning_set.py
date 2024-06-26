#Tasks: 
#T1 - Explain in comments in this code what exactly this algorithm is doing
#T2 - Make a different function for when we consider unranked candidates and ranked candidates because the ladder is more efficent than the former
#T3 - I can def make the code for A2 less horrible 

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
    greatest_theta_winning_sets = ['No winning sets found']

    #Number of ballots (n) and candidates (m)
    n = len(ballots)
    m = len(candidates)

    #A2: Directly compute θ coefficient for each pair by iterating through each ballot
    
    current_champ_tiebreaker = 0 #Tiebreaker is compared to the current theta winners tiebreaker
    for i in range(m):
        for j in range(i + 1, m):
            counter = 0 #Initialize counter
            tiebreaker = 0 #Initialize tiebreaker
            for k in range(m):
                #To account for datasests where not all candidates are ranked, we need to check if the pair of candidates are in the ballot, every non listed candidate is considered to be of lower rank than any listed candidates
                if k != i != j: #If k is not i or j
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
            #Normalize θ by the total number of votes over all compared candidates to get the coefficient
            pair_coefficient = counter / (sum(vote_counts) * m - 2)
            if pair_coefficient > max_coefficient:
                max_coefficient = pair_coefficient
                greatest_theta_winning_sets = [(candidates[i], candidates[j])]
            elif pair_coefficient == max_coefficient and max_coefficient != 0:
                #greatest_theta_winning_sets.append((candidates[i], candidates[j]))
                if tiebreaker > current_champ_tiebreaker: #If the current pair has a higher tiebreaker than the current champion
                    greatest_theta_winning_sets = [(candidates[i], candidates[j])]
                    current_champ_tiebreaker = tiebreaker
                elif tiebreaker == current_champ_tiebreaker: #If the tiebreakers are equal, this should be rare
                    #print("Tie found")
                    greatest_theta_winning_sets.append((candidates[i], candidates[j]))

    #A3: Return greatest θ-winning sets
    return greatest_theta_winning_sets, max_coefficient

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

    #Example with 50 ballots that are hard-coded, there will be a 0.631-winning set here, shows how this algorithm
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

    #Example with 6 ballots that are hard-coded, there will be a 0.59 winning set found here, shows how this algorithm
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

def check_for_ties(tests, number_of_ballots, number_of_candidates): #This method is used to check for ties in the greatest θ-winning set, this tests how good the tiebreaking method is
    #Fiddle with the numbers to test different values of m and n
    import random
    winners = []
    ballots = []
    total_ties = 0

    for i in range(tests): #Do this many tests
        candidates = [f'Candidate_{i}' for i in range(1, number_of_candidates)] #Generate this many candidates (candidate_number - 1)
        vote_counts = []
        ballots = []
        for j in range(number_of_ballots):
            ballot = random.sample(candidates, len(candidates)) 
            ballots.append(ballot)
            vote_counts.append(1)
        winners, coefficient = find_greatest_theta_winning_set(candidates, ballots, vote_counts)
        if len(winners) > 1: 
            total_ties += 1
        #if(i%1000 < 1):
        #print(i) #Print for troubleshooting
        #print(ballot) #Print for troubleshooting
    print(total_ties) #How many ties was that?
    return(total_ties)

#Testing
#if __name__ == "__main__":
#    main()
#check_for_ties(100000, 10, 20)
#with open('output.txt', 'w') as file: #Store output in output.txt text file
#    output = check_for_ties(100000, 10, 20) 
#    file.write(f"For 20 candidates and 10 ballots tested 100,000 times, there were {output} ties\n")
