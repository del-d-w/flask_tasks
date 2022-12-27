import xmltodict

handle =open("fortified.xml","r")
content=handle.read()
d=xmltodict.parse(content)
a=d['NessusClientData_v2']['Report']['ReportHost']
c=[]
for i in a:
    b=(i['ReportItem'])
    for j in b:
        c.append(j)
print(len(c))
