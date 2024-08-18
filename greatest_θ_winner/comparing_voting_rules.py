#The purpose of this is to generate a bunch of random elections and compare the results of different voting rules

import random
from other_voting_rules import plurality_k_2, borda_k_2, stv_k_2, copeland_k_2, plurality_k_1, borda_k_1, stv_k_1, copeland_k_1, greatest_theta_winning_set_k_2, find_candidate_pair_theta, greatest_theta_winning_set_k_1, find_single_candidate_theta
import csv
import pandas as pd
import numpy as np

def compare_voting_rules_k_2_random(num_tests, n, m, output_file='voting_results_k_2_random.csv'): #Compare voting rules for k=2 (random distrubution)

    #Initialize a dictionary to store results
    results_dict = {
        "n": [], "m": [],
        "Plurality": [], "Plurality θ": [], "Borda": [], "Borda θ": [],
        "Copeland": [], "Copeland θ": [], "STV": [], "STV θ": [], 
        "Greatest θ-winning Set": [], "Greatest θ Coefficient": []
    }

    for _ in range(num_tests):
        #Append test parameters
        results_dict["n"].append(n)
        results_dict["m"].append(m)
        
        #Generate ballots and vote counts
        candidates = [f'Candidate_{i}' for i in range(0, m)] #Generate m candidates
        vote_counts = []
        ballots = []
        for j in range(n):
            ballot = random.sample(candidates, m) 
            ballots.append(ballot)
            vote_counts.append(1)

        plurality_result_k_2 = plurality_k_2(candidates, ballots, vote_counts)
        borda_result_k_2 = borda_k_2(candidates, ballots, vote_counts)
        copeland_result_k_2 = copeland_k_2(candidates, ballots, vote_counts)
        stv_result_k_2 = stv_k_2(candidates, ballots, vote_counts)
        greatest_theta_result_k_2, greatest_theta_coefficient = greatest_theta_winning_set_k_2(candidates, ballots, vote_counts)

        #Add winners to the results dictionary
        results_dict["Plurality"].append(plurality_result_k_2)
        results_dict["Plurality θ"].append(find_candidate_pair_theta(plurality_result_k_2[0], plurality_result_k_2[1], candidates, ballots, vote_counts))
        results_dict["Borda"].append(borda_result_k_2)
        results_dict["Borda θ"].append(find_candidate_pair_theta(borda_result_k_2[0], borda_result_k_2[1], candidates, ballots, vote_counts))
        results_dict["Copeland"].append(copeland_result_k_2)
        results_dict["Copeland θ"].append(find_candidate_pair_theta(copeland_result_k_2[0], copeland_result_k_2[1], candidates, ballots, vote_counts))
        results_dict["STV"].append(stv_result_k_2)
        results_dict["STV θ"].append(find_candidate_pair_theta(stv_result_k_2[0], stv_result_k_2[1], candidates, ballots, vote_counts))
        results_dict["Greatest θ-winning Set"].append(greatest_theta_result_k_2)
        results_dict["Greatest θ Coefficient"].append(greatest_theta_coefficient)        

        #print(f"Test {_+1} of {num_tests} complete") #Print progress

    #Convert results dictionary to a DataFrame
    df = pd.DataFrame(results_dict)
    
    #Output DataFrame to CSV
    df.to_csv(output_file, mode="a", header=False)
    print(f"Results written to {output_file}")

def compare_voting_rules_k_1_random(num_tests, n, m, output_file='voting_results_k_1_random.csv'): #Compare voting rules for k=1 (random distribution)

    #Initialize a dictionary to store results
    results_dict = {
        "n": [], "m": [],
        "Plurality": [], "Plurality θ": [], "Borda": [], "Borda θ": [],
        "Copeland": [], "Copeland θ": [], "STV": [], "STV θ": [], 
        "Greatest θ-winning Set": [], "Greatest θ Coefficient": []
    }

    for _ in range(num_tests):
        #Append test parameters
        results_dict["n"].append(n)
        results_dict["m"].append(m)
        
        #Generate ballots and vote counts
        candidates = [f'Candidate_{i}' for i in range(0, m)] #Generate m candidates
        vote_counts = []
        ballots = []
        for j in range(n):
            ballot = random.sample(candidates, m) 
            ballots.append(ballot)
            vote_counts.append(1)

        plurality_result_k_1 = plurality_k_1(candidates, ballots, vote_counts)
        borda_result_k_1 = borda_k_1(candidates, ballots, vote_counts)
        copeland_result_k_1 = copeland_k_1(candidates, ballots, vote_counts)
        stv_result_k_1 = stv_k_1(candidates, ballots, vote_counts)
        greatest_theta_result_k_1, greatest_theta_coefficient = greatest_theta_winning_set_k_1(candidates, ballots, vote_counts)

        #Add winners to the results dictionary
        results_dict["Plurality"].append(plurality_result_k_1)
        results_dict["Plurality θ"].append(find_single_candidate_theta(plurality_result_k_1[0], candidates, ballots, vote_counts))
        results_dict["Borda"].append(borda_result_k_1)
        results_dict["Borda θ"].append(find_single_candidate_theta(borda_result_k_1[0], candidates, ballots, vote_counts))
        results_dict["Copeland"].append(copeland_result_k_1)
        results_dict["Copeland θ"].append(find_single_candidate_theta(copeland_result_k_1[0], candidates, ballots, vote_counts))
        results_dict["STV"].append(stv_result_k_1)
        results_dict["STV θ"].append(find_single_candidate_theta(stv_result_k_1[0], candidates, ballots, vote_counts))
        results_dict["Greatest θ-winning Set"].append(greatest_theta_result_k_1)
        results_dict["Greatest θ Coefficient"].append(greatest_theta_coefficient)        

    #Convert results dictionary to a DataFrame
    df = pd.DataFrame(results_dict)
    
    #Output DataFrame to CSV
    df.to_csv(output_file, mode="a", header=False)
    print(f"Results written to {output_file}")

def compare_voting_rules_k_2_normal(num_tests, n, m, output_file='voting_results_k_2_normal.csv'): #Compare voting rules for k=2 (normal distrubution)

    #Initialize a dictionary to store results
    results_dict = {
        "n": [], "m": [],
        "Plurality": [], "Plurality θ": [], "Borda": [], "Borda θ": [],
        "Copeland": [], "Copeland θ": [], "STV": [], "STV θ": [], 
        "Greatest θ-winning Set": [], "Greatest θ Coefficient": []
    }

    for _ in range(num_tests):
        #Append test parameters
        results_dict["n"].append(n)
        results_dict["m"].append(m)
        
        #Generate ballots and vote counts
        candidates = [f'Candidate_{i}' for i in range(m)] #Generate m candidates
        vote_counts = []
        ballots = []
        for j in range(n):
            #Generate normally distributed random numbers
            random_scores = np.random.normal(loc=0, scale=1, size=m)
            
            #Create a ballot by sorting candidates based on the random scores
            ballot = [x for _, x in sorted(zip(random_scores, candidates), reverse=True)]
            
            ballots.append(ballot)
            vote_counts.append(1)

        plurality_result_k_2 = plurality_k_2(candidates, ballots, vote_counts)
        borda_result_k_2 = borda_k_2(candidates, ballots, vote_counts)
        copeland_result_k_2 = copeland_k_2(candidates, ballots, vote_counts)
        stv_result_k_2 = stv_k_2(candidates, ballots, vote_counts)
        greatest_theta_result_k_2, greatest_theta_coefficient = greatest_theta_winning_set_k_2(candidates, ballots, vote_counts)

        #Add winners to the results dictionary
        results_dict["Plurality"].append(plurality_result_k_2)
        results_dict["Plurality θ"].append(find_candidate_pair_theta(plurality_result_k_2[0], plurality_result_k_2[1], candidates, ballots, vote_counts))
        results_dict["Borda"].append(borda_result_k_2)
        results_dict["Borda θ"].append(find_candidate_pair_theta(borda_result_k_2[0], borda_result_k_2[1], candidates, ballots, vote_counts))
        results_dict["Copeland"].append(copeland_result_k_2)
        results_dict["Copeland θ"].append(find_candidate_pair_theta(copeland_result_k_2[0], copeland_result_k_2[1], candidates, ballots, vote_counts))
        results_dict["STV"].append(stv_result_k_2)
        results_dict["STV θ"].append(find_candidate_pair_theta(stv_result_k_2[0], stv_result_k_2[1], candidates, ballots, vote_counts))
        results_dict["Greatest θ-winning Set"].append(greatest_theta_result_k_2)
        results_dict["Greatest θ Coefficient"].append(greatest_theta_coefficient)        

        #print(f"Test {_+1} of {num_tests} complete") #Print progress

    #Convert results dictionary to a DataFrame
    df = pd.DataFrame(results_dict)
    
    #Output DataFrame to CSV
    df.to_csv(output_file, mode="a", header=False)
    print(f"Results written to {output_file}")

def compare_voting_rules_k_1_normal(num_tests, n, m, output_file='voting_results_k_1_normal.csv'): #Compare voting rules for k=1 (normal distribution)

    #Initialize a dictionary to store results
    results_dict = {
        "n": [], "m": [],
        "Plurality": [], "Plurality θ": [], "Borda": [], "Borda θ": [],
        "Copeland": [], "Copeland θ": [], "STV": [], "STV θ": [], 
        "Greatest θ-winning Set": [], "Greatest θ Coefficient": []
    }

    for _ in range(num_tests):
        #Append test parameters
        results_dict["n"].append(n)
        results_dict["m"].append(m)
        
        # Generate candidates
        candidates = [f'Candidate_{i}' for i in range(m)] #Generate m candidates
        vote_counts = []
        ballots = []
        
        for j in range(n):
            #Generate normally distributed random numbers
            random_scores = np.random.normal(loc=0, scale=1, size=m)
            
            #Create a ballot by sorting candidates based on the random scores
            ballot = [x for _, x in sorted(zip(random_scores, candidates), reverse=True)]
            ballots.append(ballot)
            vote_counts.append(1)

        #Run voting methods and compute θ coefficients (placeholder logic)
        plurality_result_k_1 = plurality_k_1(candidates, ballots, vote_counts)
        borda_result_k_1 = borda_k_1(candidates, ballots, vote_counts)
        copeland_result_k_1 = copeland_k_1(candidates, ballots, vote_counts)
        stv_result_k_1 = stv_k_1(candidates, ballots, vote_counts)
        greatest_theta_result_k_1, greatest_theta_coefficient = greatest_theta_winning_set_k_1(candidates, ballots, vote_counts)

        #Add winners to the results dictionary
        results_dict["Plurality"].append(plurality_result_k_1)
        results_dict["Plurality θ"].append(find_single_candidate_theta(plurality_result_k_1[0], candidates, ballots, vote_counts))
        results_dict["Borda"].append(borda_result_k_1)
        results_dict["Borda θ"].append(find_single_candidate_theta(borda_result_k_1[0], candidates, ballots, vote_counts))
        results_dict["Copeland"].append(copeland_result_k_1)
        results_dict["Copeland θ"].append(find_single_candidate_theta(copeland_result_k_1[0], candidates, ballots, vote_counts))
        results_dict["STV"].append(stv_result_k_1)
        results_dict["STV θ"].append(find_single_candidate_theta(stv_result_k_1[0], candidates, ballots, vote_counts))
        results_dict["Greatest θ-winning Set"].append(greatest_theta_result_k_1)
        results_dict["Greatest θ Coefficient"].append(greatest_theta_coefficient)

    #Convert results dictionary to a DataFrame
    df = pd.DataFrame(results_dict)
    
    #Output DataFrame to CSV
    df.to_csv(output_file, mode="a", header=False)
    print(f"Results written to {output_file}")


def main():
    #marray = [3, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    #narray = [5, 25, 50, 75, 100]
    n = 200 
    m = 5
    num_tests = 5
    #for m in marray:
    #compare_voting_rules_k_1_random(num_tests, n, m)
    #compare_voting_rules_k_2_random(num_tests, n, m)
    compare_voting_rules_k_1_normal(num_tests, n, m) 
    #compare_voting_rules_k_2_normal(num_tests, n, m)

def main2():
    m = 3
    n = 20
    num_tests = 1
    compare_voting_rules_k_1_normal(num_tests, n, m)

if __name__ == '__main__':
    main()