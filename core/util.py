import json

def saveDictAsJson(path, JSON):
    '''save json'''
    with open(path, 'w') as f:
        json.dump(JSON, f)

def openJsonAsDict(path):
    '''open json'''
    f = open(path)
    data = json.load(f)
    f.close()
    return data

def vetField(text):
    '''return null if empty or non-existent'''
    if not text:
        return None
    return text
