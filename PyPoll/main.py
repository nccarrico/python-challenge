# import dependecies
import csv

# open csv file
filepath = "election_data.csv"
with open(filepath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
   
    # count number of votes cast and put row data into lists
    vote_count = 0
    voter_id = []
    counties = []
    candidates = []
    for row in csvreader:
        vote_count += 1
        voter_id.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])

# find list of candidates that received votes
candidate_list = []

for person in candidates:
    if person not in candidate_list:
        candidate_list.append(person)

# count votes for each candidate in candidate list
votes_per_candidate = []

for people in candidate_list:
    votes_per_candidate.append(candidates.count(people))

# calculate percentage of votes each candidate won
percent_per_candidate = [e / vote_count * 100 for e in votes_per_candidate ]

# find index of greatest number of votes
winner_index = votes_per_candidate.index(max(votes_per_candidate))

# find winner
winner = candidate_list[winner_index]

# print results to console
print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_count}")
print("-------------------------")
for r in range(len(candidate_list)):
    print(f"{candidate_list[r]}: {round(percent_per_candidate[r],3)}% ({votes_per_candidate[r]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# export text file with results
output_path = "Election Results.csv"

with open(output_path, 'w', newline='') as output:
    csvwriter = csv.writer(output)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Total Votes: {vote_count}"])
    csvwriter.writerow(["-------------------------"])
    for r in range(len(candidate_list)):
        csvwriter.writerow([f"{candidate_list[r]}: {round(percent_per_candidate[r],3)}% ({votes_per_candidate[r]})"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-------------------------"])

