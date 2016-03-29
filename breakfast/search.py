def findLostDrones():
    droneList = open("droneIDs.txt")
    lostDrones = {}
    for droneID in droneList:
        formattedId = droneID.rstrip('\n')
        if lostDrones.has_key(formattedId):
            del lostDrones[formattedId]
        else:
            lostDrones[formattedId] = 1
    print(lostDrones.keys())

print(findLostDrones())
