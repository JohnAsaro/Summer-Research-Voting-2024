import csv
from con_cycle import condorcet_cycle
from pathfinder import csvfinder

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) #Skip header row
        data = [row for row in reader]
    return data

def clean_data(data):
    cleaned_data = []
    for row in data:
        row = row[:-1] #Ingore the "Count" column
        cleaned_row = [candidate.strip() for candidate in row if candidate.strip() and candidate.strip().lower() != 'null'] #Process data and ignore 'Null'
        #cleaned_row = [candidate.strip() for candidate in row if candidate.strip()] #OOB Error bugfixing, processes 'Null' colums
        if cleaned_row:
            cleaned_data.append(cleaned_row)
    return cleaned_data

def format_data_for_condorcet(cleaned_data): 
    candidates = list(set(candidate for row in cleaned_data for candidate in row)) #Extracts candidates from csv
    return candidates, cleaned_data

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

def print_debug(file_path):
    
    counter = 0 #Counter used for debugging
    
    data = read_csv(file_path)
    #print("Raw data:")
    #print(data)
    
    cleaned_data = clean_data(data)
    #print("Cleaned data:")
    #print(cleaned_data)
    
    candidates, ballots = format_data_for_condorcet(cleaned_data)
    print("Ballots:")
    for ballot in ballots:
        counter += 1            
        print(counter, ballot, "Length:", len(ballot))

    print("Candidates:")
    print(candidates)

def main():
    if __name__ == "__main__":
        #Example usage
        file_path = csvfinder('2017-Mayor-Ballot-Records.csv')
        result = data_processor(file_path)
        print(f"Condorcet cycle found: {result}")

#Testing

#Test 1:
#file_path = csvfinder('2017-Mayor-Ballot-Records.csv')
#print_debug(file_path)
#main()

#Test 2:
#file_path = csvfinder('Concycle-example.csv')
#result = data_processor(file_path)
#print(f"Condorcet cycle found: {result}")
#print_debug(file_path)

#Test 3: 
#file_path = csvfinder('2021-Mayor-Cast-Vote-Record.csv')
#result = data_processor(file_path)
#print(f"Condorcet cycle found: {result}") 
#print_debug(file_path)

#Test 4:
#file_path = csvfinder('Concycle-test.csv')
#result = data_processor(file_path)
#print(f"Condorcet cycle found: {result}")
#print_debug(file_path)

#Test 5:
#file_path = csvfinder('test5.csv')
#result = data_processor(file_path)
#print(f"Condorcet cycle found: {result}")
#print_debug(file_path)

#Test 6:
#file_path = csvfinder('test6.csv')
#result = data_processor(file_path)
#print(f"Condorcet cycle found: {result}")
#print_debug(file_path)