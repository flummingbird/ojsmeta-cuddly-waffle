import csv
from lxml.builder import E

with open ('cwbr.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    csvData = [blah for blah in reader]
    issueDates = []
    rows = []
    for row in csvData:
        issueDates.append(row['Issue_date'])
        rows.append(row)
    issueDates = set(issueDates)

    issues = {}

    for issueDate in issueDates:
        issues[issueDate] = {}

    for arts in csvData:
        issueDate = arts['Issue_date']
        issues[issueDate][arts['ID']]=arts

    

    
    print (issues['Summer 2011']['4871'])      
    

