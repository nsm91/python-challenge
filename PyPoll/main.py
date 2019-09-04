#Import Dependencies
import os
import csv
#Call in File
py_poll_path = os.path.join("../election_data.csv")
#Open File
with open(py_poll_path,newline='') as pypoll_csv:
    py_poll = csv.reader(pypoll_csv,delimiter=',')
    py_poll_header = next(py_poll)
    vote_counter = 0
    candidates = {}
    for row in py_poll:
        #part 1
        vote_counter += 1
        #part 2
        if row[2] not in candidates:
            candidates.update({row[2]:0})
        #part 3
        candidates[row[2]] += 1

winner_num = 0

print("Election Results")
print("-------------------------")
print(f"Total votes: {vote_counter}")
print("-------------------------")
for i in candidates:
    if candidates[i] > winner_num:
        winner_num = candidates[i]
        winner_name = i
    prcnt  = round(((candidates[i] / vote_counter) * 100),2)
    print(f"{i} : {prcnt}% ({candidates[i]})")
print("-------------------------")
print(f"Winner : {winner_name}")

pypoll_txt = open("PyPoll_Summary.txt","w")
pypoll_txt.write("Election Results")
pypoll_txt.write("\n-------------------------")
pypoll_txt.write(f"\nTotal votes: {vote_counter}")
pypoll_txt.write("\n-------------------------")
for i in candidates:
    if candidates[i] > winner_num:
        winner_num = candidates[i]
        winner_name = i
    prcnt  = round(((candidates[i] / vote_counter) * 100),2)
    pypoll_txt.write(f"\n{i} : {prcnt}% ({candidates[i]})")
pypoll_txt.write("\n-------------------------")
pypoll_txt.write(f"\nWinner : {winner_name}")