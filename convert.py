import core.ucs as ucs
import core.util as util

def main():
    JSON = ucs.parseFile('./files/UCS_116_2023.txt')
    util.saveDictAsJson('./out/UCS_2023.json',JSON)

main()