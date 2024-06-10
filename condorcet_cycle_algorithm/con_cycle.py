#Tasks:
#1: A3 can be made more efficent, its not technically neccesary to loop through all items in the matrix,
#but its not a huge deal either, unless we run into computing limitations I wouldn't change it. 

from collections import defaultdict

def condorcet_cycle(candidates, ballots): #Takes candidates and ballots and detects if there is a condorcet cycle

    #Number of candidates (m) and voters/ballots (n)
    m = len(candidates)
    n = len(ballots[0])

    #A1: Initialize prefrence count matrix
    preference_count = [[0] * m for _ in range(m)] 

    #A2: Populate prefrence count matrix
    for ballot in ballots:
        n = len(ballot)
        for i in range(n - 1):
            for j in range(i + 1, n):
                winner = ballot[i]
                #print(f'i is {i}') #OOB error bugfixing
                loser = ballot[j]
                #print(f'j is {j}') #OOB error bugfixing
                winner_idx = candidates.index(winner)
                loser_idx = candidates.index(loser)
                preference_count[winner_idx][loser_idx] += 1
            #print('WE LOOPED') #OOB error bugfixing

    #A3: Build directed graph
    graph = defaultdict(list)
    for i in range(m - 1):
        for j in range(i + 1, m):
            if (preference_count[i][j] == 0 and preference_count[j][i] == 0): #If both prefrence counts are empty, we are counting ballots that dont exist and should move on
                pass
            elif preference_count[i][j] > preference_count[j][i]:
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

        ballots_cycle = [
            ["A", "B", "C"],  #Voter 1 prefers A > B > C
            ["B", "C", "A"],  #Voter 2 prefers B > C > A
            ["C", "A", "B"]   #Voter 3 prefers C > A > B
        ]
        print(f"In this case there is a condorcet cycle and {condorcet_cycle(example_candidates, ballots_cycle)} will be returned.") 

        ballots_no_cycle = [
            ["A", "B", "C"],  #Voter 1 prefers A > B > C
            ["A", "B", "C"],  #Voter 2 prefers A > B > C
            ["C", "B", "A"],  #Voter 3 prefers C > B > A
        ]
        print(f"In this case there is no condorcet cycle and {condorcet_cycle(example_candidates, ballots_no_cycle)} will be returned.") 

#Testing
#main()