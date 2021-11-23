#The data we need to retrieve
#1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The perceentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote

#Import modules
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Assign a variable accumulator
total_votes = 0

#Create candidate list
candidate_options = []

# Create candidate dictionary
candidate_votes = {}

#Creating winning candidate variable and tracker
winning_candidate = ""
winning_count=0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        #Add the candidate name to list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name) 

            #Begin tracking vote count
            candidate_votes[candidate_name]=0

        #Add to candidate vote count
        candidate_votes[candidate_name] += 1

    #Iterate through candidate list
    for candidate_name in candidate_votes:
        #Votes for each candidate
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #Print the candidate name and percentage of votes
        print(f"{candidate_name}: {vote_percentage:.1f} ({votes:,})\n")
        #Determining winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

