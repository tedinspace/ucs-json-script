import core.util as util
def supplementInfo(entry, satcat):
    '''add information from space-track's satcat'''
    entry['info']['type'] = util.vetField(satcat["OBJECT_TYPE"])
    entry['info']['size'] = util.vetField(satcat["RCS_SIZE"])
    entry['launch']['decay'] = util.vetField(satcat["DECAY"])
    entry['intdes']=util.vetField(satcat["INTLDES"])
    return entry