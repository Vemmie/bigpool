from flask import Flask, request, jsonify
import pandas as pd
import re

# on the terminal type: curl http://127.0.0.1:5002/
app = Flask(__name__)

# Pandas stuff as a puesdo DB
filename = 'AnimeQuoteDB.csv'
db = pd.read_csv(filename)

# gets a random quote 
@app.route('/api/quotes', methods = ['GET'])
def getRandAnime():
    # There are 8611 anime quotes in the csv
    randomQuoteInfo = db.sample(n=1).iloc[0].to_dict()
    return jsonify(randomQuoteInfo), 200

# gets a random quote from a specific anime
# name can be inputed 
@app.route('/api/quotes/<animename>', methods = ['GET'])
def getRandSpecificAnime(animename):
    cleanName = normalizeName(animename)
    subset = db[db["Anime"] == cleanName]

    # Checks if there are matching rows
    if not subset.empty:
        randomSQuoteInfo = subset.sample(1).iloc[0].to_dict()
        return jsonify(randomSQuoteInfo), 200
    else:
        return jsonify({"error" : "No anime Found"}), 404

# String cleaning function (Had to search this one up)
def normalizeName(name):
    # Convert to lowercase
    name = name.lower()
    # Remove all non-alphanumeric characters (keep letters and numbers)
    name = re.sub(r'[^\w\s]', '', name)  # removes symbols like !, -, :, etc.
    # Replace underscores, hyphens, multiple spaces with a single space
    name = re.sub(r'[\s\-_]+', ' ', name).strip()
    return name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) # Change 5003 to your desired port number