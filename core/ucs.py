import core.util as util

def parseFile(nameAndPath):
    '''open, parse, close'''
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
    '''parse single line of satellite data'''
    links = []
    for i in range(28,68):
        if "http" in l[i]:
            links.append(l[i])
    D = {
    'name': util.vetField(l[0]), 
    'number':util.vetField(l[26]), 
    'officialName':util.vetField(l[1]),
    'COSPAR':util.vetField(l[25]), 
    'orbit':{
        'orbitClass':util.vetField(l[8]), 
        'orbitType':util.vetField(l[9]), 
        'elements': {
            'longitude':util.vetField(l[10]), 
            'perigee':util.vetField(l[11]), 
            'apogee':util.vetField(l[12]), 
            'eccentricity':util.vetField(l[13]), 
            'inclination':util.vetField(l[14]),  
            'period':util.vetField(l[15])
        }
    },
    'launch':{
        'massLaunch':util.vetField(l[16]), 
        'massDry':util.vetField(l[17]), 
        'launchSite':util.vetField(l[23]), 
        'launchVehicle':util.vetField(l[24]), 
        'launchDate':util.vetField(l[19]), 
        'lifetime':util.vetField(l[20]), 
        'power':util.vetField(l[18])
    },
    'affiliation':{
        'countryRegistry':util.vetField(l[2]), 
        'countryOperator':util.vetField(l[3]), 
        'operator':util.vetField(l[4]), 
        'users':util.vetField(l[5]), 
        'contractor':util.vetField(l[21]), 
        'countryContractor':util.vetField(l[22]), 
    },
    'info':{
        'purpose':util.vetField(l[6]), 
        'purposeDetails':util.vetField(l[7]), 
        'comments':util.vetField(l[27]),   
        'links':links
    }
    }
    return D



def fullInFromSatCat(D):
    '''fill in exclusively from space-track satcat'''
    links = []

    D = {
    'name': util.vetField(D["OBJECT_NAME"]), 
    'number':util.vetField(D["NORAD_CAT_ID"]), 
    'officialName':None, 
    'COSPAR':None, 
    'orbit':{
        'orbitClass':None, 
        'orbitType':None,
        'elements': {
            'longitude':None, 
            'perigee':util.vetField(D["PERIGEE"]), 
            'apogee':util.vetField(D["APOGEE"]), 
            'eccentricity':None, 
            'inclination':util.vetField(D["INCLINATION"]), 
            'period':util.vetField(D["PERIOD"]), 
        }
    },
    'launch':{
        'massLaunch':None, 
        'massDry':None, 
        'launchSite':util.vetField(D["SITE"]), 
        'launchVehicle':None,
        'launchDate':util.vetField(D["LAUNCH"]), 
        'lifetime':None, 
        'power':None 
    },
    'affiliation':{
        'countryRegistry':util.vetField(D["COUNTRY"]), 
        'countryOperator':None, 
        'operator':None, 
        'users':None, 
        'contractor':None, 
        'countryContractor':None, 
    },
    'info':{
        'purpose':None, 
        'purposeDetails':None, 
        'comments':util.vetField(D["COMMENT"]), 
        'links':links
    }
    }
    return D