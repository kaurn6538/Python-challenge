# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('PyPoll','Resources', 'election_data.csv')
#PyPoll/Resources/election_data.csv

# initailizing PyPoll variables
count=0
Candidate_list=[]
unique_candidates=[]
vote_count=[]
vote_percent=[]

# Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    
    for row in csvreader:
        # This will count the total number of votes cast
        count=count+1
        # Append the candidatelist with candidate names
        Candidate_list.append(row[2])
    # Create a set from the candidate list to get the unique candidate names
    for x in set(Candidate_list):
        unique_candidates.append(x)
        # y is the total number of votes per candidate
        y=Candidate_list.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z=(y/count)*100
        vote_percent.append(z)
        
    winning_vote_count=max(vote_count)    
    winner=unique_candidates[vote_count.index(winning_vote_count)]

    # Print results to the terminal
    print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidates)):
            print(unique_candidates[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print(f"The winner is: {winner}")
print("-------------------------")

# Print to a text file: election_results.txt

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write(f"Total Vote:  {str(count)} \n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidates))):
        text.write(f"{unique_candidates[i]} : {round((vote_percent[i]),3)} % ( {str(vote_count[i]) } )\n")
    text.write("---------------------------------------\n")
    text.write(f"The winner is: {winner}\n")
    text.write("---------------------------------------\n")
    
                                
        
        
        
         
