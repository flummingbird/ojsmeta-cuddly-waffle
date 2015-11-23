import csv
import base64
import xml.etree.ElementTree as ET

with open ('cwbrSmallerSet.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    csvData = [blah for blah in reader]
    issueDates = []
    #rows = []
    for row in csvData:
        issueDates.append(row['Issue_date'])
        #rows.append(row)
    issueDates = set(issueDates)

    issues = {}

    for issueDate in issueDates:
        issues[issueDate] = {} #makes an empty dic for each issue
        sectionNames = []
        #rows = []
        for row in csvData:
            if row['Issue_date'] == issueDate:
                sectionNames.append(row['Record_type'])
        sectionNames = set(sectionNames)
        for section in sectionNames:
            issues[issueDate][section] = {} #empty dict for each section

    for arts in csvData:
        issueDate = arts['Issue_date']
        section = arts['Record_type']
        issues[issueDate][section][arts['ID']]=arts
        
    #convert "Reviews" into base64 encoding
    #for key, value in issues.items():
    #   for k, art in value.items():
    #       art["Review"]=base64.b64encode(bytes(str(art["Review"]), 'utf-8'))

    #create xml for each and output
    for filename in issueDates:
        xmlout = ET.Element("issue", {'current' : 'false', 'identification' : 'title', 'published' : 'false'})
        title = ET.SubElement(xmlout, 'title')
        title.text = filename
        #sections = []
        #for keys, articles in issues[issueDate]:
         #   sections.append(articles['Record_type'])
        #print (sections)
        ET.dump(xmlout)
        #output = ET.Element("issue")
        #f = open(filename, "w")
        #f.write(output)
        #f.close()
        



       
    

