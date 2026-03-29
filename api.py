from flask import Flask, jsonify, request
from flask_cors import CORS
from hotpepper_reviews import get_reviews, generate_reply

app = Flask(__name__)
CORS(app)

@app.route("/api/reviews", methods=["POST"])
def reviews():
    data = request.json
    url = data.get("url")
    
    review_list = get_reviews(url, max_pages=1)
    
    results = []
    for review in review_list[:5]:
        reply = generate_reply(review)
        results.append({"review": review, "reply": reply})
    
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
