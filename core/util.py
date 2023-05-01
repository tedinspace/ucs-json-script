import json

def saveDictAsJson(path, JSON):
    with open(path, 'w') as f:
        json.dump(JSON, f)

def openJsonAsDict(path):
    f = open(path)
    data = json.load(f)
    f.close()
    return data

def vetField(text):
    if not text:
        return None
    return text
