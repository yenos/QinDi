import xml.etree.ElementTree as etree
import sys

def openFile(f):
    return open(f,"r")

schem = "{http://schemas.mandiant.com/2010/ioc}"
def parseXML(iocRules):
    ipTable = []
    domTable = []

    catchFlag = False

    for el in iocRules.iter(schem+"IndicatorItem"):
        for content in el.iter():
        # DomCatch
            if(catchFlag):
                domTable.append(content.text)

        # IP
            try:
                if content.attrib["type"] == "IP":
                    ipTable.append(content.text)
            except:
                pass
        # DomFlag
            try:
                if content.attrib["search"] == "Network/DNS":
                    catchFlag = True
                else:
                    catchFlag = False
            except:
                catchFlag = False

    return ipTable, domTable

def genResult (ipTable, domTable, inF):
    outputName = "result-"+inF.replace(".", "-")+".txt"
    f = open(outputName, "w")
    f.write("# === Summary === #\n")
    f.write("IP Count : "+str(len(ipTable))+"\n")
    f.write("Dom Count : "+str(len(domTable))+"\n")
    f.write("\n# === IP Extracted from IOC "+inF+" === #\n")
    for ip in ipTable:
        f.write(ip+"\n")
        print("[IP] "+ip)
    f.write("\n# === Domains Extracted from IOC "+inF+" === #\n")
    for dom in domTable:
        f.write(dom+"\n")
        print("[DO] "+dom)

    print(outputName+" seccessfully created! \n")
def dispatcher(f):
    tree = etree.parse(f)
    root = tree.getroot()
    ipt, dot = parseXML(root)
    genResult(ipt, dot, f)



dispatcher(sys.argv[1])
