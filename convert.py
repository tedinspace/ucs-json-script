import json
def main():
    parseFile('./files/UCS_116_2023.txt')

def parseFile(nameAndPath):
    JSON = {}
    myFile = open(nameAndPath)
    text = myFile.readline()
    while text != "":
        text = myFile.readline()
        splitText = text.split("	")
        if len(splitText)==68:
            X = parseLine(splitText)
            if len(X["number"]) > 0:
                JSON[X["number"]] = X
    myFile.close()
    with open('./out/UCS_2023.json', 'w') as f:
        json.dump(JSON, f)

def parseLine(l):
    links = []
    for i in range(28,68):
        if "http" in l[i]:
            links.append(l[i])
    D = {
    'name':l[0], 
    'number':l[26], 
    'officialName':l[1], 
    'countryRegistry':l[2], 
    'countryOperator':l[3], 
    'operator':l[4], 
    'users':l[5], 
    'purpose':l[6], 
    'purposeDetails':l[7], 
    'orbitClass':l[8], 
    'orbitType':l[9], 
    'longitude':l[10], 
    'perigee':l[11], 
    'apogee':l[12], 
    'eccentricity':l[13], 
    'inclination':l[14], 
    'period':l[15], 
    'massLaunch':l[16], 
    'massDry':l[17], 
    'power':l[18], 
    'launchDate':l[19], 
    'lifetime':l[20], 
    'contractor':l[21], 
    'countryContractor':l[22], 
    'launchSite':l[23], 
    'launchVehicle':l[24], 
    'COSPAR':l[25], 
    'comments':l[27],
    'links':links
    }
    return D

main()