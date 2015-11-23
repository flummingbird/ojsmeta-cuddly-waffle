import csv
import base64
import xml.etree.ElementTree as ET

with open ('cwbrSmallerSet.csv', 'r') as csvfile:
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
        issues[issueDate] = {} #makes an empty dic for each issue 

    for arts in csvData:
        issueDate = arts['Issue_date']
        issues[issueDate][arts['ID']]=arts
        

    for key, value in issues.items():
       for k, art in value.items():
           art["Review"]=base64.b64encode(bytes(str(art["Review"]), 'utf-8'))

    for filename in issueDates:
        output = "It works"
        f = open(filename, "w")
        f.write(output)
        f.close()
        #filename = str(issues[issueDate])
        #filename = filename.replace('"', '').strip()
        #print (filename)
    
        #f = open("importfile" %filename, "w")
        #f.write(ET.tostring(xmlout, encoding="Unicode"))
        #f.close()
        



       
    

