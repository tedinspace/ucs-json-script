import core.ucs as ucs
import core.util as util

def main():
    SPACE_TRACK_SATCAT = "./files/sat_cat_120_2023.json"
    UCS_DB = './files/UCS_116_2023.txt'

    SATCAT_JSON = util.openJsonAsDict(SPACE_TRACK_SATCAT)
    print(SATCAT_JSON)
    
    UCS_JSON = ucs.parseFile(UCS_DB)




main()