def JSONStrFromDict(d):
    json = "{"
    for key, value in d.iteritems():
        json += JSONStrFromPrimitive(key) + ":"
        item = type(value)
        if item is list:
            json += JSONStrFromList(value)
        elif item is dict:
            json += JSONStrFromDict(value)
        else:
            json += JSONStrFromPrimitive(value)
        json += ","
    if json[-1:] is not "{":
        json = json[:-1]
    json += "}"
    return json


def JSONStrFromList(a):
    json = "["
    for value in a:
        item = type(value)
        if item is dict:
            json += JSONStrFromDict(value)
        elif item is list:
            json += JSONStrFromList(value)
        else:
            json += JSONStrFromPrimitive(value)
        json += ","
    if json[-1:] is not "[":
        json = json[:-1]
    json += "]"
    return json

def JSONStrFromPrimitive(p):
    item = type(p)
    if item is str:
        return "\"%s\"" % (p)
    elif item is int or item is float or item is bool:
        return "%s" % (str(p).lower())
    elif p is None:
        return "null"


json = [{
    "origin": "71.238.69.171",
    "listy": [1, 2, 3, 4, 5.5, True],
    "url": "http://httpbin.org/get",
    "args": {},
    "checkit": None,
    "headers": {
        "Accept-Language": "en-US,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36",
        "Host": "httpbin.org",
        "Upgrade-Insecure-Requests": "1"
    }
}]

print(JSONStrFromList(json))
