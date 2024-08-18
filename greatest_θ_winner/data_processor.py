import csv
from greatest_th_winning_set import find_greatest_theta_winning_set, find_greatest_theta_winning_set_k_is_1, find_candidate_pair_theta
from pathfinder import csvfinder
from other_voting_rules import plurality_k_2, borda_k_2, stv_k_2, copeland_k_2

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
        winners, coefficent = find_greatest_theta_winning_set_k_is_1(candidates, ballots, vote_counts)
    except ValueError as e:
        print(f"Error: {e}")
        return False
    except IndexError as e:
        print(f"Index Error: {e}")
        return False
    
    try:
        winners2, coefficent2 = find_greatest_theta_winning_set(candidates, ballots, vote_counts)
    except ValueError as e:
        print(f"Error: {e}")
        return False
    except IndexError as e:
        print(f"Index Error: {e}")
        return False
    
    return winners, coefficent, winners2, coefficent2

def get_candidates_ballots_and_vote_counts(file_path):
    data = read_csv(file_path)
    
    cleaned_data, vote_counts = clean_data(data)
    
    candidates, ballots = format_data_for_theta(cleaned_data)

    return candidates, ballots, vote_counts

def data_processor_plurality(file_path): #Data processor for plurality voting rule
    data = read_csv(file_path)
        
    cleaned_data, vote_counts = clean_data(data)
    
    candidates, ballots = format_data_for_theta(cleaned_data)

    plurality_winner_k_2 = plurality_k_2(candidates, ballots, vote_counts)

    return plurality_winner_k_2

def data_processor_borda(file_path): #Data processor for borda count voting rule
    data = read_csv(file_path)
        
    cleaned_data, vote_counts = clean_data(data)
    
    candidates, ballots = format_data_for_theta(cleaned_data)

    borda_winner_k_2 = borda_k_2(candidates, ballots, vote_counts)

    return borda_winner_k_2

def data_processor_stv(file_path): #Data processor for stv voting rule
    data = read_csv(file_path)
        
    cleaned_data, vote_counts = clean_data(data)
    
    candidates, ballots = format_data_for_theta(cleaned_data)

    stv_winner_k_2 = stv_k_2(candidates, ballots, vote_counts)

    return stv_winner_k_2

def data_processor_copeland(file_path): #Data processor for copeland voting rule
    data = read_csv(file_path)
        
    cleaned_data, vote_counts = clean_data(data)
    
    candidates, ballots = format_data_for_theta(cleaned_data)

    copeland_winner_k_2 = copeland_k_2(candidates, ballots, vote_counts)

    return copeland_winner_k_2

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

#Test 1 (see if find candidate pair theta works)
#print("---------------------------------------------------------------------------------------------------")
#print("Minneapolis 2017 data")
#file_path = csvfinder('2017-Mayor-Ballot-Records.csv')
#winners, coefficient, winners2, coefficent2 = data_processor(file_path)
#print(f"Greatest {coefficient}-winning sets when k = 1:", winners)
#print(f"Greatest {coefficent2}-winning sets when k = 2:", winners2)
#candidates, ballots, vote_counts = get_candidates_ballots_and_vote_counts(file_path)
#test = find_candidate_pair_theta('Raymond Dehn', 'Jacob Frey', candidates, ballots, vote_counts)
#print(test)
#print_debug(file_path)

#Test 2
#file_path = csvfinder('Concycle-example.csv')
#winners, coefficient, winners2, coefficent2 = data_processor(file_path)
#print(f"Greatest {coefficient}-winning sets when k = 1:", winners)
#print(f"Greatest {coefficent2}-winning sets when k = 2:", winners2)

#Test 3
#print("---------------------------------------------------------------------------------------------------")
#print("Minneapolis 2021 data")
#file_path = csvfinder('2021-Mayor-Cast-Vote-Record.csv')
#winners, coefficient, winners2, coefficent2 = data_processor(file_path)
#print_debug(file_path)
#print(f"Greatest {coefficient}-winning sets when k = 1:", winners)
#print(f"Greatest {coefficent2}-winning sets when k = 2:", winners2)
#plurality_winner_k_2 = data_processor_plurality(file_path) 
#borda_winner_k_2 = data_processor_borda(file_path)
#stv_winner_k_2 = data_processor_stv(file_path)
#copeland_winner_k_2 = data_processor_copeland(file_path)
#candidates, ballots, vote_counts = get_candidates_ballots_and_vote_counts(file_path)
#plurality_theta_k_2 = find_candidate_pair_theta(plurality_winner_k_2[0], plurality_winner_k_2[1], candidates, ballots, vote_counts) #Pluarilty winners when k = 2 theta coefficent
#borda_theta_k_2 = find_candidate_pair_theta(borda_winner_k_2[0], borda_winner_k_2[1], candidates, ballots, vote_counts) #Borda winners when k = 2 theta coefficent
#stv_theta_k_2 = find_candidate_pair_theta(stv_winner_k_2[0], stv_winner_k_2[1], candidates, ballots, vote_counts) #STV winners when k = 2 theta coefficent
#copeland_theta_k_2 = find_candidate_pair_theta(copeland_winner_k_2[0], copeland_winner_k_2[1], candidates, ballots, vote_counts) #Copeland winners when k = 2 theta coefficent
#print(f"Plurality winners when k = 2: {plurality_winner_k_2}, this is a {plurality_theta_k_2}-winning set")
#print(f"Borda winners when k = 2: {borda_winner_k_2}, this is a {borda_theta_k_2}-winning set")
#print(f"STV winners when k = 2: {stv_winner_k_2}, this is a {stv_theta_k_2}-winning set")
#print(f"Copeland winners when k = 2: {copeland_winner_k_2}, this is a {copeland_theta_k_2}-winning set")

#Test 4
#file_path = csvfinder('Concycle-test.csv')
#winners, coefficient, winners2, coefficent2 = data_processor(file_path)
#print(f"Greatest {coefficient}-winning sets when k = 1:", winners)
#print(f"Greatest {coefficent2}-winning sets when k = 2:", winners2)

#Test 5
#file_path = csvfinder('test5.csv')
#winners, coefficient, winners2, coefficent2 = data_processor(file_path)
#print(f"Greatest {coefficient}-winning sets when k = 1:", winners)
#print(f"Greatest {coefficent2}-winning sets when k = 2:", winners2)

#Test 6
#file_path = csvfinder('test6.csv')
#winners, coefficient, winners2, coefficent2 = data_processor(file_path)
#print(f"Greatest {coefficient}-winning sets when k = 1:", winners)
#print(f"Greatest {coefficent2}-winning sets when k = 2:", winners2)

#Test 7
#file_path = csvfinder('test7.csv')
#winners, coefficient, winners2, coefficent2 = data_processor(file_path)
#print(f"Greatest {coefficient}-winning sets when k = 1:", winners)
#print(f"Greatest {coefficent2}-winning sets when k = 2:", winners2)

#Test 8 (ny data)
#print("---------------------------------------------------------------------------------------------------")
#print("Ny data")
#file_path = csvfinder('aggregated_voting_NYCMayor.csv')
#winners, coefficient, winners2, coefficent2 = data_processor(file_path)
#print_debug(file_path)
#print(f"Greatest {coefficient}-winning sets when k = 1:", winners)
#print(f"Greatest {coefficent2}-winning sets when k = 2:", winners2)
#plurality_winner_k_2 = data_processor_plurality(file_path) 
#borda_winner_k_2 = data_processor_borda(file_path)
#stv_winner_k_2 = data_processor_stv(file_path)
#copeland_winner_k_2 = data_processor_copeland(file_path)
#candidates, ballots, vote_counts = get_candidates_ballots_and_vote_counts(file_path)
#plurality_theta_k_2 = find_candidate_pair_theta(plurality_winner_k_2[0], plurality_winner_k_2[1], candidates, ballots, vote_counts) #Pluarilty winners when k = 2 theta coefficent
#borda_theta_k_2 = find_candidate_pair_theta(borda_winner_k_2[0], borda_winner_k_2[1], candidates, ballots, vote_counts) #Borda winners when k = 2 theta coefficent
#stv_theta_k_2 = find_candidate_pair_theta(stv_winner_k_2[0], stv_winner_k_2[1], candidates, ballots, vote_counts) #STV winners when k = 2 theta coefficent
#copeland_theta_k_2 = find_candidate_pair_theta(copeland_winner_k_2[0], copeland_winner_k_2[1], candidates, ballots, vote_counts) #Copeland winners when k = 2 theta coefficent
#print(f"Plurality winners when k = 2: {plurality_winner_k_2}, this is a {plurality_theta_k_2}-winning set")
#print(f"Borda winners when k = 2: {borda_winner_k_2}, this is a {borda_theta_k_2}-winning set")
#print(f"STV winners when k = 2: {stv_winner_k_2}, this is a {stv_theta_k_2}-winning set")
#print(f"Copeland winners when k = 2: {copeland_winner_k_2}, this is a {copeland_theta_k_2}-winning set")

#Test 9 (snack survey)
print("---------------------------------------------------------------------------------------------------")
print("Snack survey data")
file_path = csvfinder('Reformatted_Snack_Survey.csv')
winners, coefficient, winners2, coefficent2 = data_processor(file_path)
#print_debug(file_path)
print(f"Greatest {coefficient}-winning sets when k = 1:", winners)
print(f"Greatest {coefficent2}-winning sets when k = 2:", winners2)
plurality_winner_k_2 = data_processor_plurality(file_path) #For the second winner there is a tie between chips and munchkins both with 5 votes
borda_winner_k_2 = data_processor_borda(file_path)
stv_winner_k_2 = data_processor_stv(file_path)
copeland_winner_k_2 = data_processor_copeland(file_path)
candidates, ballots, vote_counts = get_candidates_ballots_and_vote_counts(file_path)
plurality_theta_k_2 = find_candidate_pair_theta(plurality_winner_k_2[0], plurality_winner_k_2[1], candidates, ballots, vote_counts) #Pluarilty winners when k = 2 theta coefficent
borda_theta_k_2 = find_candidate_pair_theta(borda_winner_k_2[0], borda_winner_k_2[1], candidates, ballots, vote_counts) #Borda winners when k = 2 theta coefficent
stv_theta_k_2 = find_candidate_pair_theta(stv_winner_k_2[0], stv_winner_k_2[1], candidates, ballots, vote_counts) #STV winners when k = 2 theta coefficent
copeland_theta_k_2 = find_candidate_pair_theta(copeland_winner_k_2[0], copeland_winner_k_2[1], candidates, ballots, vote_counts) #Copeland winners when k = 2 theta coefficent
print(f"Plurality winners when k = 2: {plurality_winner_k_2}, this is a {plurality_theta_k_2}-winning set")
print(f"Borda winners when k = 2: {borda_winner_k_2}, this is a {borda_theta_k_2}-winning set")
print(f"STV winners when k = 2: {stv_winner_k_2}, this is a {stv_theta_k_2}-winning set")
print(f"Copeland winners when k = 2: {copeland_winner_k_2}, this is a {copeland_theta_k_2}-winning set")

#Test 10 (minneapolis data 2017)
#print("---------------------------------------------------------------------------------------------------")
#print("Minneapolis 2017 data")
#file_path = csvfinder('2017-Mayor-Ballot-Records.csv')
#winners, coefficient, winners2, coefficent2 = data_processor(file_path)
#print_debug(file_path)
#print(f"Greatest {coefficient}-winning sets when k = 1:", winners)
#print(f"Greatest {coefficent2}-winning sets when k = 2:", winners2)
#plurality_winner_k_2 = data_processor_plurality(file_path) 
#borda_winner_k_2 = data_processor_borda(file_path)
#stv_winner_k_2 = data_processor_stv(file_path)
#copeland_winner_k_2 = data_processor_copeland(file_path)
#candidates, ballots, vote_counts = get_candidates_ballots_and_vote_counts(file_path)
#plurality_theta_k_2 = find_candidate_pair_theta(plurality_winner_k_2[0], plurality_winner_k_2[1], candidates, ballots, vote_counts) #Pluarilty winners when k = 2 theta coefficent
#borda_theta_k_2 = find_candidate_pair_theta(borda_winner_k_2[0], borda_winner_k_2[1], candidates, ballots, vote_counts) #Borda winners when k = 2 theta coefficent
#stv_theta_k_2 = find_candidate_pair_theta(stv_winner_k_2[0], stv_winner_k_2[1], candidates, ballots, vote_counts) #STV winners when k = 2 theta coefficent
#copeland_theta_k_2 = find_candidate_pair_theta(copeland_winner_k_2[0], copeland_winner_k_2[1], candidates, ballots, vote_counts) #Copeland winners when k = 2 theta coefficent
#print(f"Plurality winners when k = 2: {plurality_winner_k_2}, this is a {plurality_theta_k_2}-winning set")
#print(f"Borda winners when k = 2: {borda_winner_k_2}, this is a {borda_theta_k_2}-winning set")
#print(f"STV winners when k = 2: {stv_winner_k_2}, this is a {stv_theta_k_2}-winning set")
#print(f"Copeland winners when k = 2: {copeland_winner_k_2}, this is a {copeland_theta_k_2}-winning set")