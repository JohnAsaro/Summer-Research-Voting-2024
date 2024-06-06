import csv
from collections import defaultdict

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    return data

def clean_data(data):
    cleaned_data = []
    for row in data:
        cleaned_row = [candidate.strip() for candidate in row if candidate.strip()]
        if cleaned_row:
            cleaned_data.append(cleaned_row)
    return cleaned_data

def format_data_for_condorcet(cleaned_data):
    candidates = list(set(candidate for row in cleaned_data for candidate in row))
    return candidates, cleaned_data

def condorcet_cycle(candidates, ballots):
    m = len(candidates)
    n = len(ballots)

    # Ensure all ballots have the correct number of candidates
    for ballot in ballots:
        if len(ballot) != m:
            raise ValueError("Each ballot must rank exactly all candidates.")

    preference_count = [[0] * m for _ in range(m)]

    for ballot in ballots:
        for i in range(m):
            for j in range(i + 1, m):
                winner = ballot[i]
                loser = ballot[j]
                winner_idx = candidates.index(winner)
                loser_idx = candidates.index(loser)
                preference_count[winner_idx][loser_idx] += 1

    graph = defaultdict(list)
    for i in range(m):
        for j in range(m):
            if i != j and preference_count[i][j] > preference_count[j][i]:
                graph[i].append(j)

    traverse = ["unvisited"] * m
    stack = []

    def dfs(node, traverse_dfs, stack_dfs):
        if traverse_dfs[node] == "visiting":
            return True
        if traverse_dfs[node] == "visited":
            return False
        
        traverse_dfs[node] = "visiting"
        stack_dfs.append(node)

        for neighbor in graph[node]:
            if dfs(neighbor, traverse_dfs, stack_dfs):
                return True

        traverse_dfs[node] = "visited"
        stack_dfs.pop()
        return False

    for i in range(m):
        if traverse[i] == "unvisited":
            if dfs(i, traverse, stack):
                return True

    return False

def main(file_path):
    data = read_csv(file_path)
    cleaned_data = clean_data(data)
    candidates, ballots = format_data_for_condorcet(cleaned_data)
    result = condorcet_cycle(candidates, ballots)
    return result

# Example usage
file_path = "C:/Users/johnn/Desktop/School/Summer-Research/Code/Summer_Research_Voting_2024/condorcet_cycle_algorithm/Data/2017-Mayor-Ballot-Records.csv"
result = main(file_path)
print(f"Condorcet cycle found: {result}")
