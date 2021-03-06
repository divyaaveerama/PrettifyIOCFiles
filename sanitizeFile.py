#!/usr/bin/python
#Divyaa Kamalanathan 2020
import re

IOCList = []
newIOCList = {}
		
def OpenFileAndSplitIntoSet(filename):
    fo = open(filename,"r+")
    for line in fo:
        for words in line.split():
            IOCList.append(words)
    fo.close()
    # print(IOCList)


def getIndicatorsfromList(TheList):

    URL = re.compile('(\w|-)+(\.([a-zA-Z])+)+')
    MD5 = re.compile('^\w{32}$')
    SHA256 = re.compile('^\w{64}$')
    IP = re.compile('\d+\.\d+\.\d+\.\d+')

    IOCs = {}
    IOCs['IPs'] = []
    IOCs['URLs'] = []
    IOCs['SHAs'] = []
    IOCs['MD5s'] = []
        
    for items in IOCList:
                                                    
        if URL.match(items): 
            IOCs['URLs'].append(items)
        elif IP.match(items):
            IOCs['IPs'].append(items)
        elif SHA256.match(items): 
            IOCs['SHAs'].append(items)
        elif MD5.match(items): 
            IOCs['MD5s'].append(items)
        
    return IOCs

def printIOCs(IOCs):

    for x in IOCs:
        print("%s:" %x)
        for items in IOCs[x]:
            print(items , sep='\n')
        print("\n")
		
if __name__ == "__main__":
    import sys
    OpenFileAndSplitIntoSet("") #insert filename here
    newIOCList = getIndicatorsfromList(IOCList)
    printIOCs(newIOCList)
    
