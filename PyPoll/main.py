import os
import csv

#Variables
total_votes = 0
previous_vote_count = 0
candidates = []
candidate_vote_counts = []
winner = ""

#Read file
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")
with open(election_data) as csvfile:
    election_data = csv.reader(csvfile)
    
    #Store header
    election_header = next(election_data)
    
    # Iterate through each row in file
    for row in election_data:
        total_votes += 1
        candidate_name = row[2]

        found_candidate = False

        #loop through list to see if candidate from ballot is already in list
        for idx in range(len(candidates)):
            if candidates[idx] == candidate_name:
                candidate_vote_counts[idx] += 1
                found_candidate = True
                break
        
        # add candidate if they are not currently in list
        if not found_candidate:
            candidates.append(candidate_name)
            candidate_vote_counts.append(1)

output_path = os.path.join("c:\\Users\\kklos\\OneDrive\\Desktop\\python-challenge\\py_analyses", "pypoll_analyses.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["-------------------------"])
    for idx in range(len(candidates)):

        #print candidates with vote counts and percentage of votes
        csvwriter.writerow([f"{candidates[idx]}: {round(((candidate_vote_counts[idx]/total_votes)*100), 3)}% ({candidate_vote_counts[idx]})"])

        #Find Winner
        if candidate_vote_counts[idx] > previous_vote_count:
            winner = candidates[idx]
            previous_vote_count = candidate_vote_counts[idx]
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-------------------------"])