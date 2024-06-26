import csv
from greatest_th_winning_set import find_greatest_theta_winning_set
from pathfinder import csvfinder

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    return data

def clean_data(data):
    cleaned_data = []
    vote_counts = []
    header = data[0]
    header_lower = [column.lower() for column in header] #Set all columns in header to lowercase
    count_index = header_lower.index("count") #With all of the columns in header as lowercase, index("count") is not case sensitive

    for row in data[1:]: #For row in data skipping header row
        count = int(row[count_index]) #Vote count for this row is count
        cleaned_row = [candidate.strip() for i, candidate in enumerate(row) if i != count_index and candidate.strip() and candidate.strip().lower() != 'null']  #Process data and ignore 'null' and 'count' column
        if cleaned_row:
            cleaned_data.append(cleaned_row)
            vote_counts.append(count)

    return cleaned_data, vote_counts

def format_data_for_theta(cleaned_data): 
    candidates = list(set(candidate for row in cleaned_data for candidate in row)) #Extracts candidates from csv
    return candidates, cleaned_data

def data_processor(file_path):
    data = read_csv(file_path)
    
    cleaned_data, vote_counts = clean_data(data)
    
    candidates, ballots = format_data_for_theta(cleaned_data)
    
    try:
        result = find_greatest_theta_winning_set(candidates, ballots, vote_counts)
    except ValueError as e:
        print(f"Error: {e}")
        return False
    except IndexError as e:
        print(f"Index Error: {e}")
        return False
    
    return result

def print_debug(file_path):
    
    counter = 0 #Counter used for debugging
    
    data = read_csv(file_path)
    #print("Raw data:")
    #print(data)
    
    cleaned_data, vote_counts = clean_data(data)
    #print("Cleaned data:")
    #print(cleaned_data)
    
    candidates, ballots = format_data_for_theta(cleaned_data)
    print("Ballots:")
    for ballot in ballots: #Print each ballot
        counter += 1            
        print(counter, ballot, "Length:", len(ballot))

    print("Candidates:") #Print each candidate
    print(candidates)

    print("Vote counts:") #Print vote counts
    print(vote_counts)
 
def main():
    if __name__ == "__main__":
        #Example usage
        file_path = csvfinder('2017-Mayor-Ballot-Records.csv')
        winners, coefficient = data_processor(file_path)
        print(f"Greatest {coefficient}-winning sets:", winners)

#Testing

#Example usage for Test 1
#file_path = csvfinder('2017-Mayor-Ballot-Records.csv')
#winners, coefficient = data_processor(file_path)
#print(f"Greatest {coefficient}-winning sets:", winners)

#Example usage for Test 2
#file_path = csvfinder('Concycle-example.csv')
#winners, coefficient = data_processor(file_path)
#print(f"Greatest {coefficient}-winning sets:", winners)

#Example usage for Test 3
#file_path = csvfinder('2021-Mayor-Cast-Vote-Record.csv')
#winners, coefficient = data_processor(file_path)
#print(f"Greatest {coefficient}-winning sets:", winners)

#Example usage for Test 4
#file_path = csvfinder('Concycle-test.csv')
#winners, coefficient = data_processor(file_path)
#print(f"Greatest {coefficient}-winning sets:", winners)

#Example usage for Test 5
#file_path = csvfinder('test5.csv')
#winners, coefficient = data_processor(file_path)
#print(f"Greatest {coefficient}-winning sets:", winners)

#Example usage for Test 6
#file_path = csvfinder('test6.csv')
#winners, coefficient = data_processor(file_path)
#print(f"Greatest {coefficient}-winning sets:", winners)

#Example usage for Test 7
#file_path = csvfinder('test7.csv')
#winners, coefficient = data_processor(file_path)
#print(f"Greatest {coefficient}-winning sets:", winners)

#Example usage for Test 8 (ny data)
#file_path = csvfinder('aggregated_voting_NYCMayor.csv')
#winners, coefficient = data_processor(file_path)
#print(f"Greatest {coefficient}-winning sets:", winners)
