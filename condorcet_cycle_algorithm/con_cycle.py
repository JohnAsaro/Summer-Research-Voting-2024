#Tasks:
#1: A2 can be changed so that the amount of votes added to each prefrence matrix are pulled from the "count" column and not just assumed to be 1
from collections import defaultdict

def condorcet_cycle(candidates, ballots, vote_counts): #Takes candidates/ballots/vote counts and detects if there is a condorcet cycle

    #Input: 
    #candidates - an array of each candidate
    #ballots - an array of each ballot, ballots cannot include candidates that do not appear in "candidates"
    #vote_counts - an array of the same length as "ballots", if each individual ballot is included in "ballots", each
    #member of vote_counts should be 1, if the data is aggregated, then the count should be equal to the amount of times
    #that exact ballot appeared in the raw data

    m = len(candidates) #Number of candidates = m

    #A1: Initialize prefrence count matrix
    preference_count = [[0] * m for _ in range(m)] 

    #A2: Populate prefrence count matrix
    for ballot in ballots:

        current = ballots.index(ballot) #currrent is our current ballot
        ballot_length = len(ballot) #ballot_length = length of current ballot
        listed_candidates = set(ballot)
        unlisted_candidates = set(candidates) - listed_candidates
        
        #Increment counts for candidates listed on ballot
        for i in range(ballot_length - 1):
            for j in range(i + 1, ballot_length):
                winner = ballot[i]
                #print(f'i is {i}') #OOB error bugfixing
                loser = ballot[j]
                #print(f'j is {j}') #OOB error bugfixing
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

    #A3: Build directed graph
    graph = defaultdict(list)
    for i in range(m):
        for j in range(i + 1, m):
            if preference_count[i][j] > preference_count[j][i]:
                graph[i].append(j) #Add an edge c_i'→c_j'
            elif preference_count[i][j] < preference_count[j][i]:
                graph[j].append(i) #Add an edge c_j'→c_i'
            
    #A4: Cycle detection using DFS

    #DFS variables
    traverse = ["unvisited"] * m  #Array with m entries all listed as "unvisited"
    stack = [] #Initialize empty stack

    def dfs(node, traverse_dfs, stack_dfs):
        if traverse_dfs[node] == "visiting": #Cycle found
            cycle_start = stack_dfs.index(node)
            cycle = stack_dfs[cycle_start:] + [node]
            return cycle #Return it
        if traverse_dfs[node] == "visited": #Not part of the current potential cycle
            return None #Don't return anything
        
        traverse_dfs[node] = "visiting"
        stack_dfs.append(node)
        
        for neighbor in graph[node]:
            cycle = dfs(neighbor, traverse_dfs, stack_dfs) #If our neighbor is part of a cycle
            if cycle:
                return cycle #We are aswell
        
        traverse_dfs[node] = "visited" #We visited the node without detecting a cycle
        stack.pop() #Pop our node out of the stack
        return None

    for i in range(m):
        if traverse[i] == "unvisited": #If node i is part of a cycle
            cycle = dfs(i, traverse, stack)
            if cycle:
                #Convert the cycle from indices to candidate names and print it
                cycle_names = [candidates[idx] for idx in cycle]
                print(f"A condorcet cycle exists in this input instance: {cycle_names}")
                return True #Theres a cycle so theres a condorcet cycle

    return False #No cycle so no condorcet cycle

def main(): #For manually testing inputs
    if __name__ == "__main__":
        #Example Inputs

        example_candidates = ["A", "B", "C"]
        example_vote_counts = [1, 1, 1]

        ballots_cycle = [
            ["A", "B", "C"],  #Voter 1 prefers A > B > C
            ["B", "C", "A"],  #Voter 2 prefers B > C > A
            ["C", "A", "B"]   #Voter 3 prefers C > A > B
        ]
        print(f"In this case there is a condorcet cycle and {condorcet_cycle(example_candidates, ballots_cycle, example_vote_counts)} will be returned.") 

        ballots_no_cycle = [
            ["A", "B", "C"],  #Voter 1 prefers A > B > C
            ["A", "B", "C"],  #Voter 2 prefers A > B > C
            ["C", "B", "A"],  #Voter 3 prefers C > B > A
        ]
        print(f"In this case there is no condorcet cycle and {condorcet_cycle(example_candidates, ballots_no_cycle, example_vote_counts)} will be returned.") 

#Testing
#main()