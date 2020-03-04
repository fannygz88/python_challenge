#   ------------------------------------------- PyPoll---------------------------------------
# Importnat considerations:
# For this code to work consistently it is necessary to know beforehand the candidates and
# sustitute them in the variables that are indicated in the  code.
#Have three columns that have to be in the following order  -> Voting ID, County, Candidate

#import modules to use
import csv
import os
from babel.numbers import format_currency

#path of the file for
#reading
csvpath = os.path.join('election_data.csv')
#and writing
csvpath2 = os.path.join('results.csv')

#----- read the csv file

csvfile = open(csvpath,'r')
csvreader = csv.reader(csvfile, delimiter=',')

#----- write in file

csvfile2 = open(csvpath2,'w')
csvwiter = csv.writer(csvfile2, delimiter = ',')


#extract the header
header=next(csvreader)

#function for total rows in file
def total_lines(file):
    csvfile.seek(0)
    next(csvreader)
    file=len(csvfile.readlines())
    return file

#function to write the results
def write_report(total,k,l,o,c,pk,pc,pl,po,w):

    csvwiter.writerow(["Total Votes","{:,}".format(total)])
    csvwiter.writerow(["Khan", "{:.3%}".format(pk),"{:,}" .format(k)])
    csvwiter.writerow(["Correy", "{:.3%}".format(pc),"{:,}" .format(c)])
    csvwiter.writerow(["Li", "{:.3%}".format(pl),"{:,}" .format(l)])
    csvwiter.writerow(["O'Tooley", "{:.3%}".format(po),"{:,}" .format(o)])
    csvwiter.writerow(["Winner", w])


#---- Candidates -----
candidate1="Khan"
candidate2="Correy"
candidate3="Li"
candidate4="O'Tooley"

#function to describe the data:
# -Total votes
# -Votes per candidate
# -Percentage of votes
# -Winner
def counting_votes(voters):
    #initializating variables
    r=total_lines(voters) #using the function created previously
    i=0
    k=0
    c=0
    l=0
    o=0
    total=0
    #loop to count the times that the name con a candidate appears
    for i in range(r):
        if voters[i][2]==candidate1:
            k += 1
        elif voters[i][2]== candidate2:
            c += 1
        elif voters[i][2]== candidate3:
            l += 1
        elif voters[i][2] == candidate4:
            o += 1
    
    total = k + c + l + o

    percentage_k = k/total
    percentage_c = c/total
    percentage_l = l/total
    percentage_o = o/total
    
    print("\n Election results\n")
    print("---------------------------------\n")
    print("Total Votes: "+"{:,}".format(total)+"\n")
    print("---------------------------------\n")
    print("   Khan  -> {:.3%}".format(percentage_k) +"   {:,}" .format(k)+"\n")
    print("  Correy -> {:.3%}".format(percentage_c) +"   {:,}".format(c)+"\n")
    print("    Li   -> {:.3%}".format(percentage_l) +"   {:,}" .format(l)+"\n")
    print("O'Tooley -> {:.3%}".format(percentage_o) +"   {:,}".format(o)+"\n")
    print("---------------------------------\n")
    #Determining the winner via max  number of votes
    winner= max(k,c,l,o)

    if winner == k:
        print("Winner: "+candidate1)
    elif winner == c:
        print("Winner: "+candidate2)
    elif winner == l:
        print("Winner: "+candidate3)
    elif winner == o:
        print("Winner: "+candidate4)
    print("\n---------------------------------\n")
    
    write_report(total,k,l,o,c,percentage_k,percentage_c,percentage_l,percentage_o,winner)
   



#creating anew list to store the rows that are read from the csv
data=[]

#reading the rows in csv file

for row in csvreader:
    data.append(row)
   # print (row)
#print(data[6][2])
#unique(data)
lines=total_lines(csvreader)
#print(str(lines))

counting_votes(data)
csvfile.close()

