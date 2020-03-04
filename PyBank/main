#--------------------PyBank------------------
#Important considerations:
#-It is needed to have a file with two columns, it does not import the name but its content:
#  Date and Profit/Losses (Numbers)
#-The files that are use here are on the same repository. If they are in a differente repository
# it will be necessary to change the cvspath variable 

#import modules to use
import csv
import os
from babel.numbers import format_currency
import statistics

#path of the file
#reading
csvpath = os.path.join('budget_data.csv')
csvfile = open(csvpath,'r')
csvreader = csv.reader(csvfile, delimiter=',')

#writing
csvpath2 = os.path.join("results.csv")
csvfile2  = open(csvpath2,'w')
csvwriter = csv.writer(csvfile2, delimiter =',')

#save the header
header=next(csvreader)


#counting the total of lines that are on the file. Given the fact that is one month per row
#it give us the total of months

def total_months(file):
    csvfile.seek(0)
    next(csvreader)
    file=len(csvfile.readlines())
    return file


#create a function to determine the total profits
def total_profits(data):
    csvfile.seek(0)
    next(csvreader)
    total=0
    for row in data:
        total1=int(row[1])
        total += total1 
    return total

#function to export the results

def export(m,t,ac,gi,gd,fma,fmi):
    

    csvwriter.writerow(["Finanacial Analysis"])
    csvwriter.writerow(["Total Months: ", m])
    csvwriter.writerow(["Total: ", format_currency(total_profits(csvreader),'USD', locale='en_US')])
    csvwriter.writerow(["Average Change: ","{:,.2f}".format(ac)])
    csvwriter.writerow(["Greatest Increase in Profits: ",fma,format_currency(gi,'USD', locale='en_US')])
    csvwriter.writerow(["Greatest Decrease in Profits: ",fmi,format_currency(gd,'USD', locale='en_US')])
    
   
   

#create a function to found the Greatest Increase in Profits
def indec_profit(profit) :

    #copy the data stored in the file
    rows=[]
    p=[]
    p1=[]
    csvfile.seek(0)
    next(csvreader)
    for row in profit:
        rows.append(row)  
     
    initial=rows[0][1]
    i=0
    #loop to determine the how the profits are increasin/decreasing
    for i in range(85):
        p=int(rows[i+1][1])-int(initial)
        p1.append(p) #a list is created with this values
        initial=rows[i+1][1]
    
    average = statistics.mean(p1)
    print("\nAverage Change: {:,.2f}".format(average))
 #the max increase is stored
    max_change=max(p1)
    min_change=min(p1)

 #initialize the varible for the loop
 #search the position of the max an mnin value and search it in the original list
    w=0
    months=total_months(csvreader)
    for w in range(months-1): 
       if max_change == p1[w]:
            w+=1
            fmax=rows[w][0]
            print("\nGreatest Increase in Profits: " +fmax+" "+ str(format_currency(max_change,'USD', locale='en_US')))
       elif min_change==p1[w]:
            w+=1
            fmin=rows[w][0]
            print("\nGreatest Decrease in Profits: " +fmin+" "+ str(format_currency(min_change,'USD', locale='en_US')))

    export(months,total_profits(csvreader),average,max_change,min_change,fmax,fmin)





print("\n Financial Analysis \n")
print("----------------------------- \n")
print("Total Months: "+ str(total_months(csvreader))+"\n")
print("Total: " + str(format_currency(total_profits(csvreader),'USD', locale='en_US')))
indec_profit(csvreader)




csvfile.close()

