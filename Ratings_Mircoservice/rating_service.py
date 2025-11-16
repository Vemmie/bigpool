from flask import Flask, jsonify, request
import rating_model as db

# on the terminal type: curl http://127.0.0.1:5002/
app = Flask(__name__)

@app.route('/api/rating', methods = ['POST'])
# Json needs to have to add an item
# 1. service = 'stringname'
# 2. item = anything (Try to stick to something simple)
# 3. rating = int(0 to 5)
def addRatingPost():
    # handles post request
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON format in request body"}), 400
    
    if not data.get("service"):
        return jsonify({"error": "service not found"}), 400
    if 'rating' not in data:
        return jsonify({"error": "Missing rating"}), 400
    
    service = str(data.get("service"))
    item = data.get("item") # this could be anyhing
    
    try:
        rating = float(data.get("rating"))
        if not (0 <= rating <= 5):
            raise ValueError
    except (TypeError, ValueError):
        return jsonify({"error": "Not a valid rating must be from [0 to 5]"}), 400
    
    db.addRating(str(service), item, rating)
    return jsonify({f"{item} has been rated {rating}"}),202

# handles the get for specific item
# Must have params of service and item to get
@app.route('/api/rating/<service>/<item>', methods = ['GET'])
def GetItemRatings(service, item):
    rating = db.getRating(service, item)
    if rating == {} or rating == None:
        return jsonify({"error": "service or item not found"}), 404
    return rating, 200

# handles get for all
# Must have a valid service with no empty list
@app.route('/api/rating/<service>', methods = ['GET'])
def GetAllRating(service):
    ratingsList = db.getAllRating(service)
    if ratingsList == {}:
        return jsonify({"error": "service not found or list empty"}), 404
    return jsonify(ratingsList)

# Deletes rating for specific item
# Must have params of service and item to delete
@app.route('/api/rating/<service>/<item>', methods = ['DELETE'])
def DeleteItem(service, item):
    deletedItemRes = db.deleteRating(service, item)
    if not deletedItemRes:
        return jsonify({"error": "service not found / Item not found"}), 404
    return jsonify({"message": f"Deleted {item} from {service}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True) # Change 5002 to your desired port number