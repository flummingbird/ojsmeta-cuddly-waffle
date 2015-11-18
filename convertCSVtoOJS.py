import csv
import xml.etree.ElementTree as ET

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
        
    def issuesxml(x):
        result = []
        for issue in x:
            result.append(E("issue", issue))
        return result

    xmlout = ET.Element("xmlout")
    for i in issues:
        ET.SubElement(xmlout, i)

    print (len(xmlout))
       # E.issues(
        #    for issue in issues:
         #       E.issue(
          #      )
        #)
     #)   
    #print(etree.tostring(xmloutput, pretty_print=True))

       
    

