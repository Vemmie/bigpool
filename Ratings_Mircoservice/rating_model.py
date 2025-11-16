# Python Dict will be the acting DB in this service
'''
The DB will be a dictionary that holds other dictionaries.
The first key value would be "service":{}
Within this the second {} will hold the ratings
'''
ratingsDB = {
    "anime": {"Naruto": 5, "OnePiece": 4},
    "projectX": {"FeatureA": 3},
    "projectY": {"Task1": 4}
}

'''
example:
ratingsDB = {
    "anime": {"Naruto": 5, "OnePiece": 4},
    "projectX": {"FeatureA": 3},
    "projectY": {"Task1": 4}
}
'''
# Note that all functions will take which service it belongs too

# Adds a rating based on the service and item
def addRating(service, item, rating):
    ratingsDB.setdefault(service, {})
    ratingsDB[service][item] = rating
    return True

# Returns rating based on item based on specific service, 
# if service doesn't exist return empty hashmap
# if no item return None
def getRating(service, item):
    return ratingsDB.get(service, {}).get(item, None)

# Deletes rating based on item based on specific service
# returns False if no service and item doesn't exsist
def deleteRating(service, item):
    if service in ratingsDB and item in ratingsDB[service]:
        ratingsDB[service].pop(item)
        return True
    return False

# Gets everything from specific service
# if service is not in there return empty hashmap
def getAllRating(service):
    if service in ratingsDB:
        return ratingsDB.get(service, {}).copy()
    else:
        return {}