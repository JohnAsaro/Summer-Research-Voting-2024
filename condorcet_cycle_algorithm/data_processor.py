#Tasks: Figure out why the list index goes out of range

import csv
from con_cycle import condorcet_cycle
from collections import defaultdict
from pathfinder import csvfinder

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

def print_debug(file_path):
    data = read_csv(file_path)
    print("Raw data:")
    print(data)
    
    cleaned_data = clean_data(data)
    print("Cleaned data:")
    print(cleaned_data)
    
    candidates, ballots = format_data_for_condorcet(cleaned_data)
    print("Candidates:")
    print(candidates)
    
    print("Ballots:")
    for ballot in ballots:
        print(ballot, "Length:", len(ballot))

def data_processor(file_path):
    data = read_csv(file_path)
    
    cleaned_data = clean_data(data)
    
    candidates, ballots = format_data_for_condorcet(cleaned_data)
    
    try:
        result = condorcet_cycle(candidates, ballots)
    except ValueError as e:
        print(f"Error: {e}")
        return False
    except IndexError as e:
        print(f"Index Error: {e}")
        return False
    
    return result

def main():
    if __name__ == "__main__":
        #Example usage
        file_path = csvfinder('2017-Mayor-Ballot-Records.csv')
        result = data_processor(file_path)
        print(f"Condorcet cycle found: {result}")

#Testing
#file_path = csvfinder('2017-Mayor-Ballot-Records.csv')
#main()
#print_debug(file_path)
