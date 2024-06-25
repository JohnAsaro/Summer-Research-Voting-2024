#Rewriting greatest_th_winning set
#This method is a lot less efficent and does not use a prefrence matrix, but correctly calculates 
#the result such that the definitions of a θ-winning set match the paper this is based off of

#Tasks: 
#T1 - Figure out how to break ties
#T2 - Figure out how to deal with candidates not on the ballot

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
    for i in range(m):
        for j in range(i + 1, m):
            for k in range(m):
                counter = 0 #Initialize counter
                for ballot, count in zip(ballots, vote_counts):
                    if candidates[i] in ballot and candidates[j] in ballot: #If both candidates are in the ballot
                        if ballot.index(candidates[i]) < ballot.index(candidates[k]) or ballot.index(candidates[j]) < ballot.index(candidates[k]) or candidates[k] not in ballot: #If any candidate in this pair beats k or k is not listed
                            counter += count
                    if candidates[i] in ballot and candidates[j] not in ballot: #If candidate i is in the ballot but j is not
                        if ballot.index(candidates[i]) < ballot.index(candidates[k]) or candidates[k] not in ballot: #If i beats k or k is not listed        
                            counter += count
                    if candidates[j] in ballot and candidates[i] not in ballot: #If candidate j is in the ballot but i is not           
                        if ballot.index(candidates[j]) < ballot.index(candidates[k]) or candidates[k] not in ballot: #If j beats k or k is not listed   
                            counter += count  
                #Normalize θ by the total number of votes to get the coefficient
                pair_coefficient = counter / sum(vote_counts)
                if pair_coefficient > max_coefficient:
                    max_coefficient = pair_coefficient
                    greatest_theta_winning_sets = [(candidates[i], candidates[j])]
                elif pair_coefficient == max_coefficient and max_coefficient != 0:
                    greatest_theta_winning_sets.append((candidates[i], candidates[j]))

    #A3: Return greatest θ-winning sets
    return greatest_theta_winning_sets, max_coefficient

def main():
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

    #Example  with 50 ballots that are hard-coded, there will be a 1-winning set here
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

    #OUTDATED
    #Example with 6 ballots that are hard-coded, there will be no winning sets found here
    candidates = ['A', 'B', 'C']
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

    #OUTDATED
    #Example with 6 ballots that are hard-coded, there will a 0.5-winning set here
    #We have to account for incomplete ballots because those happen in the real world a lot
    candidates = ['A', 'B', 'C', 'D']
    vote_counts = [1, 1, 1, 1, 1, 1]
    ballots = [
        ['A', 'C', 'B', 'D'],
        ['A', 'B', 'D', 'C'],
        ['B', 'A', 'C', 'D'],
        ['B', 'A', 'D', 'C'],
        ['C', 'D', 'A', 'B'],
        ['D', 'C', 'B', 'A']
    ]
    winners, coefficent = find_greatest_theta_winning_set(candidates, ballots, vote_counts)
    print(f"Greatest {coefficent}-winning sets:", winners)

#Testing
if __name__ == "__main__":
    main()