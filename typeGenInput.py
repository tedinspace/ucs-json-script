import core.util as util
def main():
    '''write out a single entry in order to auto-generate typescript type'''
    OUT_FILE = "./out/merged.json"
    D = util.openJsonAsDict(OUT_FILE)
    util.saveDictAsJson('./out/single.json',D["25544"])

main()