import csv
import io
import zipfile
import sys
import xml.etree.ElementTree as etree

caseFile = sys.argv[1]
zf    = zipfile.ZipFile(caseFile)
fn = None
for filename in zf.namelist():
    if ".graphml" in filename:
        fn = filename
graphml = zf.read(fn)
items_file  = io.TextIOWrapper(io.BytesIO(graphml))

catchFlag = False
catchType = None

clName = "<?xml version=\"1.1\" encoding=\"UTF-8\" standalone=\"no\"?>"

ipTable = []
domainTable = []
subDomainTable = []

csv.field_size_limit(sys.maxsize)

for idx, row in enumerate(csv.DictReader(items_file)):
    if(catchFlag):
        if catchType == "ip":
            ip = row[clName].replace("/","").split("<mtg:Value>")[1]
            print("[IP] " + ip)
            ipTable.append(ip)
        elif catchType == "dom":
            dom = row[clName].replace("/","").split("<mtg:Value>")[1]
            print("[DO] " + dom)
            domainTable.append(dom)
        elif catchType == "sub":
            sub = row[clName].replace("/","").split("<mtg:Value>")[1]
            print("[SD] " + sub)
            subDomainTable.append(sub)

    if "mtg:Property displayName=\"IP Address\"" in row[clName]:
        catchFlag = True
        catchType = "ip"
    elif "mtg:Property displayName=\"Domain Name\"" in row[clName]:
        catchFlag = True
        catchType = "dom"
    elif "mtg:Property displayName=\"DNS Name\"" in row[clName]:
        catchFlag = True
        catchType = "sub"
    else:
        catchFlag = False

outputname = "result-"+caseFile.replace(".","-")+".txt"
f = open(outputname, "w")
f.write("# === Summary === #\n")
f.write("IP Count : "+str(len(ipTable))+"\n")
f.write("Dom Count : "+str(len(domainTable))+"\n")
f.write("Sub Count : "+str(len(subDomainTable))+"\n")
f.write("\n# === IP Extracted from Casefile "+caseFile+" === #\n")
for ip in ipTable:
    f.write(ip+"\n")
f.write("\n# === Domains Extracted from Casefile "+caseFile+" === #\n")
for dom in domainTable:
    f.write(dom+"\n")
f.write("\n# === Subdomaines Extracted from Casefile "+caseFile+" === #\n")
for sub in subDomainTable:
    f.write(sub+"\n")
f.close()
print("\n"+outputname+" successfully created! \n")
