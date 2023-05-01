import core.ucs as ucs
import core.util as util
import core.satcat as sc

def main():
    # input files
    SPACE_TRACK_SATCAT = "./files/sat_cat_120_2023.json"
    UCS_DB = './files/UCS_116_2023.txt'

    UCS_JSON = ucs.parseFile(UCS_DB)

    SATCAT_JSON = util.openJsonAsDict(SPACE_TRACK_SATCAT)
    for item in SATCAT_JSON:
        rso = item["NORAD_CAT_ID"]
        if rso not in UCS_JSON:
            tempEntry = ucs.fullInFromSatCat(item)
            newEntry = sc.supplementInfo(tempEntry, item)
            UCS_JSON[rso]=newEntry
        else:
            supEntry = sc.supplementInfo(UCS_JSON[rso], item)
            UCS_JSON[rso]=supEntry

    util.saveDictAsJson('./out/test.json',UCS_JSON)

    
    

main()