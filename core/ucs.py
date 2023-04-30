import core.util as util
def parseFile(nameAndPath):
    JSON = {}
    myFile = open(nameAndPath)
    text = myFile.readline()
    while text != "":
        text = myFile.readline()
        splitText = text.split("	")
        if len(splitText)==68:
            X = parseLine(splitText)
            if X["number"]!="":
                JSON[X["number"]] = X
    myFile.close()
    return JSON

def parseLine(l):
    links = []
    for i in range(28,68):
        if "http" in l[i]:
            links.append(l[i])
    D = {
    'name': util.vetField(l[0]), 
    'number':util.vetField(l[26]), 
    'officialName':util.vetField(l[1]), 
    'countryRegistry':util.vetField(l[2]), 
    'countryOperator':util.vetField(l[3]), 
    'operator':util.vetField(l[4]), 
    'users':util.vetField(l[5]), 
    'purpose':util.vetField(l[6]), 
    'purposeDetails':util.vetField(l[7]), 
    'orbitClass':util.vetField(l[8]), 
    'orbitType':util.vetField(l[9]), 
    'longitude':util.vetField(l[10]), 
    'perigee':util.vetField(l[11]), 
    'apogee':util.vetField(l[12]), 
    'eccentricity':util.vetField(l[13]), 
    'inclination':util.vetField(l[14]),  
    'period':util.vetField(l[15]), 
    'massLaunch':util.vetField(l[16]), 
    'massDry':util.vetField(l[17]), 
    'power':util.vetField(l[18]), 
    'launchDate':util.vetField(l[19]), 
    'lifetime':util.vetField(l[20]), 
    'contractor':util.vetField(l[21]), 
    'countryContractor':util.vetField(l[22]), 
    'launchSite':util.vetField(l[23]), 
    'launchVehicle':util.vetField(l[24]), 
    'COSPAR':util.vetField(l[25]), 
    'comments':util.vetField(l[27]), 
    'links':links
    }
    return D