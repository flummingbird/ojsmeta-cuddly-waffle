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
        sectionNames.add('dateP') #date published is issue level metadata
        for section in sectionNames:
            issues[issueDate][section] = {} #empty dict for each section

    for arts in csvData:
        issueDate = arts['Issue_date']
        section = arts['Record_type']
        issues[issueDate][section][arts['ID']]=arts
        issues[issueDate]['dateP']=arts['Issue'] #adds date published
        
    #convert "Reviews" into base64 encoding
    for key, value in issues.items():
        for sectionKey, sectionValue in value.items():
            if sectionKey == 'dateP':
                continue
            for articleKey, articleValue in sectionValue.items():
                articleValue["Review"]="<h3>This is the isbn: " + articleValue["ISBN"] + "</h3><p>So that means other values can go here too.</p>" + articleValue["Review"]
                articleValue["Review"]=base64.b64encode(bytes(str(articleValue["Review"]), 'utf-8'))

    #create xml for each and output
    for filename in issueDates:
        xmlout = ET.Element("issue", {'current' : 'false', 'identification' : 'title', 'published' : 'false'})
        title = ET.SubElement(xmlout, 'title')
        title.text = filename
        date_published = ET.SubElement(xmlout, 'date_published')
        date_published.text = issues[filename]['dateP']
        for secKey, secValue in issues[filename].items():
            if secKey == 'dateP':
                continue
            section = ET.SubElement(xmlout, 'section')
            secTitle = ET.SubElement(section, 'title')
            secTitle.text = secKey
            for artKey, artValue in issues[filename][secKey].items():
                article = ET.SubElement(section, 'article')
                artTitle = ET.SubElement(article, 'title')
                artTitle.text = artValue['Title'] + " by " + artValue['Auth_1']
                abstract = ET.SubElement(article, 'abstract')
                abstract.text = artValue['Headline'] + artValue['Sub_headline']
                indexing = ET.SubElement(article, 'indexing')
                subject = ET.SubElement(indexing, 'subject')
                subject.text = artValue['Categories']
                author = ET.SubElement(article, 'author')
                firstname = ET.SubElement(author, 'firstname')
                #middlename = ET.SubElement(author, 'middlename')
                #middlename.text = '
                lastname = ET.SubElement(author, 'lastname')
                email = ET.SubElement(author, 'email')
                email.text = '***'
                if len(artValue['Reviewer']) < 4:
                    firstname.text = 'CWBR'
                    lastname.text = 'Staff'
                else:
                    firstname.text = artValue['Reviewer'].split(',', 1)[1].strip() 
                    lastname.text = artValue['Reviewer'].split(',', 1)[0].strip()
                galley = ET.SubElement(article, 'galley')
                label = ET.SubElement(galley, 'label')
                label.text = 'HTML'
                file = ET.SubElement(galley, 'file')
                embed = ET.SubElement(file, 'embed', {'encoding':'base64','filename':'articletext'+artKey+'.html','mime_type':'text/html'})
                embed.text = str(artValue['Review'])[2:-1]
                output = ET.tostring(xmlout, encoding="unicode")
                f = open(filename+'.xml', "w")
                f.write(output)
                f.close()

      
        



       
    

