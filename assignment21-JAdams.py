import re
askString = input("What word would you like to find? ")
askString = askString.lower()
""" 
the download link opened a page displaying the texts
So i created a new .txt file and copied the content there
If your doc is not named AliceInWonderland.txt,
please change the alice variable's open string
to match your document type/title.
"""
book = open("AliceInWonderland.txt", 'r')
content = book.readline().lower()
search = 0
findings = []
while content:
    regex = re.findall(r"\b%s\b" % askString, content)
    if len(regex) > 0:
        findings.append(regex)
    content = book.readline().lower()
book.close()
findings = len(findings)

print('I found the word - {} {} times!'.format(askString, findings))