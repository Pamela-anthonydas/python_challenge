
import os
import csv

#Function to calculate candidate vote % ( using candidate vote_count list) and print overall candidate statistics
#This code can definitely be placed inside the main code, but I am practicing functions
def candidateStats(unique_candidate,vote_count,count):
    cand_Percent=[]
    for i in range(len(vote_count)):
        x=round((vote_count[i]/count)*100,2)
        cand_Percent.append(x)
        print(f"{unique_candidate[i]} : {cand_Percent[i]} % ({vote_count[i]})")
    return cand_Percent

# Define file path
csvpath = os.path.join("Resources","election_data.csv")
#Inititalize counters and lists
rowcount = 0
candidatelist = []
unique_candidatelist = []
candidate_count = []
candidate_percent = []

# Open the CSV using the set path csvpath
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
# Loop through all rows in csv file
    for row in csvreader:
        # Count the total vote number 
        rowcount = rowcount + 1
        # Set the candidate names to candidatelist
        candidatelist.append(row[2])
    
    # Find the unique candidates from the candidatelist using set, convert it into a list and assign it to unique_candidatelist
    unique_candidatelist=list(set(candidatelist))
    # Loop through each candidate in the unique candidate list and count the votes and append to candidate_count list.
    for i in unique_candidatelist:
        y=candidatelist.count(i)
        candidate_count.append(y)
        # As mentioned in row 7, candidate vote percent can be calculated as below, however I have put the code in a function for practice
        # z=round((y/rowcount)*100,2)
        # candidate_percent.append(z)
    # Create a dictionary by zipping unique_candidatelist and candidate_count
    candidateDict=dict(zip(unique_candidatelist,candidate_count))
    # Print resuls to terminal
    print("Election Results")
    print("------------------------------")
    print(f"Total votes cast : {rowcount}")
    print("------------------------------")
    # Call to function : candidateStats with unique_candidatelist , candidate_count list and total votecount as arguments. 
    # Candidate stats will be printed in the function
    candidate_percent=candidateStats(unique_candidatelist,candidate_count,rowcount)
    print("------------------------------")
    #Declare winner and print by finding the max value in candidateDict and winner as associated key
    winner=max(candidateDict,key=lambda key:candidateDict[key])
    print(f" The winner is : {winner}")
    print("------------------------------")

# Print resuls to text file
output_path = os.path.join("output", "new.txt")

# Open the file using "write" mode. 
with open(output_path, 'w', newline='') as csvfile:

    csvfile.write("Election Results\n")
    csvfile.write("------------------------------ \n")
    csvfile.write(f"Total votes cast : {rowcount}\n")
    csvfile.write("------------------------------\n")
    # Loop through the length of the uniq_candidatelist and write the candidate name , candidate vote_percent and candidate vote count
    for i in range(len(unique_candidatelist)):
        csvfile.write(f"{unique_candidatelist[i]} : {candidate_percent[i]} % ({candidate_count[i]})\n")
    #Declare winner and print
    csvfile.write("------------------------------\n")
    csvfile.write(f" The winner is : {winner}\n")
    csvfile.write("------------------------------\n")


    

     