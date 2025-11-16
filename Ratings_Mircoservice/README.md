# Ratings Microservice

This microservice provides users to have access to a ratings system. This service will it's own DB (represented through a dict in python)

NO API KEY IS NEEDED

# Installation
**After cloning:**
pip install -r requirements.txt 

.\.venv\Scripts\Activate to use on powershell

This will install all the dependecies you need to run it.

# Get route all route example:
/api/rating/'service_name'

Replace the service name to get all the ratings of a specific service

# More quests:
1. Request all
2. Request a specific rating
3. Delete a rating
4. Add a rating

Note: **ALL Must specify the service they are using**
Look at API for all the params needed to use the service

# Sample Request:
http://127.0.0.1:5002/api/rating/anime

# Response:
```json
{
    "Naruto": 5,
    "OnePiece": 4
}
```