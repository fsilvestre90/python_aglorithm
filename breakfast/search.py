# Your company delivers breakfast via autonomous quadcopter drones. And something mysterious has happened.
# Each breakfast delivery is assigned a unique ID, a positive integer. When one of the company's 100 drones takes off with a delivery, the delivery's ID is added to a list, delivery_id_confirmations. When the drone comes back and lands, the ID is again added to the same list.

# After breakfast this morning there were only 99 drones on the tarmac. One of the drones never made it back from a delivery. We suspect a secret agent from Amazon placed an order and stole one of our patented drones. To track them down, we need to find their delivery ID.

# Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.

# The IDs are not guaranteed to be sorted or sequential. Orders aren't always fulfilled in the order they were received, and some deliveries get cancelled before takeoff.


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
