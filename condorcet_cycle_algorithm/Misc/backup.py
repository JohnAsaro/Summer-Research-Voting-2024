def condorcet_cycle(candidates, ballots):
    from collections import defaultdict

    #Number of candidates (m) and voters/ballots (n)
    m = len(candidates)
    n = len(ballots[0])

    #A1: Initialize prefrence count matrix
    preference_count = [[0] * m for _ in range(m)] 

    #A2: Populate prefrence count matrix
    for ballot in ballots:
        for i in range(m):
            for j in range(i + 1, m):
                winner = ballot[i]
                loser = ballot[j]
                winner_idx = candidates.index(winner)
                loser_idx = candidates.index(loser)
                preference_count[winner_idx][loser_idx] += 1


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
        if traverse_dfs[node] == "visiting":
            return True  #Cycle found
        if traverse_dfs[node] == "visited":
            return False #Not part of our potential cycle so false
        
        traverse_dfs[node] = "visiting"
        stack.append(node)
        
        for neighbor in graph[node]:
            if dfs(neighbor, traverse_dfs, stack_dfs): #If our neighbor is part of a cycle
                return True #We are aswell
        
        traverse_dfs[node] = "visited" #We visited the node without detecting a cycle
        stack.pop() #Pop our node out of the stack
        return False

    for i in range(m):
        if traverse[i] == "unvisited":
            if dfs(i, traverse, stack): #If node i is part of a cycle
                return True  #Condorcet cycle found

    return False  #We passed!

# Example Inputs

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
